# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for edgar_toolbox Project
"""

from os.path import split
import pandas as pd
import datetime
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

pd.set_option('display.width', 200)


def get_data():
    """ get data from sklearn
    """
    faces = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
    return faces

def data_projection(faces):
    pca = PCA(n_components=150)
    data_projected = pca.fit_transform(faces.data)
    return data_projected

if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import edgar_toolbox
    folder_source, _ = split(edgar_toolbox.__file__)
    faces = get_data()
    data_projected = data_projection(faces)
    print(' dataframe extracted')
