animals = ['cat', 'dog', 'lion', 'elephant', 'tiger']
birds=['peacock','hen','sparrow','kite','eagle']
print("Animals are :",animals)
print("Birds are :",birds)
living_things=animals+birds
print("Living things are :",living_things)
birds.remove("hen")
print("updated Snakes are :",birds) 
living_things.append("human")
print(living_things)
living_things=animals+birds
print("concatention",living_things)
print("slicing for birds :",birds[1:4])
print("slicing for animals :",animals[2:6])
print("repetion",animals*3)
