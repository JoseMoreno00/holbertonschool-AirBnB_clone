# AirBnB Clone - The Console
![Image](imgs/a.png)

## Description
Airbnb is an online marketplace that connects people 
who want to rent out their property with people who are looking for accommodations, typically for short stays. In this project we are going to make a clone of this website. It is going to be divided in parts, the first part being the console.

## The console

The Console is a command-line interface from wich you can create, modify and delete objects in a file storage.  
This console also allows the user to access the data, by listing, not only all elements of a class, but also specific instances of a specific class.

## Commands

Command|Format|Use
---|---|---
quit | quit | Exits the console
EOF | ctrl + d | Exits the console
help | help (command name) | Explains the use of any command
create | create (class name) | Creates a new instance of a class and prints its id
show | show (class name) (existing id)| Shows an existing instance with all it's info
destroy | destroy (class name) (existing id)| Deletes an existing instance
all | all [class name] | Shows all instances, or all instances of a specific class [] is optional
update | update (class name) (id) (atribute name) (value) | Updates the info of a class instance

## Program flow

Click [here](https://miro.com/welcomeonboard/U0o4amlkWWJrbWdkZUFPRlJLMzB5SjhlMmRLUlRXczM1bGtOVk5ESEhoNHpkTkQ2Sjd6N0t6TVAzMnNqdnF6eXwzNDU4NzY0NTI1Njk3ODc1NTExfDI=?share_link_id=964350957586) to check our program's flowchart.

## Examples
```c
root@2b42d4d732b5:~/holbertonschool-AirBnB_clone# ./console.py 
(hbnb) all
[]
(hbnb) create User
50697b03-1ab9-49ee-8767-e5a765c53c60
(hbnb) show User 50697b03-1ab9-49ee-8767-e5a765c53c60
[User] (50697b03-1ab9-49ee-8767-e5a765c53c60) {'id': '50697b03-1ab9-49ee-8767-e5a765c53c60', 'created_at': datetime.datetime(2023, 10, 28, 8, 36, 27, 74956), 'updated_at': datetime.datetime(2023, 10, 28, 8, 36, 27, 75056)}
(hbnb) show abc
** class doesn't exist **
(hbnb) show User abc
** no instance found **
(hbnb) create BaseModel
fba013b1-4bb1-4a3e-8c31-dd374ca5ca17
(hbnb) all
["[User] (50697b03-1ab9-49ee-8767-e5a765c53c60) {'id': '50697b03-1ab9-49ee-8767-e5a765c53c60', 'created_at': datetime.datetime(2023, 10, 28, 8, 36, 27, 74956), 'updated_at': datetime.datetime(2023, 10, 28, 8, 36, 27, 75056)}", "[BaseModel] (fba013b1-4bb1-4a3e-8c31-dd374ca5ca17) {'id': 'fba013b1-4bb1-4a3e-8c31-dd374ca5ca17', 'created_at': datetime.datetime(2023, 10, 28, 8, 37, 8, 794817), 'updated_at': datetime.datetime(2023, 10, 28, 8, 37, 8, 794864)}"]
(hbnb) destroy BaseModel fba013b1-4bb1-4a3e-8c31-dd374ca5ca17
(hbnb) all
["[User] (50697b03-1ab9-49ee-8767-e5a765c53c60) {'id': '50697b03-1ab9-49ee-8767-e5a765c53c60', 'created_at': datetime.datetime(2023, 10, 28, 8, 36, 27, 74956), 'updated_at': datetime.datetime(2023, 10, 28, 8, 36, 27, 75056)}"]
```

```c
root@2b42d4d732b5:~/holbertonschool-AirBnB_clone# ./console.py 
(hbnb) show User 50697b03-1ab9-49ee-8767-e5a765c53c60
[User] (50697b03-1ab9-49ee-8767-e5a765c53c60) {'id': '50697b03-1ab9-49ee-8767-e5a765c53c60', 'created_at': datetime.datetime(2023, 10, 28, 8, 36, 27, 74956), 'updated_at': datetime.datetime(2023, 10, 28, 8, 36, 27, 75056)}
(hbnb) update User 50697b03-1ab9-49ee-8767-e5a765c53c60 first_name Julius
(hbnb) show User 50697b03-1ab9-49ee-8767-e5a765c53c60
[User] (50697b03-1ab9-49ee-8767-e5a765c53c60) {'id': '50697b03-1ab9-49ee-8767-e5a765c53c60', 'created_at': datetime.datetime(2023, 10, 28, 8, 36, 27, 74956), 'updated_at': datetime.datetime(2023, 10, 28, 8, 41, 44, 417612), 'first_name': 'Julius'}
(hbnb) create User
de8da932-6769-40cb-823e-7ae082e0f34f
(hbnb) create BaseModel
4bde2283-8195-4dc3-b508-f85fa2b1d2a3
(hbnb) all User
["[User] (50697b03-1ab9-49ee-8767-e5a765c53c60) {'id': '50697b03-1ab9-49ee-8767-e5a765c53c60', 'created_at': datetime.datetime(2023, 10, 28, 8, 36, 27, 74956), 'updated_at': datetime.datetime(2023, 10, 28, 8, 41, 44, 417612), 'first_name': 'Julius'}", "[User] (de8da932-6769-40cb-823e-7ae082e0f34f) {'id': 'de8da932-6769-40cb-823e-7ae082e0f34f', 'created_at': datetime.datetime(2023, 10, 28, 8, 44, 41, 648547), 'updated_at': datetime.datetime(2023, 10, 28, 8, 44, 41, 648625)}"]
```

