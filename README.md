# **dynamic_website_with_django**
 In this web page it contains job,internship,project expereience of users 
 It is not easy to get internship or job so with the help of this website we get to know atleast what to do or we can say prerequisites in order to get internship or job and we can get ideas of projects and the we get to know the difficulties to succeed in life ,we can work according to that
# Basic information 
 First we visit starting page after successfull signup/login a page will appear called home page there we can check the internships,job,projects expereinces of others in internship,job,projects links respectively even we can able to find our experiences in accounts link and we can update the corressponding fields in that and a logout link redirect to home page
# Other informations
 I have used postgresql for database ,in order to run the code we have to follow some steps ...... like python manage.py runserver  ,.........
[follow this video to understood django](https://youtu.be/OTmQOjsl0eg)
website link : http://set-forth.herokuapp.com/
# Set up
Before installing Django make sure you have installed python

run the command 
```
pip install django 
```
After installing its time to create django project setup By running the following command
```
django-admin startproject projectname
```
django will create some files  ex: urls.py,settings.py .......etc

open the project files
```
cd projectname
```
In order to run this a server is needed ,for django it will automatically give a light weight server so just run the following command to run the project
```
python manage.py runserver
```
After we run that we will see link with ip address that is local host address with a port number we can change port number

Use any editor like Visual studio code and open the folder which you have created you will see code in setting.py and in some other files also 
# Create your own app
In order to create your own django app create your own app by
```
python manage.py startapp appname
```
another folder will be created with appname inside there will be some .py files  
![image](https://user-images.githubusercontent.com/64942306/119445637-c1b49900-bd4a-11eb-9e81-8895b93b376d.png)

admin.py is used after you have created database and it helps to view the database from django admin page ,about this file you will understood later clearly 

apps.py is used to connect your html,css,js or any other files with django

models.py is used t create classes and we can migrate to databse to create some table or database it might be relational database or non relational database 

tests.py for test purposes

views.py is used to tansfer data or connnect from python to html or css or js files




