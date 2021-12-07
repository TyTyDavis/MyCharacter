from django.test import TestCase
from characters.models import Character
from . import writer
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
from PIL import Image
from django.core.files.temp import NamedTemporaryFile
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your tests here.
class characterTestCase(TestCase):
    def setUp(self):
        Character.objects.create(name="OnlyRequired",
        characterClass="Ranger",
        race="Orc",
        level=1,
        armorClass=10,
        speed=30,
        proficiency=1,
        hp=1,
        strengthSave = False,
        dexteritySave = False,
        constitutionSave = False,
        intelligenceSave = False,
        wisdomSave = False,
        charismaSave = False,
        strength = 10,
        dexterity = 10,
        constitution = 10,
        intelligence = 10,
        wisdom = 10,
        charisma = 10,
        acrobaticsProficiency = False,
        animalHandlingProficiency = False,
        arcanaProficiency = False,
        athleticsProficiency = False,
        deceptionProficiency = False,
        historyProficiency = False,
        insightProficiency = False,
        intimidationProficiency = False,
        medicineProficiency = False,
        natureProficiency = False,
        perceptionProficiency = False,
        religionProficiency = False,
        sleightOfHandProficiency = False,
        stealthProficiency = False,
        survivalProficiency = False,
        cp=0,
        sp=0,
        ep=0,
        gp=0,
        pp=0,
        )

        def test_character_sheet(self):
            character = Character.objects.get(name="OnlyRequired")
            sheet = Image.open(staticfiles_storage.path('blankSheet.png'))
            sheet_io = BytesIO()
            writer.writeSheet(sheet, character)
            sheet.save(sheet_io, format='PNG')
            sheet_file = InMemoryUploadedFile(sheet_io, None, 'foo.jpg', 'jpeg', None, None)
