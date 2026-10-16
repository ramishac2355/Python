"""
main.py

Driver program for the Time Conversion project.
Prompts the user for a number of seconds and
displays time conversions using the time_conversion module.
"""

# import the module
import time_conversion

# TO DO #1: Declare a variable called num_seconds and assign it a value of 0
# add your code here
num_seconds = 0
# num_seconds = int(("Enter the number of seconds:")





def main():

    # statements for output formatting
    print("*******************************")
    print("Start - Time Conversion Program")
    print("*******************************")

    
    # TO DO #2: ask the user to enter the number of seconds to be converted
    # and assign the value to num_seconds as an integer value
    # add your code here
    global num_seconds
    num_seconds = int(input("Enter the number of seconds: "))



    #####################################################0
    # you do not need to add anything below this line

    # call function to calculate Decaseconds
    print(time_conversion.decaseconds_conversion(num_seconds))

    # call function to calculate Jiffies
    print(time_conversion.jiffies_conversion(num_seconds))

    # call function to calculate New York Minutes
    print(time_conversion.new_york_minutes_conversion(num_seconds))

    # call function to calculate Nanocenturies
    print(time_conversion.nanocenturies_conversion(num_seconds))

    # call function to calculate Snapchat Streak Days
    print(time_conversion.snapchat_streak_days_conversion(num_seconds))

    # uncomment the function call to calculate custom time
    print(time_conversion.custom_time_conversion(num_seconds))

    # statements for output formatting
    print("*******************************")
    print("End - Time Conversion Program")
    print("*******************************")


if __name__ == "__main__":
      main()
