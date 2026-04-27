import PR0.asigna as asigna
import PR1.edadPR as programa  # <-- Esta línea es vital

def test_valores():
    assert asigna.a == 1
    assert asigna.b == 2

def test_variable_edad():
    # El assert tiene que estar "dentro" de la función (con espacio)
    assert hasattr(programa, 'edad')