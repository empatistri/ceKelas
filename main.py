import streamlit as st

# settings logo
st.logo('assets/images/logo-saizu.jpg')

st.title("ceKelas")
st.markdown("Daftar kelas yang sedang/sudah dijadwalkan dipakai.")

import pandas as pd
import numpy as np

df = pd.read_csv('assets/documents/data-kelas.csv')

st.table(df)