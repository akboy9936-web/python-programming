#polymorphism
#method overriding
class phone:
    def camera(self):
        print("taking a normal photo")
class smartphone(phone):
    def camera(self):
        print("taking a portrait photo")
samsung=smartphone()
samsung.camera()
nokia=phone()