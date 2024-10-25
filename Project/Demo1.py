import csv

def check_voter(registration):
    with open('Voter.csv', 'r', newline='') as Voter:
        Reader = csv.reader(Voter)
        for i in Reader:
            if(int(registration) == i[2]):
                return True
                break


def check_registration(registration):
    with open('Eligible.csv','r',newline='') as Eligible:
        Reader = csv.reader(Eligible)
        for i in Reader:
            if(int(registration) == i[0]):
                return True
                break


def vote():
    print("\n\nWelcome to Voter system \n\n")

    Name = str(input("Enter your name: "))
    Reg = int(input("Enter your Registration: "))
    if(check_registration(Reg) and not check_voter(Reg)):
        print("You are eligible to vote \nPlease Select Candidate\n")
        print("1. Candidate1")
        print("2. Candidate2")
        print("4. Candidate3")

        Selected = int(input("Choose one candidate: "))

        if(Selected == 1):
            candidate = "Candidate 1"
        elif(Selected == 2):
            candidate = "Candidate 2"
        if(Selected == 3):
            candidate = "Candidate 3"
        
        with open('Voter.csv', 'a+', newline='') as Voter:
            Write = csv.writer(Voter)
            next(Voter)
            Write.writerow([candidate, Name, Reg])

    else:
        print("You are not eligible")

if __name__=='__main__':
    vote()