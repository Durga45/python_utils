def frinedshipScore(name1,name2):
    name1,name2=name1.lower(),name2.lower()
    score=0
    sharedLetters=set(name1) & set(name2)
    vowels=set('aeiou')

    score+=len(sharedLetters) *5
    score+=len(vowels & sharedLetters) *10
    
    return min(score,100)

def runFriendshipCalc():
    print(" Friendship Compatibility calculator")
    name1=input("enter first name: ").strip()
    name2=input("enter second name: ").strip()

    score=frinedshipScore(name1,name2)

    print(f"\n Score is :{score}")

runFriendshipCalc()