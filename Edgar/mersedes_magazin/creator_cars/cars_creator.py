import os, json


class Cars:
    def __init__(self):
        self.path = os.getcwd() + r"\creator_cars\cars.json"
        with open(self.path, 'r') as file:
            text = file.read()
            self.cars = json.loads(text)

    def update_cars(self):
        new_cars = json.dumps(self.cars, indent=4)
        with open(self.path, 'w') as file:
            file.write(new_cars)

    def Cars_add_creator(self, name, date, info, price):
        new_cars_id = self.cars['cars'][-1]['id'] + 1
        self.cars['cars'].append({'id': new_cars_id, 'name': name, 'date': date, "info": info, 'price': price})
        self.update_cars()

