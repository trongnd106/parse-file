#importing pandas as pd 
import pandas as pd 
# Read and store content 
# of an excel file  
read_file = pd.read_excel ("./cartouchemania_output_v1.xlsx")
read_file.fillna("")
# Write the dataframe object 
# into csv file
read_file.to_csv ("./cartouchemania_output_v1.csv",  
                  index = None, 
                  header=True) 
# read csv file and convert  
# into a dataframe object 
# df = pd.DataFrame(pd.read_csv("Test.csv")) 
# show the dataframe 
# df