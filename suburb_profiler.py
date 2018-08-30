from openpyxl import load_workbook

postcodes=[3087,3141,3178,3175,3138,3977]
prepend='GCP_POA'
ext='.xlsx'
sheets=['G 08', 'G 29']
cols=[7,4]
firstrows = [11,11]
lastrows = [42,29]

#files=[prepend+str(postcode)+ext for postcode in postcodes]
#print(files)
value_sheets=[]
for postcode in postcodes:
    filename=prepend+str(postcode)+ext
    wb = load_workbook(filename=filename, read_only=True)
    value_lists=[]
    for i in range(len(sheets)):
        ws = wb[sheets[i]]
        value_list = [ws.cell(row=r,column=cols[i]).value for r in range(firstrows[i],lastrows[i]+1)]
        value_list.insert(0,postcode)
        value_lists.append(value_list)
    value_sheets.append(value_lists)

title_list=[]
for i in range(len(sheets)):
    ws = wb[sheets[i]]
    title_list.append(ws.cell(row=4,column=1).value)

category_lists=[]
for i in range(len(sheets)):
    ws = wb[sheets[i]]
    category_list = [ws.cell(row=r,column=1).value for r in range(firstrows[i],lastrows[i]+1)]
    category_list.insert(0,'PostCode')
    category_lists.append(category_list)

print(category_lists)
print(value_sheets)


from openpyxl import Workbook
wb = Workbook()



'''for i in range(len(sheets)):
    wsw = wb.create_sheet(category=sheets[i])
    wsw.append(category_lists[i])
    for c in range(len(postcodes)):
        wsw.append(value_sheets[c][i])'''

for i in range(len(sheets)):
    wsw = wb.create_sheet(title=sheets[i])
    wsw.cell(row=1,column=1).value=title_list[i]
    for r in range(firstrows[i],lastrows[i]+2):
        wsw.cell(row=r-firstrows[i]+2,column=1).value=category_lists[i][r-firstrows[i]]

for c in range(len(postcodes)):
    #print(postcodes[c])
    for i in range(len(sheets)):
        wsw = wb[sheets[i]]
        for r in range(firstrows[i],lastrows[i]+2):
            #print(r,",",c)
            #print(value_sheets[c][i][r-firstrow])
            wsw.cell(row=r-firstrows[i]+2,column=c+2).value=value_sheets[c][i][r-firstrows[i]]

#save the file
wb.save('compilation.xlsx')
