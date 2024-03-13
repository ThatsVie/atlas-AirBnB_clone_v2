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
![Screenshot 2024-03-13 075201](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/31826cd9-2593-4d33-94e2-eb353b9ebeff)

Open another tab in your terminal and input this command
```bash
curl 0.0.0.0:5000 ; echo "" | cat -e
```
Your ouput should be:

![Screenshot 2024-03-13 074248](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/cbfdd337-ac26-4832-99ab-be087ae5c6c6)

Navigate to your browser. You should see Hello HBNB!

![Screenshot 2024-03-13 073857](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/b5aab8fb-cfd7-4113-b8a1-ee64d74b30de)

**After executing the task, the Flask web application will start running and listening for incoming requests on the specified address and port. To stop the server and return to the command line prompt, you need to press CTRL+C. This key combination sends a KeyboardInterrupt signal to the running process, prompting it to shut down gracefully. It's important to use this method to terminate the server properly and avoid leaving any lingering processes running in the background.**

### Task 1
Navigate back to your original terminal. Press CTRL+C to end the previous process if you havent already.
Input this command to executes the Python module web_flask.1-hbnb_route using Python 3.
```bash
 python3 -m web_flask.1-hbnb_route
```
Your output should look something like this:

![Screenshot 2024-03-13 075355](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/d30228fe-af20-486d-be0f-c8bbb04d6ca4)

Open another tab in your terminal and run this command
```bash
curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
```
You ouput should look like this:
![Screenshot 2024-03-13 075548](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/27e04b69-ce63-4ed9-a6fc-9de9326c3cc6)

Navigate to your browser and input the address
```bash
http://localhost:5000/hbnb
```
You should see HBNB
![Screenshot 2024-03-13 075649](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/0ac1dada-73cf-450d-b64b-f25802b68bee)

**After executing the task, the Flask web application will start running and listening for incoming requests on the specified address and port. To stop the server and return to the command line prompt, you need to press CTRL+C. This key combination sends a KeyboardInterrupt signal to the running process, prompting it to shut down gracefully. It's important to use this method to terminate the server properly and avoid leaving any lingering processes running in the background.**


### Task 2
Navigate back to your original terminal. Press CTRL+C to end the previous process if you havent already.
Input this command to executes the Python module web_flask.2-c_route using Python 3.
```bash
python3 -m web_flask.2-c_route
```
It should look like this:

![Screenshot 2024-03-13 080056](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/c24acf01-e101-4f7b-8c3a-09f8d6a00bd1)

Open another tab in your terminal and input this command
```
curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
```
Your ouput should look like this:
![Screenshot 2024-03-13 080029](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/5d0d3893-f63d-4c72-a6b4-19b0243a97af)

Now, let's view in your browser
```bash
http://localhost:5000/c/is_fun
```
![Screenshot 2024-03-13 080823](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/ade84b3a-f3fa-4211-a6f3-e4b82e7b97f4)

Input this command 
```bash
curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
```
Your ouput should now look like this:
![Screenshot 2024-03-13 080324](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/ecbd2363-29e5-46b2-bdd6-c616512de643)

Now, let's view in your browser:
```bash
http://localhost:5000/c/cool
```
![Screenshot 2024-03-13 080930](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/95d3557c-e38e-403b-8d5c-e98286bfa66b)

If you input this, however,
```bash
curl 0.0.0.0:5000/c
```
This should be your output:
![Screenshot 2024-03-13 080521](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/778f110e-2bf2-4a0b-ba08-49405736f573)

Now, in your browser:

```bash
http://localhost:5000/c
```
![Screenshot 2024-03-13 081103](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/6cf7c023-540d-4ecc-9696-f119959cce78)

**After executing the task, the Flask web application will start running and listening for incoming requests on the specified address and port. To stop the server and return to the command line prompt, you need to press CTRL+C. This key combination sends a KeyboardInterrupt signal to the running process, prompting it to shut down gracefully. It's important to use this method to terminate the server properly and avoid leaving any lingering processes running in the background.**

### Task 3
Navigate back to your original terminal. Press CTRL+C to end the previous process if you havent already.
Input this command to executes the Python module web_flask.3-python_route using Python 3.
```bash
python3 -m web_flask.3-python_route
```


### Task 4


### Task 5


### Task 6


### Task 8


### Task 9


### Task 10


### Task 11

