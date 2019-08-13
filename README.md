# Stranger Blogs

### 09th Aug 2019

## By **[Daniel Njuguna](https://github.com/dan-jugz)**

## Description

This is a flask web app that allows users to post blogs,users can comment on them and the owner of the post can delete user comments,update blogs and or delete blogs.Users can also enjoy random funny quotes as they read the blogs

## BEHAVIOUR DRIVEN DEVELOPMENT
Behaviour                       |Input                                     | Output                                     |
--------------------------------|------------------------------------------|--------------------------------------------|
Ability to login to your account| Login button clicked                     | Redirects the user to the login page                            |
Ability to register writer      | Sign up button                           | Redirects the user to the sign up page                         |
Add blog                        | Post a blog button clicked in dashboard | Redirects the user to a page with a form                     |
Show profile                    | Profile button clicked      | Redirects the user to his/her profile page |
Comment on a blog               | Click on a blog you would like to comment | Redirects you to a commaent page 
Delete a blog                   | Click on the blog on your dashboard         | Redirects you to an edit page. Click delete blog  
Delete a comment                | Click on the blog on your dashboard         | Redirects you cack to your dashboard once deleting is completed

## Technologies used
* [Flask](http://flask.pocoo.org/) - For both backend and fronted
* Bootstrap
* Postgres Database

## Setup/Application Requirements
1. Ensure you have [Python3.6](www://https://python.org) installed in your computer. You can run:
`sudo apt-get update && sudo apt-get install python3.6` to download.
2. Ensure you have [PiP](https://pypi.org/) in your computer. Run `python get-pip.py` to install.
3. Ensure you have [Pip Flask]() installed in your computer. Run `pip install flask-script` to install.


## Project Setup
In a Linux terminal,
1. Run `cd Desktop` - To navigate to Desktop directory.
2. Run `mkdir stranger-blogs-clone` - To make an empty directory.(This is where we will store stranger-blogs clone project)
3. Run `git clone https://github.com/dan-jugz/stranger-blogs.git`
4. Run `chmod a+x start.sh` - To make start.sh file executable.
5. Run `./start.sh` to open the app.

### Known bugs
* photo uploads are misbehaving

## FEEDBACK
Your opinion matters. 
Have some ideas how to improve my product?

## Contact Information
Email - (https://njugunadaniel364@gmail.com)

Github username - dan-jugz

### License

MIT (c) 2019 **[Daniel Njuguna](https://github.com/dan-jugz/stranger-blogs)**