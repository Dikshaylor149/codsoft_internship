import random

b= str(input("Enter Player's Name: "))
s1=0
s2=0
while s1+s2<3:
    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ROCK PAPER SCISSOR~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('-'*80)
    print('''Choose Any:
    1. ROCK
    2. PAPER
    3. SCISSOR''')
    print('-'*40)
    a= int(input('Enter Your Choice: '))
    c= random.randrange(1,3)
    print('-'*40)
    print(b,'Choice= ',a)
    print('Computer Choice= ',c)
    print('-'*40)

 
    if a==1 and c==1:
        print('TIED')
        print(b,':',s2,
              'Computer: ',s1)

    elif a==2 and c==1:
        print('Result: ',b,'Win')
        s2+=1
        print(b,':',s2,
              'Computer: ',s1)

    elif a==3 and c==1:
        print('Result: Computer Win')
        s1+=1
        print(b,':',s2,
              'Computer: ',s1)

    elif a==1 and c==2:
        print('Result: Computer Win')
        s1+=1
        print(b,':',s2,
              'Computer: ',s1)

    elif a==2 and c==2:
        print('Result: TIED')
        print(b,':',s2,
              'Computer: ',s1)

    elif a==3 and c==2:
        print('Result: ',b,'Win')
        s2+=1
        print(b,':',s2,
              'Computer: ',s1)

    elif a==1 and c==3:
        print('Result: ',b,'Win')
        s2+=1
        print(b,':',s2,
              'Computer: ',s1)

    elif a==2 and c==3:
        print('Result: Computer Win')
        s1+=1
        print(b,':',s2,
              'Computer: ',s1)

    elif a==3 and c==3:
        print('Result: TIED')
        print(b,':',s2,
              'Computer: ',s1)

    else:
        print('Wrong Option')



print('')
print('Final Scores: ')
print(b,':',s2)
print('Computer : ',s1)
print('-'*40)
if s1>s2:
    print('@ Computer Won The Game @')
else:
    print('@',b,'Won The Game @')
      
print('*'*80)





