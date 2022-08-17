# The Morning Sun

<img src="auth_app/static/svg-seeklogo.com.svg" align="right"
     alt="Size Limit logo by Anton Lovchikov" width="120" height="178">

The Morning Sun is a news scraper app with a built-in note taking functionality coded in Python and Javascript/HTML. This application allows the user to perform the following operations:

* Sign-up for a new account
* Log in with an existing account
* Retrieve the top headlines of the day from the following news sources:
• Al-Jazeera
• The Verge
• The Wall Street Journal
• TechRadar
• Reuters
* Create, read and delete notes

### Setup and Installation
To run the application on your local machine, you need to:
* Clone the repo using `git clone git@github.com:waqar-habib/flask.git`
* Run this command `pip install -r requirements.txt`
* After that, run `python main.py`
• Note: You may have to use `python3 main.py` depending on the version of Python you are running on your machine. 
* Once you see the app execute successfully, navigate to `http://127.0.0.1:5000/`
* Here, you can test out the application either by:
• Creating a new account 
• Logging in with the following credentials:
`test@test.com`
`123456`

### Screenshots

##### Landing Page
<p align="center">
<img src="auth_app/static/home.png"
  width="686" height="289">
</p>
</br>

##### Landing Page

<p align="center">
<img src="auth_app/static/wsj.png"
  width="686" height="289">
</p>
</br>

##### Notes Page
<p align="center">
<img src="auth_app/static/note.png"
  width="686" height="289">
</p>
</br>

##### Login Page
<p align="center">
<img src="auth_app/static/login.png"
  width="500" height="150">
</p>
</br>

##### Sign up Page
<p align="center">
<img src="auth_app/static/sign-up.png"
  width="600" height="350">
</p>

### Code Snippets

#### Classes & Database Models

<p align="center">
<img src="auth_app/static/classes.png" width="400" height="400">
</p>

#### APIs
<p align="center">
<img src="auth_app/static/APIs.png" width="300" height="200">
</p>

#### Jinja templates

`{% for newsReuters, descReuters, imgReuters, urlReuters in context %}`

#### CRUD operations

`@auth.route('/sign-up', methods=['GET', 'POST'])`