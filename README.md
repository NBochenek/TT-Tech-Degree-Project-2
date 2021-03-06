# Basketball Team Stats Tool
In this project you will be writing a program that reads from the "constants" data (`PLAYERS` and `TEAMS`) in `constants.py`. This data will need to be translated into a new collection of your choosing and the fields need to be changed to something that makes more sense for Python to do its comparisons.


**NOTE**: Python has no concept of actual constants like some other languages out there. But it is a convention in Python to treat ALL CAPS variables as if they are in-fact constants.


**Steps to get started:**

1. Create a new empty script file called `app.py` or `application.py`

2. Inside this new file, you will want a Dunder Main statement:
   For a refresh on Dunder Main:
   https://teamtreehouse.com/library/understanding-dunder-main-main

3. Any print statements or function calls you will want to be inside Dunder Main or inside a main function call which is nested inside Dunder Main.
   If you need a refresh, check out the supplied Project 1 files/workspace for an example.
   


If you get stuck, try to work through the problem. Sometimes it helps to try to write/draw out your steps on paper in the order your program should run in and solve each step 1 at a time. If you are still stuck be sure to reach out in the Python Techdegree #unit-02 Slack channel.

Instructions:


Create a new script

1. The very first step you will want to do after opening the workspace or unzipping the .zip file into your project folder is to create a new and blank Python script named app.py or application.py.

2. Proper use of Dunder Main

Make sure the script doesn't execute when imported; Anything that is a calculation, callable function, or a block of logic that needs to run, ensure you put all of your logic and function calls inside of a dunder main block at the bottom of your file:

Dunder main statement looks like this:

if __name__ == "__main__":

HINT: Unit 1 project files/workspace had an example of this.

NOTE: This does not mean everything you write has to be contained within Dunder Main. You can still import and define functions outside of dunder main, you can still extract pieces of logic into those functions. The main calls to your program should be protected inside Dunder Main to prevent automatic execution if your script is imported.
Import player data

3.Import from constants.py the players' data to be used within your program.

NOTE: Python has no concept of actual constants like other languages have. But it is a convention you may see in the real world. When you see ALL CAPS variable name you are meant to treat it as if it were a constant or a value that you cannot change/alter.

4. Create a clean_data function

Write the logic to:

1) read the existing player data from the PLAYERS constants provided in constants.py 2) clean the player data without changing the original data (see note below) 3) save it to a new collection - build a new collection with what you have learned up to this point.

Data to be cleaned:

    Height: This should be saved as an integer
    Experience: This should be saved as a boolean value (True or False)

HINT: Think Lists with nested Dictionaries might be one way.

NOTE: Ensure you **do not directly modify the data in PLAYERS or TEAMS constants. This data you should iterate and read from to build your own collection and would be ideal to clean the data as you loop over it building your new collection. If you are unsure of what this means, checkout this instruction step.

5. Create a balance_teams function

Now that the player data has been cleaned, balance the players across the three teams: Panthers, Bandits and Warriors. Make sure the teams have the same number of total players on them when your team balancing function has finished.

HINT: To find out how many players should be on each team, divide the length of players by the number of teams. Ex: num_players_team = len(PLAYERS) / len(TEAMS)

6. Console readability matters

When the menu or stats display to the console, it should display in a nice readable format. Use extra spaces or line breaks ('\n') to break up lines if needed. For example, '\nThis will start on a newline.'

7. Displaying the stats

When displaying the selected teams' stats to the screen you will want to include:

    Team's name as a string
    Total players on that team as an integer
    The player names as strings separated by commas

NOTE: When displaying the player names it should not just display the List representation object. It should display them as if they are one large comma separated string so the user cannot see any hints at what data type players are held inside.

Extra Credit

1. Cleaning guardian field

When cleaning the data, clean the guardian field as well before adding it into your newly created collection, split up the guardian string into a List.

NOTE: There can be more than one guardian, indicated by the " and " between their names.

2. Additional balancing to the team

Additionally, balance the teams so that each team has the same number of experienced vs. inexperienced players.

If this is done correctly each team stats should display the same number count for experienced total and inexperienced total as well as the same total number of players on the team.

3. Include additional stats for a given displayed team:

    number of inexperienced players on that team
    number of experienced players on that team
    the average height of the team
    the guardians of all the players on that team (as a comma-separated string)

HINT: You can calculate the average height for a given team by keeping a running sum total of each players height on the team and dividing that total by the total number of players on that team.

4. Quit Menu Option

The user should be re-prompted with the main menu until they decide to "Quit the program".


