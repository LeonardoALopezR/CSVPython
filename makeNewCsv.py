import csv
import itertools

lines=(['No. Pedido','Nombre','Mail','Telefono','Telefono de facturacion','Canasta','Club','Dia Pagado','Total','Tortilla Blanca','Tortilla Azul','Queso','Huevo','Pan organico de La Sastreria del Pan'],)
otherLine=(['','','','','','','','','','','','','',''],)
f1 = open("orders_export.csv")
f2 = open("customers_export.csv")

countLine = 0
countLine2= 0
orderNumber = 0

csv_f1 = csv.reader(f1)
csv_f2 = csv.reader(f2)

for row1 in itertools.izip_longest(csv_f1):
    if countLine == 0:
        pass
    else:
        print row1[0][0]
        entrega = row1[0][17].split()
        if orderNumber == row1[0][0] or len(entrega)< 6:
            print "Extras"

        else:
            print "No"
            countLine2 =0
            for row2 in itertools.izip_longest(csv_f2):
                if countLine2==0:
                    print "Norrl"
                else: 
                    if row2[0][2]==row1[0][1]:
                        entrega = row1[0][17].split()
                        print "-->",entrega
                        club = row2[0][17].split()
                        print "a--->",club
                        club = ' '.join(map(str, club[1:]))
                        otherLine = otherLine + ([row1[0][0],row2[0][0]+' '+row2[0][1],row1[0][1],row2[0][12],row1[0][33],entrega[6],club,row1[0][3][:10],row1[0][11],'','','','',''],)
                        print otherLine
                    else:
                        print row1[0][0], row2[0][0]
                countLine2 += 1
        orderNumber = row1[0][0]
    countLine += 1
    f2.seek(0) 
    next(csv_f2)
print countLine
with open('entrega.csv', 'wb') as writeFile:
    writer = csv.writer(writeFile,delimiter=',')
    writer.writerows(lines) 
    writer.writerows(otherLine) 