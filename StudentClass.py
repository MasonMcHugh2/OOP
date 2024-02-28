class Student:

    

    def __init__(self,Id,name,dob,classification):
        self.__Id = Id
        self.__name = name
        self.__dob = dob
        self.__classification = classification


    def calc_age(self,today):
        days = self.__dob.split('/')
        self.__age = today - int(days[2])

    def register_date(self,classification):
        self.__registration = {'Senior': '4/1 thru 4/3',
                        'Junior': '4/4 thru 4/6',
                        'Sophomore': '4/7 thru 4/9',
                        'Freshman': '4/10 thru 4/12'} 
        
        
        if classification in self.__registration:
            self.__register_date = f"{classification} register in the dates {self.__registration[classification]}"   
    
    def get_age(self):
        return self.__age
    
    def get_registration(self):
        return self.__register_date
    
