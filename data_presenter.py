##2
cupcakes_invoices = open("CupcakeInvoices.csv")

##3
#for cupcakes in cupcakes_invoices:
    #print(cupcakes)
##4
#cupcake_types = []

#for cupcakes in cupcakes_invoices:
#    cupcakes = cupcakes.rstrip('\n').split(',')
#    cupcake_types.append(cupcakes[2])
#print(cupcake_types)

##5
invoice = []

for num in cupcakes_invoices:
    num = num.rstrip('\n').split(',')
    quantity = int(num[3])*float(num[4])
    invoice.append(quantity)
print(invoice)

##6
def sum(list):
    sum = 0

    for i in list:
        sum = sum + i
    return(sum)
print(sum(invoice))


cupcake_invoices.close()

