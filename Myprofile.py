name = age = number = mail = filtered_index = mail_add = add_info = bank_name = ""
ogrnip = inn = score =  bik = 0

Dev="----------------------------------------------"

def Inupdinfo():
   global name, age, number, mail, filtered_index, mail_add, add_info, ogrnip, inn, score, bank_name, bik
   print(Dev,"\nВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ\n1 - Личная информация\n2 - Информация о предпринимателе\n0 - Назад")
   menu = int(input("Введите номер пункта меню: "))
   if menu == 1:
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    number = input("Введите номер телефона: ")
    mail = input("Введите email: ")
    
    while True:
            index = input("Введите индекс: ")
            filtered_index = ""
            for char in index:
                  if '0' <= char <= '9':
                     
                     filtered_index += char
                     
            if filtered_index:  
               
                  print("Очищенное значение индекса: ",filtered_index)
                  
                  break
            else:
                  print("Ошибка: индекс должен содержать хотя бы одну цифру. Попробуйте снова.")
               
    mail_add = input("Введите дополнительный адрес: ")
    add_info = input("Введите дополнительную информацию: ")
   
   elif menu == 2:
      while True:
        count = 0
        ogrnip = int(input("Введите ОГРНИП (15 цифр): "))
        
        while ogrnip > 0:
            count += 1
            ogrnip //= 10
            
        if count == 15:
            break
         
        else:
            print("Ошибка: ОГРНИП должен содержать ровно 15 цифр. Попробуйте еще раз.")
            
      inn = int(input("Введите ИНН: "))
         
      while True:
        count = 0
        score = int(input("Введите расчетный счет (20 цифр): "))
        while score > 0:
            count += 1
            score //= 10
        if count == 20:
            break
        else:
            print("Ошибка: расчетный счет должен содержать ровно 20 цифр. Попробуйте еще раз.")
      bank_name = input("Введите название банка: ")
      bik = int(input("БИК и «Корреспондентский счёт: "))
   elif menu == 0:
      main()
   return Inupdinfo()

def Ininfo():
   global name, age, number, mail, filtered_index, mail_add, add_info, ogrnip, inn, score, bank_name, bik
   print(Dev,"\nВЫВЕСТИ ИНФОРМАЦИЮ\n1 - Общей информация\n2 - Вся информация\n0 - Назад")
   menu = int(input("Введите номер пункта меню: "))
   if menu == 1:
      print(Dev)
      print("Имя:",name)
      print("Возраст:", age)
      print("Телефон:", number)
      print("Электронная почта:", mail)
      print("Индекс:", filtered_index)
      print("Почтовый адрес:", mail_add)
      print("Дополнительная информация:", add_info)
      


   elif menu == 2:
       print(Dev)
       print("Имя:", name)
       print("Возраст:", age) 
       print("Телефон:", number)
       print("Электронная почта:", mail)
       print("Индекс:", filtered_index)
       print("Почтовый адрес:", mail_add)
       print("Дополнительная информация:", add_info)
       print(" ")
       print("Информация о предпринимателе")
       print("ОГРНИП:", ogrnip)
       print("ИНН:", inn)
       print("Расчётный счёт:", score)
       print("Название банка:", bank_name)
       print("БИК:", bik)
       

       
   elif menu == 0:
      main()
   
   return Ininfo()
      

      



def main():
   print("Приложение MyProfile\nСохраняй информацию о себе и выводи ее в разных форматах\n",Dev,"\nГЛАВНОЕ МЕНЮ\n1 - Ввести или обновить информацию\n2 - Вывести информацию\n0 - Завершить работу")
   menu = int(input("Введите номер пункта меню: "))
   if menu == 1:
      Inupdinfo()
   elif menu == 2:
      Ininfo()
   elif menu == 0:
      print("Работа завершена")
      return 0
      
   


main()

