import PR0.asigna as asigna
import PR1.edadPR as programa
import PR1.aceleracionPR as pro_ace

def test_valores():
    assert asigna.a == 1
    assert asigna.b == 2

def test_variable_edad():
    assert hasattr(programa, 'edad')

def test_variable_aceleracion():
    assert hasattr(pro_ace, 'aceleracion')