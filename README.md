# FT_Labs
Problem By FullThrottle Labs


API endpoint for getting all users details : http://riteshm.pythonanywhere.com/api/v1/user/

API endpoint for getting specific user details : http://riteshm.pythonanywhere.com/api/v1/user/<<id>>

This Django App exposes API endpoint for getting user details like user ID, Name, Activity Periods, etc as json response. The application is written using django rest_framework and Faker Library to generate dummy user data.

Application opens two points one for getting all user details and other for getting specific user details.
  user_collection() -> for all user data
  user_element() -> for specific user data
Both function is responding to GET method only.


<b>What’s happening here:</b><br/>
<ol>
  <li>
  First, the @api_view decorator checks that the appropriate HTTP request is passed into the view function. Right now, app only supports GET requests.
  </li>
  <li>
  Then, the view either grabs all the data, if it’s for all users, or just a single user, if it’s for a specific user ID.
  </li>
  <li>
    Finally, the data is serialized to JSON and returned.
  </li>
  </ol>
  
  <b>Custom Django Management Command to fill apps models using fake data : </b>
  <ol>
  <li>
    Module 'set_user_activity_period.py' is using django.core.management.base.BaseCommand to create class Command and inside handle we are calling set_model_data() to fill the models with data.
  </li>
  <li>
  Module 'filler.py' is responsible for generating fake data using Faker class, by-default it will create 2 users data, you can change it by updating the value of members variable while calling.
  </li>
  <li>
    Execute <i>python manage.py set_user_activity_period</i> to before checking the API, this command will fill the data in MySQL database.
  </li>
  </ol>
  
  <b>Hosted in PythonAnywhere : </b>
  Uses MySQL Db for backend and rest_framework to open above mentioned API endpoints.
