n,kolvenergy=map(int, input('').split())
ostan=list(map(int, input('').split())) #массив с остановками
flag=False
rasttoch=[] # массив с расстояниями между точками
for i in range(len(ostan)-1):
    rasttoch.append(ostan[i+1]-ostan[i])
samiki=0 #счётчик самокатов
lostenergy=0 #счётчик потраченной энергии
biba=0 #Счётчик проеханных точек
while biba < len(rasttoch):
    if rasttoch[biba]>kolvenergy: #если расстояние между точками больше макс запаса энергии(невозможно доехать), то остановка цикла
        flag = True
        break
    while biba < len(rasttoch) and lostenergy + rasttoch[biba] <= kolvenergy:
        lostenergy+=rasttoch[biba]
        biba+=1
    samiki+=1
    lostenergy = 0
if not flag:
    print(samiki)
else:
    print(-1)
