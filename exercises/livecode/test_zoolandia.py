import unittest
import zoolandia

class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def test_animal_creation(self):
        bob = zoolandia.Betta("orange","Bob")

        self.assertEqual(bob.color, "orange")
        self.assertEqual(bob, "Bob")
        self.assertIsInstance(a_animal.species, zoolandia.BettaTrifasciata)

class TestSpecies(unittest.TestCase):

    def test_commonname_empty_string_default(self):
        species = zoolandia.Species()
        self.assertEqual(species.common_name, "")

    def test_georegion_empty_string_default(self):
        species = zoolandia.Species()
        self.assertEqual(species.geo_region, "")

class TestHabitat(unittest.TestCase):

    def test_name_empty_string_default(self):
        habitat = zoolandia.Habitat()
        self.assertEqual(habitat.name, "")

    def test_members_default(self):
        habitat = zoolandia.Habitat()
        self.assertIsInstance(habitat.members, set)

    def test_add_member(self):
        habitat = zoolandia.Habitat()
        bob = zoolandia.Habitat("orange","Bob")
        aquarium.add_member(bob)

        self.assertIn(bob, aquarium.members)

class TestWalking(unittest.TestCase):
    def test_legs_zero_default(self):
        walking = zoolandia.Walking()
        self.assertEqual(walking.legs, 0)

    def test_walk_speed_zero_default(self):
        walking = zoolandia.Walking()
        self.assertEqual(walking.walk_speed, 0)

class TestSwimming(unittest.TestCase):
    def test_appendages(self):
        swimming= zoolandia.Swimming()
        self.assertEqual(swimming.fins, False)
        self.assertEqual(swimming.flippers, False)
        self.assertEqual(swimming.web_feet, False)

    def swim_speed_zero_default(self):
        swimming = zoolandia.Species()
        self.assertEqual(swimming.species, "")

class TestFlying(unittest.TestCase):

    def test_wings_zero_default(self):
        flying = zoolandia.Flying()
        self.assertEqual(flying.wings, 0)

    def swim_speed_zero_default(self):
        swimming = zoolandia.Species()
        self.assertEqual(swimming.species, "")

if __name__ == '__main__':  # this enables tests to run
    unittest.main()
