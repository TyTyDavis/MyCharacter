# myCharacter
A web app allowing Dungeons and Dragons players to enter character stats and generate a canonical link to an auto-generated character sheet and text of important stats
## Planned features
* User accounts that allow for multiple characters to be created and updated
* Groups, allowing players and gamemasters to see a table of all characters in their campaign, and all relevant stats.
* Runtime generation of character sheet image files.
### Potential extra features
* Character page customization, including images and backstory text blocks that don't appear on a character sheet.
## Frameworks, libraries and tools
* Django
* Bootstrap
* Pillow (Python Imaging Library fork)
* Code from [DnDSheetBot](https://github.com/TyTyDavis/CharacterSheetBot)
* [Dot Grid pattern](https://www.toptal.com/designers/subtlepatterns/dot-grid-pattern/)
### For production
* Gunicorn
* Whitenoise
* Heroku
