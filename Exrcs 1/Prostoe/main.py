while(True):
    a = input()
    try:
        a = int(a)
        i = 2
        while(i*i <= a and a%i!=0):
            i+=1
        if(i*i > a):
            print(a, "-", "Простое число")
        else:
            print(a, "-", "Сложное число")
    except ValueError:
        print("Некорректный ввод. Введите число")         
    
