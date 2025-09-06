# Tennis Scheduler

This is a beginner software development project that will guide the student through developing a basic scheduling app. The application will be developed in mutliple iterations, each adding additional functionality and accessibility. 

The first iteration of the app will be a text based application that a user can use to view timeslots for an organization that provides tennis lessons. The admin of the application can define what timeslots are available and various restaints on each time slot such as how many people can join a single timeslot, the minimum age for each slot, etc. The user (the individual interested in taking a lesson) will be able to register for various time slots.

The future iterations will use a database to persist user data, will provide a webpage for the user to use, and finally the application will be deployed using aws. 

## Concepts
* python
* Basic program control flow
* Data persistance
* Using databases to persist user data
* Web development
* Managing user input both through the terminal as well as a web browser

## Day 0
Before writing code, you must first ensure that the following software is installed on your machine:
- [ ] git
- [ ] python
- [ ] vscode

The requirement for this iteration is to produce a basic 'hello world' script to ensure that you are able to write and run your code.

## Day 1
Now you will implement a minimal version of the application.
The overall goal of this is to implement all of the business rules, that is, all of the core real world features that pertain to tennis. This includes storing the timeslots and allowing people to register, and adding any kind of restrain on who can register, what age they must be, whether they are bringing a racket or not, etc.

Implement the following requirements; you are encouraged to add any additional features that you would like.
Requirements:
- [ ] You should be able to add different timeslots, eg 1-2pm, that users can register to. 
- [ ] Each timeslot will have a maximum number of students that can join it. 
- [ ] Users should be able to view these timeslots, select one, and must enter some identifiable information (at least their first name) in order to register. As long as the selected timeslot is not full, the users name should be saved and the app should remember who has registered to what timeslot. 
- [ ] Users should also be able to unregister from a given timeslot.
- [ ] User data only needs to persist as long as the app is running; it is fine if all of the data is lost when the app is closed.

# Day 2
Now it is time to add database support. This allows the user data to persist accross restarts, and also paves the way for us to deploy the application in the future. We will use sqlite since python already has support for it, and because sqlite is incredibly lightweight simple.

Requirements:
- [ ] Timeslots and the users assigned to them should be saved in a database and should persist between app restarts. 

# Day 3
The next step is to provide a more accessible interface for the users. We will implement a basic webserver that a user or admin can use to view and edit timeslots in the browser. 

Requirements:
- [ ] Users should be able to view a webpage that allows them to interact with the app using the browser. The webpage will be ultra minimal and ideally should not require css or javascript; just raw html and forms to send data.

# Day 4
The final step is to deploy this application on the public internet. This can be done using either aws or github pages. 

Requirements:
- [ ] Users can access the webpage from their personla computer on the public internet.