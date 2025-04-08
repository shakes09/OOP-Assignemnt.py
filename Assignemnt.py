# Assignment 1: Design Your Own Class (Smartphone Example)

class Smartphone:
    def __init__(self, brand, model, color, storage):
        # Constructor to initialize the object attributes
        self.brand = brand       # Brand of the smartphone
        self.model = model       # Model name
        self.color = color       # Color of the smartphone
        self.storage = storage   # Storage size in GB

    def phone_info(self):
        # Method to get phone information
        return f"{self.brand} {self.model} - {self.color}, {self.storage}GB"

    def make_call(self, phone_number):
        # Method to simulate making a phone call
        print(f"Calling {phone_number}...")

    def take_picture(self):
        # Method to simulate taking a picture
        print("Picture taken!")

# Creating an instance of Smartphone
my_phone = Smartphone("Apple", "iPhone 13", "Black", 128)

# Output the smartphone information
print(my_phone.phone_info())

# Simulate calling and taking a picture
my_phone.make_call("123-456-7890")
my_phone.take_picture()

# Adding Inheritance and Polymorphism
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, color, storage, camera_quality):
        # Call the parent class constructor
        super().__init__(brand, model, color, storage)
        # Additional attribute for camera quality
        self.camera_quality = camera_quality

    def take_picture(self):
        # Overriding the method to show polymorphism
        print(f"Taking a high-quality {self.camera_quality}MP picture!")

# Creating an instance of SmartphoneWithCamera
my_camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S21", "Silver", 256, 108)

# Output the smartphone information
print(my_camera_phone.phone_info())

# Simulate calling and taking a picture (Polymorphism in action)
my_camera_phone.make_call("098-765-4321")
my_camera_phone.take_picture()


