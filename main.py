# import tabula 
# import pandas as pd

# df = tabula.read_pdf('scrap.pdf', pages = 'all')[0]

# for i in range(len(df)):
#     df[i].to_excel('scrapped_'+str(i)+'.xlsx')


import tabula
import pandas as pd

# Path to input PDF file
pdf_in = "scrap.pdf" 

df = tabula.read_pdf('scrap.pdf', pages = 'all')[0] #xtra

# pages and multiple_tables are optional attributes
# outputs df as list
PDF = tabula.read_pdf(pdf_in, pages='all', multiple_tables=True)[0]

#View result
print ('\nTables from PDF file\n'+str(PDF))

def printpdf():
    for i in range(len(df)):
        PDF = tabula.read_pdf(pdf_in, pages='all', multiple_tables=True)[i]
        PDF = pd.DataFrame(PDF)
        pdf_out_xlsx = "scrapped_"+str(i)+".xlsx"
        PDF.to_excel(pdf_out_xlsx,index=False) 

printpdf()

#CSV and Excel save paths
# pdf_out_xlsx = "scrapped.xlsx"
# pdf_out_csv = "C:\Users\aryan\Desktop\startup work.csv"

# to Excel
# PDF = pd.DataFrame(PDF)
# PDF.to_excel(pdf_out_xlsx,index=False) 

# # to CSV
# tabula.convert_into (input_PDF, pdf_out_csv, pages='all',multiple_tables=True)
print("Done")

# def printpdf():
#     for i in range(len(df)):
#         PDF = tabula.read_pdf(pdf_in, pages='all', multiple_tables=True)[i]
#         PDF = pd.DataFrame(PDF)
#         pdf_out_xlsx = "scrapped_"+str(i)+".xlsx"
#         PDF.to_excel(pdf_out_xlsx,index=False) 
