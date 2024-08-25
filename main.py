import streamlit as st
import pandas as pd
import os
import glob
import math
import time
import re


def rotate_point(x, y, theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    x_new = x * cos_theta + y * sin_theta
    y_new = -x * sin_theta + y * cos_theta

    x_new_round = round(x_new)
    y_new_round = round(y_new)

    x_new_clipped = max(-3, min(3, x_new_round))
    y_new_clipped = max(-3, min(3, y_new_round))

    return x_new_clipped, y_new_clipped

folder_path = "music"
mp3_files = glob.glob(os.path.join(folder_path, '*.mp3'))
sorted_mp3_files = sorted(mp3_files, key=lambda x: int(os.path.basename(x).split('.')[0]))
file_names =[os.path.splitext(os.path.basename(file))[0] for file in mp3_files]
sorted_file_names = sorted(file_names, key=lambda x: int(os.path.basename(x).split('.')[0]))
music_times = [4, 4, 5, 6, 2, 4, 9, 4, 4, 5, 6, 2, 4, 9, 10, 10, 10, 10, 2, 4, 9, 4, 4, 5, 6, 2, 4, 9, 4, 4, 5, 6, 2, 4, 9, 4, 4, 5, 6, 2, 4, 9, 4, 4, 5, 6, 2, 4, 9]

data = {
    "-3":[0, 1, 2, 3, 4, 5, 6],
    "-2":[7, 8, 9, 10, 11 ,12 ,13],
    "-1":[14, 15, 16, 17, 18, 19, 20],
    "0":[21, 22, 23, 24, 25, 26, 27],
    "1":[28, 29, 30, 31, 32, 33, 34],
    "2":[35, 36, 37, 38, 39, 40, 41],
    "3":[42, 43, 44, 45, 46, 47, 48],
}

df = pd.DataFrame(data, index=["3", "2", "1", "0", "-1", "-2", "-3"])
st.markdown("# :rainbow[曼荼羅プレイリスト]")
col1, col2 = st.columns([2, 1], vertical_alignment="center")
col1.write(df)
col2.image("picture/曼荼羅.jpg")
st.snow()

def play_audio(file_path):
    st.audio(file_path, format="audio/mp3", start_time=0, autoplay=True)
    time.sleep(1)

played_tracks = set()

def main():
    with st.form("your-form"):
        column = st.slider("曲の[ 複雑さ ]←  →[ 単純さ ]（横軸の値を指定）", -3, 3, -1)
        row = st.slider("テンポの[ 遅さ ]←  →[ 速さ ]（縦軸の値を指定）", -3, 3, -1)
        theta = st.slider("反時計回りで回転（数字の値だけ〇度回転）", 0, 360, 90)
        play = st.slider("曲数（1曲平均5分）", 0, 25, 5)
        submitted = st.form_submit_button("開始")
        st.text("※一度動き出したら止まりません　※同じ曲に戻ったら止まります")
    if submitted:
        current_track_index = df.loc[str(row), str(column)]
        played_tracks.add(current_track_index)
        st.title(sorted_file_names[current_track_index])
        play_audio(sorted_mp3_files[current_track_index])
        x_new, y_new = rotate_point(row, column, math.radians(theta))

        for _ in range(play-1):
            current_track_index = df.loc[str(x_new), str(y_new)]
            if current_track_index in played_tracks:
                continue
            played_tracks.add(current_track_index)
            time.sleep(music_times[current_track_index])
            st.title(sorted_file_names[current_track_index])
            play_audio(sorted_mp3_files[current_track_index])
            x_new, y_new = rotate_point(x_new, y_new, math.radians(theta))

if __name__ == "__main__":
    main()

st.divider()

st.write("2024年10月14日 周人＆純果")

st.link_button("座標と音楽の対応", "https://docs.google.com/spreadsheets/d/1PVXAy3g0UL_5wuauGQojs6qWCzOWpXFWWL6Rp_cI0ao/edit?gid=0#gid=0")