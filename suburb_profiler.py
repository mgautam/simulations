from openpyxl import load_workbook

postcodes=[3087,3141,3178,3175,3138,3977]
prepend='GCP_POA'
ext='.xlsx'
sheet='G 29'
col=4
firstrow = 11
lastrow = 29

files=[prepend+str(postcode)+ext for postcode in postcodes]
print(files)
value_lists=[]
for postcode in postcodes:
    filename=prepend+str(postcode)+ext
    wb = load_workbook(filename=filename, read_only=True)
    ws = wb[sheet]
    value_list = [ws.cell(row=r,column=col).value for r in range(firstrow,lastrow+1)]
    value_list.insert(0,postcode)
    value_lists.append(value_list)#.insert(0,postcode))

title_list = [ws.cell(row=r,column=1).value for r in range(firstrow,lastrow+1)]
title_list.insert(0,'PostCode')

#print(title_list)
#print(value_lists)


from openpyxl import Workbook
wb = Workbook()

wsw = wb.create_sheet(title=sheet)

'''wsw.append(title_list)
for value_list in value_lists:
    wsw.append(value_list)'''

num_rows=lastrow-firstrow-1
#print(num_rows)
for r in range(firstrow,lastrow+2):
    wsw.cell(row=r-firstrow+1,column=1).value=title_list[r-firstrow]
for c in range(len(postcodes)):
    #print(postcodes[c])
    for r in range(firstrow,lastrow+2):
        #print(r,",",c)
        #print(value_lists[c][r-firstrow])
        wsw.cell(row=r-firstrow+1,column=c+2).value=value_lists[c][r-firstrow]

#save the file
wb.save('compilation.xlsx')
