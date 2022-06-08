# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# sales = SHEET.worksheet('sales')

# data = sales.get_all_values()

# print(data)

def get_sales_data():
    """
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via terminal,which must be a string of 6 numbers separated 
    by comas. the loop will repeatedly request dat, until it is valid
    """
    while True:
        
        print("Please enter the sales data ")
        print("Data shoud be six numbers, separetad by commas.")
        print("Examples: 10,20,30,40,50,60\n")
        
        data_str = input("enter your data here ")
    
        sales_data = data_str.split(",")
        
        
        if validte_data(sales_data):
            print("data is validdddd")
            break
    
    return sales_data    
    
def validte_data(values):
    """
   Inside the try, converts all string values into integers.
   Raises ValueError if Strings  cannot be converted into int,
   or if there aren't exacly 6 values 
    """
    
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exacly 6 values required, you provided{len(values)}"
            )
    except ValueError as e:
        print(f"invalid data: {e}, please try again .\n")
        return False
        
    return True        
    
 

# def update_sales_worksheet(data):
#     """
#     Update sales Worksheet, and new row with the list data provided.
#     """     
#     print("Updating sales workdheet ......\n")
#     sales_worksheet = SHEET.worksheet("sales")
#     sales_worksheet.append_row(data)
#     print("Sales worksheet updated successfully. \n")   
    
# def update_surplus_worksheet(data):
#     """
#     Update surplus Worksheet, and new row with the list data provided.
#     """     
#     print("Updating surplus workdheet ......\n")
#     surplus_worksheet = SHEET.worksheet("surplus")
#     surplus_worksheet.append_row(data)
#     print("Surplus worksheet updated successfully.\n")  
    
def update_worksheet(data, worksheet):
    """
    Receives list of integers to be inserted into a worsheet
    Update the relevant workshee with the data provided 
    """ 
    print(f"Updating {worksheet} workdheet ......\n")    
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated sucessfuly\n ")
        
        
    
  
def calculate_surplus_data(sales_row):
     """
    Compare sales with Stock and calculate the surplus for each item type 
     """

     print("calculating surplus data ....\n")
     stock =SHEET.worksheet("stock").get_all_values()
     stock_row = stock[-1]
    #  print(stock_row)
     
     surplus_data =[]
     for stock, sales in zip(stock_row, sales_row):
         surplus =int(stock) - sales
         surplus_data.append(surplus)
     
     return surplus_data
     

def get_last_5_entries_sales():
    """
    Collects collums of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data 
    as a list o lists 
    """
    sales = SHEET.worksheet("sales")
  
    
    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns   
      
  
def main(): 
    """
    Run all program functions
    """   
    data= get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data) 
    update_worksheet(new_surplus_data, "surplus")
    
print("Welcome to love sandwiches data automation")    
# main()   
sales_columns = get_last_5_entries_sales()   
    
    

