nums = input('list1 = ')[1:-1].split(',')
pos = []
for num in nums:
    if int(num) > 0:
        pos.append(num)
print('[' + ', '.join(pos) + ']')
