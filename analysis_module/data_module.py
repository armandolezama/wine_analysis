import pandas as pd
import numpy as np

class Data_manager:
  def __init__(self) -> None:
    print('hi from data module')
    self.colnames = [
      'wine_class',
      'alcohol',
      'malic_acid',
      'ash',
      'ash_alcalinity',
      'magnesium',
      'total_phenols',
      'flavanoids',
      'nonflavanoids_phenols',
      'proanthocyanins',
      'color_intensity',
      'hue',
      'OD280_OD315',
      'proline',
    ]

    self.wine_colnames=[
    'wine_class',
    'alcohol',
    'malic_acid',
    'ash',
    'ash_alcalinity',
    'magnesium',
    'total_phenols',
    'flavanoids',
    'nonflavanoids_phenols',
    'proanthocyanins',
    'color_intensity',
    'hue',
    'OD280_OD315',
    'proline',
    ]

    self.wine_data = pd.read_csv('./data/wine.data', sep=',', names=self.wine_colnames)

    self.wine_X = self.wine_data.iloc[:, 1:]

    self.wine_y = self.wine_data.wine_class

    self.transformed_data = {}


  def save_transformed_data(self, data_name, transformed_data):
    self.transformed_data[data_name] = transformed_data

  def get_transformed_data(self, data_name):
    return self.transformed_data[data_name]
