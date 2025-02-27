import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Judul Aplikasi
st.title("📊 Dashboard Hasil Analisis")
st.subheader('Dataset Air Quality')

st.write(
    """
    Dengan dataset yang berisi kolom-kolom sebagai berikut:
    - Year, Month, Day, Hour
    - PM2.5 : Partikel udara halus ≤ 2.5 µm, berbahaya bagi kesehatan.
    - PM10 : Partikel udara ≤ 10 µm, dapat menyebabkan iritasi pernapasan.
    - SO2 : Gas dari pembakaran fosil, menyebabkan iritasi dan hujan asam.
    - NO2 : Gas dari kendaraan & industri, berbahaya bagi paru-paru.
    - CO : Gas beracun dari pembakaran tidak sempurna, dapat menyebabkan keracunan.
    - O3 : Ozon di permukaan tanah, polutan yang menyebabkan masalah pernapasan.
    - TEMP : Suhu udara dalam derajat Celsius.
    - PRES : Tekanan udara dalam hPa.
    - DEWP : Titik embun, suhu di mana udara mulai mengembun.
    - RAIN : Curah hujan dalam mm.
    - wd : Arah angin.
    - WSPM : Kecepatan angin dalam m/s.
    """
)




# Pastikan file tersedia
file_path = "main_data.csv"
if load_data(file_path):
    # Load data
    df = pd.read_csv(file_path)
    st.header("Data Preview")
    st.write(df.head())

    st.header("Visualisasi Data")
    st.subheader("Pertanyaan 1 : Apakah kecepatan angin (WSPM) berpengaruh terhadap penyebaran polusi udara?")
    # Pastikan kolom yang dibutuhkan ada
    if 'WSPM' in df.columns and 'PM2.5' in df.columns:
        # Menampilkan scatter plot
        st.write("📈 Scatter Plot: Kecepatan Angin vs Polusi Udara")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=df, x='WSPM', y='PM2.5', alpha=0.5)
        ax.set_title('Hubungan antara Kecepatan Angin (WSPM) dan Polusi Udara (PM2.5)')
        ax.set_xlabel('Kecepatan Angin (m/s)')
        ax.set_ylabel('Konsentrasi PM2.5')

        # Menampilkan plot di Streamlit
        st.pyplot(fig)
    else:
        st.error("⚠️ Kolom 'WSPM' atau 'PM2.5' tidak ditemukan dalam dataset.")

    st.write("""
            - Berdasarkan scatter plot yang menunjukkan hubungan antara kecepatan angin (WSPM) dan konsentrasi PM2.5, terlihat bahwa kecepatan angin berpengaruh signifikan terhadap penyebaran polusi udara.
            - Pada kecepatan angin rendah, konsentrasi PM2.5 cenderung tinggi karena polutan mengendap dan tidak tersebar dengan baik.
            - Pada kecepatan angin tinggi, konsentrasi PM2.5 menurun, menunjukkan bahwa angin membantu menyebarkan dan mendispersikan polusi udara. Dengan demikian, kecepatan angin berperan dalam mengurangi konsentrasi polutan di udara, terutama dalam kondisi atmosfer terbuka.
             """)


    st.subheader("Pertanyaan 2 : Bagaimana Hubungan antara Suhu Udara (TEMP) dan Konsentrasi Ozon (O3)?")
    # Scatter Plot dengan Regresi: Suhu Udara vs Konsentrasi Ozon (O3)
    if 'TEMP' in df.columns and 'O3' in df.columns:
        st.write("📉 Scatter Plot dengan Regresi: Suhu Udara vs Konsentrasi Ozon")
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.regplot(data=df, x="TEMP", y="O3", scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
        ax2.set_xlabel("Suhu Udara (°C)")
        ax2.set_ylabel("Konsentrasi Ozon (µg/m³)")
        ax2.set_title("Hubungan antara Suhu Udara (TEMP) dan Konsentrasi Ozon (O3)")
        ax2.grid(True)
        st.pyplot(fig2)

    st.write("""
            - Suhu udara (TEMP) memiliki korelasi positif dengan konsentrasi Ozon (O3).
            - Pada suhu yang lebih tinggi, reaksi fotokimia yang menghasilkan Ozon cenderung meningkat, sehingga konsentrasi O3 juga lebih tinggi.
            - Jika data menunjukkan tren ini dalam grafik, maka dapat disimpulkan bahwa suhu udara yang lebih tinggi mendorong pembentukan O3 lebih banyak di atmosfer.
             """)
else:
    st.error(f"⚠️ File `{file_path}` tidak ditemukan. Pastikan file ada di folder yang sama.")
