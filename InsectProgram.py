import InsectClass as i


mosquito = i.Insect(2,4,'Mosquito')
housefly = i.Insect(2,4,'Housefly')

mosquito.calc_flight()
housefly.calc_flight()


print(f'The {mosquito.get_name()} can travel up to {mosquito.get_flight()} miles')
print(f'The {housefly.get_name()} can travel up to {housefly.get_flight()} miles')

