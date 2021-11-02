import writer



def maxKey(d):
     """ a) create a list of the dict's keys and values;
         b) return the key with the max value"""
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

class Character:
	def __init__(self):
		self.level = 1
		self.abilities = None
		self.name = None
		self.gender = random.choice(["M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "N"])
		self.characterClass = "Fighter"
		self.race = "Dwarf"
		self.alignment = ["L","G"]
		self.background = "Mercenary"
		self.hitDie = 8
		self.hp = 12
		self.proficiency = 2
		self.speed = 20
		self.AC = 10
		self.silly = None
		self.caster = False
		self.skills = {
			"Acrobatics": False,
			"Animal Handling": False,
			"Arcana": False,
			"Athletics": False,
			"Deception": False,
			"History": False,
			"Insight": False,
			"Intimidation": False,
			"Investigation": False,
			"Medicine": False,
			"Nature": False,
			"Perception": False,
			"Performance": False,
			"Persuasion": False,
			"Religion": False,
			"Sleight of Hand": False,
			"Stealth": False,
			"Survival": False
	}
		self.abilities = {
			"Str": 0,
			"Dex": 0,
			"Con": 0,
			"Int": 0,
			"Wis": 0,
			"Cha": 0
			}
		self.proficiencies = []
		self.languages = []
		self.traits = []
		self.personality = "Blank"
		self.ideal = "blank"
		self.bond = "blank"
		self.flaw = "blank"





	def setSkills(self):
		for x in self.background.skills:
			self.skills[x] = True
		numChoices = self.characterClass.skillNum
		skillChoices = self.characterClass.skillChoices
		count = 0
		failSwitch = 0
		while count < numChoices and failSwitch < 10:
			chosen = random.choice(skillChoices)
			if self.skills[chosen] == False:
				self.skills[chosen] = True
				skillChoices.remove(chosen)
				count += 1
			else:
				failSwitch += 1



	def testSkills(self):
		self.skills = {
				"Acrobatics": True,
				"Animal Handling": True,
				"Arcana": True,
				"Athletics": True,
				"Deception": True,
				"History": True,
				"Insight": True,
				"Intimidation": True,
				"Investigation": True,
				"Medicine": True,
				"Nature": True,
				"Perception": True,
				"Performance": True,
				"Persuasion": True,
				"Religion": True,
				"Sleight of Hand": True,
				"Stealth": True,
				"Survival": True
			}
