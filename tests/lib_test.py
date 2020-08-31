# -*- coding: UTF-8 -*-

# Import from standard library
import os
import edgar_toolbox
import pandas as pd
# Import from our lib
from edgar_toolbox.lib import get_data, data_projection
import pytest


def test_get_data():
    faces = get_data()
    assert faces.images.shape == (1288, 50, 37)
    assert faces.data.shape == (1288, 1850)

def test_data_projection():
    faces = get_data()
    assert data_projection(faces)[0].shape == (1288, 150)
