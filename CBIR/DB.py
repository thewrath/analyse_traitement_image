# -*- coding: utf-8 -*-

from __future__ import print_function

import pandas as pd
import os

DB_dir = 'database'

class Database(object):

  def __init__(self, *set_names):
    self.data = {}
    self.set_names = set_names
    for set_name in set_names:
      csv_name = "data-{}.csv".format(set_name)
      set_dir = "{}/{}".format(DB_dir, set_name)
      self._gen_csv(set_dir, csv_name)
      self.data[set_name] = pd.read_csv(csv_name)

  def _gen_csv(self, set_dir, csv_name):
    if os.path.exists(csv_name):
      return
    with open(csv_name, 'w', encoding='UTF-8') as f:
      f.write("img,cls")
      for root, _, files in os.walk(set_dir, topdown=False):
        root = os.path.normpath(root)
        cls = root.split('/')[-1]
        for name in files:
          if not name.endswith('.jpg'):
            continue
          img = os.path.join(root, name)
          f.write("\n{},{}".format(img, cls))

  def __len__(self):
    return len(self.data)

  def get_class(self, set_name):
    return set(self.data[set_name]["cls"])

  def get_data(self, set_name):
    return self.data[set_name]


if __name__ == "__main__":
  db = Database("train", "validation", "test")

  # Le jeu de données d'entrainement contient forcément toute les classes connues du programme.
  print("DB length:", len(db))
  print(db.get_class("train"))
