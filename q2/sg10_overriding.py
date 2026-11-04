class Animal:
    def __init__(self,name):
        self.name = name

        # the name attribute is common to all animals, so it is defined in the parent class
        # init basically means that the attributes of the class wll be initialized upon the creation of the object of the class

    def make_sound(self):
        pass  # this method will be overridden in subclasses

    def eat(self):
        pass 
    
     # the eat() will also be overridden in subclasses
    # since ths is the parent class, defining the method eat() and make_sound() means that every subclass will have the aforementioned methods
    # since animal is not yet entirely speciific and it is only where the subclasses will be derived from 1ST PART
    # it is kumbaga not yet fully defned in a sense that they any other part of this code interacting with these objects 2ND PART
    # will call the eat() and make_sound() methods without needing to knw the specific kind of animal or object it is

class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} roars loudly!")

    def eat(self):
        print(f"{self.name} eats fresh meat.")

class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} trumpets!")

    def eat(self):
        print(f"{self.name} eats grass and fruits.")

class Monkey(Animal):
    def make_sound(self):
        print(f"{self.name} chatters!")

    def eat(self):
        print(f"{self.name} eats bananas.")


        # allo of these showed overriding, primarily through the child class defining the exact same method 1ST
        # with the exact name as a method in the Parent class Animal 2ND
        # the child classes here varying kinds of animals with varying behaviors. with this, by overriding the 3RD
        # methods  of the parent class, the child classes have different implementations of the methods that are specific 4TH
        # to the kind or behavior of the animal

# objects of the subclasses 
# each are unique to the specific animal, but these names were also use in the study guide
# using the for loop to call skils and ang ambing moi kung englsh lahat kamitahimik.

a1 = Lion("Simba")
a2 = Elephant("Dumbo")
a3 = Monkey("George")
# objects were put into this list so the for lob can iterate through them

animals = [a1, a2,a3]
# calling the methods of the subclasses

# calling the methods of the subclasses
for animal in animals:
    animal.make_sound()
    animal.eat()
    print("---------------")

