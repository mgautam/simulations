from openpyxl import load_workbook

#Variables
postcodes=[3087,3141,30873,3178,3175,3138,3977]
sheets=['G 08', 'G 29','G 53']
totalcols=[7,4,11]
firstrows = [11,11,14]
lastrows = [42,29,33]

catrow=[0,0,12];#category row
totalrows=[0,0,35]
firstcols=[0,0,2]
lastcols=[0,0,10]

#Fixed parameters
prepend='GCP_POA'
ext='.xlsx'

#files=[prepend+str(postcode)+ext for postcode in postcodes]
#print(files)
num_pcodes=len(postcodes)
num_sheets=len(sheets)
num_categories=[]
for s in range(num_sheets):
    if sheets[s] == 'G 53':
        num_categories.append(lastcols[s]-firstcols[s])
    else:
        num_categories.append(lastrows[s]-firstrows[s])



# Read from file
value_sheets=[]
for postcode in postcodes:
    filename=prepend+str(postcode)+ext
    wb = load_workbook(filename=filename, read_only=True)
    value_lists=[]
    for s in range(num_sheets):
        ws = wb[sheets[s]]
        if sheets[s] == 'G 53':
            value_list = [ws.cell(row=totalrows[s],column=c).value for c in range(firstcols[s],lastcols[s]+1)]
        else:
            value_list = [ws.cell(row=r,column=totalcols[s]).value for r in range(firstrows[s],lastrows[s]+1)]
        value_list.insert(0,postcode)
        value_lists.append(value_list)
    value_sheets.append(value_lists)

title_list=[]
for s in range(num_sheets):
    ws = wb[sheets[s]]
    title_list.append(ws.cell(row=4,column=1).value)

category_lists=[]
for s in range(num_sheets):
    ws = wb[sheets[s]]
    if sheets[s] == 'G 53':
        category_list = [ws.cell(row=catrow[s],column=c).value for c in range(firstcols[s],lastcols[s]+1)]
    else:
        category_list = [ws.cell(row=r,column=1).value for r in range(firstrows[s],lastrows[s]+1)]
    category_list.insert(0,'PostCode')
    category_lists.append(category_list)

#print(category_lists)
#print(value_sheets)


# Process extracted data
sum_sheets=[]
for p in range(num_pcodes):
    sum_lists=[]
    for s in range(num_sheets):
        total=0
        for c in range(1,num_categories[s]+2):
            total = total + value_sheets[p][s][c]
        #sum(value_sheets[p][i])
        sum_lists.append(total)
    sum_sheets.append(sum_lists)

percentage_sheets=[]
for p in range(num_pcodes):
    percentage_lists=[]
    for s in range(num_sheets):
        percentage_list = [value_sheets[p][s][c]*100/sum_sheets[p][s] for c in range(1,num_categories[s]+2)]
        percentage_list.insert(0,postcodes[p])
        percentage_lists.append(percentage_list)
    percentage_sheets.append(percentage_lists)

#print(sum_sheets)


# Write to File
from openpyxl import Workbook
wb = Workbook()

'''for i in range(num_sheets):
    wsw = wb.create_sheet(category=sheets[i])
    wsw.append(category_lists[i])
    for c in range(num_pcodes):
        wsw.append(value_sheets[c][i])'''

for s in range(num_sheets):
    wsw = wb.create_sheet(title=sheets[s])
    wsw.cell(row=1,column=1).value=title_list[s]

    for r in range(num_categories[s]+2):
        wsw.cell(row=r+2,column=1).value=category_lists[s][r]

percent_col_offset = num_pcodes+3
for c in range(num_pcodes):
    #print(postcodes[c])
    for s in range(num_sheets):
        wsw = wb[sheets[s]]
        for r in range(num_categories[s]+2):
            wsw.cell(row=r+2,column=c+2).value=value_sheets[c][s][r]
            wsw.cell(row=r+2,column=percent_col_offset+c+2).value=percentage_sheets[c][s][r]

#save the file
wb.save('compilation.xlsx')
