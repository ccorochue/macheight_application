# Application for MachEight

**The task is** to create an application that takes a single integer input. The application will download the raw data from the website above
(https://mach-eight.uc.r.appspot.com) and print a list of all pairs of players whose height in inches adds up to the integer input to the application. If no matches are found, the application will print "No matches found".

**My code makes this:**

1. Import urlopen from urllib.request and json modules.
2. Save in variable *players* all players from the json response.
3. Ask to user for a number between the minimun and maximun add up of heights.
4. Save in a list *players1* all players with height major than the diff between the input number and the highest height.
5. Iterate between all players in *players1* and save in a list *players2* all players who have the height of the input number minus the height of the player in the iterate.
6. Print the couples of players who theirs heights add up the input number.
