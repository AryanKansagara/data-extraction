# this program for each table in each sheet in excel


import tabula
import pandas as pd
df = tabula.read_pdf('scrap.pdf', pages = '6')

writer = pd.ExcelWriter('file_multiple_df.xlsx', engine='xlsxwriter')

for i in range(len(df)):
    df[i].to_excel(writer, sheet_name='Sheet'+str(i))

writer.save()