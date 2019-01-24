# Sendit2
[![Build Status](https://travis-ci.org/paulzay/Sendit2.svg?branch=master)](https://travis-ci.org/paulzay/Sendit2)
[![Coverage Status](https://coveralls.io/repos/github/paulzay/Sendit2/badge.svg?branch=master)](https://coveralls.io/github/paulzay/Sendit2?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/097e6e675fa4821f9b5c/maintainability)](https://codeclimate.com/github/paulzay/Sendit2/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ba14f7479b5e4ee8b26136e1962af1d7)](https://www.codacy.com/app/paulzay/Sendit2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=paulzay/Sendit2&amp;utm_campaign=Badge_Grade)

SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.

## Getting Started

	.Python 3.6

	.Postman

	.Git


## Installing

   .Clone or download the project from git either via terminal using the commands git clone :https://github.com/PAULZAY/Sendit2.git or Download zip file from the right hand corner

    .Ensure Python 3.6 is installed
	
    .To test the API locally, set up a virtual environment in the root folder 
    - virtualenv env
	
    .Activate the virtual environment through; source env/bin/activate via the terminal
	
    .Run the export FLASK_APP=run.py command via the terminal
	
    .Install dependencies through pip install -r requirements.txt
	
    .Test using Nosetests
	
    .Test in Heroku here [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://zay-sendit.herokuapp.com/api/v1/)
    ## Use the following endpoints to perform the specified tasks
		 
| 	Endpoint                          | Functionality                                                  
| ----------------------------------------| -----------------------------------------------|
| POST /api/v1/parcels                    | Create a parcel delivery                       |
| GET /api/v1/parcels                     | Retrieve all parcel delivery                   |
| PUT /api/v1/parcels/<int:parcel_id>/    | Cancel a specific parcel delivery              |
| GET /api/v1/parcels/<int:parcel_id>     | Retrieve a specific parcel delivery            |
| GET /api/v1/parcels/<str:sender_email   | Fetch all delivery orders for a user           |
|
