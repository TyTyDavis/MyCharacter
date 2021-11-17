from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
from django.contrib.staticfiles.storage import staticfiles_storage

#either use model's skill bonuses, or remove them from form

#problem with alignment?


fontFile = staticfiles_storage.path('Verdana.ttf')

def abilityBonus(score):
	if score > 5 and score < 8:
		return -2
	elif score < 10:
		return -1
	elif score < 12:
		return 0
	elif score < 14:
		return 1
	elif score < 16:
		return 2
	elif score < 18:
		return 3
	elif score < 20:
		return 4
	elif score < 22:
		return 5

def writeAbilityBonus(score):
	if score > 5 and score < 8:
		return "-2"
	elif score < 10:
		return "-1"
	elif score < 12:
		return "+0"
	elif score < 14:
		return "+1"
	elif score < 16:
		return "+2"
	elif score < 18:
		return "+3"
	elif score < 20:
		return "+4"
	else:
		return "+5"
def writeName(image, name):
#Write character name on sheet
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,50)
	draw.text((200, 270), name,(0,0,0), font=font)

def writePlayerName(image, name):
#Write player name on sheet
	if name!=None:
		img = image
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(fontFile,40)
		draw.text((2000, 210), name,(0,0,0), font=font)

def writeAbilities(image, character):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,60)
	draw.text((200, 660), str(character.strength),(0,0,0), font=font)
	draw.text((200, 960), str(character.dexterity),(0,0,0), font=font)
	draw.text((200, 1260), str(character.constitution),(0,0,0), font=font)
	draw.text((200, 1560), str(character.intelligence),(0,0,0), font=font)
	draw.text((200, 1860), str(character.wisdom),(0,0,0), font=font)
	draw.text((200, 2160), str(character.charisma),(0,0,0), font=font)
	font = ImageFont.truetype(fontFile,30)
	draw.text((215, 785), writeAbilityBonus(character.strength),(0,0,0), font=font)
	draw.text((215, 1085), writeAbilityBonus(character.dexterity),(0,0,0), font=font)
	draw.text((215, 1380), writeAbilityBonus(character.constitution),(0,0,0), font=font)
	draw.text((215, 1680), writeAbilityBonus(character.intelligence),(0,0,0), font=font)
	draw.text((215, 1980), writeAbilityBonus(character.wisdom),(0,0,0), font=font)
	draw.text((215, 2280), writeAbilityBonus(character.charisma),(0,0,0), font=font)

def writeClass(image, characterClass, level):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,60)
	draw.text((1130, 200), characterClass + ", " + str(level),(0,0,0), font=font)

def writeRace(image, race):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,50)
	draw.text((1130, 310), race,(0,0,0), font=font)

def writeHP(image, hp):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,40)
	draw.text((1220, 820), str(hp),(0,0,0), font=font)

def writeAlignment(image, alignment):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,60)
	draw.text((1600, 310), alignment, font=font)

def writeInitiative(image, dex):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,60)
	draw.text((1210, 610), writeAbilityBonus(dex),(0,0,0), font=font)

def writeProficiency(image, proficiency):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,60)
	draw.text((410, 700), "+" + str(proficiency),(0,0,0), font=font)

def writeSpeed(image, speed):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,60)
	draw.text((1470, 610), str(speed),(0,0,0), font=font)

def writeHitDie(image, hitDie, hitDieTotal):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,75)
	draw.text((1000, 1390), hitDie,(0,0,0), font=font)
	font = ImageFont.truetype(fontFile,40)
	draw.text((1030, 1320), str(hitDieTotal),(0,0,0), font=font)

def writeSavingThrows(image, character):
#
	img = image
	draw = ImageDraw.Draw(img)
	throws = {
		"Strength": character.strengthSave,
		"Dexterity": character.dexteritySave,
		"Constitution": character.constitutionSave,
		"Intelligence": character.intelligenceSave,
		"Wisdom": character.wisdomSave,
		"Charisma": character.charismaSave
	}

	if throws["Strength"] == True:
		font = ImageFont.truetype(fontFile,30)
		draw.text((425, 860), "X",(0,0,0), font=font)
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 850), "+" + str(abilityBonus(character.strength) + character.proficiency),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 850), writeAbilityBonus(character.strength),(0,0,0), font=font)
	if throws["Dexterity"] == True:
		font = ImageFont.truetype(fontFile,30)
		draw.text((425, 920), "X",(0,0,0), font=font)
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 910), "+" + str(abilityBonus(character.dexterity) + character.proficiency),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 900), writeAbilityBonus(character.dexterity),(0,0,0), font=font)
	if throws["Constitution"] == True:
		font = ImageFont.truetype(fontFile,30)
		draw.text((425, 970), "X",(0,0,0), font=font)
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 960), "+" + str(abilityBonus(character.constitution) + character.proficiency),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 960), writeAbilityBonus(character.constitution),(0,0,0), font=font)
	if throws["Intelligence"] == True:
		font = ImageFont.truetype(fontFile,30)
		draw.text((425, 1030), "X",(0,0,0), font=font)
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 1020), "+" + str(abilityBonus(character.intelligence) + character.proficiency),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 1020), writeAbilityBonus(character.intelligence),(0,0,0), font=font)
	if throws["Wisdom"] == True:
		font = ImageFont.truetype(fontFile,30)
		draw.text((425, 1085), "X",(0,0,0), font=font)
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 1075), "+" + str(abilityBonus(character.wisdom) + character.proficiency),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 1075), writeAbilityBonus(character.wisdom),(0,0,0), font=font)
	if throws["Charisma"] == True:
		font = ImageFont.truetype(fontFile,30)
		draw.text((425, 1140), "X",(0,0,0), font=font)
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 1130), "+" + str(abilityBonus(character.charisma) + character.proficiency),(0,0,0), font=font)
	else:
		font = ImageFont.truetype(fontFile,40)
		draw.text((475, 1130), writeAbilityBonus(character.charisma),(0,0,0), font=font)

def writeSkills(image, character):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,30)
	if character.acrobaticsProficiency == True:
		draw.text((425, 1340), "X",(0,0,0), font=font)
	if character.animalHandlingProficiency == True:
		draw.text((425, 1395), "X",(0,0,0), font=font)
	if character.arcanaProficiency == True:
		draw.text((425, 1455), "X",(0,0,0), font=font)
	if character.athleticsProficiency == True:
		draw.text((425, 1510), "X",(0,0,0), font=font)
	if character.deceptionProficiency == True:
		draw.text((425, 1565), "X",(0,0,0), font=font)
	if character.historyProficiency == True:
		draw.text((425, 1625), "X",(0,0,0), font=font)
	if character.insightProficiency == True:
		draw.text((425, 1680), "X",(0,0,0), font=font)
	if character.intimidationProficiency == True:
		draw.text((425, 1735), "X",(0,0,0), font=font)
	if character.investigationProficiency == True:
		draw.text((425, 1790), "X",(0,0,0), font=font)
	if character.medicineProficiency == True:
		draw.text((425, 1845), "X",(0,0,0), font=font)
	if character.natureProficiency == True:
		draw.text((425, 1905), "X",(0,0,0), font=font)
	if character.perceptionProficiency == True:
		draw.text((425, 1960), "X",(0,0,0), font=font)
	if character.performanceProficiency == True:
		draw.text((425, 2015), "X",(0,0,0), font=font)
	if character.persuasionProficiency== True:
		draw.text((425, 2070), "X",(0,0,0), font=font)
	if character.religionProficiency == True:
		draw.text((425, 2125), "X",(0,0,0), font=font)
	if character.sleightOfHandProficiency == True:
		draw.text((425, 2185), "X",(0,0,0), font=font)
	if character.stealthProficiency == True:
		draw.text((425, 2240), "X",(0,0,0), font=font)
	if character.survivalProficiency == True:
		draw.text((425, 2295), "X",(0,0,0), font=font)

	font = ImageFont.truetype(fontFile,40)
	draw.text((465, 1330), "+" + str(character.acrobatics),(0,0,0), font=font)
	draw.text((465, 1385), "+" + str(character.animalHandling),(0,0,0), font=font)
	draw.text((465, 1440), "+" + str(character.arcana),(0,0,0), font=font)
	draw.text((465, 1500), "+" + str(character.athletics),(0,0,0), font=font)
	draw.text((465, 1555), "+" + str(character.deception),(0,0,0), font=font)
	draw.text((465, 1610), "+" + str(character.history),(0,0,0), font=font)
	draw.text((465, 1665), "+" + str(character.insight),(0,0,0), font=font)
	draw.text((465, 1725), "+" + str(character.intimidation),(0,0,0), font=font)
	draw.text((465, 1780), "+" + str(character.investigation),(0,0,0), font=font)
	draw.text((465, 1835), "+" + str(character.medicine),(0,0,0), font=font)
	draw.text((465, 1895), "+" + str(character.nature),(0,0,0), font=font)
	draw.text((465, 1950), "+" + str(character.perception),(0,0,0), font=font)
	draw.text((150, 2475), str(character.passivePerception),(0,0,0), font=font)
	draw.text((465, 2005), "+" + str(character.performance),(0,0,0), font=font)
	draw.text((465, 2060), "+" + str(character.persuasion),(0,0,0), font=font)
	draw.text((465, 2115), "+" + str(character.religion),(0,0,0), font=font)
	draw.text((465, 2175), "+" + str(character.sleightOfHand),(0,0,0), font=font)
	draw.text((465, 2230), "+" + str(character.stealth),(0,0,0), font=font)
	draw.text((465, 2285), "+" + str(character.survival),(0,0,0), font=font)


def writeEquipment(image, character):
#
	line = 0
	img = image
	draw = ImageDraw.Draw(img)
	equipmentString = character.equipment
	toPrint = textwrap.wrap(equipmentString, 30)
	font = ImageFont.truetype(fontFile,30)
	for x in range(len(toPrint)):
		draw.text((1110, 2470 + line), str(toPrint[x]).replace("'",""),(0,0,0), font=font)
		line += 47

	font = ImageFont.truetype(fontFile,40)

	draw.text((975, 2505), str(character.cp),(0,0,0), font=font)
	draw.text((975, 2615), str(character.sp),(0,0,0), font=font)
	draw.text((975, 2725), str(character.ep),(0,0,0), font=font)
	draw.text((975, 2830), str(character.gp),(0,0,0), font=font)
	draw.text((975, 2940), str(character.pp),(0,0,0), font=font)

def writeAttacks(image, character):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,25)
	if character.weapon1Name != None:
		draw.text((950, 1650), character.weapon1Name,(0,0,0), font=font)
		draw.text((1230, 1650), "+" + str(character.weapon1Attack),(0,0,0), font=font)
		draw.text((1380, 1650), character.weapon1Dmg,(0,0,0), font=font)

	if character.weapon2Name != None:
		draw.text((950, 1730), character.weapon2Name,(0,0,0), font=font)
		draw.text((1230, 1730), "+" + str(character.weapon2Attack),(0,0,0), font=font)
		draw.text((1380, 1730), character.weapon2Dmg,(0,0,0), font=font)

def writeArmor(image, character):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,60)
	draw.text((990, 610), str(character.armorClass),(0,0,0), font=font)

def writeSpells(image, character):
	if character.spells != None:
		line = 0
		img = image
		draw = ImageDraw.Draw(img)
		toPrint = textwrap.wrap(character.spells, 40)
		font = ImageFont.truetype(fontFile,30)
		for x in range(len(toPrint)):
			draw.text((925, 1880 + line), str(toPrint[x]).replace("'",""),(0,0,0), font=font)
			line += 45

def writeBackground(image, character):
#
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,60)
	draw.text((1600, 200), character.background,(0,0,0), font=font)

def writeProficiencies(image, character):
#
	line = 0
	img = image
	draw = ImageDraw.Draw(img)
	if character.languages == None:
		languageString = ""
	else:
		languageString = "Languages: " + str(character.languages)
	if character.proficiencies == None:
		proficiencyString = ""
	else:
		proficiencyString = "Proficiencies: " + str(character.proficiencies)

	toPrint = textwrap.wrap(languageString, 40)
	font = ImageFont.truetype(fontFile,30)
	for x in range(len(toPrint)):
		draw.text((140, 2600 + line), str(toPrint[x]).replace("'",""),(0,0,0), font=font)
		line += 50


	toPrint = textwrap.wrap(proficiencyString, 40)
	for x in range(len(toPrint)):
		draw.text((140, 2600 + line), str(toPrint[x]).replace("'",""),(0,0,0), font=font)
		line += 50

def writeTraits(image, character):
#
	line = 0
	img = image
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontFile,30)

	if character.traits != None:
		toPrint = textwrap.wrap(character.traits, 40)
		for x in range(len(toPrint)):
			draw.text((1720, 1600 + line), str(toPrint[x]).replace('"',''),(0,0,0), font=font)
			line += 46

def writeFlavor(image, character):
#
	line = 0
	img = image
	draw = ImageDraw.Draw(img)
	if character.personality != None:
		personalityString = character.personality
	else:
		personalityString=""
	if character.ideals != None:
		idealString = character.ideals
	else:
		idealString=""
	if character.bonds != None:
		bondString = character.bonds
	else:
		bondString=""
	if character.flaws != None:
		flawString = character.flaws
	else:
		flawString=""

	toPrint = textwrap.wrap(personalityString, 40)
	font = ImageFont.truetype(fontFile,30)
	for x in range(len(toPrint)):
		draw.text((1750, 580 + line), str(toPrint[x]),(0,0,0), font=font)
		line += 55

	line = 0
	toPrint = textwrap.wrap(idealString, 40)
	for x in range(len(toPrint)):
		draw.text((1750, 870 + line), str(toPrint[x]),(0,0,0), font=font)
		line += 55

	line = 0
	toPrint = textwrap.wrap(bondString, 40)
	font = ImageFont.truetype(fontFile,30)
	for x in range(len(toPrint)):
		draw.text((1750, 1100 + line), str(toPrint[x]),(0,0,0), font=font)
		line += 55

	line = 0
	toPrint = textwrap.wrap(flawString, 40)
	for x in range(len(toPrint)):
		draw.text((1750, 1330 + line), str(toPrint[x]),(0,0,0), font=font)
		line += 55

def skillProficient(character, bool):
	if bool:
		return character.proficiency
	else:
		return 0
def writeSheet(img, char):
	writeName(img, char.name)
	writePlayerName(img, char.playerName)
	writeAbilities(img, char)
	writeClass(img, char.characterClass, char.level)
	writeRace(img, char.race)
	writeHP(img, char.hp)
	writeHitDie(img, char.hitDie, char.hitDieTotal)
	writeAlignment(img, char.alignment)
	writeInitiative(img, char.dexterity)
	writeSpeed(img, char.speed)
	writeProficiency(img, char.proficiency)
	writeSavingThrows(img, char)
	writeSkills(img, char)
	writeEquipment(img, char)
	writeAttacks(img, char)
	writeArmor(img, char)
	writeSpells(img, char)
	writeBackground(img, char)
	writeProficiencies(img, char)
	writeTraits(img, char)
	writeFlavor(img, char)
