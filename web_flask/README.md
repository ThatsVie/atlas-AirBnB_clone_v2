# AirBnB Clone Web Framework
This project implements a web framework for an AirBnB clone using Flask, a lightweight WSGI web application framework. It includes various tasks that demonstrate the functionality of the web application, such as displaying different routes, rendering HTML templates, and interacting with a database.

## Requirements
Before running the application, ensure you have the following installed:

Python 3.x

MySQL

SQLAlchemy

MySQLDB (Python MySQL client library)

Flask

## Tasks Overview

- **Hello Route (Task 0):** Display "Hello HBNB!" on the root route.

- **HBNB Route (Task 1):** Display "Hello HBNB!" on the root route and "HBNB" on the /hbnb route.

- **C Route (Task 2):** Display "C" followed by the value of the text variable.

- **Python Route (Task 3):** Display "Python" followed by the value of the text variable (default: "is cool").

- **Number Route (Task 4):** Display "n is a number" only if n is an integer.

- **Number Template (Task 5):** Display an HTML page with "Number: n" if n is an integer.

- **Number Odd or Even (Task 6):** Display an HTML page with "Number: n is even|odd" if n is an integer.
  
- **Improve Engine (Task 7):** Update pre existing files FileStorage (models/engine/file_storage.py), DBStorage (models/engine/db_storage.py), and State (models/state.py) before moving forward with tasks.

- **States List (Task 8):** Display a list of all State objects present in the database.

- **Cities by States (Task 9):** Display a list of all State objects and their linked City objects.

- **States and State (Task 10):** Display detailed information about states and their linked cities.

- **HBNB Filters (Task 11):** Display a HTML page with filters for states, cities, and amenities.

## Usage

### Clone the Repository
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/ThatsVie/atlas-AirBnB_clone_v2.git
```
### Task 0
Navigate to atlas-AirBnB_clone_v2 directory
```bash
cd atlas-AirBnB_clone_v2
```
Input this command to executes the Python module web_flask.0-hello_route using Python 3.
```bash
python3 -m web_flask.0-hello_route
```
Your ouput should look something like this:
```bash
vie@ThatsVie:~/source/atlas-AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app '0-hello_route'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.25.115.237:5000
Press CTRL+C to quit
```
Open another tab in your terminal and input this command
```bash
curl 0.0.0.0:5000 ; echo "" | cat -e
```
Your ouput should be:

![Screenshot 2024-03-13 074248](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/cbfdd337-ac26-4832-99ab-be087ae5c6c6)

Navigate to your browser. You should see Hello HBNB!

![Screenshot 2024-03-13 073857](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/b5aab8fb-cfd7-4113-b8a1-ee64d74b30de)


### Task 1


### Task 2


### Task 3


### Task 4


### Task 5


### Task 6


### Task 8


### Task 9


### Task 10


### Task 11

