"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  Computes the wins and losses of the teams and determines their group placement based on that

Author: Khatchadourian.N

Created:  03/03/2021
------------------------------------------------------------------------------
"""

print("******* Tournament Tracker ********")
print("")

#setting up variables for number of wins and losses
win_count = 0
loss_count = 0

#has the user input their wins and losses as "w" or "l" and adds to the appropriate counter
for i in range(6):
  game_results = input("Enter the wins and losses for your team: ").lower()
  
  if game_results == "w":
    win_count = win_count + 1
  elif game_results == "l":
    loss_count = loss_count + 1

print("")
#outputs the number of wins and Losses
print("Wins: " + str(win_count) + " Losses: " + str(loss_count))

#checks the user's wins/losses and sees which group they would be in
if win_count == 6:
  print("You are in group 1")
elif win_count == 5:
  print("You are in group 1")
elif win_count == 4:
  print("You are in group 2")
elif win_count == 3:
  print("You are in group 2")
elif win_count == 2:
  print("You are in group 3")
elif win_count == 1:
  print("You are in group 3")
else:
  print("You were eliminated")