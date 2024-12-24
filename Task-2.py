food=['burger','veg-pizza','momos','chinese','garlic-bread','french-fries','non-veg pizza']
print("Data type: ",type(food))
print("Total food items: ",len(food))

food.append('Kabab')
print("Append: ",food)

del food[2:4]
print("Delete: ",food)