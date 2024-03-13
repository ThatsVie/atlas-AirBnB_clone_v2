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

- **C Route (Task 2):** Display "C" followed by the value of the text variable. ( /c/< text > )
 
- **Python Route (Task 3):** Display "Python" followed by the value of the text variable . default: "is cool". ( /python/< text > )

- **Number Route (Task 4):** Display "n is a number" only if n is an integer. ( /number/< n > )

- **Number Template (Task 5):** Display an HTML page with "Number: n" if n is an integer. ( /number_template/< n > ) 

- **Number Odd or Even (Task 6):** Display an HTML page with "Number: n is even|odd" if n is an integer. ( /number_odd_or_even/< n > )
  
- **Improve Engine (Task 7):** Update pre existing files FileStorage (models/engine/file_storage.py), DBStorage (models/engine/db_storage.py), and State (models/state.py) before moving forward with tasks.

- **States List (Task 8):** Display a list of all State objects present in the database. ( /states_list )

- **Cities by States (Task 9):** Display a list of all State objects and their linked City objects. ( /cities_by_states )

- **States and State (Task 10):** Display detailed information about states and their linked cities. ( /states and /states/< id > )

- **HBNB Filters (Task 11):** Display a HTML page with filters for states, cities, and amenities. ( /hbnb_filters )

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
![Screenshot 2024-03-13 081633](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/9d8b9a80-5e5e-4a6c-a0af-563a76d59f05)

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
![Screenshot 2024-03-13 081804](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/fe6286e7-4f0b-4aa8-915e-741f04ad7b40)

Open another tab in your terminal
Input this command
```bash
curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
```
![Screenshot 2024-03-13 081944](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/2ca2d4f2-ed40-4f25-98af-3ab7f705c03d)

Input this command
```bash
curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
```
![Screenshot 2024-03-13 082036](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/c74d6d97-7597-42c7-8663-26b7e0937577)

Input this command:
```bash
curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
```
![Screenshot 2024-03-13 082149](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/60ce2c93-d9be-4f74-a18c-d1d322d78808)

Now in your browser:
```bash
http://localhost:5000/python/is_magic
```
![Screenshot 2024-03-13 082246](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/9fdb8597-b2f5-40bb-b48a-664304452691)

```bash
http://localhost:5000/python
```

![Screenshot 2024-03-13 082414](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/6dd6d796-3f1a-4613-9b7c-6556548e4bb7)

```bash
http://localhost:5000/python/
```
![Screenshot 2024-03-13 082535](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/d4bb80ea-ad5c-4b17-8bc2-90bea8440346)

**After executing the task, the Flask web application will start running and listening for incoming requests on the specified address and port. To stop the server and return to the command line prompt, you need to press CTRL+C. This key combination sends a KeyboardInterrupt signal to the running process, prompting it to shut down gracefully. It's important to use this method to terminate the server properly and avoid leaving any lingering processes running in the background.**

### Task 4
Navigate back to your original terminal. Press CTRL+C to end the previous process if you havent already.
Input this command to executes the Python module web_flask.4-number_route using Python 3.
```bash
python3 -m web_flask.4-number_route
```
![Screenshot 2024-03-13 091601](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/9c57aaa9-215e-4e72-8146-59f8fccc69f7)

Open another tab in your terminal and run this command:
```bash
curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
```
![Screenshot 2024-03-13 091544](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/f88a0c7f-a8a6-4e23-85a4-3e445ef3c1e1)
On the browser:
```bash
http://localhost:5000/number/89
```
![Screenshot 2024-03-13 091811](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/15114a8a-a344-4e2e-9d6a-3c52dc90777e)

Back in your terminal:
```bash
curl 0.0.0.0:5000/number/8.9
```
![Screenshot 2024-03-13 092015](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/906746dc-ab24-4494-a9cc-1981b3ae5917)

In your browser:
```bash
http://localhost:5000/number/8.9
```
![Screenshot 2024-03-13 091943](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/875822d1-b7b6-478d-8a5b-d0c61ba01776)

Back in your terminal
```bash
curl 0.0.0.0:5000/number/python
```
![Screenshot 2024-03-13 092527](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/0ec4f0f9-a0c1-4783-82d5-b9a3f2724dd6)


In your browser
```bash
http://localhost:5000/number/python
```
![Screenshot 2024-03-13 092635](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/3b1f8fed-b0f3-41b5-aad3-ea4d0a4b21b2)

**After executing the task, the Flask web application will start running and listening for incoming requests on the specified address and port. To stop the server and return to the command line prompt, you need to press CTRL+C. This key combination sends a KeyboardInterrupt signal to the running process, prompting it to shut down gracefully. It's important to use this method to terminate the server properly and avoid leaving any lingering processes running in the background.**

### Task 5
Navigate back to your original terminal. Press CTRL+C to end the previous process if you havent already.
Input this command to executes the Python module web_flask.5-number_template using Python 3.
```bash
python3 -m web_flask.5-number_template
```
Open another tab in your terminal and run this command:
```bash
curl 0.0.0.0:5000/number_template/89 ; echo ""
```
![Screenshot 2024-03-13 093035](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/86701ec8-2771-42e9-8bf9-3ede036a4707)


In your browser
```bash
http://localhost:5000/number_template/89
```
![Screenshot 2024-03-13 093142](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/0a652fe8-4127-485d-bae5-ea2ea48bafeb)

Back in your terminal
```bash
curl 0.0.0.0:5000/number_template/8.9
```

In your browser
```bash
http://localhost:5000/number_template/8.9
```
![Screenshot 2024-03-13 093435](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/4151ae71-72fc-40d7-ad76-f2d971e21347)

Back in your terminal:
```bash
curl 0.0.0.0:5000/number_template/python
```
![Screenshot 2024-03-13 093546](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/5942e9c6-88df-46e0-8a61-fb4392d744a8)

Back in browser:
```bash
http://localhost:5000/number_template/python
```

![Screenshot 2024-03-13 093638](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/5655ab45-cbf6-4b11-9230-a6e4bde4986c)

**After executing the task, the Flask web application will start running and listening for incoming requests on the specified address and port. To stop the server and return to the command line prompt, you need to press CTRL+C. This key combination sends a KeyboardInterrupt signal to the running process, prompting it to shut down gracefully. It's important to use this method to terminate the server properly and avoid leaving any lingering processes running in the background.**

### Task 6
Navigate back to your original terminal. Press CTRL+C to end the previous process if you havent already.
Input this command to executes the Python module web_flask.6-number_odd_or_even using Python 3
```bash
python3 -m web_flask.6-number_odd_or_even
```
![Screenshot 2024-03-13 094001](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/60ef577b-7bad-499a-8878-63554325608d)

Open another tab in your terminal:
```bash
curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
```
![Screenshot 2024-03-13 094050](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/8b3325a7-e6f6-4f1d-a886-22d9d86feec3)

In your browser:
```bash
http://localhost:5000/number_odd_or_even/89
```
![Screenshot 2024-03-13 094302](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/d8016014-e807-46f7-bfa6-d0bc6b31e2d4)

Back in your terminal:
```bash
curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
```
![Screenshot 2024-03-13 094404](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/2974bbc8-653b-4036-9485-11779c800bfd)

In your browser:
```bash
http://localhost:5000/number_odd_or_even/32
```

![Screenshot 2024-03-13 094511](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/40eec025-c0a9-4cc3-acf4-08334df696ac)


Back in your terminal:
```bash
curl 0.0.0.0:5000/number_odd_or_even/python
```
![Screenshot 2024-03-13 094633](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/1f70c4bc-7303-4017-8634-fd72ef4e9e6b)

In your browser:
```bash
http://localhost:5000/number_odd_or_even/python
```
![Screenshot 2024-03-13 094719](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/51d8fd64-d769-45be-a5c2-e366a82b7727)

**After executing the task, the Flask web application will start running and listening for incoming requests on the specified address and port. To stop the server and return to the command line prompt, you need to press CTRL+C. This key combination sends a KeyboardInterrupt signal to the running process, prompting it to shut down gracefully. It's important to use this method to terminate the server properly and avoid leaving any lingering processes running in the background.**

### Task 8
Navigate back to your original terminal. Press CTRL+C to end the previous process if you havent already.
Run this command to concatenate data to work with
```bash
cat 100-hbnb.sql | mysql -uroot -p
```
Then:
```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
```
![Screenshot 2024-03-13 095111](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/d12b72dc-05d6-4671-be3d-6dc60cfad0c9)

Open another tab in your terminal and input this command
```bash
curl 0.0.0.0:5000/states_list ; echo ""
```
![Screenshot 2024-03-13 095305](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/a9c0cb34-bfdc-468f-9fe8-4a878a8bac43)

In your browser:
```bash
http://localhost:5000/states_list
```
![Screenshot 2024-03-13 095402](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/d9642a57-b82f-4fe5-a082-ed625ee74608)

**After executing the task, the Flask web application will start running and listening for incoming requests on the specified address and port. To stop the server and return to the command line prompt, you need to press CTRL+C. This key combination sends a KeyboardInterrupt signal to the running process, prompting it to shut down gracefully. It's important to use this method to terminate the server properly and avoid leaving any lingering processes running in the background.**

### Task 9
Navigate back to your original terminal. Press CTRL+C to end the previous process if you havent already.
Run this command to concatenate data to work with
```bash
cat 100-hbnb.sql | mysql -uroot -p
```
Then:
```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
```

![Screenshot 2024-03-13 145015](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/880f892e-ed72-4c30-8b38-4ece56bff3de)

Open another tab in your terminal and input this command
```bash
curl 0.0.0.0:5000/cities_by_states ; echo ""
```
![Screenshot 2024-03-13 100507](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/df4d553e-6bbd-4669-8f38-fbd87e3a0391)

In your browser:
```bash
http://localhost:5000/cities_by_states
```
![Screenshot 2024-03-13 100610](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/4414e941-76a0-4d7c-9374-4b970febbbad)

**After executing the task, the Flask web application will start running and listening for incoming requests on the specified address and port. To stop the server and return to the command line prompt, you need to press CTRL+C. This key combination sends a KeyboardInterrupt signal to the running process, prompting it to shut down gracefully. It's important to use this method to terminate the server properly and avoid leaving any lingering processes running in the background.**

### Task 10
Navigate back to your original terminal. Press CTRL+C to end the previous process if you havent already.
Run this command to concatenate data to work with
```bash
cat 100-hbnb.sql | mysql -uroot -p
```
Then:
```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
```
![Screenshot 2024-03-13 101202](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/91a8b638-9b71-411b-9432-29ce5c5dbb65)


Open another tab in your terminal and input this command:
```bash
curl 0.0.0.0:5000/states ; echo ""
```

![Screenshot 2024-03-13 101331](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/bcf9370e-7da6-48ae-b613-53fad5f9a539)

In your browser:
```bash
http://localhost:5000/states
```

![Screenshot 2024-03-13 112833](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/262c21a4-0bce-40de-86f2-250a7fc1bf53)

In your terminal:

```bash
curl 0.0.0.0:5000/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd ; echo ""
```
![Screenshot 2024-03-13 104305](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/e504f9bb-63f3-4fd4-be09-734396d3fb84)

In your browser:
```bash
http://localhost:5000/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd
```
![Screenshot 2024-03-13 104443](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/9a7ecf33-a50e-444c-9a8f-dfb03d352d58)

In your terminal:

```bash
curl 0.0.0.0:5000/states/holberton ; echo ""
```
![Screenshot 2024-03-13 103243](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/50a53007-9e0b-4580-b080-d7ac72ee2883)


In your browser
```bash
http://localhost:5000/states/holberton
```

![Screenshot 2024-03-13 104955](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/04d3af29-310d-48f1-972f-e8cd8e15f199)

**After executing the task, the Flask web application will start running and listening for incoming requests on the specified address and port. To stop the server and return to the command line prompt, you need to press CTRL+C. This key combination sends a KeyboardInterrupt signal to the running process, prompting it to shut down gracefully. It's important to use this method to terminate the server properly and avoid leaving any lingering processes running in the background.**

### Task 11
Navigate back to your original terminal. Press CTRL+C to end the previous process if you havent already.
Run this command to concatenate data to work with
```bash
cat 100-hbnb.sql | mysql -uroot -p
```
Then:
```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
```
![Screenshot 2024-03-13 144646](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/93951ce1-a7fe-49a2-9ac8-9d45546e1b91)


In your browser
```bash
http://localhost:5000/hbnb_filters
```
![Screenshot 2024-03-13 101915](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/a34d2b9c-3052-4b3f-8b60-ba34021771f3)

![Screenshot 2024-03-13 101928](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/2e55ec20-a9e9-4ca7-88ec-9c4339cc7fd2)

![Screenshot 2024-03-13 101944](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/cb96a801-eda6-4431-8181-8bb3b1d90388)

And the final view of your terminal:
![Screenshot 2024-03-13 112317](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/143755961/c6d33c75-3d91-4cff-8a21-da951b5bfd4c)

K! Thanx! Bye!
