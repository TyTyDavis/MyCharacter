# myCharacter
[Check it out!](http://www.mycharacters.co/)
A web app allowing Dungeons and Dragons players to enter character stats and generate a canonical link to an auto-generated character sheet and text of important stats
* [Sample character](http://www.mycharacters.co/5/)
* [Sample campaign](http://www.mycharacters.co/campaign/1/)
## Features
* User accounts that allow for multiple characters to be created and updated
* Groups, allowing players and gamemasters to see a table of all characters in their campaign, and all relevant stats.
* Runtime generation of character sheet image files.
### To do
* Guided character creation form
* Profile pictures and other fields for personalizing characters
* Adding characters to campaign from character profile page
## Technologies
* Python 3.9.9
* Django 3.2.8
* Bootstrap 5.1.3
* Pillow (Python Imaging Library fork)
* Code from my [DnDSheetBot](https://github.com/TyTyDavis/CharacterSheetBot)
* [Dot Grid pattern](https://www.toptal.com/designers/subtlepatterns/dot-grid-pattern/)
### For production
* Gunicorn for WSGI
* Whitenoise for static file serving
* Heroku
