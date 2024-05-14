# WSAA-bigproject
WSAA big project Spring 2024

## PROJECT TITLE
PROJECT TYPE B: AVIATION DATA SERVICE WITH FLASK AND REST API

## PROJECT BRIEF
The objective of this project is to retrieve data on airport infrastructure in European countries from 2001 to 2021. Airport data was extracted from Eurostat and the web application was created in Flask. The python code consumes the Eurostat data and displays it in the html dashboard page. The web application is hosted on pythonanywhere.com.

The components are:

> app.py, which is the main entry point of the Flask application. It initializes the Flask app, sets up the database connection, and establishes the routes for different API endpoints and web pages.

> routes.py, which contains the route definitions that handle incoming requests from the web interface. It includes functions for CRUD operations.

> wsgi_for_pythonanywhere.py.py, which serves as the entry point for the WSGI server to run the Flask application. It initializes the Flask app and provides the server with the callable application object.

> base.html, which is the base template that other HTML pages inherit from. It contains elements such as the header, footer, and navigation bar.

> index.html, which serves as the main landing page of the web application. It contains a list of available data and options to interact with the API.

> dashboard.html, which provides a more detailed view of the data and allowing users to perform CRUD operations via a user-friendly interface.

The user can perform CRUD operations by making a request via REST API endpoints which handle requests and return responses in JSON format. The application interacts with MySQL database, used PyMySQL for MySQL database connectivity and SQLAlchemy as a tool for database interaction. The HTML templates consume the API endpoints to display data to users and allow them to perform CRUD operations. Plotly was used as a plotting library for data visualization.

## REFERENCES

### Course material
Beatty, A. (2024). andrewbeattycourseware/wsaa-course-material. [online] GitHub. Available at: https://github.com/andrewbeattycourseware/wsaa-course-material [Accessed 1 May 2024].

### Eurostat
Cazzaniga, N.E. (n.d.). eurostat: Eurostat Python Package. [online] PyPI. Available at: https://pypi.org/project/eurostat/ [Accessed 9 May 2024].

Chirita, G. (2023). Eurostat API. [online] kaggle.com. Available at: https://www.kaggle.com/code/crischir/eurostat-api [Accessed 10 May 2024].

Eurostat (2024). Number of commercial airports. [online] Europa.eu. Available at: https://ec.europa.eu/eurostat/databrowser/view/avia_if_arp/default/bar?lang=en&category=avia.avia_if [Accessed 6 May 2024].

Eurostat (n.d.). API - Getting started - Eurostat Online Help for Data Browser - EC Public Wiki. [online] wikis.ec.europa.eu. Available at: https://wikis.ec.europa.eu/display/EUROSTATHELP/API+-+Getting+started [Accessed 9 May 2024].

Eurostat (n.d.). API Statistics - data query - Eurostat Online Help for Data Browser - EC Public Wiki. [online] wikis.ec.europa.eu. Available at: https://wikis.ec.europa.eu/display/EUROSTATHELP/API+Statistics+-+data+query [Accessed 9 May 2024].

Eurostat (n.d.). API - Detailed guidelines - API Statistics - Eurostat Online Help for Data Browser - EC Public Wiki. [online] wikis.ec.europa.eu. Available at: https://wikis.ec.europa.eu/display/EUROSTATHELP/API+-+Detailed+guidelines+-+API+Statistics [Accessed 9 May 2024].

Eurostat (2023). Database - Eurostat. [online] ec.europa.eu. Available at: https://ec.europa.eu/eurostat/web/main/data/database [Accessed 1 May 2024].

Judge, C. (n.d.). Python function to get Eurostat web services data as Pandas DataFrame. [online] Gist. Available at: https://gist.github.com/ciaranjudge/43a9b3d9dacff77905e9eff59bc372c6 [Accessed 9 May 2024].

Stack Overflow (2018). pandas data mining from Eurostat. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/50390889/pandas-data-mining-from-eurostat [Accessed 9 May 2024].

### Flask
Flask (2010). Welcome to Flask — Flask Documentation (3.0.x). [online] flask.palletsprojects.com. Available at: https://flask.palletsprojects.com/en/3.0.x/ [Accessed 8 May 2024].

Flask (n.d.). Blueprints and Views — Flask Documentation (3.0.x). [online] flask.palletsprojects.com. Available at: https://flask.palletsprojects.com/en/3.0.x/tutorial/views/ [Accessed 8 May 2024].

Flask (2023). flask/examples/tutorial/flaskr/auth.py at 3.0.3 · pallets/flask. [online] GitHub. Available at: https://github.com/pallets/flask/blob/3.0.3/examples/tutorial/flaskr/auth.py [Accessed 1 May 2024].

Flask (n.d.). JavaScript, fetch, and JSON — Flask Documentation (2.3.x). [online] flask.palletsprojects.com. Available at: https://flask.palletsprojects.com/en/2.3.x/patterns/javascript/ [Accessed 1 May 2024].

Grinberg, M. (2017a). The Flask Mega-Tutorial Part I: Hello, World! - miguelgrinberg.com. [online] Miguelgrinberg.com. Available at: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world [Accessed 2 May 2024].

Grinberg, M. (2021). Beautiful Interactive Tables for your Flask Templates. [online] blog.miguelgrinberg.com. Available at: https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates [Accessed 9 May 2024].

Keenan, J. (2019). Flask import issues (Example) | Treehouse Community. [online] Treehouse. Available at: https://teamtreehouse.com/community/flask-import-issues [Accessed 9 May 2024].

lukedelray (2022). Passing a JSON object from Flask to static folde file JavaScript. [online] www.reddit.com. Available at: https://www.reddit.com/r/flask/comments/tek82c/passing_a_json_object_from_flask_to_static_folde/?rdt=45690 [Accessed 9 May 2024].

python-web.teclado.com (n.d.). Jinja2: Conditional Statements | Web Developer Bootcamp with Flask and Python. [online] python-web.teclado.com. Available at: https://python-web.teclado.com/section07/lectures/06_jinja2_conditional_statements/ [Accessed 8 May 2024].

Stack Overflow (2012a). Can Flask have optional URL parameters? [online] Stack Overflow. Available at: https://stackoverflow.com/questions/14032066/can-flask-have-optional-url-parameters [Accessed 12 May 2024].

Stack Overflow (2012b). Sending data from HTML form to a Python script in Flask. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask [Accessed 9 May 2024].

Stack Overflow (2014). python flask ImmutableMultiDict. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/23205577/python-flask-immutablemultidict [Accessed 9 May 2024].

Stack Overflow (2018a). How can I pass JSON of flask to Javascript. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/49590870/how-can-i-pass-json-of-flask-to-javascript [Accessed 12 May 2024].

Stack Overflow (2020). how to use parameters in add_url_rule flask. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/64126522/how-to-use-parameters-in-add-url-rule-flask [Accessed 10 May 2024].

w3schools (2019b). Window alert() Method. [online] W3schools.com. Available at: https://www.w3schools.com/jsref/met_win_alert.asp [Accessed 9 May 2024].

### HTML <base> Tag
w3schools (n.d.). HTML base tag. [online] www.w3schools.com. Available at: https://www.w3schools.com/tags/tag_base.asp [Accessed 8 May 2024].

Grinberg, M. (2024). microblog/app/templates/index.html at v0.23 · miguelgrinberg/microblog. [online] GitHub. Available at: https://github.com/miguelgrinberg/microblog/blob/v0.23/app/templates/index.html [Accessed 6 May 2024].

### HTML Index
Schurov, I.V. (2023). pass object to javascript via json in flask. [online] Gist. Available at: https://gist.github.com/ischurov/34fb9e3d2ccd7a177275adac98bde42b [Accessed 12 May 2024].

### Template
Django Project. (n.d.). Django. [online] Available at: https://docs.djangoproject.com/en/5.0/ref/templates/language/ [Accessed 9 May 2024].

Grinberg, M. (2017b). The Flask Mega-Tutorial Part II: Templates - miguelgrinberg.com. [online] Miguelgrinberg.com. Available at: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates [Accessed 9 May 2024].

### Bootstrap
Cloudinary (2023). How to Easily Resize an Image with Bootstrap. [online] Cloudinary. Available at: https://cloudinary.com/guides/responsive-images/how-to-easily-resize-an-image-with-bootstrap [Accessed 12 May 2024].

freecodecamp (2018). Bootstrap/CSS How to shrink image on webpage. [online] The freeCodeCamp Forum. Available at: https://forum.freecodecamp.org/t/bootstrap-css-how-to-shrink-image-on-webpage/180705 [Accessed 12 May 2024].

Mark Otto, Jacob Thornton, and Bootstrap contributors (n.d.). Typography. [online] getbootstrap.com. Available at: https://getbootstrap.com/docs/5.3/content/typography/#headings [Accessed 6 May 2024].

Mark Otto, Jacob Thornton, and Bootstrap contributors (n.d.). Sizing. [online] getbootstrap.com. Available at: https://getbootstrap.com/docs/4.0/utilities/sizing/ [Accessed 12 May 2024].

Mark Otto, Jacob Thornton, and Bootstrap contributors (n.d.). Images. [online] getbootstrap.com. Available at: https://getbootstrap.com/docs/4.0/content/images/ [Accessed 12 May 2024].

Otto, M. (2019). Tables. [online] Getbootstrap.com. Available at: https://getbootstrap.com/docs/4.0/content/tables/ [Accessed 8 May 2024].

### Buttons
Mark Otto, Jacob Thornton, and Bootstrap contributors (n.d.). Buttons. [online] getbootstrap.com. Available at: https://getbootstrap.com/docs/5.3/components/buttons/#button-tags [Accessed 9 May 2024].

### Plotly
plotly (2024). Function. [online] plotly.com. Available at: https://plotly.com/javascript/plotlyjs-function-reference/ [Accessed 10 May 2024].

w3schools (n.d.). W3Schools online HTML editor. [online] Available at: https://www.w3schools.com/graphics/tryit.asp?filename=tryplotly_bars [Accessed 9 May 2024].

### MySQL
GCORE (n.d.). A step-by-step guide on how to delete all rows in MySQL. [online] Gcore. Available at: https://gcore.com/learning/how-to-delete-all-rows-mysql/ [Accessed 10 May 2024].

PythonAnywere (2015b). Using MySQL. [online] PythonAnywhere help. Available at: https://help.pythonanywhere.com/pages/UsingMySQL/ [Accessed 9 May 2024].

Stack Overflow (2019a). How to insert a Pandas Dataframe into MySql using PyMySQL. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/58232218/how-to-insert-a-pandas-dataframe-into-mysql-using-pymysql [Accessed 9 May 2024].

Stack Overflow (2024). TRUNCATE table only if it exists (to avoid errors). [online] Stack Overflow. Available at: https://stackoverflow.com/questions/25394493/truncate-table-only-if-it-exists-to-avoid-errors [Accessed 10 May 2024].

### SQLAlchemy
SQLAlchemy (2024). Engine Configuration — SQLAlchemy 2.0 Documentation. [online] docs.sqlalchemy.org. Available at: https://docs.sqlalchemy.org/en/20/core/engines.html [Accessed 10 May 2024].

### Flask API
tedboy.github.io (n.d.). flask.Flask.add_url_rule — Flask API. [online] tedboy.github.io. Available at: https://tedboy.github.io/flask/generated/generated/flask.Flask.add_url_rule.html [Accessed 10 May 2024].

w3schools (n.d.). JavaScript Fetch API. [online] www.w3schools.com. Available at: https://www.w3schools.com/jsref/api_fetch.asp [Accessed 2 May 2024].

### Pythonanywhere
PythonAnywere (2015). The PythonAnywhere help pages. [online] PythonAnywhere help. Available at: https://help.pythonanywhere.com/pages/ [Accessed 8 May 2024].

PythonAnywere (2017). Debugging issues with static files. [online] PythonAnywhere help. Available at: https://help.pythonanywhere.com/pages/DebuggingStaticFiles/ [Accessed 12 May 2024].

PythonAnywhere (n.d.). Host, run, and code Python in the cloud: PythonAnywhere. [online] Available at: https://www.pythonanywhere.com/ [Accessed 29 Apr. 2024].

PythonAnywhere developers (2015). A beginner’s guide to building a simple database-backed Flask website on PythonAnywhere - PythonAnywhere News. [online] Pythonanywhere.com. Available at: https://blog.pythonanywhere.com/121/ [Accessed 6 May 2024].

Stack Overflow (2019). pythonanywhere: - img src not showing picture. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/57479405/pythonanywhere-img-src-not-showing-picture [Accessed 12 May 2024].

### Image
LN_Photoart (n.d.). airplane-flight-city-landing-river-3702676/. Available at: https://pixabay.com/photos/airplane-flight-city-landing-river-3702676/ [Accessed 12 May 2024].

w3schools (2019). HTML img tag. [online] W3schools.com. Available at: https://www.w3schools.com/tags/tag_img.asp [Accessed 12 May 2024].


## Repository contents:

* .gitignore

* License

* Project Description.pdf

* README.md

* requirements.txt

* app.py

* routes.py

* wsgi_for_pythonanywhere.py

* base.html

* dashboard.html

* index.html

## Technologies Used

Python 3.11.5

## Installation Instructions

* pip install pandas

* pip install pymysql

* pip install Flask

* pip install sqlalchemy

* pip install eurostat

* pip install plotly

* pip install plotly-express

## Running The Code

* Install [Anaconda](https://www.anaconda.com/download)

* Install [Visual Studio Code](https://code.visualstudio.com/) 

* Clone Repository

* Open Repository in Visual Studio Code

## Usage Instructions

* .ipynb extension file

* markdown for narrative text

* plain text for code

## Support Information

G00426044@atu.ie

## License Information

GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007


