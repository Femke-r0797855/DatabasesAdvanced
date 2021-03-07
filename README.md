# DatabasesAdvanced
After you install the ubuntu you need to put next commands in the terminal for the file to work.<br>
<br>
- `pip3 install bs4`
- `pip3 install requests`
- `chmod +x bitcoin.py`
- `pip3 install pymongo`
- `pip3 install redis`

We need to install MongoBD and get the results we put our output into a DB.
You download the file or make it yourself.

When you want to make it yourself you first need to make a file 
Then you put all the code into this file:
- `sudo apt-get install gnupg`
- `wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -`
- `echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list`
- `sudo apt-get update`
- `sudo apt-get install -y mongodb-org`

Now we also need a visual representation of our database.
So we install Compass.

Downloadd mongoDB Compass:<br>
`wget https://downloads.mongodb.com/compass/mongodb-compass_1.25.0_amd64.deb` <br>
Install MongoDB Compass:<br>
`sudo dpkg -i mongodb-compass_1.25.0_amd64.deb`<br>
Start MongoDB Compass:<br>
`mongodb-compass`<br>

Download Redis <br>

For Redis there is a bash file included in this repos 
To test if it is installed, Type the following commands:
- `redis-cli`
- `ping`
If you don't get any errors, then Redis is ready. 
If you get an error, try one of these commands:
- `sudo apt install redis-server`
- `sudo apt install redis-tools`
<br>
When you want to run the code, type this into your terminal: `python3 bitcoin.py`
To test and start this code you need to type into the terminal following command: `python3 bitcoin.py`

![MongoDBWerkt](https://user-images.githubusercontent.com/79083840/109400704-6ee56400-794a-11eb-97c4-77d7b02acdcf.PNG)

