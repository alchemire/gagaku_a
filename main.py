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
music_times = [444, 319, 332, 1046, 4, 5, 6, 133, 8, 9, 221, 11, 298, 549, 14, 401, 168, 17, 223, 19, 330, 417, 224, 23, 1156, 165, 523, 598, 694, 29, 85, 371, 32, 255, 657, 35, 216, 37, 674, 39, 485, 313, 42, 447, 301, 45, 288, 600, 343]
music_titles = ["Toccata_Emerson, Lake & Palmer", "津軽総合独奏曲_高橋竹山" ,"It Was A Camel_Jah Wobble Holger Czukay", "秋庭歌_武満徹", "4", "5", "6", "Rumba Mama_Weather Report", "8", "9", "Biassy_Florence Foster Jenkins", "11", "陪臚_東儀秀樹", "参音声_武満徹", "14", "退出音声_武満徹", "New Orleans_Emerson, Lake & Palmer", "17", "Romeo and Juliet_Emerson, Lake & Palmer", "19", "Goodbye Pork Pie Hat_Jeff Beck", "三味線よされ（旧節）_高橋竹山", "Die Zauberflöte, K 620_Florence Foster Jenkins", "23",  "Mandala_佐藤聰明", "外山節_高橋竹山", "しおさい Tidal sound_吉村七重", "Taqsim_吉村七重", "越天楽_東儀秀樹", "29", "Like A Bird_Florence Foster Jenkins", "Kafari_Sigur Rós", "32", "納曽利急_東儀秀樹", "Madagascar_Weather Report", "35", "津軽よされ節（旧節）_高橋竹山", "37", "森よ Ode to forest_吉村七重", "39", "二星_東儀秀樹", "双魚譜 緩の魚 Largo_吉村七重", "42", "塩梅_武満徹", "双魚譜 急の魚 Finale/Presto_吉村七重", "45", "吹渡_武満徹", "Hafsól_Sigur Rós", "Cause We've Ended As Lovers_Jeff Beck"]
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
# st.markdown("# :rainbow[曼荼羅プレイリスト]")
# col1, col2 = st.columns([2, 1], vertical_alignment="center")
# col1.write(df)
# col2.image("picture/座標図.png")
st.image("picture/座標図5.png")
# st.snow()

# def play_audio(file_path):
#     st.audio(file_path, format="audio/mp3", start_time=0, autoplay=True)
#     time.sleep(1)

# 追加
# def play_audio_with_delay(file_path, delay):
#     time.sleep(delay)
#     play_audio(file_path)
    
played_tracks = set()
x_new, y_new = None, None
def main():
    with st.form("your-form"):
        st.sidebar.title("≫ 曲を選ぶ")
        column = st.sidebar.slider("よこ ⇄", -3, 3, 0)
        row = st.sidebar.slider("たて ⇅", -3, 3, 0)
        theta = st.sidebar.slider("回転 ↺", 0, 360, 180)
        play = st.sidebar.slider("曲数 ", 1, 25, 1)
        st.sidebar.text("※一時停止禁止")
        submitted = st.form_submit_button("▷再生")
        st.divider()
        st.text("49曲収録")
    
    if submitted:
        current_track_index = df.loc[str(row), str(column)]
        st.title(f"{sorted_file_names[current_track_index]} - {music_titles[current_track_index]}")
        audio_player = st.audio(sorted_mp3_files[current_track_index], format="audio/mp3", start_time=0, autoplay=True)
        time.sleep(music_times[current_track_index] + 1)
        # x_new, y_new = rotate_point(row, column, math.radians(theta))
        def rotation():
            global x_new, y_new
            if x_new is None:
                x_new, y_new = rotate_point(row, column, math.radians(theta))
            else:
                x_new, y_new = rotate_point(x_new, y_new, math.radians(theta))

        for _ in range(play - 1):
            rotation()
            if x_new is not None and y_new is not None:
                current_track_index = df.loc[str(x_new), str(y_new)]

                if current_track_index in played_tracks:
                    continue
                played_tracks.add(current_track_index)
                st.title(f"{sorted_file_names[current_track_index]} - {music_titles[current_track_index]}")
                audio_player = st.audio(sorted_mp3_files[current_track_index], format="audio/mp3", start_time=0, autoplay=True)
                time.sleep(music_times[current_track_index] + 1)
                # audio_player.empty()
            # 追加
            # Thread(target=play_audio_with_delay, args=(sorted_mp3_files[current_track_index], music_times[current_track_index])).start()
            # play_audio(sorted_mp3_files[current_track_index])
            

if __name__ == "__main__":
    main()

st.divider()

st.write("2024年10月14日 周人＆純果")

st.link_button("座標と音楽の対応", "https://docs.google.com/spreadsheets/d/1PVXAy3g0UL_5wuauGQojs6qWCzOWpXFWWL6Rp_cI0ao/edit?gid=0#gid=0")