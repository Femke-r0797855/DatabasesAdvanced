# DatabasesAdvanced
First you need to install Ubuntu. I used this to make my dockerfile.
This is a link to my dockerfile.
Then you download the 
https://hub.docker.com/repository/docker/r0797855/bitcoinscraper

- `sudo apt-get update`
- `sudo apt-get install docker.io`
- `sudo docker pull r0797855/bitcoinscraper:latest`
- `sudo docker run -d --network="host" redis`
- `sudo docker run -d --network="host" mongo`
- `sudo docker run --network="host" r0797855/bitcoinscraper`


![MongoDBWerkt](https://user-images.githubusercontent.com/79083840/109400704-6ee56400-794a-11eb-97c4-77d7b02acdcf.PNG)
https://phoenixnap.com/kb/how-to-install-python-3-ubuntu


Wilt u naar mongo compas kijken volg de volgende stappen.
Downloadd mongoDB Compass:<br>
`wget https://downloads.mongodb.com/compass/mongodb-compass_1.25.0_amd64.deb` <br>
Install MongoDB Compass:<br>
`sudo dpkg -i mongodb-compass_1.25.0_amd64.deb`<br>
Start MongoDB Compass:<br>
`mongodb-compass`<br>

