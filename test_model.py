
import streamlit as st 
import joblib

@st.cache
def load_model():
    return joblib.load('regression.joblib')




# Tests pour vérifier la valeur du prix de la maison
def test_prix():

  # Défintion des limites de notre prix
  prix_min = [5000]
  prix_max = [300000]

  # Chargement du modèle
  model = load_model()
  
  # Défintion de nos valeurs (taille de la maison, nombre de chambre, présence d'un jardin ou non)
  X = [[100, 3, 1]]

  # Prédiction du prix de la maison
  pred = model.predict(X)

  #Vérification de la cohérence du prix de la maison
  assert pred[0] > prix_min and  pred[0] < prix_max, "La valeur du prix de la maison semble incorrect"





# Tests pour vérifier la surface de la maison et le nombre de chambre > 0
def test_surface () :
  # Chargement du modèle
  model = load_model()
  
  # Défintion de nos valeurs (taille de la maison, nombre de chambre, présence d'un jardin ou non)
  X = [[-100, -3, 1]]

  # Prédiction du prix de la maison
  pred = model.predict(X)

  #Vérification de la cohérence du prix de la maison
  assert X[0][0] > 0 , "La surface de la maison doit être suéprieure à 0"
  assert X[0][1] > 0 , "Le nombre de chambres doit être supérieure à 0"
