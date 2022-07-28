x = input("Please enter feeding map as a list: ")
y = input("Please enter direction of movements as a list: ")
list_x = [i for i in x if i == 'X' or i == 'W' or i == 'C' or i == 'A' or i == 'M' or i == 'P' or i == '*']
list2 = [i for i in y if i == 'R' or i == 'L' or i == 'U' or i == 'D']
number_alt_list = int((x.count("[")) - 1)
number_of_letter = int(len(list_x))
len_of_alt_list = int(number_of_letter / number_alt_list)
list1 = [list_x[i:i + len_of_alt_list] for i in range(0, len(list_x), len_of_alt_list)]
print("Your board is: ")
for i in range(0, (len(list1))):
    print(*list1[i])
score = 0
breaking = False
for i in list2:
    if breaking:
        break
    a, b = 0, 0
    for j in list1:
        if '*' in j:
            a = list1.index(j)
            b = j.index('*')
    if i == 'U' and a != 0:
        for j in list1:
            if j == list1[a-1] and j[b] == 'W':
                break
            elif j == list1[a]:
                j[b] = 'X'
            elif j == list1[a-1] and j[b] == 'P':
                j[b] = '*'
                j = list1[a]
                j[b] = 'X'
                breaking = True
                break
            elif j == list1[a-1]:
                if j[b] == 'A':
                    score += 5
                elif j[b] == 'M':
                    score += -5
                elif j[b] == 'C':
                    score += 10
                j[b] = '*'
    elif i == 'D' and len(list1) >= a+1:
        for j in list1:
            if j == list1[a+1] and j[b] == 'W':
                break
            elif j == list1[a+1]:
                if j[b] == 'A':
                    score += 5
                elif j[b] == 'M':
                    score += -5
                elif j[b] == 'C':
                    score += 10
                j[b] = '*'
            elif j == list1[a]:
                j[b] = 'X'
            elif j == list1[a+1] and j[b] == 'P':
                j[b] = '*'
                j = list1[a]
                j[b] = 'X'
                breaking = True
                break
    elif i == 'R':
        for j in list1:
            if j == list1[a] and len(j) >= (b+1):
                if j[b+1] == 'P':
                    j[b + 1] = '*'
                    j[b] = 'X'
                    breaking = True
                    break
                elif j[b+1] == 'W':
                    break
                elif j[b+1] == 'A':
                    score += 5
                elif j[b+1] == 'M':
                    score += -5
                elif j[b+1] == 'C':
                    score += 10
                j[b+1] = '*'
                j[b] = 'X'
    elif i == 'L':
        for j in list1:
            if j == list1[a] and b != 0:
                if j[b-1] == 'W':
                    break
                elif j[b-1] == 'A':
                    score += 5
                elif j[b-1] == 'M':
                    score += -5
                elif j[b-1] == 'C':
                    score += 10
                j[b-1] = '*'
                j[b] = 'X'
                if j[b-1] == 'P':
                    breaking = True
                    break
print("Your output should be like this:  ")
for i in range(0, (len(list1))):
    print(*list1[i])
print("Your score is:", score)
