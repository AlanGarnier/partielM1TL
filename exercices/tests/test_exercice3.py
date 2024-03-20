import unittest
from unittest.mock import MagicMock

inventory = {"apples": 30, "bananas": 15, "oranges": 10}


def update_inventory(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity


class MyTestInventory(unittest.TestCase):
    def test_update_inventory(self):
        # On copie de l'inventaire existant
        inventory_copy = inventory.copy()

        # Mock de la fonction update_inventory
        update_inventory_mock = MagicMock(side_effect=update_inventory)

        with unittest.mock.patch(
            "__main__.update_inventory", update_inventory_mock
        ):
            update_inventory("bananas", -2)  # Ajouter 2 oranges
            update_inventory_mock.assert_called_once_with("bananas", -2)

            # On vérifie que l'inventaire n'a pas été modifié
            self.assertEqual(inventory, inventory_copy)


if __name__ == "__main__":
    unittest.main()
