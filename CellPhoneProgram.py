import CellPhoneClass as c

def main():

    manufact = input('Enter the manufacturer of the phone: ')
    model = input('Enter the model of the phone: ')
    price = input('Enter the price of the phone: ')

    Cell_phone = c.Phone(manufact,model,price)

    manu_change = input('Would you like to change the manufacturer? (y/n) ')
    if manu_change == 'y':
        new_manu = input('Please enter new manufacturuer: ')
        manufact = new_manu
    else:
        print(f"The manufacturer is: {manufact}")
        
    Cell_phone.set_manufact(manufact)

    model_change = input('Would you like to change the model? (y/n) ')
    if model_change == 'y':
        new_model = input('Please enter new model: ')
        model = new_model
    else:
        print(f"The model is: {model}")

    Cell_phone.set_model(model)

    price_change = input('Would you like to change the price? (y/n) ')
    if price_change == 'y':
        new_price = input('Please enter new price: ')
        price = new_price
        print(f'The new price is: {price}')
    else:
        print(f"The price is: {price}")

    Cell_phone.set_retail_price(price)

    print(Cell_phone.get_manufact())
    print(Cell_phone.get_model())
    print(Cell_phone.get_retail_price())

main()