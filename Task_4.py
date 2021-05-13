'''
4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
and create an HPLaptop class by using your interface.
'''
from abc import abstractmethod, ABC

class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError

class HPlaptop(Laptop):
    def __init__(self, name, year, screen_type, keyboard_type, touchpad_type, webcam_type, port_type, dynamics_type):
        self.name = name
        self.year = year
        self.screen_type = screen_type
        self.keyboard_type = keyboard_type
        self.touchpad_type = touchpad_type
        self.webcam_type = webcam_type
        self.port_type = port_type
        self.dynamics_type = dynamics_type

    def screen(self):
        print(f'Screen: {self.screen_type}')

    def keyboard(self):
        print(f'Keyboard: {self.keyboard_type}')

    def touchpad(self):
        print(f'Touchpad: {self.touchpad_type}')

    def webcam(self):
        print(f'Webcam: {self.webcam_type}')

    def ports(self):
        print(f'Ports: {self.port_type}')

    def dynamics(self):
        print(f'Dynamics: {self.dynamics_type}')

if __name__ == '__main__':
    laptop = HPlaptop('HPlaptop', '2017', 'MVA', 'Butterfly keyboard', 'mat', 'Full HD', 'USB, LPT', 'OEM')

    laptop.screen()
    laptop.keyboard()
    laptop.touchpad()
    laptop.webcam()
    laptop.ports()
    laptop.dynamics()
