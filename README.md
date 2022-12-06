
"Game Tonight?" is a website created to find a football game to play in or find players to play in a game of your own. Organisers of local games are constantly looking for players to fill in for absentees or some people dont't know enough people to get a game organised themselves. This site aims to provide an oppurtunity for all people to access a game of football. 

A user will be able to make a post advertising a football game and other users will be able to comment on the post to confirm their availability.


## User Experience (UX)

### Strategy

#### Project Goals

* The site is designed very simply with a very basic colour scheme and layout so as to not take away the attention of the user and keep it on the important part of the site, the posts.

* The site must be responsive so as to be able to use it on multiple devices.

* The navigation and structure of the site must be easy to understand and easily navigated.

* Users of the site must be able to create an account so that they can comment and post.

* Site users should be able to search for a post so as to find one local to them.


#### User Goals


As a Site User I can see the amount of comments on a post so that I cam see how many responses the post has.

As a Site user I can create, read, update and delete posts so that I can advertise my post or change it as and when needed.

As a Site User I can leave comments on a post so that I can declare availabilty.

As a Site User I can register an account so that I can comment and like

Site User / Admin I can view comments on an individual post so that I can read the conversation

As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral

As a Site User I can click on a post so that I can read the full text

As a Site User I can view a list of posts so that I can select one to read


### Scope

The following aspects must be present in the aplication:

* Responsive design

* Ability to create an account.

* Create, read, update and delete posts.

* Create and read comments.

* Ability to search for for posts.


![F0wbIMCUNd](https://user-images.githubusercontent.com/103134533/205859002-fad4825a-59b1-4d18-9029-94aee9f00c75.png)
![chrome_jeClRoUeAI](https://user-images.githubusercontent.com/103134533/205859036-be2d04ea-240d-4ca0-99ee-cd18b702e6e0.png)
![chrome_0jy6t2MzZ9](https://user-images.githubusercontent.com/103134533/205859063-a74e5b2e-747a-482c-976a-0d7283096a84.png)
![chrome_E7bNuVG5k5](https://user-images.githubusercontent.com/103134533/205859086-402d174d-1130-496d-8042-9bd447dd2435.png)
>

the header, footer and navigation bar are the same on every page as they are in the base.html that everythihng else is extended from.

Forms must be very simple and clearly describe what the user must do.

Some information on the site is accessible without log in and some content is only visable if a user is authenticated.

![chrome_8bkiGGLo23](https://user-images.githubusercontent.com/103134533/205864673-9a843653-bb04-4e26-9eac-6cba69710949.png)

Post Model 

Title - The title of the post. A charachter field limited to 100 characters
Slug - A slug field created by the title of the post 
Author - A User foreign key to store the author of the post
Excerpt - A text field 
Last updated - The time and date the post was last edited
Content - The content of the post in a text field
Created date  - The time and date the post was created
Status - Whether the post is drafted or published. Auto default to published.


Comment Model 

Post - a foeign key to store post details
Name  - The name of the commenter
Email - The email or the commenter 
Created on - The time and date the comment was created
Approved - Automatically approves comments for posting

## WireFrames

Home
![BalsamiqWireframes_7x3m0Xns9C](https://user-images.githubusercontent.com/103134533/205857738-cf817c68-a1c4-48e9-b599-d62cd4c147c2.png)


Post Detail
![BalsamiqWireframes_QOLU5h3tcQ](https://user-images.githubusercontent.com/103134533/205857767-8cb58237-9160-46ac-9b92-23a48f2762c0.png)


Make a Post
![BalsamiqWireframes_162waNIwxM](https://user-images.githubusercontent.com/103134533/205857786-18acd6e2-478e-4a3a-a346-4908a877d7c0.png)
![BalsamiqWireframes_O4U91J9DG2](https://user-images.githubusercontent.com/103134533/205857803-77005942-a21c-4723-8334-463630426f9a.png)


Sign In/Out
![BalsamiqWireframes_PCmtAuTjjQ](https://user-images.githubusercontent.com/103134533/205857825-cc82de93-a5e7-4f05-a1b4-41baa3b3a517.png)
![BalsamiqWireframes_61UIP3e1mZ](https://user-images.githubusercontent.com/103134533/205857853-776b739e-a4d9-4b7d-a14f-3da79fe780b7.png)


Registration
![BalsamiqWireframes_pNttOUqNY9](https://user-images.githubusercontent.com/103134533/205857878-c56019f6-2a63-4401-a6ca-e879cd46bca8.png)


## Colour Scheme 

The colours used in this site are mostly green to suit the subject content of football. It is mostly green and white with a variation of black and white text. The primary buttons are blue to set them apart from the green background. 

## Features 

Navbar - The navbar appears on every page and was created with the help of Bootstrap. It displays links to the homepage as well as log in/log out and registration.
![chrome_1ZtTW6LHrF](https://user-images.githubusercontent.com/103134533/205867239-8177a731-b53f-436c-94c2-2c63c86e999e.png)

List of Posts - This is the homepage which will display all the posts that have been made on the site. It involves the title, the poster and small excerpt of the post.
![chrome_8uzWMz8CEJ](https://user-images.githubusercontent.com/103134533/205867166-4bd7d52a-3822-488e-9b06-5cde5eb41b31.png)

Post Form - This is the form that allows a user to make a post. It is a very simple form with instructions displayed through html text and simply asks for a post title and post content. 
![chrome_KkubMK1vvA](https://user-images.githubusercontent.com/103134533/205867359-bbb752c0-e252-4139-9580-ba2d02c12594.png)


Comment Form  - This is a simple form that allows users to comment on posts to allow users to communicate with each other. It only has one text box as there is no need for any more information to be displayed.
![chrome_ocCu69WZem](https://user-images.githubusercontent.com/103134533/205867419-fc3c0c78-01ac-4574-b84b-85ebc130a960.png)

Footer - This simple footer just improves the aesthetics of the page. The footer makes it clear that this is the end of the page and just simply states the name of the site with a solid white bar across the bottom of the screen.

Pagination - This features allows the homepage to hold a maximum of 9 posts before the user will need to press the "next" button that will appear when there is more than 9 posts. This feature exists to keep the site looking tidy and prevents it from having too much information on one page.  
![chrome_Kn5JH9V4T4](https://user-images.githubusercontent.com/103134533/205867606-a468cbf4-8cb0-46f1-8e30-56a7e2658cc0.png)

Detailed View -![chrome_1qWZvEIBPI](https://user-images.githubusercontent.com/103134533/205867564-44b7884b-1a80-4adf-b6e1-c4ab2961f1cd.png)
 This is a link used to access the more detailed view of a particular post and enables the comment feature as well. 

Edit and Delete - If the original poster clicks into a more detailed view of their own post they will have the edit and delete buttons available to them. This allows a user to update their own post or even delete it. 
![7bEPCgkTuO](https://user-images.githubusercontent.com/103134533/205867687-ac815bac-88a8-4f09-bc7b-e7277271fa8a.png)
![chrome_XIQckK33zX](https://user-images.githubusercontent.com/103134533/205867708-8088a8ec-e8aa-4807-a11a-292925b4bc92.png)

Search - This funtion allows a user to search for a post.




## Tests

Testing User Stories

As a Site User I can see the amount of comments on a post so that I cam see how many responses the post has.
-Clearly displays the amount of comments on the post beside a comment icon

As a Site user I can create, read, update and delete posts so that I can advertise my post or change it as and when needed.
-By using the post form I can post to the site and then edit it with the edit form and delete it by pressing two buttons.

As a Site User I can leave comments on a post so that I can declare availabilty.
-Comments are successfully left through the comment form on a post.

As a Site User I can register an account so that I can comment and like
-By using the registration page I can create an account. 

Site User / Admin I can view comments on an individual post so that I can read the conversation
-Comments are easily visable on the post detail page.

As a Site User I can click on a post so that I can read the full text
-By clicking on the post you will see it in more detail.

As a Site User I can view a list of posts so that I can select one to read
-The user is greeted with a full list of posts.

Multiple Browsers and Screens 

| Test | Outcome | Pass/Fail |
| ----------- | ----------- | ---------- |
| Does the site work on different browsers? | The site has been viewed on Google Chrome, Firefox, Microsoft Edge and Safari | Pass |
| Is the site responsive to different screen sizes? | The site is fully respnsonsive | Pass |


Homepage

| Test | Outcome | Pass/Fail |
| ----------- | ----------- | ---------- |
| Navbar | All navigation links are working | Pass |
| Posts are visable | When page is loaded posts show on page | Pass |
| Footer | Footer is present | Pass |

Post Detail 

| Test | Outcome | Pass/Fail |
| ----------- | ----------- | ---------- |
| Navbar | All navigation links are working | Pass |
| Post visable | Post loads up on its own page | Pass |
| Created on/ Updated on | The post has a time and date for posting or most recent edit | Pass |
| Comments | Comments are visable | Pass |
| Comment author | the username of the author is visable | Pass | 
| Comment form | Comment form is visable and working | Pass |
| Comment post | When comment is submitted it is added to the comment list in chronological order | Pass |
| Authorisation | Comment box only available to those who have made an account | Pass |
| Delete Post | If the original poster clicks onto their post the delete button is present | Pass |
| Edit Post | If the original poster clicks onto their post the edit button is present | Pass |
| Footer | Footer is present | Pass |

Sign In 

| Test | Outcome | Pass/Fail |
| ----------- | ----------- | ---------- |
| Navbar | All navigation links are working | Pass |
| Username | The textbox for the user's unique username is available | Pass | 
| Password | The password textbox is available and characters are hidden when typed | Pass | 
| Button | When button is pressed the user is logged in | Pass |
| Footer | Footer is present | Pass |

Sign Out 

| Test | Outcome | Pass/Fail |
| ----------- | ----------- | ---------- |
| Navbar | All navigation links are working | Pass |
| Button | When button is pressed the user is logged out | Pass |
| Footer | Footer is present | Pass |

Registration

| Test | Outcome | Pass/Fail |
| ----------- | ----------- | ---------- |
| Navbar | All navigation links are working | Pass |
| Username | The textbox for the user's unique username is available | Pass | 
| Password | The password textbox is available and characters are hidden when typed | Pass | 
| Button | When button is pressed the user is logged in | Pass |
| Footer | Footer is present | Pass |

User Post  

| Test | Outcome | Pass/Fail |
| ----------- | ----------- | ---------- |
| Navbar | All navigation links are working | Pass |
| Textbox | 2 textboxes are present for title and content. Both work. | Pass |
| Submit Button | When button is pressed the post is published | Pass |
| Cancel button | When post is cancelled the page redirects | Pass
| Footer | Footer is present | Pass |

Edit Post

| Test | Outcome | Pass/Fail |
| ----------- | ----------- | ---------- |
| Navbar | All navigation links are working | Pass |
| Textbox | 2 textboxes are present for title and content. Both work. | Pass |
| Submit Button | When button is pressed the post is updated | Pass |
| Cancel button | When post is cancelled the page redirects | Pass |
| Footer | Footer is present | Pass |

Delete Post 

| Test | Outcome | Pass/Fail |
| ----------- | ----------- | ---------- |
| Navbar | All navigation links are working | Pass |
| Textbox | 2 textboxes are present for title and content. Both work. | Pass |
| Yes Button | When button is pressed the post is deleted | Pass |
| No button | When clicked the deletion is abandoned | Pass |
| Footer | Footer is present | Pass |
## Technologies Used

### Languages Used

* HTML
* CSS
* JavaScript
* Python


### Libraries and Frameworks

* Django framework

* Django Template 
   
* bootstrap 5 

* Font Awesome

### Packages / Dependecies Installed

* Django AllAuth used for authentication

* Django crispy forms. 
 
* Gunicorn 

* Summernote

* Cloudinary

### Database Management
* Heroku Postgres


### Tools and Programs

* GitPod

* GitHub

* Heroku

* amiresponsive

* Balsamiq wireframes

* Google Chrome

* W3C HTML and CSS validator

* PEP8 Code Validator

* JShint


## Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

Create the Heroku App:

Select "Create new app" in Heroku.
Choose a name for your app and select the location.
Attach the Postgres database:

In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
Prepare the environment and settings.py file:

In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
In your GitPod workspace, create an env.py file in the main directory.
Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
Add the SECRET_KEY value to the Config Vars in Heroku.
Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
In settings.py add the following sections:
Cloudinary to the INSTALLED_APPS list
STATICFILE_STORAGE
STATICFILES_DIRS
STATIC_ROOT
MEDIA_URL
DEFAULT_FILE_STORAGE
TEMPLATES_DIR
Update DIRS in TEMPLATES with TEMPLATES_DIR
Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']
Store Static and Media files in Cloudinary and Deploy to Heroku:

Create three directories in the main directory; media, storage and templates.
Create a file named "Procfile" in the main directory and add the following:
web: gunicorn viewpoint.wsgi
Go to Deploy tab on Heroku and connect to the GitHub, then to the required recpository. Click on Delpoy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.

## Remaining features to implements 
Search 

Like button 

Delete and edit comments 

Geographical categories 

## Acknowledgments 

Stack Overflow

Code taken from I think therefore I blog from CodeInstitute 

Code taken from https://github.com/josswe26/code-buddy

My mentor Marcel Mulders




