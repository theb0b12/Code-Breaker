def checkDuplicateValues(num):
    lst = []
    for c in num:
        lst.append(c)
    return len(set(lst)) == len(lst)
def compareNumbers(user, rand, max_digits):
    count_x = 0
    count_t = 0
    count_o = 0
    user_lst = [c for c in user]

    for i in range(len(user_lst)):
        if user_lst[i] not in rand:
            count_x += 1
            else:
                match = False
                for j in range(len(rand)):
                    if user_lst[i] == rand[j]:
                        match = True
                        break
                    if match:
                        count_o += 1
                    else
                        count_t += 1
    return max_digits == count_o, [str(count_x), str(count_t), str(count_o)]
def printKeypad(digits):
    print("Please enter a " + str(digets) + "digit number avec non duplicate values")
def getMinMax(digets):





    if __name__ == '__main__':
    run()