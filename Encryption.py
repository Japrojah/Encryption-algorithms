#powered by @japrojah
def function_RSA():             #Назначение функции на исполнение алгоритма RSA
    z = 1
    v = 0                      
    print("Выбран шифр RSA")
    
    while (z==1):
        print("Введите сообщение: ")
        m = int(input())
        print("Введите значение P: ")
        p = int(input())
        print("Введите значение Q: ")
        q = int(input())
        print("Введите значение E: ")
        e = int(input())
        print('Вы ввели точные данные?\nДа-1, Нет-2')
        v = int(input())
        if (v==1):
            z = 0


    n = p * q
    print("n =",n)
    Fn = (p - 1) * (q - 1)
    print("Fn =",Fn)

    r1=Fn
    r2=e

    while (r2!=0):
        q=r1//r2
        r=r1-r2*q
        r1=r2
        r2=r
    if(r1==1) & (e<Fn):
        print ('e = ', e)
        r1=Fn
        r2=e
        t1=0
        t2=1
        w=r1
        while (r2!=0):
            q=r1//r2
            r=r1-q*r2
            t=t1-q*t2
            r1=r2
            r2=r
            t1=t2
            t2=t

        if t1<0:
            while t1<0:
                t1=t1+w

        d=t1
        print('d = ', d)



        Cm = m**d % n  
        print("Зашифрованное сообщение:",Cm)
        Dm = Cm**e % n  
        print("Расшифрованное сообщение:",Dm)
        print('Цифровая подпись: (', m, ', ', Cm, ')')


def function_EGSA():                 #Алгоритм EGSA
    z = 1
    v = 0                             
    print("Выбран шифр EGSA")

    while (z==1):    
        print("Введите сообщение: ")
        m = int(input())
        print("Введите значение P: ")
        p = int(input())
        print("Введите значение G: ")
        g = int(input())
        print("Введите значение X: ")
        x = int(input())
        print("Введите значение K: ")
        k = int(input())
        print('Вы ввели точные данные?\nДа-1, Нет-2')
        v = int(input())
        if (v==1):
            z = 0


    y = g ** x % p  
    print('y =',y)
    a = g ** k % p  
    print('a =',a)

    P=p-1

    r1=P
    r2=k

    while(r2!=0):
        q=r1//r2
        r=r1-r2*q
        r1=r2
        r2=r
    if(r1==1) & (1<k) & (k<P):
        r1=P
        r2=k
        t1=0
        t2=1
        w=r1
        while(r2!=0):
            q=r1//r2
            r=r1-r2*q
            t=t1-t2*q
            r1=r2
            r2=r
            t1=t2
            t2=t
    
    if  (t1<0):
        while (t1<0):
            t1=t1+w

    b=(t1*(m-x*a))%P
    print('b = ', b)

    print('Цифровая подпись: (', m, ', ', a, ', ', b, ')')



    A1 = int(((y ** a) * ( a ** b)) % p)
    print('A1 =',A1)
    A2 = g ** m % p
    print('A2 =',A2)

    if (A1==A2):
        print('Цифровая подпись подлина!')
    else:
        print('Цифровая подпись не верна')


def function_DSA():               #Начало алгоритма DSA
    z = 1
    v = 0                       
    print("Выбран шифр DSA")
    
    while (z==1):
        print("Введите сообщение (m): ")
        m = int(input())
        print("Введите значение g: ")
        g = int(input())
        print("Введите значение p: ")
        p = int(input())
        print("Введите значение q: ")
        q = int(input())
        print("Введите значение x: ")
        x = int(input())
        print("Введите значение k: ")
        k = int(input())
        print('Вы ввели точные данные?\nДа-1, Нет-2')
        v = int(input())
        if (v==1):
            z = 0



    y = g ** x % p
    print("y = ", y)
    R =int(((g ** k )% p) % q)
    print("r = ", R)

    r1=q
    r2=k
    t1=0
    t2=1
    w=r1
    while (r2!=0):
        Q=r1//r2
        r=r1-r2*Q
        t=t1-Q*t2
        r1=r2
        r2=r
        t1=t2
        t2=t

        if t1<0:
            while t1<0:
                t1=t1+w
    print('t1 = ', t1)
            


    s = int((m + R * x) * t1) % q
    print("s = ", s)

    print('Электронная подпись: (', m,', ', R, ', ', s,')')

    r1=q
    r2=s
    t1=0
    t2=1
    w=r1

    while (r2!=0):
        Q=r1//r2
        r=r1-r2*Q
        t=t1-Q*t2
        r1=r2
        r2=r
        t1=t2
        t2=t
    if t1<0:
        while t1<0:
            t1=t1+w
        
    W = int(t1%q)
    print("w = ", W)
    u1=int((m*W)%q)
    print("u1 = ", u1)
    u2 =int((R*W)%q)
    print("u2 = ", u2)
    V = (((g ** u1) * (y ** u2)) % p) % q  
    print("V = ", V)
    if (R==V):
        print('R=V Электронная подпись верна')
    else: ('Электронная не верна')


def function_GOST():                      #Алгоритм GOST
    Z = 1
    v = 0                         
    print("Выбран шифр GOST")

    while(Z==1):
        print("Введите сообщение(m): ")
        m = int(input())
        print("Введите значение g: ")
        g = int(input())
        print("Введите значение p: ")
        p = int(input())    
        print("Введите значение q: ")
        q = int(input())
        print("Введите значение x: ")
        x = int(input())    
        print("Введите значение k: ")
        k = int(input())
        print('Вы ввели точные данные?\nДа-1, Нет-2')
        v = int(input())
        if (v==1):
            Z = 0
    


    y = g ** x % p
    print("y = ",y)
        
    r =int(((g ** k )% p) % q)  
    print("r = ",r)
    s = int(((k * m) + (x * r)) % q)  
    print("S = ",s)

    print('Электронная подпись: (', m,', ', r, ', ', s,')')

    v = int((m ** (q - 2)) % q)
    print("V = ",v)
    u1 = int((s * v) % q)
    u2 = int(((q-r) * v) % q)
    R = int((((g ** u1) * (y ** u2)) % p) % q)
    print("R = ",R)
    if (r==R):
        print('r=R Электронная подпись верна')
    else: 
        print('Электронная не верна')

# рабочее тело программы

print("Выберете способ шифрования: \nRSA-1   EGSA-2   DSA-3   GOST-4   Выход-5 ")

l = int(input())

while (l!=5):
    if (l==1):
        function_RSA()
        print("Выберете способ шифрования: \nRSA-1   EGSA-2   DSA-3   GOST-4   Выход-5 ")
        l = int(input())
    elif (l==3):
        function_DSA()
        print("Выберете способ шифрования: \nRSA-1   EGSA-2   DSA-3   GOST-4   Выход-5 ")
        l = int(input())
    elif(l==4):
        function_GOST()
        print("Выберете способ шифрования: \nRSA-1   EGSA-2   DSA-3   GOST-4   Выход-5 ")
        l = int(input())
    else:
        function_EGSA()
        print("Выберете способ шифрования: \nRSA-1   EGSA-2   DSA-3   GOST-4   Выход-5 ")
        l = int(input())



print("До свидания\nСпасибо, что пользуетесь нашим софтом")

