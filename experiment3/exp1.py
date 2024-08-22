noteOf_TT = 0
noteOf_FH = 0
noteOf_TH = 0
noteOf_H = 0

withdraw = int(input("Input the amount of money you want to withdraw: "))

if(withdraw%100 == 0) :
    if(withdraw/2000!=0):
        noteOf_TT = int(withdraw/2000)
        withdraw = withdraw%2000

    if(withdraw/500!=0):
        noteOf_FH = int(withdraw/500)
        withdraw = withdraw%500

    if(withdraw/200!=0):
        noteOf_TH = int(withdraw/200)
        withdraw = withdraw%200

    if(withdraw/100!=0):
        noteOf_H = int(withdraw/100)
        withdraw = withdraw%100

    print("Please take ", noteOf_TT, " notes of 2000\nPlease take ", noteOf_FH," notes of 500\nPlease take ", noteOf_TH, " notes of 200\nPlease take ", noteOf_H," notes of 100")

else:
    print("Invalid Amount:!")