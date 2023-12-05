def check_string_brakets(input_string):
    i, o = 0,0
    while i < len (input_string) and o>0:
        if "(" == input_string[i]:
            o +=1
        else:
            o -=1
            i +=1
            if 0 == o:
                print("YES")
    else:
        print("NO")

check_string_brakets("())(()")