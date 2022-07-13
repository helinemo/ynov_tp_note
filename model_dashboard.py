import streamlit as st 
import joblib

@st.cache
def load_model():
    return joblib.load('regression.joblib')


st.title('Prédiction de prix de maison')

taille = st.number_input("Taille maison",
                         step=1 #permet de mettre en integer
                        )

nb_rooms = st.number_input("Nombre de chambre",
                            step=1 #permet de mettre en integer
                        )

garden = st.number_input("Y a un jardin",
                            step=1 #permet de mettre en integer
                        )

model = load_model()

if taille <= 0:
    st.write('mettre taille correcte')
if nb_rooms <= 0:
    st.write("mettre nombre de chambre correct")

if taille > 0 and nb_rooms > 0:
    
    X = [[
        taille,
        nb_rooms,
        garden # Remplacement de -3 par garden
    ]]
    prediction = model.predict(X)

    ## afficher la prediction
    st.write("le prix de la maison est : {}". format(int(prediction[0])))

