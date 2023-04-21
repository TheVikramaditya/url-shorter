# url-shorter
this is the django project where , we can shorte any url and visit the original url with that tiny url

SETTING UP THE PROJECT

just pull the code and create a virtual environment 
install requirement.txt
got inside TinyUrl project
run migrations
run the project with python manage.py runserver


FEATURES OF THE PROJECT

Signup 
Login
URL Shorter
User Profile Where User can see his top searched url and history
User Can delete his History 
Data Cleanup Policy
Auto Expire Session

Note -  This project also have "Data Cleanup policy inside cleanup app , where if a user is inactive for 10 minutes
(the time you can increase as per your choice ) then the cleanup will delete the users whole data

command "python manage.py cleanup"


