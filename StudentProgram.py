import StudentClass as s

from datetime import date

def main():

    Id = 8911155
    name = 'John'
    dob = '02/28/1999'
    classification = 'Junior'

    Student = s.Student(Id,name,dob,classification)

    today = date.today().year
    
    Student.calc_age(today)
    Student.register_date(classification)

    print(Student.get_age())
    print(Student.get_registration())

main()