# Sendit
[![Build Status](https://travis-ci.org/paulzay/Sendit2.svg?branch=master)](https://travis-ci.org/paulzay/Sendit2)
[![Coverage Status](https://coveralls.io/repos/github/paulzay/Sendit2/badge.svg?branch=master)](https://coveralls.io/github/paulzay/Sendit2?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/097e6e675fa4821f9b5c/maintainability)](https://codeclimate.com/github/paulzay/Sendit2/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ba14f7479b5e4ee8b26136e1962af1d7)](https://www.codacy.com/app/paulzay/Sendit2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=paulzay/Sendit2&amp;utm_campaign=Badge_Grade)

SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.

## Live demo
[live demo link](https://shipr.herokuapp.com/api/v1/)

## Getting Started

	.Python 3.6

	.Postman

	.Git

	.Nosetest

	.Flask

	.Flask-restful

# Getting Started 🚀

These instructions will get you a copy of the project up and running on your local machine.

## How To Use 🔧

From your command line, first clone the project:

1. Clone the repo or Download zip file from the right hand corner

   > `https://github.com/paulzay/Sendit2/`
   
2. cd into the project folder.

## First install

1. python3

   > `sudo apt-get install python3`

2. install python3 pip

   > `sudo apt-get install python3-pip`

3. install vitual environment

   > `pip3 install virtualenv`

5. create the virtual environment

   > `virtualenv env`

6. Activate the vitualenv in the parent directory of your **"env"**

   > `source env/bin/activate`

7. Install requirement

   > `pip install -r requirements.txt`

8. Run the app

   > `flask run`

9. Testing

   > `nosetests`

| 	Endpoint                          | Functionality                                                  
| ----------------------------------------| -----------------------------------------------|
| POST /api/v1/parcels                    | Create a parcel delivery                       |
| GET /api/v1/parcels                     | Retrieve all parcel delivery                   |
| PUT /api/v1/parcels/<int:parcel_id>/    | Cancel a specific parcel delivery              |
| GET /api/v1/parcels/<int:parcel_id>     | Retrieve a specific parcel delivery            |
| GET /api/v1/parcels/<str:sender_email>  | Fetch all delivery orders for a user           |


## CONTRIBUTOR

👤 **Paul Ogolla**

- [Github](https://github.com/paulzay)
- <img width="40" valign="middle" src="https://storage.googleapis.com/gregsramblings-downloads/Twitter_Logo_Blue.png">[Twitter](https://twitter.com/_paulzay_)
- [Linkedin](https://linkedin.com/in/paulogolla)

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- Andela

## 📝 License
 - MIT
