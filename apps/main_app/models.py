from django.db import models

class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=2)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  desc = models.CharField(max_length=45)
  def __repr__(self):
    return f"<Dojo object: {self.name} {self.city} {self.state}>"

class Ninja(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  dojo = models.ForeignKey(Dojo, related_name='ninjas')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __repr__(self):
    return f"<Dojo object: {self.first_name} {self.last_name} {self.dojo}>"