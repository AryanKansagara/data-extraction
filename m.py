import pandas as pd
import tabula as tb
file = "scrap.pdf"

table = tb.read_pdf(file,pages=9)

# csv_table = tb.convert_into(file,'pdf_convert.csv')

df = pd.concat(table)

excel_file = df.to_excel('pdf_convert.xlsx')



