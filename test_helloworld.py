import pytest
from helloworld import add, divise  # Importer les fonctions à tester

def test_add():
        """Test de la fonction add()"""
        # Tests avec des cas normaux
        assert add(10, 2) == 12       # Test normal (10 + 2 = 12)
        assert add(-1, 1) == 0        # Test avec des nombres négatifs (-1 + 1 = 0)
        assert add(0, 0) == 0        # Test avec zéro (0 + 0 = 0)
        assert add(1.5, 2.5) == 4  # Test avec des nombres à virgule (1.5 + 2.5 = 4.0)

def test_divise():
        """Test de la fonction divise()"""
        # Tests avec des cas normaux
        assert divise(10, 2) == 5.0   # Test normal (10 / 2 = 5.0)
        assert divise(20, 4) == 5    # Test normal (20 / 4 = 5.0)
        assert divise(5, 2) == 2.5    # Test avec des nombres à virgule (5 / 2 = 2.5)

        # Tests avec des erreurs
        with pytest.raises(ValueError):
            divise(10, 0)  # Test division par zéro

