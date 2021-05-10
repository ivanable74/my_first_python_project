try:
    a = input()
    b = input()
    while(b!='='):
        a += b
        a = eval(a)
        a = str(a)
        b = input()
        print(a)
except TypeError:
    print("Некорректный ввод. Введите число")    
except SyntaxError:
    print("Некорректный ввод. Введите число") 
