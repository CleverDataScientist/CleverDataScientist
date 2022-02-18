# write a program to check a student grade
def marks(x):
    if x>90:
        print("Grade is A")
    elif x>75 and x<=90:
        print("Grade is B")
    elif x>55 and x<=75:
        print("Grade is C")
    elif x>35 and x<=55:
        print("Grade is D")
    else:
        print("failed")
marks(92)
marks(80)
marks(58)             
marks(46)              
marks(25)              
              
