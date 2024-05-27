# lib/dog.py

class Dog:
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

# Testing the Dog class
if __name__ == "__main__":
    fido = Dog()
    fido.bark()  # Output: Woof!
    fido.sit()   # Output: The dog is sitting.

    snoopy = Dog()
    snoopy.bark()  # Output: Woof!
    snoopy.sit()   # Output: The dog is sitting.
