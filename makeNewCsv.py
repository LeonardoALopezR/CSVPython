#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import itertools

lines=(['No. Pedido','Nombre','Mail','Telefono','Telefono de facturacion','Canasta','Club','Dia Pagado','Total','Tortilla Blanca','Tortilla Azul','Queso','Huevo','Pan integral','Panque integral te verde','Pan integral multigrano','Miel','Frijol','Jitomate','Rosca','Cafe','Pan de caja integral','Panque integral platano','Panque brioche','Panque sin gluten platano','Plan de caja blanco','Pan integral matcha','Panque sin gluten','Pan caja canela y pasas','Panque red velvet','Panque sin gluten matcha','Red velvet','Pan de caja blanco multigrano','Lechuga PZ','Acelga KG','Mermelada mango','Salsa Xoconostle','Sal'],)
userLines=(['Pagina','Nombre','Canasta','Dia','Club','Email','Telefono','Dia Pagado','Pago'],)
heather=(['Encabezado'],)
otherLine=[]
otherUserLine=[]

with open('orders_export.csv', encoding='utf-8', mode='rt') as f, open('sorted.csv', encoding='utf-8', mode='w', newline='') as final:
    writer = csv.writer(final, delimiter=',')
    reader = csv.reader(f, delimiter=',')
    next(reader)
    sorted2 = sorted(reader, key=lambda row: (str(row[1]), str(row[17]))) 
    writer.writerows(heather)       
    for row in sorted2: 
        writer.writerow(row)

f1 = open("sorted.csv", encoding='utf-8')
f2 = open("customers_export.csv", encoding='utf-8')
f3 = open("allUsers.csv", encoding='utf-8')

countLine = 0
countLine2= 0
countLine3= 0
orderNumber = 0
index = 0

csv_f1 = csv.reader(f1)
csv_f2 = csv.reader(f2)
csv_f3 = csv.reader(f3)

for row1 in itertools.zip_longest(csv_f1):
    if countLine == 0:
        pass
    else:
        entrega = row1[0][17].split()
        # print row1[0][1], orderNumber, len(entrega)
        if orderNumber == row1[0][1] or len(entrega)< 6:
            products = {
                " Blanca":9,
                " Azul":10,
                "Queso":11,
                "Huevo":12
            }
            subtot = row1[0][16]
            
            try:
                splited = row1[0][17].split('-')
                # print splited[1]
                otherLine[index-1][products[splited[1]]]=subtot
            except:
                try:
                    splited = row1[0][17].split(' ')
                    # print splited[0],row1[0][17].find('Medio kilo')
                    if(row1[0][17].find('Medio kilo') != -1):
                        otherLine[index-1][products[splited[0]]]="0.5"
                    else:
                        otherLine[index-1][products[splited[0]]]=subtot
                except:
                    pass
            # print ">>>>>>>>",row1[0][17],"<<<<<<<<",otherLine[index-1]
            # try:
            
            # except:
                # print "This is an error message!"

        else:
            # print "No"
            countLine2 =0
            countLine3 =0
            for row3 in itertools.zip_longest(csv_f3):
                # print 'aaaaaaaaaaa',row3[0][4],row1[0][1]
                if countLine2==0:
                    pass
                else:
                    if row3[0][4]==row1[0][1]:
                        otherUserLine.append(['p',row3[0][0],row3[0][1],row3[0][2],row3[0][3],row3[0][4]+" ",row3[0][5],row1[0][3][:10],row1[0][11]])
                    else:
                        pass
                countLine3 += 1
            for row2 in itertools.zip_longest(csv_f2):
                if countLine2==0:
                    pass
                else: 
                    if row2[0][2]==row1[0][1]:
                        entrega = row1[0][17].split()
                        # print "-->",entrega
                        club = row2[0][17].split()
                        # print "a--->",club
                        club = ' '.join(map(str, club[1:]))
                        index += 1
                        otherLine.append([row1[0][0],row2[0][0]+' '+row2[0][1],row1[0][1],row2[0][12],row1[0][33],entrega[6],club,row1[0][3][:10],row1[0][11],'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
                        # temp=([row1[0][0],row2[0][0]+' '+row2[0][1],row1[0][1],row2[0][12],row1[0][33],entrega[6],club,row1[0][3][:10],row1[0][11]],)
                        # print otherLine
                    else:
                        pass
                countLine2 += 1
        orderNumber = row1[0][1]
    countLine += 1
    f2.seek(0) 
    next(csv_f2)
    f3.seek(0) 
    next(csv_f3)
# print countLine
with open('entrega.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile,delimiter=',')
    writer.writerows(lines) 
    writer.writerows(otherLine) 

with open('entrega.csv', mode='rt') as f, open('entrega_final.csv', 'w') as final:
    writer = csv.writer(final, delimiter=',')
    reader = csv.reader(f, delimiter=',')
    next(reader)
    sorted2 = sorted(reader, key=lambda row: (str(row[6]))) 
    writer.writerows(lines)       
    for row in sorted2: 
        writer.writerow(row)

with open('entrega_usuarios.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile,delimiter=',')
    writer.writerows(userLines) 
    writer.writerows(otherUserLine) 

with open('entrega_usuarios.csv', mode='rt') as f, open('entrega_usuarios_final.csv', 'w') as final:
    writer = csv.writer(final, delimiter=',')
    reader = csv.reader(f, delimiter=',')
    next(reader)
    sorted2 = sorted(reader, key=lambda row: (str(row[4]))) 
    writer.writerows(userLines)       
    for row in sorted2: 
        writer.writerow(row)
