# StackOverflow-API
StackOverflow-lite is a platform where people can ask questions and provide answers. 


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/munniomer/StackOverflow-API.svg?branch=develop)](https://travis-ci.com/munniomer/StackOverflow-API)
[![Coverage Status](https://coveralls.io/repos/github/munniomer/StackOverflow-API/badge.svg?branch=bg-fix-app-structure-162694259)](https://coveralls.io/github/munniomer/StackOverflow-API?branch=bg-fix-app-structure-162694259)
## The required API Endpoints that enable one:
 1. Register a user
 2. Login a user.
 3. Fetch all questions.
 4. Fetch a specific question.
 5. Post a question
 6. Delete a question
 7. Post an answer to a question
 8. Mark an answer as accepted or update an answer.

## The list of the functioning API Endpoints

Method        | EndPoint      | Functionality |
------------- | ------------- | ---------------
POST  | api/v1/auth/signup  | Register a user   |
POST  | api/v1/auth/login  | Login a user   |
GET  | /api/v1/questions   | Fetch all questions   |
GET  | /api/v1/questions/<questionId> | Fetch a specific question   
POST  | /api/v1/questions | Post a question   |
Delete  | /api/v1/questions/<questionId>| Delete a question   |
POST | /api/v1/<questionId>/answers| Post an answer to a question   |
PUT | /api/v1/questions/<questionId>/answers/<answerId>| Mark an answer as accepted or update an answer. |

## Installation
Make sure you have Python3 installed on your machine
- Clone this repo and Switch to it
 ```bash
$ git clone https://github.com/munniomer/StackOverflow-API.git 
$ cd StackOverflow-API
```
- Install a virtual Environment and activate it
 ```bash
$ python -m venv venv 	
$ source venv/bin/activate
```
- Install the dependencies using the requirements file
 ```bash
$ pip install -r requirements.txt
```
- Run the app
 ```bash
$ export FLASK_ENV=development
$ export FLASK_APP=run.py
$ flask run
```
## Testing the endpoints
- Install postman to test the endpoints 

- Open postman and navigate to the localhost and add the enpoint route you are testing
 ```bash
 http://localhost:5000/api/v1/<endpoint>
 
```
## Running tests
To Run the tests you have to use the terminal, switch to the project folder and activate the venv.

- To check if all tests pass
```bash
$ pytest 
```
- To check the test Coverage 

```bash
$ pytest --cov app  
```

## Technologies used
- Python 3.6
- Flask framework
- Unittest for testing

## Author: Munira Omar

__Copyright © Andela 2018__


