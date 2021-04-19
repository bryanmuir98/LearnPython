lucky_numbers = [34, 4, 125, 8, 15, 16, 23, 42]
friends = ["John", "Morgan", "Justin", "Justin", "Kyle", "Ritter"]


friends.append("Nick")
friends.insert(2, "Micah")
friends.remove(friends[0])
#friends.pop() removes last list item
#friends.clear() clears whole list
print(friends)
print(friends.index("Justin"))
print(friends.count("Justin"))
friends.remove(friends[2])
friends.sort() #alphabetical order
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse() #backwards order
print(lucky_numbers)
friends2 = friends.copy() #copy a list to another
print(friends2)
friends.extend(lucky_numbers) #add 2 lists together
print(friends)