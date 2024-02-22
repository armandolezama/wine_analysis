import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class Graphics_manager:
  def __init__(self) -> None:
    print('hi from graphics module')
    self.axes_graphics = {}

  def create_heat_map(self, corr_table, use_mask = False):
    mask = np.triu(np.ones_like(corr_table, dtype=bool)) if use_mask else None

    sns.heatmap(data=corr_table, mask=mask)