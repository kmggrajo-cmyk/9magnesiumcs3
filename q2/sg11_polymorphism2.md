# ACTIVITY 2

## 1. Answer the following questions:
a. What is duck typing, as explained in the video?

b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

## Answer
a. Duck typng gets its name from the saying, "If it looks like a duck and quacks like a duck, then it must be a duck." With this, Duck Typing is essentially another form of polymorphism, where Python does not tune into what class an object truly belongs to, for it only tunes into the attributes and methods defined --- as long as an object has the minimium necessary attributes and methods expected by the code, Python will treat it as a valid type. Ultimately, Duck typing focusesstrictly on behavior (what an object can do) rather than lineage (what class it inherited from)

b. Based on the video, the Car class needed to have its own speak() method and an alive attribute in order to work inside the same lop as the Dog and Cat classes without inheriting from Animal. Initially, when a Car object was placed into th elist of animals, the program threw an AttributeError because the loop expected every object to have a sepak() method, whereas the car only had a horn() method. When the horn method of the car was renamed to speak(), it was able to successfully run alongside the dog and cat during the first part of the loopp. Later, when the loop was updated, to also print each object's alive attribute, another AttributeError occurred until the creator explicitly gave the Car class an alive attribute of its own. Once the Car class possessed both the speak() method and the alive attribute, it met the requirements needed to be treated just like the other animal objects through Duck typing.

## 2. Create the Python code that:
a. Creates three classes: Car, Boat, and Drone with a method move().

move() in the Car class prints "The car drives on the road."

move() in the Boat class prints "The boat sails on water."

move() in the Drone class prints "The drone flies in the sky."

b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the
move() method: vehicle.move().

c. Creates one object of each class.

d. Calls the start_trip() method for each object.

## Answer
* [SG 11 ACTIVITY 2 QUESTION 2 CODE](g11_polymorphism2.py)

## 3. How does the code in 2.2 demonstrate polymorphism?

## Answer
Through the code in number 2, polymorphism was shown primarily because the same start_trip(vehicle) function can work with different types of objects such as the Car, Boat, and Drone, and produce different behaviors using a single method call, vehicle.move(). All vehicles/classes share a method with the exact name, which is move().  However, despite being used all throughout the classes with the same name, each class had a differnet implementation of it to print message that suits the vehicle being utilized. Throough Duck typing, the start_trip() function does not need to check whether the vehicle passed into it is a Car, Boat, or Drone, for it simply calls vehicle.move() and automatically runs the version of move() for that specific objet/vehicle.

Furthermore, even though the varying classes do not inherit from the shared parent class, they all have a move() method that allows the loop and start_trip() function to treat them interchangeably. 


