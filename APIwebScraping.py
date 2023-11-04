from flask import Flask, request, jsonify
import json
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
from selenium.webdriver.support import expected_conditions as EC
import time

def script(state, commodity, market):
    # URL of the website with the dropdown fields
    initial_url = "https://agmarknet.gov.in/SearchCmmMkt.aspx"

    driver = webdriver.Chrome()
    driver.get(initial_url)

    print("Commodity")
    dropdown = Select(driver.find_element("id", 'ddlCommodity'))
    dropdown.select_by_visible_text(commodity)

    print("State")
    dropdown = Select(driver.find_element("id", 'ddlState'))
    dropdown.select_by_visible_text(state)

    print("Date")
    # Calculate the date 7 days ago from today
    today = datetime.now()
    desired_date = today - timedelta(days=7)
    date_input = driver.find_element(By.ID, "txtDate")
    date_input.clear()
    date_input.send_keys(desired_date.strftime('%d-%b-%Y'))

    print("Click")
    button = driver.find_element("id", 'btnGo')
    button.click()

    time.sleep(3)

    print("Market")
    dropdown = Select(driver.find_element("id", 'ddlMarket'))
    dropdown.select_by_visible_text(market)

    print("Click")
    button = driver.find_element("id", 'btnGo')
    button.click()

    time.sleep(1)

    driver.implicitly_wait(10)
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Wait for the table to be present
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'cphBody_GridPriceData'))
    )
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    data_list = []
    # Iterate over each  row
    for row in soup.find_all("tr"):
        data_list.append(row.text.replace("\n", "_").replace("  ", "").split("__"))

    jsonList = []
    for i in data_list[4:len(data_list) - 1]:
        d = {}
        d["S.No"] = i[1]
        d["City"] = i[2]
        d["Commodity"] = i[4]
        d["Min Prize"] = i[7]
        d["Max Prize"] = i[8]
        d["Model Prize"] = i[9]
        d["Date"] = i[10]
        jsonList.append(d)

    driver.quit()
    return jsonList

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homePage():
    dataSet = {"Page": "Home Page navigate to request page", "Time Stamp": time.time()}
    return jsonify(dataSet)

@app.route('/request', methods=['GET'])
def requestPage():
    commodityQuery = request.args.get('commodity')
    stateQuery = request.args.get('state')
    marketQuery = request.args.get('market')

    if not commodityQuery or not stateQuery or not marketQuery:
        return jsonify({"error": "Missing query parameters"})

    try:
        json_data = json.dumps(script(stateQuery, commodityQuery, marketQuery), indent=4)
        return json_data
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()
