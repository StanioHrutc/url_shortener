# URL Shortener

Simple service-clone for shortening your url and tracking clicks statistics.

## Installation
Basically, there are 2 ways to start the app. Manual and automative.
Let's start with automated:

```bash
make
# or make rise_and_shine
```
Executes and setup the whole flow with the config creation
and dockerizing the application.

Next one is manual and consists of different manual steps:
```bash
pip install -r requirements.txt # installing packages

sed -f conf_subst.sed docker-compose.yaml.in > docker-compose.yaml # building the docker-compose

docker-compose up --build
# flask service could be removed on this step

# then we should set ENV variables for Flask application:
# check conf_subst.sed file to know which variables to set.

flask run
```
