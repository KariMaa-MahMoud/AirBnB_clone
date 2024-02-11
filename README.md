\*Description of the project:

The goal of the project is to replica of the Airbnb Website using my console.

folders/files:

1- models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
2- tests directory will contain all unit tests.
3- console.py file is the main file of our command interpreter.
4- models/base_model.py file is the base class of all our models(parent). It contains common elements:
*attributes: unique_id, created_at and updated_at
*methods: save() and to_json()
5- models/engine directory will contain all storage classes.

- how to start it:

* Creat a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of instances.
* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all our classes and storage engine
* Create a data model that Manage (create, update, destroy, etc) objects via a console/command interpreter
* Store and persist objects to files (JSON files)

\*Description of the command interpreter:

Commands Description:
1-exit exits the console
2-Ctrl+D Quits the console
3-help or help <command> Displays all commands or Displays instructions for a specific command
4-create <class> Creates an object of type , saves it to a JSON file, and prints the objects ID
5-show <class> <unique_ID> Shows string representation of an object
5-destroy <class> <unique_ID> Deletes an objects
6-all or all <class> Prints all string representations of all objects or Prints all string representations of all objects of a specific class
7-update <class> <unique_id> <attribute name> "<attribute value>" Updates an object with a certain attribute (new or existing)
8-<class>.all() Same as all <class>
9-<class>.count() Retrieves the number of objects of a certain class
10-<class>.show(<unique_ID>) Same as show <class> <unique_ID>
11-<class>.destroy(<unique_ID>) Same as destroy <class> <unique_ID>
12-<class>.update(<unique_ID>, <attribute name>, <attribute value> Same as update <class> <unique_ID> <attribute name> <attribute value>
<class>.update(<unique_ID>, <dictionary representation>) Updates an objects based on a dictionary representation of attribute names and values.

\*General Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

# Documented commands (type help <topic>):

EOF help exit
(hbnb)
(hbnb)
(hbnb) exit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

# Documented commands (type help <topic>):

EOF help exit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

# Documented commands (type help <topic>):

EOF help exit
(hbnb)
$
