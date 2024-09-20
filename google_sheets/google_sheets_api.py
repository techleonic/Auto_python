import gspread

gc = gspread.service_account("keys/thermal-tome-432713-t4-ee838cf372a4.json")
flight_deals = gc.open("Flight Deals")
# price = flight_deals.get_worksheet(0)

price = flight_deals.worksheet("prices")
list_of_prices = price.get_all_records()
print(list_of_prices)