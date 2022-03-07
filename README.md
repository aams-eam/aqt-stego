# steganographyLab

## Install python
In this it is being used python3, to install it, you can execute:
```
sudo apt-get install python3
```
You can see if python3 is installed with:
```
python3 --version
```
<br />

## Install python dependencies
```
pip install -r requirements.txt
```
<br />

## Run Django
Go to the directory [**stego/**](https://github.com/alexauf/steganographyLab/tree/main/stego)
Then run the following commands:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Nice!! Now the server is running, you can stop it with `ctrl+c` and can create an user by doing:
```
python manage.py createsuperuser
```
I suggest you to use simple user and pass.
Maybe a super user is already created: **admin/admin**
To see if it is created you can go to:
```
https://localhost:8000/admin
```
Then introduce the user and password mentioned before.
But this is not necessary for testing the application.

The main page can be seen in:
```
https://localhost:8000/
```
<br />

## TRANSMITTER
To execute the transmitter you must execute file (client1.py)[https://github.com/alexauf/steganographyLab/blob/main/stego/mainPage/pythonScripts/client1.py] with:
```
python client1.py
```
The message and passwords can be configured with the configuration variables:
https://github.com/alexauf/steganographyLab/blob/e867eb8cc2071d0cf4f9b6a7902051cd95150457/stego/mainPage/pythonScripts/client1.py#L5
<br />

## RECEIVER
To execute the receiver you must execute file (client1.py)[https://github.com/alexauf/steganographyLab/blob/main/stego/mainPage/pythonScripts/client2.py] with: 
```
python client2.py
```
The passwords can be configured with the configuration variables:
https://github.com/alexauf/steganographyLab/blob/e867eb8cc2071d0cf4f9b6a7902051cd95150457/stego/mainPage/pythonScripts/client2.py#L48
<br />

## STATISTICS
A script for creating graphics and calculating statistics has also been created in (statistics.py)[https://github.com/alexauf/steganographyLab/blob/main/stego/mainPage/pythonScripts/statistics.py], it can be executed with:
```
python statistics.py
```
<br />
