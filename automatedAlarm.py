# automatedAlarm.py
# by Matthew Laurins

# Write function defintion: automatedAlarm()

# Make sure it returns a value
def automatedAlarm(day, school):
    if day == 'monday' and school == True:
        time = '9:30'
    elif day == 'monday' and school == False:
        time = '7:00'
    elif day== 'wednesday' and school== True:
        time ='8:30'
    elif day== 'wednesday' and school == False:
        time = '7:30'
    elif day == 'tuesday' and school == True:
        time = '8:30'
    elif day == 'tuesday' and school ==False:
        time = '7:00'
    elif day == 'thursday' and school == True:
        time = '8:30'
    elif day == 'thursday' and school == False:
        time = '7:00'
    elif day == 'friday' and school == True:
        time = '8:30'
    elif day == 'friday' and school == False:
        time = '7:00'
    elif day == 'saturday':
        time = '9:00'
    elif day == 'sunday':
        time ='9:00'
    else:
        print ("You did it wrong")
        
    return(time)



if __name__ == '__main__':
    while True:
        print (" What day is Tomorrow?");
        day = input()
        listdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        if day in listdays:
            print('Tomorrow is a ' + day )
            break
        else:
            print("Please enter a valid day")
        continue
    while True:
        print ("is there school tomorrow? (Yes or No)");
        school = input()
        if school == 'yes':
            print ("and there is school tomorrow")
            school = False
            break
        elif school == 'no':
            print ("and there is no school tomorrow")
            school = True
            break
        else:
            print("Please enter Yes or No")
            continue


