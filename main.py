import streamlit as st
import pandas as pd
import os
import glob

st.title("BLOW BY BLOW")
st.write("You Know What I Mean")

folder_path =  "music"
mp3_files = glob.glob(os.path.join(folder_path, '*.mp3'))

data = [
    [0, 1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10 ,11 ,12 ,13],
    [14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27],
    [28, 29, 30, 31, 32, 33, 34],
    [35, 36, 37, 38, 39, 40, 41],
    [42, 43, 44, 45, 46, 47, 48],
]

df = pd.DataFrame(data)

with st.form("my-form"):
    row = st.slider("ピコ[テンポ遅め]← →[テンポ早め]", -3, 3, 0)
    column = st.slider("パコ[複雑、内省的]← →[単純、愉快]", -3, 3, 0)

    submitted = st.form_submit_button("ピ！")
if submitted: 
    st.audio(mp3_files[(df.iloc[row, column])], format="audio/mpeg", autoplay=True)


st.write("2024年10月14日 周人＆純果")

st.link_button("座標と音楽の対応", "https://docs.google.com/spreadsheets/d/1PVXAy3g0UL_5wuauGQojs6qWCzOWpXFWWL6Rp_cI0ao/edit?gid=0#gid=0")