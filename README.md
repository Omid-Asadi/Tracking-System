
<br>

<img src= https://www.betterwholesaling.com/wp-content/uploads/2019/03/JTI-Track-Trace-logo-col.jpg style="border-radius:25px; background-color: white;" height="40%" width="70%">

# Tracking Project:
Tracking project is created for tracing customers order status plus being aware of the destination weather temperature.
This project has been powered by using python 3.11, Django 4.2, OpenAPI swaggers and dockerfile.

<br>

### To start it's better to follow the instructions:


#### Run the dockerfile easily or 
#### 1. clone the project to a specific directory.
`git clone https://github.com/Omid-Asadi/Tracking-System.git .`

<br>

#### 2. run a virtual environment with using below command:

   * ``virtualenv -p python3.11 venv/``

   * ``source venv/bin/activate/``

   * ``pip install -r requirements.txt``

<br>


#### 3. For simplicity, local_settings.py removed from gitignore, so you don't need to create it.

<br>


#### 4. Start your project with below command:
   * ``python manage.py runserver 0.0.0.0:8000``
   
<br>


#### 5. For simplicity, there has been a postman api.json with response examples beside the project which could be imported in postman for further develop.

<br>

#### 6. This project needs to use a redis server. So it's better to be sure that it is up and running.

<br>


#### 7. To fill country and city tables try to run below command: ( It's not necessary and it takes long to fetch them all.)
 ` ./manage.py cities_light --progress `
 
