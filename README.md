<p align="center">
    <img src="https://github.com/Pulsar7/Catch-Me/blob/main/images/icon.png" style="display: block; margin: 0 auto;">
</p>

[![Author](https://img.shields.io/badge/author-Pulsar7-lightgrey.svg?colorB=9900cc&style=flat-square)](https://github.com/Pulsar7)
[![Release](https://img.shields.io/github/release/dmhendricks/file-icon-vectors.svg?style=flat-square)](https://github.com/Pulsar7/CatchMe/releases)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/dmhendricks/file-icon-vectors.svg?style=social)](https://twitter.com/SevenPulsar)

# CatchMe

:small_blue_diamond: Catch your friends with your phone.

## :heavy_exclamation_mark:<code>Is still in progress</code>

## :pushpin: Table of contents

* :point_right: [Client Explanation](#client-explanation)
* :point_right: [Server Explanation](#server-explanation)
* :point_right: [Server Deployment](#server-deployment)
* :point_right: [Client Deployment](#client-deployment)
* :point_right: [Suggestions & Reports](#suggestions--reports)

## Client Explanation
    
- Android-APP (Client): Using Python-Module: [**Kivy**](https://kivy.org/#home), [**KivyMD**](https://kivymd.readthedocs.io/en/latest/)

    - Converting to <code>.apk</code> by using [**Buildozer**](https://buildozer.readthedocs.io/en/latest/)

## Server Explanation

The server is summarized a [**Flask**](https://flask.palletsprojects.com/en/2.1.x/) API, which is communicating with the client. 

## Server Deployment
When you decided to self host a CatchMe-Service, please follow these points:
    
:small_orange_diamond: **Download the repository from github with git and go to directory**
    
    sudo apt-get install git
    git clone https://github.com/Pulsar7/CatchMe.git
    cd CatchMe/

:small_orange_diamond: **Install requirements**

    pip install -r requirements.txt
    
:small_orange_diamond: **Run Server**

    python3 rest_api_server.py
    

## Client Deployment
 

## Suggestions & Reports

Suggestions or errors are welcome to be [:link: reported](https://github.com/Pulsar7/Catch-Me/issues)!
