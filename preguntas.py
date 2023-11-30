"""
Clasificación de Créditos Riesgosos usando SVM
-----------------------------------------------------------------------------------------

Construya un modelo de clasificación que permita determinar si un crédito es riesgoso
o no.

Las entidades financieras desean mejorar sus procedimientos de aprobación de créditos con
el fin de disminuir los riesgos de no pago de la deuda, lo que acarrea pérdidas a la 
entidad. El problema real consiste en poder decidir si se aprueba o no un crédito 
particular con base en información que puede ser fácilmente recolectada por teléfono o en
la web. Se tiene una muestra de 1000 observaciones. Cada registro contiene 20 atributos
que recopilan información tanto sobre el crédito como sobre la salud financiera del 
solicitante. Construya un sistema de recomendación que use máquinas de vectores de 
soporte.

Los atributos y sus valores son los siguientes:

     Attribute 1:  (qualitative)
     	      Status of existing checking account
     	      A11 :      ... <    0 DM
     	      A12 : 0 <= ... <  200 DM
     	      A13 :      ... >= 200 DM /
     	            salary assignments for at least 1 year
     	      A14 : no checking account

     Attribute 2:  (numerical)
     	      Duration in month

     Attribute 3:  (qualitative)
     	      Credit history
     	      A30 : no credits taken/
     	            all credits paid back duly
     	      A31 : all credits at this bank paid back duly
     	      A32 : existing credits paid back duly till now
     	      A33 : delay in paying off in the past
     	      A34 : critical account/
     	            other credits existing (not at this bank)

     Attribute 4:  (qualitative)
     	      Purpose
     	      A40 : car (new)
     	      A41 : car (used)
     	      A42 : furniture/equipment
     	      A43 : radio/television
     	      A44 : domestic appliances
     	      A45 : repairs
     	      A46 : education
     	      A47 : (vacation - does not exist?)
     	      A48 : retraining
     	      A49 : business
     	      A410 : others

     Attribute 5:  (numerical)
     	      Credit amount

     Attribute 6:  (qualitative)
     	      Savings account/bonds
     	      A61 :          ... <  100 DM
     	      A62 :   100 <= ... <  500 DM
     	      A63 :   500 <= ... < 1000 DM
     	      A64 :          .. >= 1000 DM
     	      A65 :   unknown/ no savings account

     Attribute 7:  (qualitative)
     	      Present employment since
     	      A71 : unemployed
     	      A72 :       ... < 1 year
     	      A73 : 1  <= ... < 4 years  
     	      A74 : 4  <= ... < 7 years
     	      A75 :       .. >= 7 years

     Attribute 8:  (numerical)
     	      Installment rate in percentage of disposable income

     Attribute 9:  (qualitative)
     	      Personal status and sex
     	      A91 : male   : divorced/separated
     	      A92 : female : divorced/separated/married
     	      A93 : male   : single
     	      A94 : male   : married/widowed
     	      A95 : female : single

     Attribute 10: (qualitative)
     	      Other debtors / guarantors
     	      A101 : none
     	      A102 : co-applicant
     	      A103 : guarantor

     Attribute 11: (numerical)
     	      Present residence since

     Attribute 12: (qualitative)
     	      Property
     	      A121 : real estate
     	      A122 : if not A121 : building society savings agreement/
     				   life insurance
     	      A123 : if not A121/A122 : car or other, not in attribute 6
     	      A124 : unknown / no property

     Attribute 13: (numerical)
     	      Age in years

     Attribute 14: (qualitative)
     	      Other installment plans 
     	      A141 : bank
     	      A142 : stores
     	      A143 : none

     Attribute 15: (qualitative)
     	      Housing
     	      A151 : rent
     	      A152 : own
     	      A153 : for free

     Attribute 16: (numerical)
              Number of existing credits at this bank

     Attribute 17: (qualitative)
     	      Job
     	      A171 : unemployed/ unskilled  - non-resident
     	      A172 : unskilled - resident
     	      A173 : skilled employee / official
     	      A174 : management/ self-employed/
     		         highly qualified employee/ officer

     Attribute 18: (numerical)
     	      Number of people being liable to provide maintenance for

     Attribute 19: (qualitative)
     	      Telephone
     	      A191 : none
     	      A192 : yes, registered under the customers name

     Attribute 20: (qualitative)
     	      foreign worker
     	      A201 : yes
     	      A202 : no


La columna default es la variable de salida (1-pago, 2-no pago).

"""

import numpy as np
import pandas as pd
from sklearn.compose import make_column_selector


def pregunta_01():
    """
    En esta función se realiza la carga de datos.
    """
    # Lea el archivo `german.csv` y asignelo al DataFrame `df`
    df = ____

    # Asigne la columna `default` a la variable `y`.
    ____ = ____

    # Asigne una copia del dataframe `df` a la variable `X`.
    ____ = ____.____()

    # Remueva la columna `default` del DataFrame `X`.
    ____.____(____)

    # Retorne `X` y `y`
    return X, y


def pregunta_02():
    """
    Preparación del dataset.
    """

    # Importe train_test_split
    from ____ import ____

    # Cargue los datos de ejemplo y asigne los resultados a `X` y `y`.
    X, y = pregunta_01()

    # Divida los datos de entrenamiento y prueba. La semilla del generador de números
    # aleatorios es 123. Use 100 patrones para la muestra de prueba.
    (X_train, X_test, y_train, y_test,) = ____(
        ____,
        ____,
        test_size=____,
        random_state=____,
    )

    # Retorne `X_train`, `X_test`, `y_train` y `y_test`
    return X_train, X_test, y_train, y_test


def pregunta_03():
    """
    Especificación y entrenamiento del modelo.
    """

    # Importe ColumnTransformer
    # Importe SVC
    # Importe OneHotEncoder
    # Importe Pipeline
    from ____ import ____

    # Cargue las variables.
    X_train, _, y_train, _ = pregunta_02()

    # Cree un objeto ColumnTransformer que aplique OneHotEncoder a las columnas
    # tipo texto. Use make_column_selector para seleccionar las columnas. Las
    # columnas numéricas no deben ser transformadas.
    columnTransformer = make_column_transformer(
        (
            ____(),
            ____(____=____),
        ),
        remainder=____,
    )

    # Cree un pipeline que contenga el columnTransformer y el modelo SVC.
    pipeline = ____(
        steps=[
            ("____", ____),
            ("____", ____),
        ],
    )

    # Entrene el pipeline con los datos de entrenamiento.
    ____.____(____, ____)

    # # Retorne el pipeline entrenado
    return pipeline


def pregunta_04():
    """
    Evalue el modelo obtenido.
    """

    # Importe confusion_matrix
    from ____ import ____

    # Obtenga el pipeline de la pregunta 3.
    pipeline = pregunta_03()

    # Cargue las variables.
    X_train, X_test, y_train, y_test = pregunta_02()

    # Evalúe el pipeline con los datos de entrenamiento usando la matriz de confusion.
    cfm_train = ____(
        y_true=____,
        y_pred=____.____(____),
    )

    cfm_test = ____(
        y_true=____,
        y_pred=____.____(____),
    )

    # Retorne la matriz de confusion de entrenamiento y prueba
    return cfm_train, cfm_test
