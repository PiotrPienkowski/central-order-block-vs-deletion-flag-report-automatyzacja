import pandas as pd
import datetime as dt

df = pd.read_excel(r'C:\Users\02703821\Elanco\CS-SD-DB Exchange - General\source file\semantic_model_de.xlsx')
df.columns = ['yes/no','Customer_to_be_blocked']
df = df[df['yes/no'] == 'yes']

df['Customer_Service'] = ""
df['Cash_APP'] = ""
df['Colection_Team'] = ""

day = dt.date.today().strftime("%Y-%m-%d")

df.to_excel(r'C:\Users\02703821\Elanco\CS-SD-DB Exchange - General\DE\\' + day + '.xlsx' , index = False)
#