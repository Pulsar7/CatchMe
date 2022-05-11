<p align="center">
    <img src="https://github.com/Pulsar7/Catch-Me/blob/main/images/rounded_logo.png" width=400px; style="display: block; margin: 0 auto;border-radius:10px;">
</p>

[![Author](https://img.shields.io/badge/author-Pulsar7-lightgrey.svg?colorB=9900cc&style=flat-square)](https://github.com/Pulsar7)
[![Release](https://img.shields.io/github/release/dmhendricks/file-icon-vectors.svg?style=flat-square)](https://github.com/Pulsar7/CatchMe/releases)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/dmhendricks/file-icon-vectors.svg?style=social)](https://twitter.com/SevenPulsar)

# CatchMe

:large_orange_diamond: Catch your friends with your phone. <br/><br/>
:warning: In order to be able to use the APP, a separate server would have to be set up, as there is currently no publicly accessible server.
Sensitive location data is collected and shared with the server. However, since the server does not yet have any encryption standards for securing the data in the database, use the APP at your own risk. In the development of this project, general use was the most important.

## :heavy_exclamation_mark:<code>Is still in progress</code>

<p align="center">
    <img src="https://github.com/Pulsar7/Catch-Me/blob/main/images/Basic-Structure.png" width=900px; 
         style="display: block; margin: 0 auto;border-radius:10px;">
</p>
:arrow_right: This is a mind map of what the rough structure of the server and client could look like. A VServer is used as a publicly accessible API.

## :pushpin: Table of contents

* :point_right: [Client Explanation](#client-explanation)
* :point_right: [Server Explanation](#server-explanation)
* :point_right: [Server Deployment](#server-deployment)
* :point_right: [Client Deployment](#client-deployment)
* :point_right: [ToDo](#todo)
* :point_right: [Suggestions & Reports](#suggestions--reports)

## Client Explanation
    
- Android-APP (Client): Using Python-Module: [**Kivy**](https://kivy.org/#home), [**KivyMD**](https://kivymd.readthedocs.io/en/latest/)

    - Converting to <code>.apk</code> by using [**Buildozer**](https://buildozer.readthedocs.io/en/latest/)

When starting the APP, the connection to the server is tested immediately and as soon as this fails, an error dialog is displayed. </br>
:unlock: Required [permissions](https://developer.android.com/reference/android/Manifest.permission):

 	ACCESS_FINE_LOCATION, ACCESS_BACKGROUND_LOCATION, ACCESS_NETWORK_STATE, INTERNET, MANAGE_EXTERNAL_STORAGE, MANAGE_MEDIA

<p align="center">
    <img src="https://github.com/Pulsar7/Catch-Me/blob/main/images/Client-Aufbau_Elemente.png" width=900px; 
         style="display: block; margin: 0 auto;border-radius:10px;">
</p>

## Server Explanation

The server is summarized a [**Flask**](https://flask.palletsprojects.com/en/2.1.x/) API, which is communicating with the client. The location data sent by the client is cached for a short time in order to calculate the distance with the other players. Each game is also written to the MongoDB with the players and remains stored until the respective game ends.
The configuration data is stored in the <code>conf.json</code>-file and can be modified at will. But you should be aware that careless changes can affect the functioning of the server.

## Server Deployment
When you decided to self host a CatchMe-Service, please follow these points:

:small_orange_diamond: **Download MongoDB**

- You can install it at the official website of [**MongoDB**](https://www.mongodb.com/)
- or install [**PyMongo**](https://pymongo.readthedocs.io/en/stable/) via pip:
    
      pip3 install pymongo
      
- or install MongoDB via the [**APT-Manager**](https://wiki.ubuntuusers.de/APT/) (for linux)
      
      sudo apt-get install mongodb
     
:small_orange_diamond: **Download the repository from github with git and go to directory**
 
    sudo apt-get install git
    git clone https://github.com/Pulsar7/CatchMe.git
    cd CatchMe/backend/Rest-API-Server/

:small_orange_diamond: **Install requirements**

    pip install -r requirements.txt
    
:arrow_forward: Before the server is started, it should be checked whether the connection address of the mongo database in the config file is correct.
    
:small_orange_diamond: **Start MongoDB and run server**

    sudo service mongodb start
    python3 rest_api_server.py
    
The Server should now be reachable on http://localhost:5000. But you can change some configurations in <code>/server/conf/config.json</code>.

## Client Deployment

:small_blue_diamond: **Download the repository from github with git and go to directory**

    sudo apt-get install git
    git clone https://github.com/Pulsar7/CatchMe.git
    cd CatchMe/frontend/Android-APP/

:small_blue_diamond: **Install requirements**

    pip install -r requirements.txt

:small_blue_diamond: **Insert the correct API-URL from Server in the <code>config.json</code>-File**

Example (A snippet from the file): 
    
    "Server": {
        "url": "http://localhost:5000"
    },

:small_blue_diamond: **Run Client**

    python3 catchme.py

:small_blue_diamond: **Create a package for Android (APK)**

    git clone https://github.com/kivy/buildozer.git
    cd buildozer
    sudo python3 setup.py install
    buildozer init
    buildozer android debug deploy run

## ToDo

- [ ] SHA-256 encryption - all data in database (Server)
- [ ] Improve layout from client
- [ ] Auto reconnecting when losing internet connection (Client)
- [ ] Add docker deployment (Server)

## Suggestions & Reports

Suggestions or errors are welcome to be [:link: reported](https://github.com/Pulsar7/Catch-Me/issues)!
