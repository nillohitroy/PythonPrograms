def Rec_Odd(start, end):
    if start > end:
        return
    
    if start % 2 != 0:
        print(start)
        

    Rec_Odd(start + 1, end)

Rec_Odd(2, 10)