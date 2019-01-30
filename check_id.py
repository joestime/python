def check_id_num(num):
    num = '50024019961009'
    lis1 = '01'
    las =[0,2,4,6,8]
    fact = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    sum = 0
    for i in range(17):
        sum += fact[i] * int(num[i])
    m = sum % 11
    chk = '10X98765432'
    return chk[m]
    #if chk[m] == num[-1]:
        #return True
    #else:
        #return False



a = check_id_num('50024019961009012')
print(a)





