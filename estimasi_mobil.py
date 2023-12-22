import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil_toyota_webOTO.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
cc = st.number_input('Input CC mesin')
#seat = st.number_input('muatan kursi mobil')
# mpg = st.number_input('Kebutuhan rata-rata bahan bakar dalam satuan mpg')

predict = ''

if st.button('Estimasi Harga'):
  predict = model.predict(
    [[year, mileage, tax, cc]]
  )
  
st.write ('Estimasi Harga Mobil Bekas Dalam Rupiah IDR (Juta) : ', predict)
st.write ('NOTE : angka dibelakang (.) tidak dianggap')
#st.write ('Estimasi Harga Mobil Bekas Dalam Rupiah (IDR) : ', predict*19625)
