# QA_Project_1

## Introduction
### What was my original idea for this project?
* The original idea for this project would be a complaints webform for a garden centre franchise. The reason I chose a garden centre was because the objects and situations would be 'easily imaginable', which means the relationship between the tables and columns would be very clear. 

### How and why did the idea change?
* Ultimately, the idea evolved from the web application which customers would use to submit complaints, to an internal portal which employees would use to create reports. This was because it would make more sense to perform CRUD - customers would not be able to read, update or delete other customers' complaints. Having it be an internal system was also a good way to get around a 'log-in' functionality, which we haven't yet been taught. 

## Planning
### Creating a Risk Assessment for the project
* To begin, I drew up a risk assessment for the project, which would examine any issue would could arise and jeopardise the function of the application. I returned to it at the end of the project in order to update the risk for each possible scenario:
[Risk Assessment - Sheet1.pdf](https://github.com/LisaJP4/QA_Project_1/files/6722550/Risk.Assessment.-.Sheet1.pdf)

### Using Draw.io to create the ERD for the database
* At first, I designed 3 tables: reports, types of reports, and employees. The employee table would have a 'ref' as a primary key - similar to a P-number used for a payroll. I would have had Create and Delete on this third table, for new employees or for those who leave the business. Ultimately, I chose to keep it to two tables:
![databasedesign](https://user-images.githubusercontent.com/84873140/123564800-ace87c80-d7b2-11eb-908a-c77e4bf92197.png)
* The 'types of report' table would also be static and fixed: only being Read on the website. 

### Using a Trello board to plan tasks 
* Using Trello, I was able to keep track of the tasks I had to perform throughout the project's development: 
<img width="883" alt="trello" src="https://user-images.githubusercontent.com/84873140/123564903-0e105000-d7b3-11eb-9d14-3c56bcecb545.png">

## Development
### Using Google Cloud Shell in SQL to ensure functionality
* Before starting any html pages or routes, I wanted to ensure that the tables I was creating was actually putting the data into the database. I used SQL to check the tables and the values: and this was a good idea at this stage, as I forgot brackets after _commit_ after my table creation. No errors were generated when I ran _create.py_ and this oversight would have been a problem later on:
<img width="721" alt="commit no brackets" src="https://user-images.githubusercontent.com/84873140/123565413-af4bd600-d7b4-11eb-9d3a-de715e3e2551.png">
<img width="433" alt="database_error" src="https://user-images.githubusercontent.com/84873140/123563675-f08cb780-d7ad-11eb-927d-41a693ddad18.png">

### Data Design within the tables
* In my database, I implemented datetime to automatically timestamp the creation of the reports I was making. I also set the primary key for the Reports table to autoincrement. This would prove to be useful later when identifying reports to update or delete, as there were no other integers in the table: **_Reports.query.get(<primarykey>)_**

### Front-End Design
* When I created my webpages, I created buttons for easy navigation. You can easily see which page wil be used to Create, Update and Delete reports: 
<img width="195" alt="logged issues" src="https://user-images.githubusercontent.com/84873140/123565537-28e3c400-d7b5-11eb-8af6-7a77f8e2a326.png">
* There is also a caution when a user tries to delete a report: 
<img width="255" alt="delete report page" src="https://user-images.githubusercontent.com/84873140/123565632-7fe99900-d7b5-11eb-9fe0-b03858fd0b77.png">
