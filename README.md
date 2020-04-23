# Capital Services - Flask Project

Flask Project for Capital Services (BU MET CS 634);

### Prerequisites
```
+Python 3.6.5+
```

### Installing requirements

install via requirements.txt - see getting started for more exact instructions

```
pip install -r requirements.txt
```

## Getting Started
```
git clone https://github.com/ckarjadi/capital_services

cd capital_services/

pip install -r requirements.txt

git checkout <branch> ## master / stable / test

git pull ## if your head is behind the branch you're checking out

flask run

navigate to localhost:5000 in a browser (Chrome, Safari, etc) to see the application

```

### Run the application

```
flask run
```

### Important notes about email functionality and credentials

```
In order for the email functionalities to work (emails are being sent when certain actions occur on the website),
the developer has to supply a gmail username and gmail password.

The credentials used to develop this program have not been included in this public repository.

A developer can supply their own credentials directly in app/send_email.py on line 19 or the developer can
create another way to supply their email credentials to the program. username, pwd have to be defined in
app/send_email.py in some way for the emailing to work.

A developer also must supply their own email address to receive the 'Contact Us' emails.
This can be done in app/routes.py on line 34 or in any other way that defines
the CONTACT_US_EMAIL variable in that file.

```

## Built With

* [Flask](https://github.com/pallets/flask) - The web framework used

## Authors

* **Alina Akram**
* **Michael Broadman**
* **Lauren Cvilikas**
* **Mackenzie Feeley**
* **Mike Hodge**
* **Cody Karjadi**
* **Namita Kasbekar**
* **Chenrun Liu**
* **Steven Shoyer**
