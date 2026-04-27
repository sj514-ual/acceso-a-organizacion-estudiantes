import PR0.asigna as asigna
import PR1.edadPR as programa_edad
import PR1.aceleracionPR as pro_ace
import PR1.enordenPR as programa_orden

def test_valores():
    assert asigna.a == 1
    assert asigna.b == 2

def test_variable_edad():
    assert hasattr(programa_edad, 'edad')

def test_variable_aceleracion():
    assert hasattr(pro_ace, 'aceleracion')

def test_variable_orden():
    # Solo verificamos que el archivo existe y tiene la variable
    assert hasattr(programa_orden, 'en_orden')