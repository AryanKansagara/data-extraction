import tabula as tb
import pandas as pd


# box = [1.5, 22,3.8,26.741]
# fc = 28.28
         
# for i in range(0, len(box)):
#     box[i] *= fc

pages = [6,7,8,9]

# file = 'scrap.pdf'

# df = tabula.read_pdf(file, pages = pages,multiple_tables=True)
# # -----------------------------
# import pandas as pd

box = [1.5, 22,3.8,26.741]
fc = 28.28
         
for i in range(0, len(box)):
    box[i] *= fc

file = 'scrap.pdf'
df = pd.DataFrame()
region_column = []
regions_raw = tb.read_pdf(file, pages=pages,area=[box],output_format="json")

regions = []
for i in range(0,len(regions_raw)):
    regions.append(regions_raw[i]['data'][0][0]['text'])

for page in pages:
    
    index = pages.index(page)
    region = regions[index]
    print(region)
    
    tl = tb.read_pdf(file, pages=page,area=[box],output_format="dataframe", stream=True)
    
    dft = tl[0]
    dft.rename(columns={ dft.columns[0]: "Fascia d'età", dft.columns[1]: "Casi"}, inplace = True)
    
    region_column = []
    for i in range(0, len(dft)):
        region_column.append(region)
    dft['Regione'] = region_column
    
    df = pd.concat([df, dft])

    df.to_csv('output'+str(page)+'.csv')