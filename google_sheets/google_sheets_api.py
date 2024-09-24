import time

import gspread

gc = gspread.service_account("keys/thermal-tome-432713-t4-ee838cf372a4.json")
flight_deals = gc.open("Flight Deals")
# price = flight_deals.get_worksheet(0)

price = flight_deals.worksheet("prices")

"""
list_of_prices = price.get_all_records()
print(list_of_prices[0])

#TODO:GET VALUES FROM A RANGE OF CELLS
#VALUES NOT KEYS
range_of_cells = price.get_values('A5:E5')
print(range_of_cells)

#TODO: GET COLUNM BY INDEX
col_2 =  price.col_values(1)
print(col_2)
# get rip of the title
col_2_no_title = price.col_values(1)[1:]
print(col_2_no_title)

#TODO: GET ROW BY INDEX
row_1 = price.row_values(2)
print(row_1)


#TODO: GET ESPECIFIC CELL:
cell =  price.acell("D5").value
print(cell)

#TODO:FIND BY QUERY
cell_query = price.find("5.52")
#coordinace
print(cell_query.row, cell_query.col)

#TODO: SEARCH FOR MANY CELLS
no_layovers = price.findall("0")
for layover in no_layovers:
    print(price.row_values(layover.row))

#TODO: GET ROW WHERE ONE COLUMN MATCH
#search term
search = "MIA"
#column for search
arrival_col = price.col_values(8)
print(arrival_col)
#list of matching indexes
list_of_rows = [i+1 for i, value in enumerate(arrival_col) if value == search]
#interates geting thw rows
for i in list_of_rows:
    print(price.row_values(i))


#TODO: GET ROW WHERE TWO COLUMNS MATCHES
arrival_search = "MIA"
price_limit = 1000

arrival_col = price.col_values(8)[1:]
price_col = price.col_values(6)[1:]
price_col_f = [float(price.replace("$","").replace(",","")) for price in price_col]

list_match_i = []
for i,(arrival, fly_price) in enumerate(zip(arrival_col, price_col_f)):
    if arrival == arrival_search and fly_price < price_limit:
        print(i, arrival, fly_price)
        list_match_i.append(i+2)

for i in list_match_i:
    print(price.row_values(i))



#TODO: UPDATE CELL
price.update_cell(col=5, row=2,value=0)
"""

#TODO: UPDATE COLUMN
existing_column = price.get_values("E2:E34")
new_column = [int(i[0]) for i in existing_column]
print(new_column)
# price.update("K1:K32",[["new_column"]]+new_column)

#TODO:MEAN
import statistics
mean = statistics.mean(new_column)
print(mean)
price.update("E35", str(mean))

#TODO LISEN TO CHANGE VALUE IN A CELL
change = flight_deals.worksheet("change")
while True:
    value1 = price.acell("E2").value
    time.sleep(2)
    value2 = price.acell("E2").value
    if value1 == value2:
        change.update("A2", value2)
