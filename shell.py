from credit.models import Client, Account, Credit 
import random

#Создаем клиентов

c1 = Client(name='Бердиев Н.Д.', birth_year = 1994, work_place='Codify')
c1.save()

c2 = Client(name='Шаршембаева Ч.М.', birth_year = 1990, work_place='НБКР')
c2.save()

# Создаем счета

def generate_number(n):
    min = pow(10, n-1)
    max = pow(10, n)-1
    return random.randint(min, max)
    
a1 = Account(number=generate_number(16), client=c1)
a1.save()
a2 = Account(number=generate_number(16), client=c1)
a2.save()
a3 = Account(number=generate_number(16), client=c2)
a3.save()
a4 = Account(number=generate_number(16), client=c2)
a4.save()

# Создаем кредиты

c1 = Credit(sum=1000, account=a1)
c1.save()
c2 = Credit(sum=2000, account=a2)
c2.save()
c3 = Credit(sum=3000, account=a3)
c3.save()
c4 = Credit(sum=4000, account=a4)
c4.save()






    
    





