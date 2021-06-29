from django.db import models

# Create your models here.
class Obs(models.Model):
    """class that holds observation info"""
    type = models.CharField(max_length=50)
    move1 = models.CharField(max_length=100)
    move2 = models.CharField(max_length=100)
    move3 = models.CharField(max_length=100)
    move4 = models.CharField(max_length=100)
    HP = models.IntegerField()
    ATK = models.IntegerField()
    DEF = models.IntegerField()
    ACC = models.IntegerField()
    EVA = models.IntegerField()
    SPD = models.IntegerField()

    def __str__(self):
        return self.type

    def create_obs(self, type, move1, move2, move3, move4, hp, atk, defense, acc, eva, spd):
        self.type = type
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.HP = hp
        self.ATK = atk
        self.DEF = defense
        self.ACC = acc
        self.EVA = eva
        self.SPD = spd
        return self

