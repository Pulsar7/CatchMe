<p align="center">
    <img src="https://github.com/Pulsar7/Catch-Me/blob/main/images/icon.png" style="display: block; margin: 0 auto;">
</p>

[![Author](https://img.shields.io/badge/author-Pulsar7-lightgrey.svg?colorB=9900cc&style=flat-square)](https://github.com/Pulsar7)
[![Release](https://img.shields.io/github/release/dmhendricks/file-icon-vectors.svg?style=flat-square)](https://github.com/Pulsar7/CatchMe/releases)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/dmhendricks/file-icon-vectors.svg?style=social)](https://twitter.com/SevenPulsar)

# CatchMe

:large_orange_diamond: Catch your friends with your phone. <br/>
:warning: In order to be able to use the APP, a separate server would have to be set up, as there is currently no publicly accessible server.

## :heavy_exclamation_mark:<code>Is still in progress</code>

## :pushpin: Table of contents

* :point_right: [Client Explanation](#client-explanation)
* :point_right: [Server Explanation](#server-explanation)
* :point_right: [Server Deployment](#server-deployment)
* :point_right: [Client Deployment](#client-deployment)
* :point_right: [To Do](#to-do)
* :point_right: [Suggestions & Reports](#suggestions--reports)

## Client Explanation
    
- Android-APP (Client): Using Python-Module: [**Kivy**](https://kivy.org/#home), [**KivyMD**](https://kivymd.readthedocs.io/en/latest/)

    - Converting to <code>.apk</code> by using [**Buildozer**](https://buildozer.readthedocs.io/en/latest/)

When starting the APP, the connection to the server is tested immediately and as soon as this fails, an error dialog is displayed.

## Server Explanation

The server is summarized a [**Flask**](https://flask.palletsprojects.com/en/2.1.x/) API, which is communicating with the client. The configuration data is stored in the <code>conf.json</code>-file and can be modified at will. But you should be aware that careless changes can affect the functioning of the server.

## Server Deployment
When you decided to self host a CatchMe-Service, please follow these points:
    
:small_orange_diamond: **Download the repository from github with git and go to directory**
    
    sudo apt-get install git
    git clone https://github.com/Pulsar7/CatchMe.git
    cd CatchMe/backend/Rest-API-Server/

:small_orange_diamond: **Install requirements**

    pip install -r requirements.txt
    
:small_orange_diamond: **Run Server**

    python3 rest_api_server.py
    
The Server should now be reachable on http://localhost:5000. But you can change some configurations in <code>/server/conf/config.json</code>.

## Client Deployment

:small_blue_diamond: **Download the repository from github with git and go to directory**

    sudo apt-get install git
    git clone https://github.com/Pulsar7/CatchMe.git
    cd CatchMe/frontend/Android-APP/

:small_blue_diamond: **Install requirements**

    pip install -r requirements.txt

## To Do

- [ ] Encrypting all data in database (Server)
- [ ] Improve layout from client
- [ ] Auto reconnecting when losing internet connection

## Suggestions & Reports

Suggestions or errors are welcome to be [:link: reported](https://github.com/Pulsar7/Catch-Me/issues)!
