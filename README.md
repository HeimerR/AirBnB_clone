# Holberton-AirBnB clone

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

[![holberton_airbnb_logo](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20190703%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190703T152323Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fad27256d815f6d0b1720d8d7a9effc1b6995a5254853cede6512b6741a08605)]

AirBnB-clone is a web application that seeks to replicate the AirBnB software platform for educational purposes. 

### Definition:

According to Wikipedia:

> Airbnb, Inc., is an American online marketplace and hospitality service brokerage company based in San Francisco, California, United States. Members can use the service to arrange or offer lodging, primarily homestays, or tourism experiences.

### Block Diagram of the Project:

![holberton-pipeline](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20190703%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190703T152323Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ea2fde939c393fae2f9efb865aa4ab40200d83f42efe387d329c3acfae3efb5a)

### Tech

AirBnB-clone uses a number of open source projects to work properly:

* [Python](https://github.com/python) - Python programming language

# Console

### Installation:

AirBnB-clone requires Python version. 3.4.3 to run.

### How to run:

```sh
# First clone the repo
$ git clone https://github.com/HeimerR/AirBnB_clone.git
# Second executes the file "console.py" inside the folder AirBnB_clone
$ cd AirBnB_clone && ./console.py
# Start using the console!
```

### How to use it:

You will get a prompt like this:
```sh
(hbnb) 
```
You can now start typing console commands to create, update or destroy users, places, etc.
```sh
(hbnb) create User
697d2586-e3ca-451a-8221-88ead0eb8283
(hbnb)
```

### Commands available:

The following commands are available to use:

| Command | Arguments |
| ------ | ------ |
| create | `<class name>` |
| show | `<class name> <id>` |
| destroy | `<class name> <id>` |
| all | `[OPTIONAL <class name>]`  |
| update | `<class name> <id> <attribute name> "<attribute value>"`  |
| `<class name>.<command>(arguments)`| it depends on the type of command you use |

### Classes available:

The following commands are available to use:

| Class name | Default Attributes |
| ------ | ------ |
| BaseModel | `id, created_at, updated_at` |
| User | `email, password, first_name, last_name` |
| Place | `city_id, user_id, name, description, number_rooms, number_bathrooms` |
| Place | `max_guest, price_by_night, latitude, longitude, amenity_ids` |
| State | `name`  |
| City | `state_id, name`  |
| Amenity | `name`  |
| Review | `place_id, user_id, text`  |

### Example

Let's create a user:
```sh
(hbnb) create User
dcc89f74-2663-4f2d-b647-9c829d2b4797
(hbnb)
```

Now, let's see what it has this instance:
```sh
(hbnb) show User dcc89f74-2663-4f2d-b647-9c829d2b4797
[User] (dcc89f74-2663-4f2d-b647-9c829d2b4797) {'updated_at': datetime.datetime(2019, 7, 3, 19, 14, 32, 536201), 'id': 'dcc89f74-2663-4f2d-b647-9c829d2b4797', 'created_at': datetime.datetime(2019, 7, 3, 19, 14, 32, 536180)}
(hbnb)
```

Let's update an attribute and display all the users:
```sh
(hbnb) User.update("dcc89f74-2663-4f2d-b647-9c829d2b4797", "first_name", "Heimer")
(hbnb) User.all()
["[User] (dcc89f74-2663-4f2d-b647-9c829d2b4797) {'created_at': datetime.datetime(2019, 7, 3, 19, 14, 32, 536180), 'id': 'dcc89f74-2663-4f2d-b647-9c829d2b4797', 'first_name': 'Heimer', 'updated_at': datetime.datetime(2019, 7, 3, 19, 18, 4, 845273)}", "[User] (697d2586-e3ca-451a-8221-88ead0eb8283) {'created_at': datetime.datetime(2019, 7, 3, 17, 55, 49, 24311), 'id': '697d2586-e3ca-451a-8221-88ead0eb8283', 'updated_at': datetime.datetime(2019, 7, 3, 18, 1, 19, 126604)}"]
```
Let's delete the user we created:
```sh
(hbnb) destroy User dcc89f74-2663-4f2d-b647-9c829d2b4797
(hbnb) show User dcc89f74-2663-4f2d-b647-9c829d2b4797
** no instance found **
(hbnb)
```
License
----

MIT
