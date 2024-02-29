class RetailItem:

    def __init__(self,Obj1,Obj2,Obj3):
        self.__Obj1 = Obj1
        self.__Obj2 = Obj2
        self.__Obj3 = Obj3

    def set_obj1(self):
        self.__Obj1_name = input('Enter the first retail item: ')
        self.__Obj1_inventory = input('Enter the amount of the first retail item: ')
        self.__Obj1_price = input('Enter the price of the first retail item: ')

    def set_obj2(self):
        self.__Obj2_name = input('Enter the second retail item: ')
        self.__Obj2_inventory = input('Enter the amount of the second retail item: ')
        self.__Obj2_price = input('Enter the price of the second retail item: ')

    def set_obj3(self):
        self.__Obj3_name = input('Enter the third retail item: ')
        self.__Obj3_inventory = input('Enter the amount of the third retail item: ')
        self.__Obj3_price = input('Enter the price of the third retail item: ')

    def get_obj1(self):
        return self.__Obj1_name, self.__Obj1_inventory, self.__Obj1_price
    
    def get_obj2(self):
        return self.__Obj2_name, self.__Obj2_inventory, self.__Obj2_price
    
    def get_obj3(self):
        return self.__Obj3_name, self.__Obj3_inventory, self.__Obj3_price
    
    