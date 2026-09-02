


class HumanClass:
    def __init__(self, name, age, gender, living_address, civil_status, is_foreigner=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.living_address = living_address
        self.civil_status = civil_status
        
        self.is_foreigner = is_foreigner



    def get_information(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.living_address)
        print(self.civil_status)
        return self.name, self.age, self.gender, self.living_address, self.civil_status
    
    
    
    def move_in_to_appartment(self, apartment_name : str) -> None:
        
        print(self.name, " wants to move in at apartment : ", apartment_name)
        self.living_address = apartment_name

    def change_living_address(self, current_address : str) -> None:
        old_address = self.living_address
        self.living_address = current_address
        print(self.name, 'has changed the address, from: ', old_address, ' to: ', current_address)

    def set_age(self,age: int) -> None:
        self.age = age

    def set_civil_status(self,civil_status:str) -> None:
        self.civil_status = civil_status

    def set_gender(self,gender: str) -> None:
        self.gender = gender

    def get_age(self) -> int:
        return self.age




