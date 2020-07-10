############################################
# 1. Assigning elements to different lists #
############################################
my_list1 = []
my_list2 = []
while True:
    element = input('Enter an element: ')
    if element == '-1':
        break
    choice = input('Enter 1 or 2 for different lists: ')
    if choice == 1:
        my_list1.append(element)
    else:
        my_list2.append(element)
print('my_list1 = ', my_list1)
print('my_list2 = ', my_list2)

#################################################
# 2. Accessing different elements from a tuple. #
#################################################
my_tuple = (10, 20, 30, 50, 40, 90)
while True:
    index = int(input('Enter the index number of the tuple [0 - 5]: '))
    if index == -1:
        break
    print(index)

#####################################################
# 3. Deleting different elements from a dictionary. #
#####################################################
my_map = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}
while True:
    print('The keys in the map are:', my_map.keys())
    key = int(input('Enter the key do you want to delete: '))
    if key == -1:
        break
    my_map.pop(key)
