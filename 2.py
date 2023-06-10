import tabula 

pdf_in = "scrap.pdf"

dfs = tabula.read_pdf(pdf_in,pages='6')

print(len(dfs))
# problem:
'''
in dfs[0] we get proper output but in dfs 1 we get only first two lines of table 1 instead of getting table 2 then in dfs[3] we get empty
in dfs[4] we get whole table 3 but we dont get first line of table 
'''
# print(dfs[0])
# dfs[0].to_csv("first_table.csv")
# dfs[1].to_csv("second_table.csv")
dfs[5].to_csv("third_table.csv")

# print(dfs[1])