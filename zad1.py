


class Human:

    default_name = "Антон"
    default_age = 22

    #Конструктор класса
    def __init__(self, name = default_name, age = default_age):
        #Публичные свойства
        self.name = name    #Имя
        self.age = age      #Возраст

        #Приватные свойства
        self.__money = 0    #Деньги
        self.__house = None

    #Метод  вывода информации
    def info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Наличие дома: {self.__house}")
        print(f"Деньги: {self.__money}")


    def default_info(self):
        print(f"Имя по умолчанию: {Human.default_name}")
        print(f"Возраст по умолчанию: {Human.default_age}")


    def __make_deal(self, house, price):

        self.__money -= price

        self.__house = house


    def earn_money(self, sum):
        self.__money += sum

    #Метод для проверки денег и покупки дома
    def buy_house(self, house):

        if self.__money >= house._House__price: 
            print(f"Сделка состоялась! Дом куплен")
            self.__make_deal(house, house._House__price)
        #Иначе не состоится сделка
        else:
            print(f"Недостаточно средств!")



#Унаследованный класс
class House(Human):
    def __init__(self, area, price, name = Human.default_name, age = Human.default_age):

        super().__init__()

        self.__area = area
        self.__price = price

    def final_price(self, discount):
        #Скидка
        size_discount = self.__price * (discount / 100)

        return self.__price - size_discount
    



class SmallHouse(House):
    def __init__(self, price):
        #Конструктор унаследованного класса 
        super().__init_(area = 40, price = price)
        #Вывод информации о классе
        print(f"Маленький дом с площадью - 40 квадратных метров")

# Часть 4

#Вызов справочного метода
Human.default_info()


human = Human("Вася", 33)

#Вывод справочной инф
human.info()


small_house = SmallHouse(price = 1000000)

#Попытка купить  дом
human.buy_house(small_house, discount = 0)

#Поправление финанс
human.earn_money(2000000)


human.buy_house(small_house, discount = 0)


human.info()





