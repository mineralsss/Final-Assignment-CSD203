import random
class Airport:
    def __init__(self, id, cord, type):
        self.id = id
        self.cord = cord
        self.type = type
        self.connected_airport = []
    def __repr__(self):
        return f"{self.id}, {self.cord}, {self.type}, {self.connected_airport}"
class Airport_manager:
    def __init__(self):
        self.airports = []
        self.routes = []
        self.cost = []
    def show_airports(self):
        return self.airports

    def show_route(self):
        for each in self.airports:
            return each.connected_airport

    def create_route(self):
        for i in range(len(self.airports)):
            for j in range(len(self.airports)):
                if i != j:
                    self.add_route(self.airports[i], self.airports[j])

    def add_route(self, departure, destination):
        if departure in self.airports:
            if destination in self.airports:
                self.routes.append([departure, destination])
                self.cost.append(random.randint(1,10))
        else:
            return False

    def add_Airport(self, id, cord, type):
        new_Airport = Airport(id, cord, type)
        if new_Airport not in self.airports:
            self.airports.append(new_Airport)
        else:
            return False

    def del_Airport_byid(self, id):
        flag = False
        idx = 0
        for i in self.airports:
            idx += 1
            if id == i.id:
             flag = True
            else:
                flag = False
        if flag:
            tmp = self.airports[idx]
            self.airports.pop(idx)
            return tmp

    def udpdate_Airport_byid(self, id, cord, type):
        tmp = []
        for i in self.routes:
            if id == i.id:
                tmp = i
                i.id = id
                i.cord = cord
                i.type = type
            return tmp
    def cost_calculation(self, departure, destination):
        pass
    #im still lazy asf

am = Airport_manager()
am.add_Airport("A", "x", "X")
print(am.show_airports())