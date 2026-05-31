
# if elif else useage 

candidate1 = 'PAT'
candidate2 = 'ATK'
candidate3 = 'PO'

can_vote = False 

try:
    age = int(input('enter your age : '))
    #> < >= , <= , == 
    if age >= 18 :
        can_vote = True 
    
except Exception as e :
    print('sorry we cannot process voting as at now ')
    print(e)



if can_vote :
    print("Ready to vote for your prefer candidate ")
    print("="*50)
    print("CANDIDATES")
    print(f'''
        (1) {candidate1}  
        (2) {candidate2}
        (3) {candidate3}
    ''')
    print("="*50)
    while True :
        user_choice = int(input("Select your preferred candidate by their number : "))
        if user_choice == 1:
            print(f'You vote for {candidate1}')
            break
        elif user_choice == 2:
            print(f'You vote for {candidate2}')
            break
        elif user_choice == 3:
            print(f'You vote for {candidate3}')
            break
        else :
            print('Your choice is invalid')
            print("you need to retry entering a valid choice from 1 - 3 ")
else :
    print('You are not eligible to vote')
