import RetailItemClass as r

def main():
    Obj1 = ''
    Obj2 = ''
    Obj3 = ''

    Space = ' ' * 10

    RetailItem = r.RetailItem(Obj1,Obj2,Obj3)

    RetailItem.set_obj1()

    RetailItem.set_obj2()

    RetailItem.set_obj3()

    print(RetailItem.get_obj1())
    print(RetailItem.get_obj2())
    print(RetailItem.get_obj3())

    O1_n, O1_i, O1_p = RetailItem.get_obj1()
    O2_n, O2_i, O2_p = RetailItem.get_obj2()
    O3_n, O3_i, O3_p = RetailItem.get_obj3()

    print(f"{Space} {'Description':12} {'Units in inventory':18} {'Price':6}")
    print()
    print(f"{'Item 1:':10} {O1_n:12} {O1_i:18} {O1_p:6}")
    print()
    print(f"{'Item 2:':10} {O2_n:12} {O2_i:18} {O2_p:6}")
    print()
    print(f"{'Item 3:':10} {O3_n:12} {O3_i:18} {O3_p:6}")

main()    