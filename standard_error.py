import numpy as np
import random
import plotly.express as px
import pandas as pd
import os


# Height example
class HeightPopulation:
    """
    We examine statistical concepts based on the height value in cm of a population.
    """

    def __init__(self,n:int):
        self.set_samples(n)
        self.set_descriptive_stats()


    def get_samples(self):
        return self._samples

    def set_samples(self,n:int):
        self._samples = list(map(lambda x: random.randint(150,190),range(0,n)))

    def set_descriptive_stats(self):
        self.mean = np.mean(self.get_samples())
        self.stdev= np.std(self.get_samples())

    def get_normalized_samples(self):
        return list(map(lambda x: (x-self.mean)/self.stdev,self.get_samples()))

    def get_pdf(self):
        return list(map(lambda x: 1/ (np.sqrt(2*np.pi) * self.stdev) * np.exp(-(x-self.mean) **2 / (2*self.stdev**2)),self.get_samples()))

    def get_value_dataframe(self):
        base = pd.DataFrame([self.get_samples(),self.get_normalized_samples(),self.get_pdf()]).T
        base.columns = ["height","z","p"]
        return base



example = HeightPopulation(300)
fig = px.scatter(data_frame=example.get_value_dataframe(),x="z",y="p")

with open("test.png","wb") as writer:
    writer.write(fig.to_image(format="png"))

os.system("open ./test.png")
