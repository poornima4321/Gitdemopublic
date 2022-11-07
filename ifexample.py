def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print('The max number is: '+str(max_num(7, 49, 59)))

### Lists ###
print('###########################################################')
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends.extend(lucky_numbers) #add lucky_numbers list to the end of friends list
friends.append('Creed') #add creed at the end of the list
friends.insert(1, 'Joe') #insert Joe in the index 1 of the list
friends.remove('Jim') #it removes jim of the list
print(friends.pop(1)) #it removes the element at the position (index) 1
print(friends.index('Kevin')) #it return the position of the (first ocurrence) element kevin in friends' list
print(lucky_numbers.sort()) #it will sort the list (the list got to be homogeneus (just one type)) --> error otherwise
print(lucky_numbers.reverse())
print(friends.reverse()) #it sortes the list in reverse order
friends2 = friends.copy() #it copies the list friends into friends2
print(friends2)
print(friends[0]) # first element
print(friends[1:]) # from index 1 to the end
print(friends[1:3]) # from index 1 to index 2
print(friends[::-1]) #to show the list in inverse order
print(lucky_numbers)
print(friends2)
print('###########################################################')
""""
### Tuples ### (Can't be modified)
"""
print('###########################################################')
coordinates = [(4, 5), (6, 7), (80, 34)]
coordinates[1] = (7,8) #we modified the list, not the tuple, that's why this is allowed
print(coordinates[1])
print(coordinates)
print('###########################################################')
