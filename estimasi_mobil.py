import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil_toyota_webOTO.sav', 'rb'))

# title
st.title('Estimasi Harga Mobil Bekas')

# input
year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
cc = st.number_input('Input CC mesin')

# predict
predict = ''

if st.button('Estimasi Harga'):
  predict = model.predict(
    [[year, mileage, tax, cc]]
  )
  
st.write ('Estimasi Harga Mobil Bekas Dalam Rupiah IDR (Juta) : ', predict)
st.write ('NOTE : angka dibelakang (.) tidak dianggap')