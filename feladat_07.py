import random

def alahuzas(valtozó):
    print(valtozó)
    print('-----------')

# 1 feladat
szám1=int(input('Adj meg egy számot! '))
print(szám1)
# wr.write(f'{szám1}\n')
szám2=random.randint(10,50)
print(szám2)
# wr.write(f'{szám2}\n')
SZÁM3 = 15
print(SZÁM3)
# wr.write(f'{SZÁM3}\n')

alahuzas([szám1,szám2,SZÁM3])


# 2 feladat
szám2=random.randrange(10,50,3)
print(szám2)
alahuzas([szám1,szám2,SZÁM3])

if szám2%2 ==0:
    szám2+=1

while szám2%2 ==0:
    szám2=random.randint(10,50)
alahuzas([szám1,szám2,SZÁM3])
# wr.write(f'{szám2}\n')
# 3 feladat
if szám1%2 ==0:
    print('Páros a beírt szám.')
    # wr.write('Páros a beírt szám.\n')
else:
    print('Nem páros a beírt szám.')
    # wr.write('Nem páros a beírt szám.\n')
alahuzas([szám1,szám2,SZÁM3]) 
# 4 feladat
számok=[]
számok.append(szám1)
számok.append(szám2)
számok.append(SZÁM3)

print(számok)
# wr.write(f'{számok}\n')

print(számok.count(4))
# wr.write(f'{számok.count(4)}\n')
print(számok[1])
# wr.write(f'{számok[1]}\n')
számok.extend([10,5,4])
print(számok)
# wr.write(f'{számok}\n')
számok.sort()
print(számok)
# wr.write(f'{számok}\n')
számok.reverse()
print(számok)
alahuzas([szám1,szám2,SZÁM3])
# wr.write(f'{számok}\n')

#5 feladat
halmaz={szám1,szám2,SZÁM3}

print(halmaz)
# wr.write(f'{halmaz}\n')

halmaz.add(25)
print(halmaz)
# wr.write(f'{halmaz}\n')
halmaz.discard(25)
print(halmaz)
# wr.write(f'{halmaz}\n')
halmaz.add(50)
print(halmaz)
# wr.write(f'{halmaz}\n')
halmaz.add(45)
print(halmaz)
# wr.write(f'{halmaz}\n')
halmaz.pop()
print(halmaz)
alahuzas([szám1,szám2,SZÁM3])
# wr.write(f'{halmaz}\n')

# 6 feladat kontexstus kezelő
with open('feladat_07.txt','w') as file:
    file.write(str(számok))
    file.close()

file=open('feladat_07.txt','r')
line=file.readline()
while line !="":
    # alahuzas(line)
    line = file.readline()
file.close()
alahuzas([szám1,szám2,SZÁM3])
