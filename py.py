p = 0
while p == 0:

    que = input("please enter first number> ")
    a = 0
    while a <= 0:
        try:
            que_int = int(que)
            a = + 1
        except:
            que = input("please enter number> ")

    s_que = input("please enter second number> ")
    while a <= 1:
        try:
            s_que_int = int(s_que)
            break
        except:
            s_que = input("please enter number>")

    i = 0
    while i == 0:
        sign = input("please enter sign> ")
        sign_list = ["+", "-", "*", "/"]

        for element in sign:
            if element in sign == sign_list[0]:
                print(que_int + s_que_int)
                i = +1
            elif element in sign == sign_list[1]:
                print(que_int - s_que_int)
                i = +1

            elif element in sign == sign_list[2]:
                print(que_int * s_que_int)
                i = +1

            elif element in sign == sign_list[3]:
                print(que_int / s_que_int)
                i = +1

    ask = input("do you want to continue? ")
    l = 0
    while l == 0:

        if ask.lower() == "yes":
            print("No Problem")
            l += 1
        elif ask.lower() == "no":
            print("okay")
            l += 1
            p += 1
        else:
            ask = input("please enter yes or no> ")
