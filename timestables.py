#!/usr/bin/env python
# Author : Abbey Pates
# Date : 14.01.18
# Version : 1

# ask user for a value and check their reply - if not a number the loop is restarted
# if the number is too high or low it is also returned
def askUser(question , lowerLimit, upperLimit):
   while True:
      try:
         answer = int(raw_input(question))
      except ValueError:
         print("Not an integer value...")
         continue
      else:
         if (answer < lowerLimit) | (answer > upperLimit):
            print("Not within the range " + str(lowerLimit) + " and " + str(upperLimit))
         else:
            return (answer)
            break

# show you the entire timestable e.g 2 x 2 = 4   
def displayTimestable(table, times):
    print("\n")
    print(str(table) + " timestable up to " + str(times))

    for lineNumber in range(1, times+1):
       answer = lineNumber * table
       print("   " + str(lineNumber) + " x " + str(table) + " = " + str(answer))


if __name__ == '__main__':
   print "Timestables"
   print "==========="

   # asks you for your timetable and the range
   timestable = askUser("Please select a timestable between 1 and 50: ", 1, 50)
   timesRange = askUser("How far up the table do you want to go (1 to 50)? ", 1, 50)

   displayTimestable(timestable, timesRange)