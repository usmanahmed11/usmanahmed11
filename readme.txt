(+)Project Description

Project Name: Heart Disease Prediction System
Overview:
The feature of this Heart disease prediction system is that the system will tell the person if he has heart disease or not. For this, the person have to fill the form which contains the following information. Age, sex, chestpain, restbp, chol, fastingbs, restecg, heartrate, ex-angina ,oldpeak ,slope, mjrvessel, thal. When person fill out the details our system will tell us if the person has heart disease or not. 

Libraries Required:
The Project is developed in python language and you will need following libraries for the system to work perfectly:
•	Pandas
•	Numpy
•	Matplotlib
•	Seaborn
•	sklearn
If you want to install the libraries just type pip install [library name] on command prompt
OR
You can install the anaconda which have already all the libraries installed .

Project Details:
The project contains following files:
1.	heart.csv:
This is an excel file which contains all the data of our system
2.	dataset characteristics.txt file:
This is a text file which tells us the characteristics of all the data used in our system

3.	heart disease.py File:
This is the main file where model is trained and it contains all the code . The Support vector classifier & random forest classifier is used through sklearn library and model is trained on 75% of total data while tested on 25%.The accuracy of random forest is greater then support vector so we decided to proceed with the random forest classifier.

4.	Heart.pkl file:
This is model file which can be used in deployment process

5.	Web deployment.py:
This python coded file is the main bridge for html and python. Flask library is used in this code to render the template of Front End.html file and return the output by feeding the html inputs to the heart disease.py file.

6.	templates/ Front End.html:
 The directory templates contains the file Front End.html which  is the basic UI for our system.

7.	static/images&styles:
This is a folder linked with Front End.html file It contains styles and pics used in Front End.html File


(+)Project Deployment:
 Project is deployed on HTML and developed on Python.
