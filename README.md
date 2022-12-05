
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


<!-- insert pictures of user stories here >

<!-- insert pictures of website structure here >

<-- picture of site flow chart  -->

the header, footer and navigation bar are the same on every page as they are in the base.html that everythihng else is extended from.

Forms must be very simple and clearly describe what the user must do.

Some information on the site is accessible without log in and some content is only visable if a user is authenticated.

<!-- insert database flowchart  -->

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

WireFrames

Home
(vscode-remote://darraghmurphy-gametonight-hf7hkmk2jk0.ws-eu77.gitpod.io/workspace/gametonight/readmemedia/homewireframe.png)
Post Detail
(vscode-remote://darraghmurphy-gametonight-hf7hkmk2jk0.ws-eu77.gitpod.io/workspace/gametonight/readmemedia/postdetailwire.png)
Make a Post
(vscode-remote://darraghmurphy-gametonight-hf7hkmk2jk0.ws-eu77.gitpod.io/workspace/gametonight/readmemedia/post1.png)
(vscode-remote://darraghmurphy-gametonight-hf7hkmk2jk0.ws-eu77.gitpod.io/workspace/gametonight/readmemedia/post2.png)
Sign In/Out
(vscode-remote://darraghmurphy-gametonight-hf7hkmk2jk0.ws-eu77.gitpod.io/workspace/gametonight/readmemedia/loginwire.png)
(vscode-remote://darraghmurphy-gametonight-hf7hkmk2jk0.ws-eu77.gitpod.io/workspace/gametonight/readmemedia/signoutwire.png)
Registration
(vscode-remote://darraghmurphy-gametonight-hf7hkmk2jk0.ws-eu77.gitpod.io/workspace/gametonight/readmemedia/registrationwire.png)

Colour Scheme 

The colours used in this site are mostly green to suit the subject content of football. It is mostly green and white with a variation of black and white text. The primary buttons are blue to set them apart from the green background. 

Features 

Navbar - The navbar appears on every page and was created with the help of Bootstrap. It displays links to the homepage as well as log in/log out and registration.

List of Posts - This is the homepage which will display all the posts that have been made on the site. It involves the title, the poster and small excerpt of the post.

Post Form - This is the form that allows a user to make a post. It is a very simple form with instructions displayed through html text and simply asks for a post title and post content. 

Comment Form  - This is a simple form that allows users to comment on posts to allow users to communicate with each other. It only has one text box as there is no need for any more information to be displayed.

Footer - This simple footer just improves the aesthetics of the page. The footer makes it clear that this is the end of the page and just simply states the name of the site with a solid white bar across the bottom of the screen.

Pagination - This features allows the homepage to hold a maximum of 9 posts before the user will need to press the "next" button that will appear when there is more than 9 posts. This feature exists to keep the site looking tidy and prevents it from having too much information on one page.  

Detailed View - This is a link used to access the more detailed view of a particular post and enables the comment feature as well. 

Edit and Delete - If the original poster clicks into a more detailed view of their own post they will have the edit and delete buttons available to them. This allows a user to update their own post or even delete it. 

Search - This funtion allows a user to search for a post.

<!-- insert screenshots of every page and split features into their own pages -->


Tests

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
