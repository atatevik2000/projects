class Phonebook():
    def __init__(self, book):
        self.book = book



    def get_phone_number(self):
        def phone_info():
            number = input("Add the phone number. \n")
            boo = False
            while boo == False :
                for i in number:
                    if i.isdigit() and len(number) == 6:
                        boo = True
                        return number
                    else:
                        number = input("Add the phone number. It should contain 6 digits.### \n")
                        boo == False
        new_name = input("Input user`s name. \n")
        if self.book.get(new_name) == None:
            new_phone = phone_info()
            self.book[new_name] = new_phone
        else:
            choose= input("If you want to modify user`s number, press 'm'.\nIf you want to get user`s name, press ENTER.\n")
            if choose == 'm':
                new_phone = phone_info()
                self.book[new_name] = new_phone
            else:
                print(new_name,"`s phone number is ", self.book.get(new_name))

    def info(self, book):
        for i in self.book:
            print("{:<15}  ---  {:<6}".format(i,self.book[i]))


b= {"Tatevik":'654321', "Harut":'543210', "Gayane": '987654', "Ruben":'753467',"Sofiya":'366543'}
phone = Phonebook(b)
phone.info(b)
while True:
    phone.get_phone_number()
    ex = input("If you want to print Phone Book, input 'book'.\nIf you want to exit, input 'exit'.\nElse press ENTER.\n")
    if ex == 'exit':
        break
    elif ex == 'book':
        phone.info(b)
        ex = input("If you want to exit, input 'exit'. Else press ENTER\n")
        if ex == 'exit':
            break


