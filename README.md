# instadash
## Author
Albunus Nyalita.
### Description
This is a Django web application replica website for the photo app Instagram.It requires users to sign in to the application to start using and upload pictures to the application.A user can follow other users and see their pictures on my timeline and also like a picture or leave a comment on it.
### Prerequisites
* Python 3.8
* Text editor 
* You need to have git installed. You can install it with the following command in your terminal
* *****
 ### Prerequisites
* Python 3
* Text editor eg Visual Studio Code
* *****
## Setup Instruction
To access this project on your local files, you can clone it using these steps
1. Open your terminal
1. Use this command to clone $ git clone 
1. This will clone the repositoty into your local folder
*****
### Admin Site
There is an admin site to manage the application entities
### User Profile and Timeline posts
After a user successfully sign up and login, they will be redirected to profile page showing user information and posts by other users

*****
### View Photo details
A user can click on any image and a page will be displayed containing the photo information like image name, caption, number of comments and likes and also date posted.  
A user can only see a delete button if they are the owner of the post so they cannot delete a post belonging to another user
*****

*****
### Search Function
A user can search other users and it will return users found or display "Found 0 results if no match found by the search function.
*****
*****
## Behaviour Driven Development
1. Provides comment form
   - INPUT: comment typed in the form input
   - INPUT: comment button clicked
   - OUTPUT: New comment added to the image
1. Provides form to post photo 
   - INPUT: Account action option 'post' clicked
   - OUTPUT: Form page displayed
   - INPUT: Form field inputs filled
   - INPUT: Post button clicked
   - OUTPUT: New post added
1. Show user profile 
   - INPUT: Account action option profile clicked
   - OUTPUT: Profile page with user information and other users posts displayed
1. Shows a like button
   - INPUT: Heart  button icon clicked
   - OUTPUT: Image liked
1. Provides a search form
   - INPUT: Search term entered in the search field
   - OUTPUT: Number of matched user results displayed in the page
1. Show photo details
   - INPUT: Image is clicked
   - OUTPUT: A new page loaded with image details
1. Provides a delete function for image
   - INPUT: Delete button clicked
   - OUTPUT: Image deleted
 ## Dependencies
* django-bootstrap
* Pillow
* cloudinary
* psycopg2
* django-registration
* python-decouple
* Python Venv
* whitenoise
* gunicorn
*****
## Technologies Used
* HTML
* Python 3
* JavaScript
* CSS
******
### License
This project is under:  
MIT LICENSE
*****
