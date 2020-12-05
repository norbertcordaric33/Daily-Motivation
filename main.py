print("Welcome to daily motivation!")
name = input("What is your name? ")
Occupation = input("What is your profession? ")
Big_dream = input("Do you have a dream, (yes/no)? ").lower()


if Big_dream == "yes":
        print("Nice!")
        the_dream = input("What is your dream? ")
        print("It's great that you know what you want!")
        print("To make sure you get the right inspirational story for the day, we would like to ask you some extra details about yourself if that is ok?")
        give_answer = input("Choose please, (yes/no)? ")
        
        
        if give_answer == "yes":
            print("Let's begin then!")
            
            Detail2 = input("What type of a person are you, see examples:(positive/happy/strict/perfectionist/stubborn/serious/negative/fearless/etc.)? ")

            print("Knowing who you are really does help in life...")


            Detail = int(input("How would you rate your Will-power from 1 - 10, 1 being the lowest? "))



            if Detail == 10:
                print("Wow, powerful!")
            elif Detail == 1:
                print("Dont be too hard on yourself!")
            else:
                print("Not bad at all!")
                    



            Detail3 = input("How often do you think about your dream becoming True, (daily/every second/sometimes)? ")
            print("Thank you, we just found a perfect Story for you!")
            print("PLEASE READ IT CAREFULLY, ONCE YOU DONE PRESS ENTER...")

            true_story = input("A 24 year old boy seeing out from the train’s window shouted… Dad, look the trees are going behind! Dad smiled and a young couple sitting nearby,looked at the 24 year old’s childish behavior with pity suddenly he again exclaimed… Dad, look the clouds are running with us! The couple couldn’t resist and said to the old man… Why don’t you take your son to a good doctor?The old man smiled and said… I did and we are just coming from the hospital, my son was blind from birth, he just got his eyes today. ")

            print("Every single person on the planet has a story. Don’t judge people before you truly know them. The truth might surprise you. ")



        else:
            print("We can't find a prober Story without more info about you, please try again!")
else:
    print("Try to think of one, Perhaps comeback later,Goodbye!")
   
    




            


                
            
            
        