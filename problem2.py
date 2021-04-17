"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  Computes the days it took the user to surpass 100km driven as well as calculating the average per day

Author: Khatchadourian.N

Created:  03/03/2021
------------------------------------------------------------------------------
"""

print("******* DoorDash Distance Tracker ********")
print("")

#setting up variables for the things needed in the loop and to make the final calculations (the total distance, the daily distance, and the days driven)
total_distance = 0
daily_distance = 0
days_driven = 0

print("** Travel Log **")

#getting the user to input the distance they travelled per day until it reaches 100. Also adding to the total distance and the total number of days
while total_distance < 100:
  daily_distance = int(input("Enter the distance travelled for the day: "))
  total_distance = total_distance + daily_distance
  days_driven = days_driven + 1

print("")
print("** Summary **")

#outputs the information to the user and also calculates the average
average_distance = total_distance//days_driven

print("It took " + str(days_driven) + " days to reach 100km")
print("The average distance driven per day is" , round(average_distance, 0))