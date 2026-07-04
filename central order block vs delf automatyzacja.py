import shutil
import pandas as pd
import datetime as dt
import win32com.client as win32
import os


# usuwamy wszystkie plikie z folderu de

sciezka = r'https://elancoah.sharepoint.com/sites/CS-SD-DBExchange/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x012000C4F2DFAEE10E0942AEE5E850EF5504DE&id=%2Fsites%2FCS%2DSD%2DDBExchange%2FShared%20Documents%2FGeneral%2FDE'

for i in os.listdir(sciezka):
    pelna_sciezka = os.path.join(sciezka, i)

    if os.path.isfile(pelna_sciezka):
        os.remove(pelna_sciezka)

today = dt.date.today()

# otwiera plik znajdujacy sie na sharepoincie i majacy dostep do modelu semantycznego
excel = win32.Dispatch ("Excel.Application")
excel.Visible = False
wb = excel.Workbooks.Open(r'C:\Users\02703821\Elanco\CS-SD-DB Exchange - General\source file\semantic_model_de.xlsx')

# klika przycisk refresh all
wb.RefreshAll()

#czekaj az odswiezanie sie zakonczy
excel.CalculateUntilAsyncQueriesDone()

ws = wb.Worksheets('central order block vs delf de')

#UsedRange oznacza wszystkie komórki, które zawierają dane.
#Value pobiera wartości z tych komórek.
data = ws.UsedRange.Value

df = pd.DataFrame(data)
df = df[df[0] == 'yes']

df['Customer Service'] = ""
df['Cash App'] = ""
df['Credit Team'] = ""
df = df.iloc[:,1:]


df.to_excel(rf"C:\Users\02703821\Elanco\CS-SD-DB Exchange - General\DE\{today}.xlsx",index=False)
wb.Close(SaveChanges=False) # mowi ze nie zapisuje zmiany w zmiennej wb
excel.Quit()


link_dla_zespolow = r'https://elancoah.sharepoint.com/sites/CS-SD-DBExchange/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FCS%2DSD%2DDBExchange%2FShared%20Documents%2FGeneral%2FDE&viewid=1b4638f8%2Df1c6%2D41dc%2Dae6d%2D04c3dfb7ec95&FolderCTID=0x012000C4F2DFAEE10E0942AEE5E850EF5504DE'

outlook = win32.Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)
mail.Display()
mail.To = "stammdaten@elancoah.com"
mail.subject = rf"Central Order Block vs delf de {today}"
mail.body = f"""Hallo All.\n Please find central order block vs delf de {link_dla_zespolow} \n please mark x and let me know when done so that I could set deletion flag"""
mail.Display()

##