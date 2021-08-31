# Job Finder

This project served as an introduction to building a full stack, multi page web app, using Flask for the backend functionality, and React for the frontend, connected via a REST API.

Initial functionality includes create account / login / logout with regex validation and bcrypt encryption (handles salt/hash and stores salt in hash for security). Flask Session for encrypted server-side sessions. Navbar for navigation. Account management including changing passwords and deleting account from db. Contact form using smtplib. Job search by title and location, returns results from multiple websites, combined. Ability to save/unsave jobs to db.

Following this I will create an application tracker, showing saved jobs and their application status, this will include responsive drag and drop status changes, and edit job info functionality.

## Challenges

    - Initially built using just Flask, this made responsiveness, UI and design a little more difficult
    - Initially client-side sessions left unsecure data in broswer
    - JQuery not the best implementation, need to change
    - Free mySQL hosting was using old version so newer default datetime not working
    - Contact form not working with environment variables initially
    - Combination of data from Scraper, lots of factors to consider to remove duplicates, also Indeed changed frontend layout midway through so had to re-do. Need to add testing to ensure this is caught early in future

## File Structure

```
.
├── flask-backend 
│   ├── flask_session           # Server-side sessions    
│   ├── venv                    # Virtual environment 
│   ├── website                 # Flask files
│   │   ├── static              # Assets and base CSS/Js
│   │   │   ├── assets          # Images folder   
│   │   │   ├── app.js          # Js main   
│   │   │   ├── form.js         # Form functionaltiy JQuery   
│   │   │   └── sytles.css      # CSS main    
│   │   ├── templates           # HTML templates
│   │   ├── __init__.py         # Initialise Flask/tools   
│   │   ├── auth.py             # Authentication handler   
│   │   ├── combines_jobs.py    # Scraper combine tool
│   │   ├── contact.py          # Email functionality
│   │   ├── db.py               # Database & queries 
│   │   ├── indeed_scraper.py   # Job scraper 1 
│   │   ├── reed_scraper.py     # Job scraper 2
│   │   └── views.py            # Routing
│   ├── test                    # Automated tests - in progress
│   ├── app.py            
│   ├── Procfile                # For Heroku deployment  
│   └── requirements.txt          
├── react-frontend              
│   ├── node modules            # Node files
│   ├── public                  # Public files
│   ├── src                     # Source files 
│   │    ├ components           # Component files
│   │    ├ styles               # Scss files
│   │    ├ views                # Views (components)
│   │    ├ App.js               # Main app
│   │    ├ index.js             
│   │    └ reportWebVitals.js   
│   ├── test                    # Automated tests - in progress
│   ├── package-lock.json
│   └── package.json
├── docs                    # Documentation files
└── README.md
```