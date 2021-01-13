"""
Task 1
A Person class
Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them
as attributes. Make another method called talk() which makes prints a greeting from the person containing, for example
like this: “Hello, my name is Carl Johnson and I’m 26 years old”.
"""


class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname.title()} {self.lastname.title()} and I’m {self.age} years old")


if __name__ == "__main__":
    person = Person("ivanka", 'hnybediuk', 24)
    person.talk()



"""
Task 2
Doggy age
Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age. 
Then create a method `human_age` which returns the dog’s age in human equivalent.
"""


class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * self.age_factor


if __name__ == "__main__":
    my_dog = Dog(9)
    print(my_dog.human_age())

"""
Task 3
TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' 
exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.
```
CHANNELS = ["BBC", "Discovery", "TV1000"]
 class TVController:
pass
 controller = TVController(CHANNELS)
controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"
"""

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    currentChanel = 1

    def __init__(self, chanels):
        self.chanels = chanels

    def first_channel(self):
        self.currentChanel = 1
        return self.chanels[self.currentChanel - 1]

    def last_channel(self):
        self.currentChanel = -1
        return self.chanels[self.currentChanel]

    def turn_channel(self, numb):
        self.currentChanel = numb
        return self.chanels[self.currentChanel - 1]

    def next_channel(self):
        if self.currentChanel == len(self.chanels):
            self.currentChanel = 1
        else:
            self.currentChanel += 1
        return self.chanels[self.currentChanel - 1]

    def previous_channel(self):
        if self.currentChanel == 1:
            self.currentChanel = len(self.chanels)
        else:
            self.currentChanel -= 1
        return self.chanels[self.currentChanel - 1]

    def current_channel(self):
        return self.chanels[self.currentChanel - 1]

    def is_exist(self, arg):
        if type(arg) == int:
            try:
                self.chanels[arg - 1]
                return "Yes"
            except IndexError:
                return "No"
        else:
            if arg in self.chanels:
                return "Yes"
            else:
                return "No"


if __name__ == "__main__":
    controller = TVController(CHANNELS)
    print(controller.first_channel())
    print(controller.last_channel())
    print(controller.turn_channel(1))
    print(controller.next_channel())
    print(controller.previous_channel())
    print(controller.current_channel())
    print(controller.is_exist(4))
    print(controller.is_exist("BBC"))
