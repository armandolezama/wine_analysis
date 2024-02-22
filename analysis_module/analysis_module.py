import seaborn as sns
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA


class Analyzer_module:
  def __init__(self) -> None:
    print('hi from analyzer')

  def normalize_data(self, data_to_transform: pd.DataFrame):
    self.set_scaler()
    return self.scaler.fit_transform(data_to_transform)

  def set_scaler(self):
    self.scaler = preprocessing.StandardScaler()