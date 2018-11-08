
suma = 0
broj =0
while True:
    num = input("Unesi broj ili =: ")

    if num !='=':

        if int(num) % 3==0 and int(num) % 5 !=0:

            suma += int(num)
            broj +=1
    else:

        print("Rezultat je " + str (suma/broj) + ".")
        break