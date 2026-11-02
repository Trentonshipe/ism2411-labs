#Lab 10
# I didn't expect .sort() to change the original list and return None, so my first print showed "None" instead of the sorted items. 
# When I worked at smoothie king, I counted inventory by hand and flagged low and high stock fruits and supplements, but a list and a short loop could check every item and its listed value and flag the low and high ones instantly. 


print("--- Exercise 1: Build a List ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index practice ---")
print(inventory[0]) # always grabs the first item in a list
print(inventory[-1]) # always grabs the last item in a list

middle = len(inventory) // 2 
print(inventory[middle])

print("--- Exercise 3: List Slicing ---")

print(inventory[:3]) # grabs items at index 1, 2, and 3
print(inventory[-2])
print(inventory[::2]) # grabs every other item in the list

print("--- Exercise 4: List Methods ---")
inventory.append("envelope") # adds an item to the end of the list 
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort() #sorts the list in alphabetical order
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060) # New York City coordinates

# coords [0] = 99 
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinated from being changed by accident.")

print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales [0]
worst = sales [0]

for amount in sales: 
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount
print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2)) # apply a 10% discount

print(prices)
print(discounted)

print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = [] # an empty list

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print("Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")













