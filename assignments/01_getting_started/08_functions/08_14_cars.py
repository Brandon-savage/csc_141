def make_car(manufacturer, model, **car_info):
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car("Bmw", "M4", color="Jet black", year=2024)
print(car)