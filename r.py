import random
a=''
for i in range(1,100):
    a+="8 "+ str(random.randint(100,999))+ " " + str(random.randint(100,999)) + " " + str(random.randint(10,99)) + " "+ str(random.randint(10,99)) + "   "+ "Имя"+str(i) + "   "+ "_ "+"   "+ "_ "+ '\n'
print(a)