
![AirBnB_clone_v2](https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/144152489/fea4e1cb-eb30-4e4b-bafa-d59aa67d6e52)

<br>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Static Badge](https://img.shields.io/badge/Queers%20Ruling-Code%20Space-purple?style=string&logoColor=purple) 
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

<h3><p align="center">
	Original repo forked from this <a href="https://github.com/justinmajetich/AirBnB_clone">codebase</a>,
edits and new additions by ✨ <a href="https://github.com/ThatsVie/">Vie</a> and  <a href="https://github.com/Srixx24/">Jackie</a> ✨
</h3></p>

<br>

This repository contains the initial stages of our student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. 

<br>

New additions were made to increase functionality of the consoles data storage and management. SQLAlchemy was used in our storage engine to help streamline this process. 

<br>

Lastly we used a Many-to-Many relationship to link an amenity to multiple places and so a place can have multiple amenities. This feature helps reduce the overall code size, helps with code flexibility, and enables efficient querying of related data.

---
<center> <h3>General Use</h3> </center>

1. The console can be ran by typing in the terminal:
 ```
/AirBnB_clone$ ./console.py
 ```

2. When this command is run the following prompt should appear:
```
(hbnb)
```
3. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h3>Examples</h3> </center>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
---

<p align="center">
  <img width="350" src="https://github.com/ThatsVie/atlas-AirBnB_clone_v2/assets/144152489/4f106fa6-839e-4ccc-b4db-ad4f14f76c26">
</p>

All testing, files, and code works as intended. All checks green with the single exception of "Can list all City in MySQL (created outside the program)"
check (worth 1 point). 
