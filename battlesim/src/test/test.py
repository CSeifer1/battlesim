# File: tests.py
# Author: Colin Seifer, Danielle Dishop
# Description: This file contains the test suite for multiple files and functionalities

import json

from django.test import TestCase, Client
from django.urls import reverse

from ..utils.TypeAssign import Type
from ..utils.StatsAssign import FLOOR, CEILING, INCREASE_MOD, DECREASE_MOD, QUALITY_MOD, Stats
from .. import Moves
from .. import LoadObservation
from .. import BattleCalc
from .. import BattleSys
from .. import BattleEffects

client = Client()

# Tests go here.
class StatsGenTestCase(TestCase):

    # Tests that stats are correctly assigned for Mammalia
    def test_Mammalia_needs_ID(self):
        # Mammalia has increased evasion and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mammal = Stats('Mammalia', "needs_id")
        mammalStats = mammal.AssignStats()
        for stat in mammalStats:
            statValue = mammalStats.get(stat)
            if (stat != "Evasion") and (stat != "Accuracy"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Actinopterygii
    def test_Actinopterygii_needs_ID(self):
        # Actinopterygii has increased speed and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fish = Stats('Actinopterygii', "needs_id")
        fishStats = fish.AssignStats()
        for stat in fishStats:
            statValue = fishStats.get(stat)
            if (stat != "Speed") and (stat != "Attack"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Fungi
    def test_Fungi_needs_ID(self):
        # Fungi has increased health and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fungi = Stats('Fungi', "needs_id")
        fungiStats = fungi.AssignStats()
        for stat in fungiStats:
            statValue = fungiStats.get(stat)
            if (stat != "Health") and (stat != "Evasion"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Reptilia
    def test_Reptilia_needs_ID(self):
        # Reptilia has increased accuracy and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        reptile = Stats('Reptilia', "needs_id")
        reptileStats = reptile.AssignStats()
        for stat in reptileStats:
            statValue = reptileStats.get(stat)
            if (stat != "Accuracy") and (stat != "Evasion"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Chromista
    def test_Chromista_needs_ID(self):
        # Chromista has increased health and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        chromist = Stats('Chromista', "needs_id")
        chromistStats = chromist.AssignStats()
        for stat in chromistStats:
            statValue = chromistStats.get(stat)
            if (stat != "Health") and (stat != "Speed"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Plantae
    def test_Plantae_needs_ID(self):
        # Plantae has increased defense and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        plant = Stats('Plantae', "needs_id")
        plantStats = plant.AssignStats()
        for stat in plantStats:
            statValue = plantStats.get(stat)
            if (stat != "Defense") and (stat != "Attack"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Animalia
    def test_Animalia_needs_ID(self):
        # Animalia has no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        animal = Stats('Animalia', "needs_id")
        animalStats = animal.AssignStats()
        for stat in animalStats:
            statValue = animalStats.get(stat)
            if (statValue < FLOOR) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mollusca
    def test_Mollusca_needs_ID(self):
        # Mollusca has increased defense and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mollusc = Stats('Mollusca', "needs_id")
        molluscStats = mollusc.AssignStats()
        for stat in molluscStats:
            statValue = molluscStats.get(stat)
            if (stat != "Defense") and (stat != "Speed"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Insecta
    def test_Insecta_needs_ID(self):
        # Insecta has increased speed and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        insect = Stats('Insecta', "needs_id")
        insectStats = insect.AssignStats()
        for stat in insectStats:
            statValue = insectStats.get(stat)
            if (stat != "Speed") and (stat != "Defense"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Aves
    def test_Aves_needs_ID(self):
        # Aves has increased accuracy and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        bird = Stats('Aves', "needs_id")
        birdStats = bird.AssignStats()
        for stat in birdStats:
            statValue = birdStats.get(stat)
            if (stat != "Accuracy") and (stat != "Health"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Amphibia
    def test_Amphibia_needs_ID(self):
        # Amphibia has increased attack and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        amphibian = Stats('Amphibia', "needs_id")
        amphibianStats = amphibian.AssignStats()
        for stat in amphibianStats:
            statValue = amphibianStats.get(stat)
            if (stat != "Attack") and (stat != "Accuracy"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Arachnida
    def test_Arachnida_needs_ID(self):
        # Arachnida has increased attack and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        arachnid = Stats('Arachnida', "needs_id")
        arachnidStats = arachnid.AssignStats()
        for stat in arachnidStats:
            statValue = arachnidStats.get(stat)
            if (stat != "Attack") and (stat != "Defense"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Protozoa
    def test_Protozoa_needs_ID(self):
        # Protozoa has increased evasion and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        protozoa = Stats('Protozoa', "needs_id")
        protozoaStats = protozoa.AssignStats()
        for stat in protozoaStats:
            statValue = protozoaStats.get(stat)
            if (stat != "Evasion") and (stat != "Health"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    def test_Undefined_needs_ID(self):
        # Undefined observations have no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        undef = Stats('Undefined', "needs_id")
        undefStats = undef.AssignStats()
        for stat in undefStats:
            statValue = undefStats.get(stat)
            if (statValue < FLOOR) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mammalia
    def test_Mammalia_casual(self):
        # Mammalia has increased evasion and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mammal = Stats('Mammalia', "casual")
        mammalStats = mammal.AssignStats()
        for stat in mammalStats:
            statValue = mammalStats.get(stat)
            if (stat != "Evasion") and (stat != "Accuracy"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Actinopterygii
    def test_Actinopterygii_casual(self):
        # Actinopterygii has increased speed and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fish = Stats('Actinopterygii', "casual")
        fishStats = fish.AssignStats()
        for stat in fishStats:
            statValue = fishStats.get(stat)
            if (stat != "Speed") and (stat != "Attack"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Fungi
    def test_Fungi_casual(self):
        # Fungi has increased health and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fungi = Stats('Fungi', "casual")
        fungiStats = fungi.AssignStats()
        for stat in fungiStats:
            statValue = fungiStats.get(stat)
            if (stat != "Health") and (stat != "Evasion"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Reptilia
    def test_Reptilia_casual(self):
        # Reptilia has increased accuracy and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        reptile = Stats('Reptilia', "casual")
        reptileStats = reptile.AssignStats()
        for stat in reptileStats:
            statValue = reptileStats.get(stat)
            if (stat != "Accuracy") and (stat != "Evasion"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Chromista
    def test_Chromista_casual(self):
        # Chromista has increased health and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        chromist = Stats('Chromista', "casual")
        chromistStats = chromist.AssignStats()
        for stat in chromistStats:
            statValue = chromistStats.get(stat)
            if (stat != "Health") and (stat != "Speed"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Plantae
    def test_Plantae_casual(self):
        # Plantae has increased defense and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        plant = Stats('Plantae', "casual")
        plantStats = plant.AssignStats()
        for stat in plantStats:
            statValue = plantStats.get(stat)
            if (stat != "Defense") and (stat != "Attack"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Animalia
    def test_Animalia_casual(self):
        # Animalia has no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        animal = Stats('Animalia', "casual")
        animalStats = animal.AssignStats()
        for stat in animalStats:
            statValue = animalStats.get(stat)
            if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mollusca
    def test_Mollusca_casual(self):
        # Mollusca has increased defense and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mollusc = Stats('Mollusca', "casual")
        molluscStats = mollusc.AssignStats()
        for stat in molluscStats:
            statValue = molluscStats.get(stat)
            if (stat != "Defense") and (stat != "Speed"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Insecta
    def test_Insecta_casual(self):
        # Insecta has increased speed and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        insect = Stats('Insecta', "casual")
        insectStats = insect.AssignStats()
        for stat in insectStats:
            statValue = insectStats.get(stat)
            if (stat != "Speed") and (stat != "Defense"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Aves
    def test_Aves_casual(self):
        # Aves has increased accuracy and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        bird = Stats('Aves', "casual")
        birdStats = bird.AssignStats()
        for stat in birdStats:
            statValue = birdStats.get(stat)
            if (stat != "Accuracy") and (stat != "Health"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Amphibia
    def test_Amphibia_casual(self):
        # Amphibia has increased attack and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        amphibian = Stats('Amphibia', "casual")
        amphibianStats = amphibian.AssignStats()
        for stat in amphibianStats:
            statValue = amphibianStats.get(stat)
            if (stat != "Attack") and (stat != "Accuracy"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Arachnida
    def test_Arachnida_casual(self):
        # Arachnida has increased attack and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        arachnid = Stats('Arachnida', "casual")
        arachnidStats = arachnid.AssignStats()
        for stat in arachnidStats:
            statValue = arachnidStats.get(stat)
            if (stat != "Attack") and (stat != "Defense"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Protozoa
    def test_Protozoa_casual(self):
        # Protozoa has increased evasion and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        protozoa = Stats('Protozoa', "casual")
        protozoaStats = protozoa.AssignStats()
        for stat in protozoaStats:
            statValue = protozoaStats.get(stat)
            if (stat != "Evasion") and (stat != "Health"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    def test_Undefined_casual(self):
        # Undefined observations have no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        undef = Stats('Undefined', "casual")
        undefStats = undef.AssignStats()
        for stat in undefStats:
            statValue = undefStats.get(stat)
            if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mammalia
    def test_Mammalia_research(self):
        # Mammalia has increased evasion and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mammal = Stats('Mammalia', "research")
        mammalStats = mammal.AssignStats()
        for stat in mammalStats:
            statValue = mammalStats.get(stat)
            if (stat != "Evasion") and (stat != "Accuracy"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Actinopterygii
    def test_Actinopterygii_research(self):
        # Actinopterygii has increased speed and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fish = Stats('Actinopterygii', "research")
        fishStats = fish.AssignStats()
        for stat in fishStats:
            statValue = fishStats.get(stat)
            if (stat != "Speed") and (stat != "Attack"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Fungi
    def test_Fungi_research(self):
        # Fungi has increased health and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fungi = Stats('Fungi', "research")
        fungiStats = fungi.AssignStats()
        for stat in fungiStats:
            statValue = fungiStats.get(stat)
            if (stat != "Health") and (stat != "Evasion"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Reptilia
    def test_Reptilia_research(self):
        # Reptilia has increased accuracy and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        reptile = Stats('Reptilia', "research")
        reptileStats = reptile.AssignStats()
        for stat in reptileStats:
            statValue = reptileStats.get(stat)
            if (stat != "Accuracy") and (stat != "Evasion"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Chromista
    def test_Chromista_research(self):
        # Chromista has increased health and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        chromist = Stats('Chromista', "research")
        chromistStats = chromist.AssignStats()
        for stat in chromistStats:
            statValue = chromistStats.get(stat)
            if (stat != "Health") and (stat != "Speed"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Plantae
    def test_Plantae_research(self):
        # Plantae has increased defense and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        plant = Stats('Plantae', "research")
        plantStats = plant.AssignStats()
        for stat in plantStats:
            statValue = plantStats.get(stat)
            if (stat != "Defense") and (stat != "Attack"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Animalia
    def test_Animalia_research(self):
        # Animalia has no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        animal = Stats('Animalia', "research")
        animalStats = animal.AssignStats()
        for stat in animalStats:
            statValue = animalStats.get(stat)
            if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mollusca
    def test_Mollusca_research(self):
        # Mollusca has increased defense and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mollusc = Stats('Mollusca', "research")
        molluscStats = mollusc.AssignStats()
        for stat in molluscStats:
            statValue = molluscStats.get(stat)
            if (stat != "Defense") and (stat != "Speed"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Insecta
    def test_Insecta_research(self):
        # Insecta has increased speed and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        insect = Stats('Insecta', "research")
        insectStats = insect.AssignStats()
        for stat in insectStats:
            statValue = insectStats.get(stat)
            if (stat != "Speed") and (stat != "Defense"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Aves
    def test_Aves_research(self):
        # Aves has increased accuracy and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        bird = Stats('Aves', "research")
        birdStats = bird.AssignStats()
        for stat in birdStats:
            statValue = birdStats.get(stat)
            if (stat != "Accuracy") and (stat != "Health"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Amphibia
    def test_Amphibia_research(self):
        # Amphibia has increased attack and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        amphibian = Stats('Amphibia', "research")
        amphibianStats = amphibian.AssignStats()
        for stat in amphibianStats:
            statValue = amphibianStats.get(stat)
            if (stat != "Attack") and (stat != "Accuracy"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Arachnida
    def test_Arachnida_research(self):
        # Arachnida has increased attack and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        arachnid = Stats('Arachnida', "research")
        arachnidStats = arachnid.AssignStats()
        for stat in arachnidStats:
            statValue = arachnidStats.get(stat)
            if (stat != "Attack") and (stat != "Defense"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Protozoa
    def test_Protozoa_research(self):
        # Protozoa has increased evasion and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        protozoa = Stats('Protozoa', "research")
        protozoaStats = protozoa.AssignStats()
        for stat in protozoaStats:
            statValue = protozoaStats.get(stat)
            if (stat != "Evasion") and (stat != "Health"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    def test_Undefined_research(self):
        # Undefined observations have no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        undef = Stats('Undefined', "research")
        undefStats = undef.AssignStats()
        for stat in undefStats:
            statValue = undefStats.get(stat)
            if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mammalia
    def test_Mammalia_invalid_Quality(self):
        # Mammalia has increased evasion and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mammal = Stats('Mammalia', "invalid_Quality")
        mammalStats = mammal.AssignStats()
        for stat in mammalStats:
            statValue = mammalStats.get(stat)
            if (stat != "Evasion") and (stat != "Accuracy"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Actinopterygii
    def test_Actinopterygii_invalid_Quality(self):
        # Actinopterygii has increased speed and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fish = Stats('Actinopterygii', "invalid_Quality")
        fishStats = fish.AssignStats()
        for stat in fishStats:
            statValue = fishStats.get(stat)
            if (stat != "Speed") and (stat != "Attack"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Fungi
    def test_Fungi_invalid_Quality(self):
        # Fungi has increased health and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fungi = Stats('Fungi', "invalid_Quality")
        fungiStats = fungi.AssignStats()
        for stat in fungiStats:
            statValue = fungiStats.get(stat)
            if (stat != "Health") and (stat != "Evasion"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Reptilia
    def test_Reptilia_invalid_Quality(self):
        # Reptilia has increased accuracy and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        reptile = Stats('Reptilia', "invalid_Quality")
        reptileStats = reptile.AssignStats()
        for stat in reptileStats:
            statValue = reptileStats.get(stat)
            if (stat != "Accuracy") and (stat != "Evasion"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Chromista
    def test_Chromista_invalid_Quality(self):
        # Chromista has increased health and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        chromist = Stats('Chromista', "invalid_Quality")
        chromistStats = chromist.AssignStats()
        for stat in chromistStats:
            statValue = chromistStats.get(stat)
            if (stat != "Health") and (stat != "Speed"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Plantae
    def test_Plantae_invalid_Quality(self):
        # Plantae has increased defense and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        plant = Stats('Plantae', "invalid_Quality")
        plantStats = plant.AssignStats()
        for stat in plantStats:
            statValue = plantStats.get(stat)
            if (stat != "Defense") and (stat != "Attack"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Animalia
    def test_Animalia_invalid_Quality(self):
        # Animalia has no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        animal = Stats('Animalia', "invalid_Quality")
        animalStats = animal.AssignStats()
        for stat in animalStats:
            statValue = animalStats.get(stat)
            if (statValue < FLOOR) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mollusca
    def test_Mollusca_invalid_Quality(self):
        # Mollusca has increased defense and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mollusc = Stats('Mollusca', "invalid_Quality")
        molluscStats = mollusc.AssignStats()
        for stat in molluscStats:
            statValue = molluscStats.get(stat)
            if (stat != "Defense") and (stat != "Speed"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Insecta
    def test_Insecta_invalid_Quality(self):
        # Insecta has increased speed and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        insect = Stats('Insecta', "invalid_Quality")
        insectStats = insect.AssignStats()
        for stat in insectStats:
            statValue = insectStats.get(stat)
            if (stat != "Speed") and (stat != "Defense"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Aves
    def test_Aves_invalid_Quality(self):
        # Aves has increased accuracy and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        bird = Stats('Aves', "invalid_Quality")
        birdStats = bird.AssignStats()
        for stat in birdStats:
            statValue = birdStats.get(stat)
            if (stat != "Accuracy") and (stat != "Health"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Amphibia
    def test_Amphibia_invalid_Quality(self):
        # Amphibia has increased attack and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        amphibian = Stats('Amphibia', "invalid_Quality")
        amphibianStats = amphibian.AssignStats()
        for stat in amphibianStats:
            statValue = amphibianStats.get(stat)
            if (stat != "Attack") and (stat != "Accuracy"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Arachnida
    def test_Arachnida_invalid_Quality(self):
        # Arachnida has increased attack and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        arachnid = Stats('Arachnida', "invalid_Quality")
        arachnidStats = arachnid.AssignStats()
        for stat in arachnidStats:
            statValue = arachnidStats.get(stat)
            if (stat != "Attack") and (stat != "Defense"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Protozoa
    def test_Protozoa_invalid_Quality(self):
        # Protozoa has increased evasion and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        protozoa = Stats('Protozoa', "invalid_Quality")
        protozoaStats = protozoa.AssignStats()
        for stat in protozoaStats:
            statValue = protozoaStats.get(stat)
            if (stat != "Evasion") and (stat != "Health"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    def test_Undefined_invalid_Quality(self):
        # Undefined observations have no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        undef = Stats('Undefined', "invalid_Quality")
        undefStats = undef.AssignStats()
        for stat in undefStats:
            statValue = undefStats.get(stat)
            if (statValue < FLOOR) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

class TestStats(TestCase):

    # test that moves are imported correctly
    def test_moves(self):
        test_move = Moves.Moves()
        move = test_move.RetMove("Nature's Wrath")
        # test import
        self.assertEqual(move.get("name"), "Nature's Wrath")
        # test that invalid move returns None
        move = test_move.RetMove("invalid_move")
        self.assertIsNone(move)

    # test that observation is created correctly
    def test_observation(self):
        stats = [100, 100, 100, 100, 100, 100]
        moves = ["Nature's Wrath", "Autotomy", "Spine Shield", "Mimesis"]
        obs_type = "Insecta"
        obs_id = 1
        test_obs = LoadObservation.LoadObservation(obs_id, obs_type, moves, stats)
        # test that values are non-empty
        self.assertEqual(test_obs.stats[0], 100)
        self.assertEqual(test_obs.moves[0].get("name"), "Nature's Wrath")
        self.assertEqual(test_obs.stat_mod[0], 0)
        self.assertEqual(test_obs.observation_type, "Insecta")
        self.assertEqual(test_obs.obs_id, 1)

    # test that battle calculations are correctly computed
    def test_battleCalc(self):
        hit = 0
        miss = 0
        for i in range(1000):
            res = BattleCalc.Hit(80, 100, 100)
            if(res):
                hit += 1
            else:
                miss += 1
        # test that some moves hit and some missed
        self.assertTrue(hit > 0 and miss > 0)
        # test that damage is calculated correctly
        self.assertEqual(BattleCalc.Damage(100, 100, 80), 80)
        # test that speed is computed correctly
        self.assertTrue(BattleCalc.Speed(120, 100) > 0)
        self.assertTrue(BattleCalc.Speed(100, 101) < 0)
        self.assertEqual(BattleCalc.Speed(100, 100), 0)

    # test that battle system works properly
    def test_battle_sys(self):
        stats = [100, 100, 100, 100, 100, 100]
        moves = ["Flight Feathers", "Autotomy", "Sacrificial Tail", "Mimesis"]
        obs_type = "Insecta"
        observations = []
        # create list of 6 observations
        for i in range(6):
            observations.append(LoadObservation.LoadObservation(obs_type, moves, stats))
        # create battle object
        test_battle = BattleSys.Battle(observations)
        # test battle object observations size
        self.assertEqual(len(test_battle.observations), 6)
        # test that observations were imported correctly
        self.assertEqual(test_battle.observations[0].stats[0], 100)

        # test get methods in range
        self.assertEqual(test_battle.GetFlavorText(1), "The observation uses its fight feathers to increase its speed by 60%.")
        self.assertEqual(test_battle.GetBP(4), 60)
        self.assertEqual(test_battle.GetACC(4), 100)

        # test get methods out of range
        self.assertIsNone(test_battle.GetFlavorText(5))
        self.assertIsNone(test_battle.GetBP(1))
        self.assertIsNone(test_battle.GetACC(1))
        self.assertIsNone(test_battle.GetBP(5))
        self.assertIsNone(test_battle.GetACC(5))

        # test set methods
        # valid input
        test_battle.SetSwitch(1)
        self.assertEqual(test_battle.switch, 1)
        # test invalid input
        test_battle.SetSwitch(6)
        self.assertEqual(test_battle.switch, 1)
        # valid input
        test_battle.SetMoveChoice(4)
        self.assertEqual(test_battle.move_choice, 4)
        # test invalid input
        test_battle.SetMoveChoice(0)
        self.assertEqual(test_battle.move_choice, 4)
        test_battle.SetSwitch(0)
        # reset values
        test_battle.PlayerTurn()

        # test player turn switch
        test_battle.switch = 1
        test_battle.PlayerTurn()
        self.assertEqual(test_battle.p1_active_obs, 1)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        #test player turn move
        test_battle.move_choice = 4
        test_battle.PlayerTurn()
        self.assertEqual(test_battle.p1_move, test_battle.observations[1].moves[3])
        # test that move is reset
        self.assertEqual(test_battle.move_choice, 0)

        # test opponent not ai turn switch
        test_battle.switch = 4
        test_battle.OpponentTurn(False)
        self.assertEqual(test_battle.p2_active_obs, 4)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        #test opponent not ai turn move
        test_battle.move_choice = 4
        test_battle.OpponentTurn(False)
        self.assertEqual(test_battle.p2_move, test_battle.observations[4].moves[3])
        # test that move is reset
        self.assertEqual(test_battle.move_choice, 0)

        # test priority
        # p1_move should have higher priority
        test_battle.p1_move = test_battle.observations[1].moves[2]
        test_battle.p2_move = test_battle.observations[1].moves[3]
        # p1 priority indicated by return of 0
        self.assertEqual(test_battle.Priority(), 0)

        # p2_move should have higher priority
        test_battle.p1_move = test_battle.observations[1].moves[3]
        test_battle.p2_move = test_battle.observations[1].moves[2]
        # p2 priority indicated by return of 1
        self.assertEqual(test_battle.Priority(), 1)

        # test player switch
        test_battle.switch = 2
        test_battle.PlayerSwitch()
        self.assertEqual(test_battle.p1_active_obs, 2)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        # test opponent not ai switch
        test_battle.switch = 5
        test_battle.OpponentSwitch(False)
        self.assertEqual(test_battle.p2_active_obs, 5)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        # test attack not ai
        test_battle.p1_move = test_battle.observations[test_battle.p1_active_obs].moves[3]
        test_battle.p2_move = test_battle.observations[test_battle.p2_active_obs].moves[0]
        test_battle.Attack(False)
        # test that p1 attack reduces HP of p2 observation by 60
        self.assertEqual(test_battle.observations[5].stats[0], 40)
        # knock out p2 observation
        test_battle.switch = 4
        test_battle.p1_move = test_battle.observations[test_battle.p1_active_obs].moves[3]
        test_battle.p2_move = test_battle.observations[test_battle.p2_active_obs].moves[0]
        test_battle.Attack(False)
        self.assertTrue(test_battle.observations[5].stats[0] <= 0)
        # test that p2 observation was switched to 4
        self.assertEqual(test_battle.p2_active_obs, 4)
        # knock out p2 observation 4
        test_battle.p1_move = test_battle.observations[test_battle.p1_active_obs].moves[3]
        test_battle.p2_move = test_battle.observations[test_battle.p2_active_obs].moves[0]
        test_battle.Attack(False)
        test_battle.switch = 3
        test_battle.p1_move = test_battle.observations[test_battle.p1_active_obs].moves[3]
        test_battle.p2_move = test_battle.observations[test_battle.p2_active_obs].moves[0]
        test_battle.Attack(False)
        self.assertTrue(test_battle.observations[4].stats[0] <= 0)
        self.assertEqual(test_battle.p2_active_obs, 3)
        # attack one more time to get p2 final observation to 40hp
        test_battle.p1_move = test_battle.observations[test_battle.p1_active_obs].moves[3]
        test_battle.p2_move = test_battle.observations[test_battle.p2_active_obs].moves[0]
        test_battle.Attack(False)

        # test final turn in BattleLoop with ai
        # commented out since it will fail ~1/4 of the time due to secondary move effects.
        #test_battle.move_choice = 4
        # player 1 should win which is returned as a 0
        #self.assertEqual(test_battle.BattleLoop(True), 0)

    # test battle effects handled before attack
    def test_pre_attack(self):
        # HP_STAT = 10000 not a mistake. We don't want any KOs in this test.
        stats = [10000, 100, 100, 100, 100, 100]
        moves = ["Talon Grab", "Thorns", "Drop", "Extra Membrane"]
        obs_type = "Insecta"
        observations = []
        # create new list of observations
        for i in range(6):
            observations.append(LoadObservation.LoadObservation(obs_type, moves, stats))
        # create battle object
        test_atk = BattleSys.Battle(observations)

        # test that require contact works
        test_atk.p1_move = test_atk.observations[test_atk.p1_active_obs].moves[1]
        test_atk.p2_move = test_atk.observations[test_atk.p2_active_obs].moves[0]
        test_atk.Attack(False)
        self.assertEqual(test_atk.observations[test_atk.p2_active_obs].stats[0], 10000)
        test_atk.p1_move_prev = None
        test_atk.p2_move_prev = None
        test_atk.p1_move = test_atk.observations[test_atk.p1_active_obs].moves[1]
        test_atk.p2_move = test_atk.observations[test_atk.p2_active_obs].moves[1]
        test_atk.Attack(False)
        self.assertEqual(test_atk.observations[test_atk.p1_active_obs].stats[0], 9900)
        self.assertEqual(test_atk.observations[test_atk.p2_active_obs].stats[0], 9900)

        # test next attack lock
        test_atk.p1_move_prev = test_atk.observations[test_atk.p1_active_obs].moves[0]
        test_atk.p2_move_prev = None
        test_atk.p1_move = test_atk.observations[test_atk.p1_active_obs].moves[2]
        test_atk.p2_move = test_atk.observations[test_atk.p2_active_obs].moves[1]
        test_atk.Attack(False)
        self.assertEqual(test_atk.observations[test_atk.p1_active_obs].stats[0], 9900)
        self.assertEqual(test_atk.observations[test_atk.p2_active_obs].stats[0], 9800)

        # test previous move requirement
        test_atk.p1_move_prev = test_atk.observations[test_atk.p1_active_obs].moves[0]
        test_atk.p2_move_prev = None
        test_atk.p1_move = test_atk.observations[test_atk.p1_active_obs].moves[2]
        test_atk.p2_move = test_atk.observations[test_atk.p2_active_obs].moves[2]
        test_atk.Attack(False)
        self.assertEqual(test_atk.observations[test_atk.p1_active_obs].stats[0], 9900)
        self.assertEqual(test_atk.observations[test_atk.p2_active_obs].stats[0], 9700)

        # test first turn requirement
        test_atk.turn = 1
        test_atk.p1_move_prev = None
        test_atk.p2_move_prev = None
        test_atk.p1_move = test_atk.observations[test_atk.p1_active_obs].moves[3]
        test_atk.p2_move = test_atk.observations[test_atk.p2_active_obs].moves[3]
        test_atk.Attack(False)
        self.assertTrue(test_atk.p1_move_prev == test_atk.observations[test_atk.p1_active_obs].moves[3])
        self.assertTrue(test_atk.p2_move_prev == test_atk.observations[test_atk.p2_active_obs].moves[3])
        test_atk.turn = 2
        test_atk.p1_move_prev = None
        test_atk.p2_move_prev = None
        test_atk.p1_move = test_atk.observations[test_atk.p1_active_obs].moves[3]
        test_atk.p2_move = test_atk.observations[test_atk.p2_active_obs].moves[3]
        test_atk.Attack(False)
        self.assertIsNone(test_atk.p1_move_prev)
        self.assertIsNone(test_atk.p2_move_prev)

    # test battle effects handled in attack
    def test_attack(self):
        # HP_STAT = 10000 not a mistake. We don't want any KOs in this test.
        stats = [10000, 100, 100, 100, 100, 100]
        moves = ["Seafood Surprise", "Host Control", "Den Trap", "Extra Membrane"]
        obs_type = "Insecta"
        observations = []
        # create new list of observations
        for i in range(6):
            observations.append(LoadObservation.LoadObservation(obs_type, moves, stats))
        # create battle object
        test_atk = BattleSys.Battle(observations)

        # test use opponent attack
        test_atk.p1_move_prev = None
        test_atk.p2_move_prev = None
        test_atk.p1_move = test_atk.observations[test_atk.p1_active_obs].moves[1]
        test_atk.p2_move = test_atk.observations[test_atk.p2_active_obs].moves[3]
        test_atk.Attack(False)
        self.assertEqual(test_atk.p1_move_prev, test_atk.observations[test_atk.p2_active_obs].moves[3])

        # test require priority
        test_atk.p1_move_prev = None
        test_atk.p2_move_prev = None
        test_atk.p1_move = test_atk.observations[test_atk.p1_active_obs].moves[2]
        test_atk.p2_move = test_atk.observations[test_atk.p2_active_obs].moves[3]
        test_atk.Attack(False)
        self.assertIsNone(test_atk.p1_move_prev)

        # test reduce damage
        test_atk.p1_move_prev = test_atk.observations[test_atk.p1_active_obs].moves[3]
        test_atk.p2_move_prev = test_atk.observations[test_atk.p2_active_obs].moves[3]
        test_atk.p1_move = None
        test_atk.p2_move = test_atk.observations[test_atk.p2_active_obs].moves[2]
        test_atk.Attack(False)
        self.assertTrue(test_atk.observations[test_atk.p1_active_obs].stats[0] == 10000)

        # test random move (not guaranteed to pass, but statistically unlikely it will fail)
        passed = False
        for i in range(1000):
            test_atk.p1_move_prev = None
            test_atk.p2_move_prev = None
            test_atk.p1_move = test_atk.observations[test_atk.p1_active_obs].moves[0]
            test_atk.p2_move = None
            test_atk.Attack(True)
            # in case an observation was knocked out, revive it.
            for obs in test_atk.observations:
                if(obs.stats[0] <= 0):
                    obs.stats[0] = 10000
            # if p1 used a move, test passed.
            if(test_atk.p1_move_prev != None):
                passed = True
        self.assertTrue(passed)
            
    # test switch effects handled in attack
    def test_switch(self):
        # HP_STAT = 10000 not a mistake. We don't want any KOs in this test.
        stats = [10000, 100, 100, 100, 100, 100]
        moves = ["Sacrificial Tail", "Passive Aggression", "Flight Feathers", "Flight Feathers"]
        obs_type = "Insecta"
        observations = []
        # create new list of observations
        for i in range(6):
            observations.append(LoadObservation.LoadObservation(obs_type, moves, stats))
        # create battle object
        test_atk = BattleSys.Battle(observations)

        # test free switch
        test_atk.p1_active_obs = 0
        test_atk.switch = 1
        test_atk.p1_move = test_atk.observations[test_atk.p1_active_obs].moves[0]
        test_atk.p2_move = test_atk.observations[test_atk.p2_active_obs].moves[3]
        test_atk.Attack(False)
        self.assertEqual(test_atk.p1_active_obs, 1)

        # test force switch
        test_atk.p2_active_obs = 3
        test_atk.switch = 4
        test_atk.p1_move = test_atk.observations[test_atk.p1_active_obs].moves[1]
        test_atk.p2_move = test_atk.observations[test_atk.p2_active_obs].moves[3]
        test_atk.Attack(False)
        self.assertEqual(test_atk.p2_active_obs, 4)

    # test that battle effects work properly
    def test_battle_effects(self):
        stats = [100, 100, 100, 100, 100, 100]
        moves = ["Nature's Wrath", "Nature's Beauty", "Hiss", "Deep Roots"]
        obs_type = "Insecta"
        observations = []
        p1_obs = 0
        p2_obs = 3
        # create new list of observations
        for i in range(6):
            observations.append(LoadObservation.LoadObservation(obs_type, moves, stats))

        # test that additional_effects modifies user stats
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[0], 0)
        # make sure all stat modifiers were set to 0.2
        for stat in observations[p1_obs].stat_mod:
            self.assertAlmostEqual(stat, 0.2, 2)
        # make sure stat modifications occurred properly
        for stat in observations[p1_obs].stats:
            self.assertEqual(stat, 120)
        # try to get stats above 1 (not allowed) and test again
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[0], 0)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[0], 0)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[0], 0)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[0], 0)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[0], 0)
        for stat in observations[p1_obs].stat_mod:
            self.assertAlmostEqual(stat, 1.0, 2)

        # test opponent stat modifiers
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p2_obs].moves[0], 1)
        # make sure all stat modifiers were set to 0.2
        for stat in observations[p2_obs].stat_mod:
            self.assertAlmostEqual(stat, 0.2, 2)

        # reset observations
        for i in range(6):
            observations[i] = LoadObservation.LoadObservation(obs_type, moves, stats)
        
        # test that team stat mods and user_dmg work correctly
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[1], 0)
        self.assertAlmostEqual(observations[0].stat_mod[1], 0.2, 2)
        self.assertAlmostEqual(observations[1].stat_mod[1], 0.2, 2)
        self.assertAlmostEqual(observations[2].stat_mod[1], 0.2, 2)
        self.assertAlmostEqual(observations[0].stat_mod[2], 0.2, 2)
        self.assertAlmostEqual(observations[1].stat_mod[2], 0.2, 2)
        self.assertAlmostEqual(observations[2].stat_mod[2], 0.2, 2)
        self.assertTrue(observations[0].stats[0] <= 0)

        # test that team stat mods and user_dmg work correctly for opponent
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p2_obs].moves[1], 1)
        self.assertAlmostEqual(observations[3].stat_mod[1], 0.2, 2)
        self.assertAlmostEqual(observations[4].stat_mod[1], 0.2, 2)
        self.assertAlmostEqual(observations[5].stat_mod[1], 0.2, 2)
        self.assertAlmostEqual(observations[3].stat_mod[2], 0.2, 2)
        self.assertAlmostEqual(observations[4].stat_mod[2], 0.2, 2)
        self.assertAlmostEqual(observations[5].stat_mod[2], 0.2, 2)
        self.assertTrue(observations[3].stats[0] <= 0)

        # reset observations
        for i in range(6):
            observations[i] = LoadObservation.LoadObservation(obs_type, moves, stats)

        # test that lowering opponent's stats works correctly
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[2], 0)
        for stat in observations[p2_obs].stat_mod:
            self.assertAlmostEqual(stat, -0.1, 2)
        # test that stats cannot go below -0.5 * base stat
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[2], 0)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[2], 0)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[2], 0)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[2], 0)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[2], 0)
        for stat in observations[p2_obs].stat_mod:
            self.assertAlmostEqual(stat, -0.5, 2)

        # test that lowering user's stats works correctly
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p2_obs].moves[2], 1)
        for stat in observations[p1_obs].stat_mod:
            self.assertAlmostEqual(stat, -0.1, 2)
        # test that stats cannot go below -0.5 * base stat
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p2_obs].moves[2], 1)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p2_obs].moves[2], 1)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p2_obs].moves[2], 1)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p2_obs].moves[2], 1)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p2_obs].moves[2], 1)
        for stat in observations[p1_obs].stat_mod:
            self.assertAlmostEqual(stat, -0.5, 2)

        # test no retreat
        self.assertEqual(observations[p1_obs].retreat, 1)
        self.assertEqual(observations[p2_obs].retreat, 1)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p1_obs].moves[3], 0)
        BattleEffects.additional_effects(observations, p1_obs, p2_obs, observations[p2_obs].moves[3], 1)
        self.assertEqual(observations[p1_obs].retreat, 0)
        self.assertEqual(observations[p2_obs].retreat, 0)