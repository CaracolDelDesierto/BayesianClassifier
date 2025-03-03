class BayesianClassifier:
  def __init__():
    pass

def fit(self, training_data, data_type):
  """
  ***Description***

  :params:
  training_data : Pandas.DataFrame
  A DataFrame containing the data that the classifier will use to learn the classes.

  data_type : dict
  A dictionary whose length has to be the same as the attributes vector of the training dataframe (the number of columns minus one). It indicates wether the data of a column is "continous", "integer" or "categoric".
  """

  """
  TODO :
  Las probabilidades a priori de cada clase en Y. Es decir, P(Y=y_i)

  Las funciones de masa o densidad de probabilidad condicionales p(X_j = x | Y = y_i), para cada j=1,...,L y y_i para i=1,...,M, donde L es la dimensión de los datos y M el número de clases.

  Para las variables categóricas debe usar la distribución Bernoulli (o en general distribución categórica).

  Para las variables enteras calcular la media y estimar el pdf de una distribución Poisson.

  Para las variables continuas calcular la media y la varianza de los datos para estimar el pdf de la normal, o estimar el KDE, de acuerdo con el parámetro de la clase.

  """
  pass

def predict(self, x_pred):
  """
  ***Description***

  :params:
  x_pred : list / array / Pandas.Series
  An object that will contain the attributes vector of a pattern.

  :return:
  class : ????
  The class with the greatest likelihood according to the Naive Bayes Classifier.
  """

  """
  TODO
  Recibir un vector X_pred que debe tener el mismo número de columnas que X.

  Calcular el clasificador bayesiano ingenuo \PI_{j=1}^L p(X_j=x_j | Y=y_i)P(Y=y_i) para cada clase i=1,...,M y devolver el valor de y_i que lo maximiza.
  """
  pass
