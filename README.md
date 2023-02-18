# Price Paid Data API
API created with Django REST Framework containing data from UK Price Paid Data file ([LINK](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads#single-file)). 

## Table of contents
* [Functionalities](#functionalities)
* [Technologies](#technologies)
* [Setup](#setup)
* [Contact](#contact)

## Functionalities
* Command populating database with PPD file lines
* Endpoint with list of transactions stored in database
* Filtering API response
* Ordering API response

## Technologies
* Python 3.9.7
* PostgreSQL 13
* Django 4.1.7
* Django REST Framework 3.14.0
* requests 2.28.2

## Setup
To install and run app you will need to:
* Clone this repository to your computer or unpack .zip file in chosen directory,
* Install PostgreSQL, create user and database,
* Fill .env file with PostreSQL credentials and database name. Environment file contains default values of demanded variables,
* Run IDE or command line,
* Command in IDE to install demanded packages:
> pip install -r **{your_directory}**/requirements.txt
* Run database migrations
> python **{your_directory}**/ppd_api/manage.py migrate
* Load data from PPD file. This command by default loads 100 first rows of given file. If you want to add other number of rows pass it in --rows argument. 
> python **{your_directory}**/ppd_api/manage.py load_data --url="http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv"
* Run local server
> python **{your_directory}**/ppd_api/manage.py runserver
* Go to  http://127.0.0.1:8000/ in your browser


## Contact
Created by [@matedawid](https://linkedin.com/in/matedawid) - if you have any questions, just contact me!