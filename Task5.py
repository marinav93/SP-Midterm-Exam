
n = int(input("unesite n: "))
b=n
c=n

x=[]
ProizvodGlavne=1
ProizvodSporedne=1
for i in range(n):
    x.append([])
    for j in range(n):
        x[i].append(broj)
        if i==j:
            ProizvodGlavne+=broj
        if i+j==(n-i-1):
            ProizvodSporedne+=broj
        broj+=1
print ('\n')
print("Generisana matrica: ")
for vektor in x:
    print(vektor)
print ('\n')
print("Zbir elemenata glavne dijagonale je: "+str(ProizvodGlavne))
print("Zbir elemenata sporedne dijagonale je: "+str(ProizvodSporedne))

print("ZbirProizvoda je "+str(ProizvodGlavne+ProizvodSporedne))
