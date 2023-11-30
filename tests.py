"""
Calificación del laboratorio
-----------------------------------------------------------------------------------------
"""

import sys

import preguntas


def test_01():
    """
    ---< Input/Output test case >----------------------------------------------------
    Pregunta 01
    pip3 install scikit-learn pandas numpy
    python3 tests.py 01
    """

    x_data, y_data = preguntas.pregunta_01()

    assert x_data.shape == (1000, 20)
    assert y_data.shape == (1000,)
    assert "default" not in x_data.columns


def test_02():
    """
    ---< Input/Output test case >----------------------------------------------------
    Pregunta 02
    pip3 install scikit-learn pandas numpy
    python3 tests.py 02
    """

    x_train, x_test, y_train, y_test = preguntas.pregunta_02()

    assert y_train.value_counts().to_dict() == {1: 634, 2: 266}
    assert y_test.value_counts().to_dict() == {1: 66, 2: 34}
    assert x_train.iloc[:, 0].value_counts().to_dict() == {
        "unknown": 368,
        "1 - 200 DM": 240,
        "< 0 DM": 233,
        "> 200 DM": 59,
    }
    assert x_test.iloc[:, 0].value_counts().to_dict() == {
        "< 0 DM": 41,
        "1 - 200 DM": 29,
        "unknown": 26,
        "> 200 DM": 4,
    }


def test_03():
    """
    ---< Run command >-----------------------------------------------------------------
    Pregunta 03
    pip3 install scikit-learn pandas numpy
    python3 tests.py 03
    """

    x_train, x_test, y_train, y_test = preguntas.pregunta_02()
    pipeline = preguntas.pregunta_03()

    assert pipeline.score(x_train, y_train).round(4) == 0.7133
    assert pipeline.score(x_test, y_test).round(4) == 0.7000


def test_04():
    """
    ---< Run command >--------------------------------------------------------------------
    Pregunta 04
    pip3 install scikit-learn pandas numpy
    python3 tests.py 04
    """

    cfm_train, cfm_test = preguntas.pregunta_04()

    assert cfm_train.tolist() == [[626, 8], [250, 16]]
    assert cfm_test.tolist() == [[66, 0], [30, 4]]


test = {
    "01": test_01,
    "02": test_02,
    "03": test_03,
    "04": test_04,
}[sys.argv[1]]

test()
