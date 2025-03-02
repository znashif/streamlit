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
    - SO2, NO2, CO, O3 : Gas polutan udara.
    - TEMP : Suhu udara dalam derajat Celsius.
    - PRES : Tekanan udara dalam hPa.
    - DEWP : Titik embun, suhu di mana udara mulai mengembun.
    - RAIN : Curah hujan dalam mm.
    - wd : Arah angin.
    - WSPM : Kecepatan angin dalam m/s.
    """
)

# Pastikan file tersedia
file_path = os.path.join(os.path.dirname(__file__), "main_data.csv")

@st.cache_data
def load_data():
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df[['year', 'month', 'day']])  # Buat kolom tanggal
    return df

if os.path.exists(file_path):
    # Load data
    df = load_data()
    
    # Sidebar untuk filtering tanggal
    min_date, max_date = df['Date'].min().date(), df['Date'].max().date()
    start_date, end_date = st.sidebar.date_input(
        "Pilih Rentang Tanggal:", (min_date, max_date), min_value=min_date, max_value=max_date
    )
    
    # Filter data berdasarkan rentang tanggal yang dipilih
    df_filtered = df[(df['Date'] >= pd.Timestamp(start_date)) & (df['Date'] <= pd.Timestamp(end_date))]
    
    st.header("Data Preview")
    st.write(df_filtered.head())

    st.header("Visualisasi Data")
    st.subheader("Pertanyaan 1: Apakah kecepatan angin (WSPM) berpengaruh terhadap penyebaran polusi udara?")
    if 'WSPM' in df_filtered.columns and 'PM2.5' in df_filtered.columns:
        st.write("📈 Scatter Plot: Kecepatan Angin vs Polusi Udara")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=df_filtered, x='WSPM', y='PM2.5', alpha=0.5)
        ax.set_title('Hubungan antara Kecepatan Angin (WSPM) dan Polusi Udara (PM2.5)')
        ax.set_xlabel('Kecepatan Angin (m/s)')
        ax.set_ylabel('Konsentrasi PM2.5')
        st.pyplot(fig)
    else:
        st.error("⚠️ Kolom 'WSPM' atau 'PM2.5' tidak ditemukan dalam dataset.")

    st.subheader("Pertanyaan 2: Bagaimana Hubungan antara Suhu Udara (TEMP) dan Konsentrasi Ozon (O3)?")
    if 'TEMP' in df_filtered.columns and 'O3' in df_filtered.columns:
        st.write("📉 Scatter Plot dengan Regresi: Suhu Udara vs Konsentrasi Ozon")
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.regplot(data=df_filtered, x="TEMP", y="O3", scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
        ax2.set_xlabel("Suhu Udara (°C)")
        ax2.set_ylabel("Konsentrasi Ozon (µg/m³)")
        ax2.set_title("Hubungan antara Suhu Udara (TEMP) dan Konsentrasi Ozon (O3)")
        ax2.grid(True)
        st.pyplot(fig2)
    else:
        st.error("⚠️ Kolom 'TEMP' atau 'O3' tidak ditemukan dalam dataset.")
else:
    st.error(f"⚠️ File `{file_path}` tidak ditemukan. Pastikan file ada di folder yang sama.")
