b='str'
p='end'
def mainmenu():
    print('1.ENCODE')
    print('2.DECODE')
    print('3.EXIT')
def encode(s):
    s1=''
    j=s.split(' ')
    for i in j:
        w=b+i[1:]+i[0]+p
        s1=s1+w
        s1+=' '
    print(s1)
def decode(s):
    s1=''
    j=s.split(' ')
    for i in j:
        w=i[-4]+i[3:-4]
        s1=s1+w
        s1+=' '
    print(s1)
print('----------------------------------------------------')
print('WELCOME TO SECRET CODE ENCODING AND DECODING PROGRAM')
print('----------------------------------------------------')
while True:
    mainmenu()
    x=input('Enter your option(1-3): ')
    if x=='1':
        print('WELCOME TO ENCODING SECTION')
        mess=input('Type in your message: ')
        print('---------------------------------')
        print('your encoded message is:')
        if len(mess)>=3:
            encode(mess)
        else:
            print(mess[::-1])
        print('----------------------------------')
        input('Press ENTER to return to main menu')
    elif x=='2':
        print('WELCOME TO DECODING SECTION')
        mess=input('Type in your message: ')
        print('---------------------------------')
        print('your decoded message is:')
        if len(mess)>=3:
            decode(mess)
        else:
            print(mess[::-1])
        print('----------------------------------')
        input('Press ENTER to return to main menu')
    elif x=='3':
        print('Thank You!')
        break
        