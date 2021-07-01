from django.http.response import HttpResponse
from wagtail.core import fields
from .models import Obs
from django.core import serializers
from .utils.StatsAssign import Stats
import json

def onLoad(request):
    """view function for home page"""
    # clear previously populated database
    if(Obs.objects.exists()):
        Obs.objects.all().delete()
    # get stats
    stats_insect = Stats("Insecta", "needs_id").AssignStats()
    stats_reptile = Stats("Reptilia", "needs_id").AssignStats()
    stats_fish = Stats("Actinopterygii", "needs_id").AssignStats()
    stats_mammal = Stats("Mammalia", "needs_id").AssignStats()
    stats_amphibian = Stats("Amphibia", "needs_id").AssignStats()
    stats_arachnid = Stats("Arachnida", "needs_id").AssignStats()
    stats_bird = Stats("Aves", "needs_id").AssignStats()
    stats_mollusc = Stats("Mollusca", "needs_id").AssignStats()
    stats_chromist = Stats("Chromista", "needs_id").AssignStats()
    stats_animal = Stats("Animalia", "needs_id").AssignStats()
    stats_plant = Stats("Plantae", "needs_id").AssignStats()
    stats_fungi = Stats("Fungi", "needs_id").AssignStats()
    stats_protozoa = Stats("Protozoa", "needs_id").AssignStats()
    # create observations and store in db
    insect = Obs.create_obs(Obs(), "Insecta", "Nature's Wrath", "Spine Shield", "Explosive Reaction", "Stinging Venom", stats_insect.get("Health"), stats_insect.get("Attack"), stats_insect.get("Defense"), stats_insect.get("Accuracy"), stats_insect.get("Evasion"), stats_insect.get("Speed"))
    insect.save()
    reptile = Obs.create_obs(Obs(), "Reptilia", "Hiss", "Embiggen", "Spines", "Element of Surprise", stats_reptile.get("Health"), stats_reptile.get("Attack"), stats_reptile.get("Defense"), stats_reptile.get("Accuracy"), stats_reptile.get("Evasion"), stats_reptile.get("Speed"))
    reptile.save()
    fish = Obs.create_obs(Obs(), "Actinopterygii", "Daily Migration", "Cognitive Mapping", "Wrassling", "Shoal Up", stats_fish.get("Health"), stats_fish.get("Attack"), stats_fish.get("Defense"), stats_fish.get("Accuracy"), stats_fish.get("Evasion"), stats_fish.get("Speed"))
    fish.save()
    mammal = Obs.create_obs(Obs(), "Mammalia", "Passive Aggression", "Nail Scratch", "Sharp Teeth", "Strong Kick", stats_mammal.get("Health"), stats_mammal.get("Attack"), stats_mammal.get("Defense"), stats_mammal.get("Accuracy"), stats_mammal.get("Evasion"), stats_mammal.get("Speed"))
    mammal.save()
    amphibian = Obs.create_obs(Obs(), "Amphibia", "Warning Colors", "Secrete Mucous", "Neurotoxin", "Tail Lash", stats_amphibian.get("Health"), stats_amphibian.get("Attack"), stats_amphibian.get("Defense"), stats_amphibian.get("Accuracy"), stats_amphibian.get("Evasion"), stats_amphibian.get("Speed"))
    amphibian.save()
    arachnid = Obs.create_obs(Obs(), "Arachnida", "Sclerotised Pharynx", "Stinger", "Hide and Strike", "Spidey Sense", stats_arachnid.get("Health"), stats_arachnid.get("Attack"), stats_arachnid.get("Defense"), stats_arachnid.get("Accuracy"), stats_arachnid.get("Evasion"), stats_arachnid.get("Speed"))
    arachnid.save()

    context = {
        'Insecta':Obs.objects.filter(type='Insecta').__dict__,
        'Reptilia':Obs.objects.filter(type='Reptilia').__dict__,
        'Actinopterygii':Obs.objects.filter(type='Actinopterygii').__dict__,
        'Mammalia':Obs.objects.filter(type='Mammalia').__dict__,
        'Amphibia':Obs.objects.filter(type='Amphibia').__dict__,
        'Arachnida':Obs.objects.filter(type='Arachnida').__dict__,
        'Aves':Obs.objects.filter(type='Aves').__dict__,
        'Mollusca':Obs.objects.filter(type='Mollusca').__dict__,
        'Chromista':Obs.objects.filter(type='Chromista').__dict__,
        'Animalia':Obs.objects.filter(type='Animalia').__dict__,
        'Plantae':Obs.objects.filter(type='Plantae').__dict__,
        'Fungi':Obs.objects.filter(type='Fungi').__dict__,
        'Protozoa':Obs.objects.filter(type='Protozoa').__dict__
    }
    data = serializers.serialize('json', Obs.objects.all(), fields=('type',
    'move1',
    'move2',
    'move3',
    'move4',
    'HP',
    'ATK',
    'DEF',
    'ACC',
    'EVA',
    'SPD'))
    return HttpResponse(json.dumps(data))
