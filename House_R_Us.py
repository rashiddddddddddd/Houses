class House:
    def __init__(self, house_number, rooms, rent, rented, lease_expiry_days, next_inspection, tenant):
        self.house_number = house_number
        self.rooms = rooms
        self.rent = rent
        self.rented = rented
        self.lease_expiry_days = lease_expiry_days
        self.next_inspection = next_inspection
        self.tenant = tenant


class Houses:
    def __init__(self):
        self.house_list = []


    def search_house(self, attribute, value):
        if attribute == '1': ##num_rooms
            for i in range(len(self.house_list)):
                if (self.house_list[i].rooms == value) and (self.house_list[i].lease_expiry_days <= 60):
                    print(f'House number {self.house_list[i].house_number} available in {self.house_list[i].lease_expiry_days} days')

        if attribute == '2': ##rent
            for i in range(len(self.house_list)):
                if (self.house_list[i].rent <= value) and (self.house_list[i].lease_expiry_days <= 60):
                    print(f'House number {self.house_list[i].house_number} available in {self.house_list[i].lease_expiry_days} days')

