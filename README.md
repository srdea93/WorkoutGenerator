This is a web application built using Python's Flask Application. The purpose of this app is to 
generate at-home workouts for people to do. The application has a SQLite database connected it to it to store
Users, Exercises, and Workouts.

The application has 3 main functions:
1) The home page displays useful metrics based on the user that is signed it. It shows how many workouts a user has
performed, the number of minutes they have worked out, and the proportion of time spent working out specific muscles.

2) The add_exercise page will allow users to add new exercises to the application's database using a form-based 
approach. This form will allow users to input an exercise's name, select which workout group it belongs to,
include a link demonstrating how to perform an exercise, and specify a suggested amount of time to do the specific 
exercise.

3) The generate_workout page will allow users to use the application to generate a new at-home workout based
on the exercises that are in the database. It is a form that users can select how long they wish to workout for,
what muscle groups they wish to include and what muscle groups they wish to exclude. A randomized list of exercises
that meet the input criteria will be generated in an easy-to-read format specifying the exercises in a specific order
with rest breaks included.