import csv
import sqlite3
class DatabaseConnector:
"""
Manages a connection to a sqlite database.
"""
def __init_ (self, database_file):
self.connection = sqlite3.connect(database_file)
self.cursor = self.connection.cursor()
def populate(self, spreadsheet_folder):
"""
Populate the database with data imported from each spreadsheet.
"""
# open the spreadsheets with open(f*{spreadsheet_folder}/shipping_data_0.csv", "r") as
spreadsheet_file_0: with open(f'{spreadsheet_folder}/shipping_data_1.csv", "r") as spreadsheet _file_1:
with open(f'{spreadsheet_folder}/shipping_data_2.csv", "r") as spreadsheet _file_2: # prepare the csv
readers csv_reader_0 = csv.reader(spreadsheet_file_0) csv_reader_1 = csv.reader(spreadsheet_file_1)
csv_reader_2 = csv.reader(spreadsheet_file_2)

# populate first spreadsheet
self populate_first_shipping_data(csv_reader_0)
self.populate_second_shipping_data(csv_reader_1, csv_reader_2)
def populate_first_shipping_data(self, csv_reader_0):
"""
Populate the database with data imported from the first spreadsheet.
"""
for row_index, row in enumerate(csv_reader_0):
# ignore the header row
if row_index > 0:
# extract each required field
product_name = row[2]
product_quantity = row[4]
origin = row[0]
destination = row[1]
# insert the data into the database
self.insert_product_if_it_does_not_already_exist(product_name)
self.insert_shipment(product_name, product_quantity, origin, destination)
# give an indication of progress
print(f'inserted product {row_index} from shipping_data_0")

