import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Membaca data rental.csv
rental_df = pd.read_csv('../Proyek Analisis Data/project-colab/rental.csv')


# Mengubah nama musim
rental_df['season_day'].replace((1, 2, 3, 4), ('Winter', 'Spring', 'Summer', 'Fall'), inplace=True)

# Menkonversi nama bulan menjadi urutan numerik
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rental_df['date'] = pd.to_datetime(rental_df['date'])
rental_df['month'] = pd.Categorical(rental_df['date'].dt.strftime('%B'), categories=month_order, ordered=True)


# Membuat dataframe rata-rata total rental berdasarkan musim
season_count_df = rental_df.groupby('season_day')['count_day'].mean().reset_index().sort_values('count_day', ascending=True)

# Membuat dataframe rata-rata total rental berdasarkan bulan
month_count_df = rental_df.groupby('month')['count_day'].mean().reset_index().sort_values(by='month')


# Dashboard ---
sns.set(style='whitegrid')

# Sidebar
with st.sidebar:
    st.title(':bike: Arn Bike Rental :sparkles:')
    st.text('Arn Bike Rental Dashboard')
    st.text('')
    st.text('by: Urjel Arnold Benamen')
    st.text('')
    st.text('')
    st.subheader('Tentang Dashboard')
    st.markdown(
        """
            Dashboard ini dibuat untuk memudahkan dalam melihat data rental sepeda pada perusahaan Arn Bike Rental. 
            Pada dashboard ini, Anda dapat melihat rata-rata total rental sepeda berdasarkan musim dan bulan. 
            Semoga dashboard ini dapat membantu Anda dalam pengambilan keputusan.
        """
    )
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.markdown('© 2024 Arn Bike Rental. All rights reserved.')


# Judul
st.title('Bike Rental Dashboard :bike: :bar_chart:')

st.text('')
st.text('')

# 1. Grafik rata-rata total rental berdasarkan musim diurutkan dari yang terkecil
st.subheader('Rata-rata Total Rental Sepeda Berdasarkan Musim')
fig, ax = plt.subplots(figsize=(10, 6))
colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4"]
sns.barplot(x='season_day', y='count_day', data=season_count_df, palette=colors, ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Total Rental')
st.pyplot(fig)

# Menampilkan nilai rata-rata terbanyak untuk musim
max_season_index = season_count_df['count_day'].idxmax()
max_season_value = season_count_df.loc[max_season_index, 'count_day']
max_season_name = season_count_df.loc[max_season_index, 'season_day']
st.text(f'Rata-rata terbanyak ada pada musim {max_season_name} dengan nilai {max_season_value}')

st.text('')
st.text('')

# 2. Grafik rata-rata total rental berdasarkan bulan
st.subheader('Rata-rata Total Rental Sepeda Berdasarkan Bulan')
fig, ax = plt.subplots(figsize=(10, 6))
colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#9bb4c2", "#D3D3D3", "#D3D3D3", "#4A8AAE", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x='month', y='count_day', data=month_count_df, palette=colors, ax=ax)
ax.set_xlabel('Bulan')
ax.set_ylabel('Rata-rata Total Rental')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Menampilkan nilai rata-rata terbanyak untuk bulan
max_month_index = month_count_df['count_day'].idxmax()
max_month_value = month_count_df.loc[max_month_index, 'count_day']
max_month_name = month_count_df.loc[max_month_index, 'month']
st.text(f'Rata-rata terbanyak ada pada bulan {max_month_name} dengan nilai {max_month_value}')