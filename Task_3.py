'''
3.
class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """
'''
class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.info = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday, self.age, self.sex]

    def __str__(self):
        return f'All profile information: {self.info}'

if __name__ == '__main__':
    human = Profile('Ira', 'Semchuk', '098 618 3927', 'Lviv', 'iryna@gmail.com', '21.02.1999', '22', 'mate')

    print(human)