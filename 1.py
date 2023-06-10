import tabula 
import pandas as pd

# Path to input PDF file
pdf_in = "scrap.pdf" #Path to PDF

# pages and multiple_tables are optional attributes
# outputs df as list
PDF = tabula.read_pdf(pdf_in, pages='all', multiple_tables=True)

#View result
print ('\nTables from PDF file\n'+str(PDF))

#CSV and Excel save paths
pdf_out_xlsx = "output.xlsx"
pdf_out_csv = "output.csv"

# to Excel
PDF = pd.DataFrame(PDF)
PDF.to_excel(pdf_out_xlsx,index=False) 

# to CSV
tabula.convert_into (pdf_in, pdf_out_csv, pages='all',multiple_tables=True)
print("Done")