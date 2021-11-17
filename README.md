# myCharacter
A web app allowing Dungeons and Dragons players to enter character stats and generate a canonical link to an auto-generated character sheet and text of important stats
## Planned features
* User accounts that allow for multiple characters to be created and updated
* Groups, allowing players and gamemasters to see a table of all characters in their campaign, and all relevant stats.
* Runtime generation of character sheet image files.
* Character page customization, including images and backstory text blocks that don't appear on a character sheet.
## Frameworks, libraries and tools
* Django
* Bootstrap
* Pillow (Python Imaging Library fork)
* Code from [DnDSheetBot](https://github.com/TyTyDavis/CharacterSheetBot)

## To do
* Allow for guests to make characters (hiring managers don't want to spend time making accounts)
* Add character model fields for ability bonuses, clean up skill system
* Figure out why alignment isnt printing to sheet
* make sure people don't have permissions to edit other people's stuff
