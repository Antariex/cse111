from pytest import approx
import pytest

from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction


def test_water_column_height_1():
    result = water_column_height(0, 0)
    assert result == 0

def test_water_column_height_2():
    result = water_column_height(0, 10)
    assert result == 7.5

def test_water_column_height_3():
    result = water_column_height(25, 0)
    assert result == 25

def test_water_column_height_4():
    result = water_column_height(48.3, 12.8)
    assert result == 57.9


def test_pressure_gain_from_water_height():
    result = pressure_gain_from_water_height(0)
    assert result == approx(0, abs=0.001)

    result = pressure_gain_from_water_height(30.2)
    assert result == approx(295.628, abs=0.001)

    result = pressure_gain_from_water_height(50)
    assert result == approx(489.450, abs=0.001)
    
    
def test_pressure_loss_from_pipe():
    result = pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75)
    assert result == approx(0, abs=0.001)

    result = pressure_loss_from_pipe(0.048692, 200, 0, 1.75)
    assert result == approx(0, abs=0.001)

    result = pressure_loss_from_pipe(0.048692, 200, 0.018, 0)
    assert result == approx(0, abs=0.001)

    result = pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75)
    assert result == approx(-113.008, abs=0.001)

    result = pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65)
    assert result == approx(-100.462, abs=0.001)

    result = pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65)
    assert result == approx(-61.576, abs=0.001)

    result = pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65)
    assert result == approx(-110.884, abs=0.001)
    
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])


def test_pressure_loss_from_fittings():
    result = pressure_loss_from_fittings(0, 3)
    assert result == approx(0, abs=0.001)

    result = pressure_loss_from_fittings(1.65, 0)
    assert result == approx(0, abs=0.001)

    result = pressure_loss_from_fittings(1.65, 2)
    assert result == approx(-0.109, abs=0.001)

    result = pressure_loss_from_fittings(1.75, 2)
    assert result == approx(-0.122, abs=0.001)

    result = pressure_loss_from_fittings(1.75, 5)
    assert result == approx(-0.306, abs=0.001)
        

def test_reynolds_number():
    result = reynolds_number(0.048692, 0)
    assert result == approx(0, abs=1)

    result = reynolds_number(0.048692, 1.65)
    assert result == approx(80069, abs=1)

    result = reynolds_number(0.048692, 1.75)
    assert result == approx(84922, abs=1)

    result = reynolds_number(0.28687, 1.65)
    assert result == approx(471729, abs=1)

    result = reynolds_number(0.28687, 1.75)
    assert result == approx(500318, abs=1)
    
    
def test_pressure_loss_from_pipe_reduction():
    result = pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692)
    assert result == approx(0, abs=0.001)

    result = pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692)
    assert result == approx(-163.744, abs=0.001)

    result = pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692)
    assert result == approx(-184.182, abs=0.001)