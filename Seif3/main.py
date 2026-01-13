from animals import Dog, Cat, Animal

animals = [Dog(), Cat()]

for animal in animals:
    if isinstance(animal, Animal):
        print(animal.speak())
    else:
        print("This object is not an animal!")