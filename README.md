# ORB-CHALLENGE-IMPROVED


API CHALLENGE PROJECT <br />

P.S. This project made for a company's job application challenge project! Not personal project! <br /> <br />



DESCRIPTION<br />

--First, the user have to register in order to send request to endpoints (except /register/). When you send request to register, If user is unique (by username), you can create your account. After created the account, the system will create automatically your own api_key and api_secret_key, then sends email these keys to the user's email address. <br />

--If user is registered,<br />

-You can create a room <br />

-You can subscribe in room <br />

-You can add event in room <br />

-You can get events in the room <br />
  
-You can update event <br />

-You can delete event <br />

-You can get upcoming events in every room that you are subscribed. <br />



<br /><br />

RESTRICTIONS <br />

-If user doesn't have api_key and api_secret_key, user cannot send request to the endpoints. <br />
  
-Every room has its own creator. Only room creators can add or delete event in the room, the rest of the users will be read-only. They cannot make any changes. <br />

-Users that want to get events, have to subscribe to the room. It means, a user only can see the events if the user subscribed to the corresponded room. Cannot see other rooms's events if the user doesn't subscribed. <br />





<br /><br />
API ENDPOINTS & REQUESTS BODY <br />

/register/ <br />

{
    "username": "testuser",
    "password": "Test1234!",
    "email": "test@example.com"
}



<br />
/api/room/create/<br />

{
    "api_key": "your_api_key",
    "api_secret_key": "your_api_secret_key",
    "room_name": "your_room_name"
}



<br />
/api/room/subscribe/ <br />

{
    "api_key": "your_api_key",
    "api_secret_key": "your_api_secret_key",
    "subscribe": "room_name_that_want_to_subscribe"
}



<br />
/api/event/create/ <br />

{
    "creator_api_key": "your_api_key",
    "creator_api_secret_key": "your_api_secret_key",
    "room": "in_which_room_you_want_to_create_event(RoomName)",
    "title": "Test Title",
    "description": "This is a test event.",
    "date": "2024-03-17",
    "time": "10:00"
}



<br />
/api/room/<room_id>/events/ <br />

{
    "api_key": "your_api_key",
    "api_secret_key": "your_api_secret_key"
}



<br />
/api/event/update/<event_id>/ <br />

{
    "api_key": "your_api_key",
    "api_secret_key": "your_api_secret_key",
    "title": "New Title",
    "description": "New Description",
    "date": "2024-03-18",
    "time": "13:00"
}



<br />
/api/event/delete/<event_id>/ <br />

{
    "api_key": "your_api_key",
    "api_secret_key": "your_api_secret_key"
}



<br />
/api/event/upcoming/ <br />

{
    "api_key": "your_api_key",
    "api_secret_key": "your_api_secret_key"
}



<br /><br />
NOTE : You can test the API by sending requests by using POSTMAN or with any other method, I used POSTMAN. <br />


<br /><br />

INSTALLATION AND SETUP<br />
Make sure to install all requirements, in order to do that;<br />
pip install -r requirements.txt (be sure you are in the right path in terminal)<br />
<br />
If you want to create your own .venv ;<br />
python -m venv venv<br />
<br />
After installing requirements we can start,<br />
python manage.py makemigrations<br />
(This command detects changes made to the model files in your project and creates a "migrations" file according to these changes. This file defines changes to the database schema but does not update the database, it just saves the changes made to the model.)<br />

python manage.py migrate (this command will do that)<br />
<br />
In order to run project,<br />
python manage.py runserver  (it will run local server and the project)







<br /><br />
EXAMPLE REQUESTS <br />

I created three account for the test purposes: <br />


<br />
User A have:<br />

"api_key": "c8ba4f992b42ab436af785d2fc21caf5" <br />

"api_secret_key": "hEPkASJm_efDzgwYgMpjvNCThuLlW3aYx6aLf--rihM" <br />


<br />
User B have: <br />

"api_key": "16ec6e874e224499b725a9a20c68d99b" <br />

"api_secret_key": "89811mny3s76QJSamml6nstDRB8WA-FkKVXMBLNOkjk" <br />


<br />
User C have: <br />

"api_key": "c2bd29a2af3c5dd2c6fb8fc06661f80b" <br />

"api_secret_key" : "2W8e6OMKbg7MpJVs0XLhEIK4s8IZ2IiOY_2Pqs6EMuQ" <br />



<br /><br />
REGISTER AND ITS RESPONSE:<br />

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/66de306c-956e-4b81-82a2-e4b2a4a1f080)



![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/f1ec1005-06d6-4961-a36e-f0bfd3d89fd1)




EMAIL:

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/f27a4cd9-70bc-4ac3-b6b8-28f3e5b69d07)


api/room/create/ : 

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/289dc084-16c8-469c-a40b-c1f556244fb3)


its response:

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/90083d47-5dda-4860-9f17-fb1d8af8ad26)


api/room/subscribe/ and its response:

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/2a4e5a7f-fb6d-424f-8da8-202406a082d4)



api/room/<room_id>/events/ and its response : 

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/377c4da1-fb2c-40fa-90ee-21b9b6dc466e)

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/f7238e08-f4c9-4745-a57f-e19293c9e746)


api/event/update/<event_id>/ and its response :

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/826c91b3-fd42-4260-bc14-bba5294c9b4d)


if you are unauthorized the response:

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/55f60fe7-a458-43df-a887-176542ed6671)



api/even/delete/<event_id>/ and its response:

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/1fd0cfa4-7518-4173-a257-188591b64457)



api/event/upcoming/ :

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/04003f2e-2a25-4a8d-8110-f5f2065b3a76)


its response :

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/b6c23e05-0281-4d1e-8bbf-972defab49eb)



api/room/create/ and api/event/create/ and if you are unauthorized on api/event/create/:

![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/db6f4be4-bd3a-4858-aeb2-dadabb0bbc81)


![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/cd74c145-0afb-452a-829b-9f1f2df8fa6a)


![image](https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED/assets/139239394/e78d6d03-715f-47a4-b029-a85c1f4783e8)





Last Thoughts :

There are many other things can add to the project, such as the maximum number of requests per minute, the restriction of registering from the same IP address within a day, creating events according to categories, upcoming events within a specified time period (not just those within 24 hours), etc. The features can be added to the project and can make it much more complex, ,however, since adding all the features that need to be added as much as possible for now is beyond the scope of the challenge project, the project author the development of the project was terminated here.








