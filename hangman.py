import random 
def display_hangman(wrong_answers):
    stages = [
        """
        ----------
        |     |
        |     
        |    
        |     
        |   
        -
        """,
        """
        ----------
        |     |
        |     O
        |    
        |    
        |    
        -
        """,
        """
        ----------
        |     |
        |     O
        |     |
        |  
        |  
        -
        """,
        """
        ----------
        |     |
        |     O
        |     |
        |     |
        |    
        -
        """,
        """
        ----------
        |     |
        |     O
        |    \\|
        |     |
        |    
        -
        """,
        """
        ----------
        |     |
        |     O
        |    \\|/
        |     |
        |   
        -
        """,
        """
        ----------
        |     |
        |     O
        |    \\|/
        |     |
        |    / 
        -
        """,
        """
        ----------
        |     |
        |     O
        |    \\|/
        |     |
        |    / \\
        -
        """
    ]
    print(stages[wrong_answers])


def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele  
    print("\n"+ str1 + "\n") 
    return str1 

if __name__ == "__main__":
    print("                            ________HANGMAN________")
    print("                            THEME : STATES OF INDIA")

    #selecting question
    options = ['m a h a r a s h t r a','k a r n a t a k a','r a j a s t h a n','j h a r k h a n d','c h a t t i s g a r h']
    random.shuffle(options)
    pick  = options[0]
    word = list(pick.split())
    
    #making empty ansnswer string
    g =""
    for i in range(len(word)):
        g +='- '
    guess = list(g.split())
    listToString(guess)
    wrong_list = []

    wrong_guess = -1
    while wrong_guess<7:
        print("Take a guess number : ")
        print("Enter a character")
        flag = 0
        found = 0
        k = input()
        for i in range(len(word)):
            if word[i] == k:
                found = 1
                guess[i] = word[i]
                if guess == word:
                    print("CONGRATULATIONS! YOU WON")
                    flag = 1
                    break 
        listToString(guess)
        if found ==0:
            wrong_list.append(k)
            w = set(wrong_list)
            print("WRONG GUESS")
            print("List of wrong guesses :")
            print(w)
            wrong_guess +=1
            if wrong_guess !=8:
                display_hangman(wrong_guess)
                listToString(guess) 
                if wrong_guess==7:
                    print("GAME OVER! YOU LOSE!")
                    print("The answer was :")
                    listToString(word)
                    break
        if flag == 1:
                break
    

                
  
                    
                

        


