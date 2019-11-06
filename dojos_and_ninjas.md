class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=2)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  <!-- ninjas -->

class Ninja(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  dojo = models.ForeignKey(Dojo, related_name='ninjas')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

Query: Create 3 new dojos
Dojo.objects.create(name='OC', city='Costa Mesa', state='CA')
Dojo.objects.create(name='Burbank', city='Burbank', state='CA')
Dojo.objects.create(name='Seattle', city='Bellevue', state='CA')

Query: Delete the 3 dojos you just created
all=Dojo.objects.all()
all.delete()

Query: Create 3 more dojos
Dojo.objects.create(name='OC', city='Costa Mesa', state='CA')
Dojo.objects.create(name='Burbank', city='Burbank', state='CA')
Dojo.objects.create(name='Seattle', city='Bellevue', state='CA')

Query: Create 3 ninjas that belong to the first dojo
OC = Dojo.objects.get(id=4)
ninja1 = Ninja.objects.create(first_name='Michelle', last_name='Tanzil', dojo='OC')
ninja2 = Ninja.objects.create(first_name='Jane', last_name='Doe', dojo='OC')
ninja3 = Ninja.objects.create(first_name='Harry', last_name='Potter', dojo='OC')

Query: Create 3 ninjas that belong to the second dojo
ninja4 = Ninja.objects.create(first_name='Emma', last_name='Smith', dojo=Dojo.objects.get(id=5))
ninja5 = Ninja.objects.create(first_name='Olivia', last_name='Smith', dojo=Dojo.objects.get(id=5))
ninja6 = Ninja.objects.create(first_name='Ava', last_name='Smith', dojo=Dojo.objects.get(id=5))

Query: Create 3 ninjas that belong to the third dojo
seattle = Dojo.objects.get(id=6)
ninja7 = Ninja.objects.create(first_name='Isabella', last_name='Smith', dojo='seattle')
ninja8 = Ninja.objects.create(first_name='Sophia', last_name='Smith', dojo='seattle')
ninja9 = Ninja.objects.create(first_name='Charlotte', last_name='Smith', dojo='seattle')

Query: Retrieve all the ninjas from the first dojo
OC = Dojo.objects.get(id=4)
OC_ninjas = Ninja.objects.filter(dojo=OC)

Query: Retrieve all the ninjas from the last dojo
seattle = Dojo.objects.get(id=6)
seattle_ninjas=Ninja.objects.filter(dojo=seattle)

Query: Retrieve the last ninja's dojo
ninja9.dojo

Add a new text field called "desc" to your Dojo class
desc = models.CharField(max_length=45)
python manage.py makemigrations
Option 1

Create and run the migration files to update the table in your database. If needed, provide a default value of "old dojo"
"old dojo"

Query: Create a new dojo
Dojo.objects.create(name="OC_Two", city="Costa Mesa", state="CA", desc="good")