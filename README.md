![MongoDBWerkt](https://user-images.githubusercontent.com/79083840/109400704-6ee56400-794a-11eb-97c4-77d7b02acdcf.PNG)
![MongoDBWerkt](https://user-images.githubusercontent.com/79083840/109400714-799ff900-794a-11eb-8911-112bda6df0b9.PNG)
# DatabasesAdvanced
After you install the ubuntu you need to put next commands in the terminal for the file to work.<br>
<br>
- `pip3 install bs4`
- `pip3 install requests`
- `chmod +x bitcoin.py`
- `python3 bitcoin.py`
- `pip3 install pymongo`

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

Downlaod mongoDB Compass:<br>
`wget https://downloads.mongodb.com/compass/mongodb-compass_1.25.0_amd64.deb` <br>
Install MongoDB Compass:<br>
`sudo dpkg -i mongodb-compass_1.25.0_amd64.deb`<br>
Start MongoDB Compass:<br>
`mongodb-compass`<br>

To test and start this code you need to type into the terminal following command: ` python3 bitcoin.py`
