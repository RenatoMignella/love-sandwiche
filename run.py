# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
    Get sales figures
    """
    print("Please enter the sales data ")
    print("Data shoud be six numbers, separetad by commas.")
    print("Examples: 10,20,30,40,50,60\n")
    
    data_str = input("enter your data here ")
   
    sales_data = data_str.split(",")
    validte_data(sales_data)
    
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
        print(f"invalid data: {e}, please try again .")        
    
        
    
get_sales_data()    
    

