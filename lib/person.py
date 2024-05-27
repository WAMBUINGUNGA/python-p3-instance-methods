#!/usr/bin/env python3

# lib/person.py

class Person:
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

# Testing the Person class
if __name__ == "__main__":
    john = Person()
    john.talk()  # Output: Hello World!
    john.walk()  # Output: The person is walking.

