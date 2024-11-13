
# Dasbor Analisis Kualitas Udara dan Cuaca

Dasbor ini memungkinkan pengguna untuk mengeksplorasi bagaimana kondisi cuaca memengaruhi tingkat polusi udara, khususnya PM2.5 dan PM10. Selain itu, dasbor ini mengidentifikasi pola musiman dan harian dalam konsentrasi polutan, memberikan wawasan penting untuk pengendalian polusi dan pembuatan kebijakan.

## Persyaratan

Pastikan Anda memiliki pustaka Python berikut yang terinstal:
- **Python** (versi 3.7 atau lebih tinggi)
- **Streamlit**: Pustaka untuk membuat aplikasi web interaktif
- **Pandas**: Untuk manipulasi data
- **Matplotlib** dan **Seaborn**: Untuk visualisasi data

Instal pustaka ini dan pustaka lainnya yang diperlukan dengan perintah berikut:

```bash
pip install -r requirements.txt
```

### Isi `requirements.txt`

Berikut adalah daftar lengkap pustaka yang diperlukan:

```
altair==5.4.1
attrs==24.2.0
blinker==1.9.0
cachetools==5.5.0
certifi==2024.8.30
charset-normalizer==3.4.0
click==8.1.7
contourpy==1.3.1
cycler==0.12.1
fonttools==4.54.1
gitdb==4.0.11
GitPython==3.1.43
idna==3.10
Jinja2==3.1.4
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
kiwisolver==1.4.7
markdown-it-py==3.0.0
MarkupSafe==3.0.2
matplotlib==3.9.2
mdurl==0.1.2
narwhals==1.13.4
numpy==2.1.3
packaging==24.2
pandas==2.2.3
pillow==11.0.0
protobuf==5.28.3
pyarrow==18.0.0
pydeck==0.9.1
Pygments==2.18.0
pyparsing==3.2.0
python-dateutil==2.9.0.post0
pytz==2024.2
referencing==0.35.1
requests==2.32.3
rich==13.9.4
rpds-py==0.21.0
seaborn==0.13.2
six==1.16.0
smmap==5.0.1
streamlit==1.40.1
tenacity==9.0.0
toml==0.10.2
tornado==6.4.1
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.2.3
watchdog==6.0.0
```

## Cara Menjalankan Dasbor

1. **Simpan Script Dasbor**:
   - Simpan kode Python yang disediakan untuk dasbor dalam file bernama `air_quality_dashboard.py`.

2. **Tempatkan File Data**:
   - Pastikan file data `cleaned_dataset.csv` berada di direktori yang sama dengan `air_quality_dashboard.py`.
   - Jika file berada di tempat lain, perbarui jalur file di script.

3. **Jalankan Dasbor**:
   - Buka terminal atau command prompt, navigasikan ke direktori yang berisi script dan file data, dan jalankan:

   ```bash
   streamlit run air_quality_dashboard.py
   ```

4. **Akses Dasbor**:
   - Streamlit akan memulai server lokal, biasanya tersedia di:
     ```
     http://localhost:8501
     ```
   - Buka URL ini di browser web Anda untuk mengakses dasbor.

## Fitur Dasbor

- **Filter Sidebar**: Pilih tahun tertentu untuk menganalisis data polusi dan cuaca pada periode tersebut.
- **Heatmap Korelasi**: Visualisasikan korelasi antara faktor cuaca (misalnya, suhu, tekanan) dan polutan (misalnya, PM2.5, PM10).
- **Scatter Plots**: Bandingkan fitur cuaca individu dengan konsentrasi PM2.5 dan PM10.
- **Tren Bulanan dan Harian**: Amati tren musiman dan harian dalam tingkat polusi, berguna untuk mengidentifikasi waktu kritis untuk pengendalian polusi.

## Pemecahan Masalah

- Jika Anda menemui kesalahan terkait pustaka yang hilang, pastikan semua paket yang diperlukan telah diinstal menggunakan `pip install -r requirements.txt`.
- Verifikasi bahwa file `cleaned_dataset.csv` diberi nama dengan benar dan terletak di direktori yang sesuai; jika tidak, perbarui jalur di script.

## Output Contoh

Setelah menjalankan perintah, Anda akan melihat URL lokal yang disediakan oleh Streamlit, biasanya `http://localhost:8501`, yang dapat Anda buka di browser web untuk menjelajahi dasbor.

