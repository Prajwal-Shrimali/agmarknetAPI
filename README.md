# agmarknetAPI
 API for agmarknet Website

http://127.0.0.1:5000/request?commodity=Item&state=State&market=City
replace "Item" by the name of the whose price is to be found
replace "State" with the name of the state where you want to see the prize
replace "City" by the name of the city in the state where you want to view the prize

it returns a JSON output 
example:
http://127.0.0.1:5000/request?commodity=Potato&state=Karnataka&market=Bangalore
Outptut: [ { "S.No": "1", "City": "Bangalore", "Commodity": "Potato", "Min Prize": "1500", "Max Prize": "1800", "Model Prize": "1600", "Date": "04 Nov 2023" }, { "S.No": "2", "City": "Bangalore", "Commodity": "Potato", "Min Prize": "1400", "Max Prize": "1700", "Model Prize": "1500", "Date": "04 Nov 2023" }, { "S.No": "3", "City": "Bangalore", "Commodity": "Potato", "Min Prize": "1500", "Max Prize": "1800", "Model Prize": "1600", "Date": "03 Nov 2023" }, { "S.No": "4", "City": "Bangalore", "Commodity": "Potato", "Min Prize": "1400", "Max Prize": "1700", "Model Prize": "1500", "Date": "03 Nov 2023" }, { "S.No": "5", "City": "Bangalore", "Commodity": "Potato", "Min Prize": "1500", "Max Prize": "1800", "Model Prize": "1600", "Date": "02 Nov 2023" }, { "S.No": "6", "City": "Bangalore", "Commodity": "Potato", "Min Prize": "1400", "Max Prize": "1700", "Model Prize": "1500", "Date": "02 Nov 2023" }, { "S.No": "7", "City": "Bangalore", "Commodity": "Potato", "Min Prize": "1800", "Max Prize": "2000", "Model Prize": "1900", "Date": "30 Oct 2023" }, { "S.No": "8", "City": "Bangalore", "Commodity": "Potato", "Min Prize": "1300", "Max Prize": "1600", "Model Prize": "1400", "Date": "30 Oct 2023" } ]
