def add(a, b):
    """Additionne deux nombres."""
    return a + b

def divise(a, b):
    """Effectue la division de a par b."""
    # Essayer de diviser a par b
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

# Exemple d'utilisation
try:
    x = 10
    y = 5
    print(f"L'addition de {x} et {y} donne: {add(x, y)}")
    
    # Test de la division
    print(f"La division de {x} par {y} donne: {divise(x, y)}")
    
    # Essayer une division par zéro
    z = 0
    print(f"La division de {x} par {z} donne: {divise(x, z)}")

except ValueError as e:
    print(f"Erreur: {e}")


  

