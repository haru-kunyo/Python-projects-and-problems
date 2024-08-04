def mainmenu():
    print('1.RULES')
    print('2.START')
    print('3.EXIT')
def rules():
    print('''   You will be given 5 questions each 
        correct answer guarantees you ₹1000
        each incorrect ans deducts your 
        balance by ₹1000, if your balance hits
        negative you need to pay us (ʃƪ¬‿¬)''')
    print('--------------------------------------')
amount=0
opt=('A.Nose\nB.Hand\nC.Ear\nD.Tongue','A.Eyes\nB.Hand\nC.Heart\nD.Brain','A.Snow\nB.Bricks\nC.Iron\nD.Brass','A.Zinc\nB.Copper\nC.Graphite\nD.Gold','A.Smelling\nB.Running\nC.Feeling\nD.Hearing')
ques=('Which one of the following is not a sense organ ?','Which of the following body part is called " Storehouse of knowledge " ?','Igloos are usually made of?','The lead in pencil is made of?','Rahul is listening to his favorite songs. He is using his sense of________.')
ans=('B','D','A','C','D')
name=input('Enter your name: ')
print('-----------------------------------------')
print(f'{name}, WELCOME TO KAUN BANEGA CROREPATI')
print('-----------------------------------------')
while True:
    mainmenu()
    c1=int(input('Enter your choice: '))
    if c1==1:
        rules()
        input('Press enter to return to main menu')
    elif c1==2:
        for i in range(5):
            if i==4:
                print(ques[i])
                print(opt[i])
                x=input('Enter your option: ')
                if x == ans[i]:
                    amount+=1000
                    input('End of KBC press enter to return to main menu')
                    break
            print(f'Your {i+1}st question is: ')
            print(ques[i])
            print(opt[i])
            x=input('Enter your option: ')
            if x == ans[i]:
                amount+=1000
                j = input('Press Y to continue or N to return to main menu')
                if j=='Y':
                    print('---------------------')
                if j=='N':
                    break
            else:
                amount-=1000
                j = input('Press Y to continue or N to return to main menu')
                if j=='Y':
                    print('---------------------')
                if j=='N':
                    break
    elif c1==3:
        print(f'Thanks {name} for playing')
        print(f'Your total amount earned is ₹{amount}')
        break
