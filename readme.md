# Sample size Calculator with Python Flask
The purpose of this project is to learn Flask, Object Oriented Programming, SOLID principles, and Docker and put it in one single application and how to write tests for all the modules. This project also gives a good understanding of MVC framework, and statistics which is used to calculate sample size. Overall, it really helps in learning some of the important aspects of web development.


## INSTALLATION:

1. Clone the repository to your local
2. Install the dependencies using following commands:
- Packages: `pip3 install -r requirements.txt` (could be pip instead of pip3)
- DB initialization: `flask db init`
- DB migration: `flask db migrate -m 'first migration'`
- DB upgrade: `flask db upgrade`
3. Run the application using `flask --debug run or flask run`

## USAGE:
1. A user goes to the homepage
2. A user clicks on the link for "Calculate Sample"
3. If the user is not logged in they are prompted to login and after login they are redirected to a sample calculation form.
4. The sample calculation form should have a dropdown form control to select the z-score / confidence.
5. Once the user enters the values they should press the submit button and be redirected to a list of sample size calculations that they have previously entered.


## Features:
- User registration and login
- Sample size calculation
- Sample size calculation history
- User profile
- User groups

## Technologies:
- Python
- Flask
- SQLAlchemy
- Docker

## Features built using:
- Object oriented programming
- SOLID Principles
- Pandas, Flask, Jinja 
- Docker

## Contributing:
- Feel free to contribute to this repo by raising the pull request
- Use the proper names for variable and functions
- Do not import libraries unless needed
- Test well before submitting the PR

## LICENSE:
This repository is MIT licensed.

## Acknowledgements
This project was done under the guidance of Professor Keith Williams at NJIT, during the course IS 601 - Web Systems Development
