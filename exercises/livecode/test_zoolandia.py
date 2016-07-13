import unittest
import zoolandia

class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def test_animal_creation(self):
        bob = zoolandia.Betta("orange", "Bob")
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(bob.species.color, "orange")
        self.assertIsInstance(bob, zoolandia.Animal)
        self.assertIsInstance(bob.species, zoolandia.BettaTrifasciata)

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
        aquarium = zoolandia.Aquarium("freshwater")
        bob = zoolandia.Betta("orange","Bob")
        james= zoolandia.Betta("blue", "James")

        aquarium.add_member(bob)
        self.assertIn(bob, aquarium.members)

        aquarium.add_member(james)
        self.assertIn(bob, aquarium.members)
        self.assertIn(james, aquarium.members)

    def test_remove_member(self):
        james= zoolandia.Betta("blue", "James")
        aquarium = zoolandia.Aquarium("freshwater")

        aquarium.add_member(james)
        aquarium.remove_member(james)
        self.assertNotIn(james, aquarium.members)

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
        swimming = zoolandia.Swimming()
        self.assertEqual(swimming.swim_speed, 0)

class TestFlying(unittest.TestCase):

    def test_wings_zero_default(self):
        flying = zoolandia.Flying()
        self.assertEqual(flying.wings, 0)

    def wingspan_zero_default(self):
        flying = zoolandia.Flying()
        self.assertEqual(flying.wing_span, 0)

    def walk_speed_zero_default(self):
        flying = zoolandia.Flying()
        self.assertEqual(flying.air_speed, 0)

if __name__ == '__main__':  # this enables tests to run
    unittest.main()
