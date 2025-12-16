import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr

# =========================================================
# CEK APAKAH openpyxl TERSEDIA
# =========================================================
try:
    import openpyxl
    OPENPYXL_AVAILABLE = True
except ImportError:
    OPENPYXL_AVAILABLE = False

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="Aplikasi Analisis Data Survei",
    layout="wide"
)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("📊 Analisis Data Survei")

language = st.sidebar.radio(
    "🌐 Bahasa",
    ("Indonesia", "English")
)

menu = st.sidebar.radio(
    "📌 Menu",
    ("Tentang Aplikasi", "Profil Tim", "Analisis Data")
)

# =========================================================
# VARIABEL TEKS
# =========================================================
if language == "Indonesia":
    app_title = "📈 Aplikasi Analisis Data Survei"
    if OPENPYXL_AVAILABLE:
        upload_label = "Unggah File Excel atau CSV"
        upload_types = ["csv", "xlsx", "xls"]
    else:
        upload_label = "Unggah File CSV"
        upload_types = ["csv"]
else:
    app_title = "📈 Survey Data Analysis Application"
    if OPENPYXL_AVAILABLE:
        upload_label = "Upload Excel or CSV File"
        upload_types = ["csv", "xlsx", "xls"]
    else:
        upload_label = "Upload CSV File"
        upload_types = ["csv"]

# =========================================================
# JUDUL UTAMA
# =========================================================
st.title(app_title)

# =========================================================
# HALAMAN TENTANG APLIKASI
# =========================================================
if menu == "Tentang Aplikasi":
    if language == "Indonesia":
        st.header("📌 Tentang Aplikasi")
        st.write("""
        Aplikasi ini digunakan untuk menganalisis data survei secara interaktif.
        
        **Fitur Utama:**
        - Upload data dari Excel atau CSV
        - Analisis statistik deskriptif
        - Analisis korelasi antar variabel
        - Antarmuka bilingual (Indonesia/English)
        
        **Teknologi yang Digunakan:**
        - Python
        - Streamlit
        - Pandas
        - NumPy
        - SciPy
        """)
    else:
        st.header("📌 About This Application")
        st.write("""
        This application is used to analyze survey data interactively.
        
        **Main Features:**
        - Upload data from Excel or CSV
        - Descriptive statistical analysis
        - Correlation analysis between variables
        - Bilingual interface (Indonesia/English)
        
        **Technologies Used:**
        - Python
        - Streamlit
        - Pandas
        - NumPy
        - SciPy
        """)

# =========================================================
# HALAMAN PROFIL TIM (DENGAN FOTO & KONTRIBUSI)
# =========================================================
elif menu == "Profil Tim":
    if language == "Indonesia":
        st.header("👥 Profil Tim")
        st.markdown("Kenali anggota tim pengembang aplikasi ini beserta kontribusi mereka.")
        
        # Data tim lengkap dengan foto dan kontribusi
        members = [
            {
                "nama": "Agni Aisyah Putri",
                "id": "004202400137",
                "foto": "agni.jpeg",
                "role": "Ketua Tim & Backend Developer",
                "kontribusi": [
                    "Mengembangkan struktur dan logika utama aplikasi",
                    "Implementasi analisis statistik deskriptif",
                    "Membuat fungsi korelasi Pearson dan Spearman",
                    "Menyiapkan dan mengolah data responden",
                    "Mengelola deployment aplikasi",
                    "Membuat dokumentasi teknis"
                ]
            },
            {
                "nama": "Andita Nurul Azizah",
                "id": "004202400059",
                "foto": "andita.jpeg",
                "role": "Frontend Developer & UI Designer",
                "kontribusi": [
                    "Mendesain antarmuka pengguna aplikasi",
                    "Membuat halaman profil tim",
                    "Implementasi sistem bilingual",
                    "Mengembangkan layout responsif",
                    "Membuat Google Form survei",
                    "Mendesain visualisasi data"
                ]
            },
            {
                "nama": "Cahyani Dwi Gemawang",
                "id": "004202400044",
                "foto": "cahyani.jpeg",
                "role": "Data Analyst & Documentation",
                "kontribusi": [
                    "Analisis data survei responden",
                    "Menyusun laporan hasil analisis",
                    "Membuat panduan penggunaan aplikasi",
                    "Testing dan debugging aplikasi",
                    "Dokumentasi proyek",
                    "Presentasi hasil proyek"
                ]
            }
        ]
        
        # Pilih mode tampilan
        st.subheader("📋 Detail Anggota Tim")
        
        # Dropdown untuk memilih anggota
        selected_member_name = st.selectbox(
            "Pilih anggota untuk melihat detail:",
            [member["nama"] for member in members]
        )
        
        # Cari anggota yang dipilih
        selected_member = next(member for member in members if member["nama"] == selected_member_name)
        
        # Tampilkan detail anggota yang dipilih
        col_foto, col_info = st.columns([1, 2])
        
        with col_foto:
            st.image(selected_member["foto"], width=220)
            st.markdown(f"**Nama:** {selected_member['nama']}")
            st.markdown(f"**ID:** `{selected_member['id']}`")
            st.markdown(f"**Peran:** {selected_member['role']}")
        
        with col_info:
            st.markdown("### 📝 Kontribusi")
            for i, kontrib in enumerate(selected_member["kontribusi"], 1):
                st.markdown(f"{i}. **{kontrib}**")
            
            # Statistik kontribusi
            st.markdown("---")
            col_stat1, col_stat2, col_stat3 = st.columns(3)
            with col_stat1:
                st.metric("Total Kontribusi", len(selected_member["kontribusi"]))
            with col_stat2:
                st.metric("Peran", selected_member["role"].split("&")[0].strip())
            with col_stat3:
                st.metric("Status", "Aktif")
        
        st.markdown("---")
        
        # Tampilkan semua anggota dalam grid
        st.subheader("🌟 Semua Anggota Tim")
        
        cols = st.columns(3)
        for idx, member in enumerate(members):
            with cols[idx]:
                # Card untuk setiap anggota
                with st.container():
                    st.image(member["foto"], width=180)
                    st.markdown(f"**{member['nama']}**")
                    st.markdown(f"*{member['role']}*")
                    st.markdown(f"`{member['id']}`")
                    
                    with st.expander(f"Lihat {len(member['kontribusi'])} kontribusi"):
                        for kontrib in member["kontribusi"]:
                            st.write(f"• {kontrib}")
        
        # Informasi proyek
        st.markdown("---")
        st.subheader("📚 Tentang Proyek")
        
        col_proj1, col_proj2 = st.columns(2)
        
        with col_proj1:
            st.markdown("""
            ### 🎯 Tujuan Proyek
            - Membuat aplikasi analisis data survei yang interaktif
            - Menerapkan konsep statistik dalam bentuk aplikasi web
            - Membantu proses pembelajaran analisis data
            - Menghasilkan produk yang bermanfaat untuk penelitian
            """)
        
        with col_proj2:
            st.markdown("""
            ### 📅 Timeline Proyek
            - **Perencanaan**: 1 minggu
            - **Pengembangan**: 2 minggu
            - **Testing**: 3 hari
            - **Deployment**: 2 hari
            - **Dokumentasi**: 2 hari
            """)
        
    else:
        # ENGLISH VERSION
        st.header("👥 Team Profile")
        st.markdown("Meet the team members who developed this application and their contributions.")
        
        # Team data with photos and contributions
        members = [
            {
                "name": "Agni Aisyah Putri",
                "id": "004202400137",
                "photo": "agni.jpeg",
                "role": "Team Lead & Backend Developer",
                "contributions": [
                    "Developing main application structure and logic",
                    "Implementing descriptive statistical analysis",
                    "Creating Pearson and Spearman correlation functions",
                    "Preparing and processing respondent data",
                    "Managing application deployment",
                    "Creating technical documentation"
                ]
            },
            {
                "name": "Andita Nurul Azizah",
                "id": "004202400059",
                "photo": "andita.jpeg",
                "role": "Frontend Developer & UI Designer",
                "contributions": [
                    "Designing application user interface",
                    "Creating team profile page",
                    "Implementing bilingual system",
                    "Developing responsive layout",
                    "Creating Google Form survey",
                    "Designing data visualizations"
                ]
            },
            {
                "name": "Cahyani Dwi Gemawang",
                "id": "004202400044",
                "photo": "cahyani.jpeg",
                "role": "Data Analyst & Documentation",
                "contributions": [
                    "Analyzing survey respondent data",
                    "Compiling analysis result reports",
                    "Creating application user guide",
                    "Testing and debugging application",
                    "Project documentation",
                    "Project presentation"
                ]
            }
        ]
        
        # Select display mode
        st.subheader("📋 Team Member Details")
        
        # Dropdown to select member
        selected_member_name = st.selectbox(
            "Select member to view details:",
            [member["name"] for member in members]
        )
        
        # Find selected member
        selected_member = next(member for member in members if member["name"] == selected_member_name)
        
        # Display selected member details
        col_photo, col_info = st.columns([1, 2])
        
        with col_photo:
            st.image(selected_member["photo"], width=220)
            st.markdown(f"**Name:** {selected_member['name']}")
            st.markdown(f"**ID:** `{selected_member['id']}`")
            st.markdown(f"**Role:** {selected_member['role']}")
        
        with col_info:
            st.markdown("### 📝 Contributions")
            for i, contrib in enumerate(selected_member["contributions"], 1):
                st.markdown(f"{i}. **{contrib}**")
            
            # Contribution statistics
            st.markdown("---")
            col_stat1, col_stat2, col_stat3 = st.columns(3)
            with col_stat1:
                st.metric("Total Contributions", len(selected_member["contributions"]))
            with col_stat2:
                st.metric("Role", selected_member["role"].split("&")[0].strip())
            with col_stat3:
                st.metric("Status", "Active")
        
        st.markdown("---")
        
        # Display all members in grid
        st.subheader("🌟 All Team Members")
        
        cols = st.columns(3)
        for idx, member in enumerate(members):
            with cols[idx]:
                # Card for each member
                with st.container():
                    st.image(member["photo"], width=180)
                    st.markdown(f"**{member['name']}**")
                    st.markdown(f"*{member['role']}*")
                    st.markdown(f"`{member['id']}`")
                    
                    with st.expander(f"View {len(member['contributions'])} contributions"):
                        for contrib in member["contributions"]:
                            st.write(f"• {contrib}")
        
        # Project information
        st.markdown("---")
        st.subheader("📚 About the Project")
        
        col_proj1, col_proj2 = st.columns(2)
        
        with col_proj1:
            st.markdown("""
            ### 🎯 Project Goals
            - Create interactive survey data analysis application
            - Implement statistical concepts in web application form
            - Assist data analysis learning process
            - Produce useful product for research
            """)
        
        with col_proj2:
            st.markdown("""
            ### 📅 Project Timeline
            - **Planning**: 1 week
            - **Development**: 2 weeks
            - **Testing**: 3 days
            - **Deployment**: 2 days
            - **Documentation**: 2 days
            """)

# =========================================================
# HALAMAN ANALISIS DATA
# =========================================================
elif menu == "Analisis Data":
    
    # Tampilkan warning jika openpyxl tidak tersedia
    if not OPENPYXL_AVAILABLE:
        if language == "Indonesia":
            st.warning("""
            ⚠️ **PERINGATAN: openpyxl belum terinstall**
            
            Hanya file CSV yang dapat dibaca.
            Untuk membaca file Excel (.xlsx), install openpyxl:
            ```
            pip install openpyxl
            ```
            """)
        else:
            st.warning("""
            ⚠️ **WARNING: openpyxl not installed**
            
            Only CSV files can be read.
            To read Excel files (.xlsx), install openpyxl:
            ```
            pip install openpyxl
            ```
            """)
    
    # Upload file
    uploaded_file = st.file_uploader(upload_label, type=upload_types)
    
    if uploaded_file is None:
        if language == "Indonesia":
            st.info("Silakan unggah file data untuk memulai analisis.")
        else:
            st.info("Please upload a data file to begin analysis.")
    else:
        try:
            # Baca file berdasarkan ekstensi
            file_name = uploaded_file.name.lower()
            
            if file_name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
                file_type = "CSV"
            elif file_name.endswith(('.xlsx', '.xls')):
                if OPENPYXL_AVAILABLE:
                    df = pd.read_excel(uploaded_file)
                    file_type = "Excel"
                else:
                    st.error("Excel files require openpyxl. Please install it.")
                    if language == "Indonesia":
                        st.info("Gunakan file CSV atau install openpyxl terlebih dahulu.")
                    else:
                        st.info("Use CSV file or install openpyxl first.")
                    st.stop()
            else:
                st.error(f"Format file tidak didukung: {file_name}")
                st.stop()
            
            # Jika berhasil membaca file, lanjutkan analisis
            st.success(f"✅ File {file_type} berhasil dibaca: {uploaded_file.name}")
            
            # Tampilkan data
            if language == "Indonesia":
                st.subheader("📋 Data Survei")
            else:
                st.subheader("📋 Survey Data")
            
            st.dataframe(df, use_container_width=True)
            
            # Tampilkan info dataset
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Jumlah Data" if language == "Indonesia" else "Total Rows", len(df))
            with col2:
                st.metric("Jumlah Variabel" if language == "Indonesia" else "Total Columns", len(df.columns))
            with col3:
                st.metric("Format File", file_type)
            
            # ==========================================
            # ANALISIS DESKRIPTIF
            # ==========================================
            st.markdown("---")
            
            if language == "Indonesia":
                st.subheader("📊 Analisis Deskriptif")
                var_label = "Pilih variabel numerik"
            else:
                st.subheader("📊 Descriptive Analysis")
                var_label = "Select numeric variables"
            
            # Pilih kolom numerik
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            
            if not numeric_cols:
                if language == "Indonesia":
                    st.warning("Tidak ditemukan variabel numerik dalam data.")
                else:
                    st.warning("No numeric variables found in the data.")
            else:
                selected_vars = st.multiselect(
                    var_label,
                    numeric_cols,
                    default=numeric_cols[:min(5, len(numeric_cols))]
                )
                
                if selected_vars:
                    st.dataframe(df[selected_vars].describe().T)
            
            # ==========================================
            # ANALISIS KORELASI
            # ==========================================
            st.markdown("---")
            
            if language == "Indonesia":
                st.subheader("🔗 Analisis Korelasi")
                x_label = "Variabel X"
                y_label = "Variabel Y"
                method_label = "Metode Korelasi"
                result_title = "📈 Hasil Analisis"
                interp_title = "📋 Interpretasi Korelasi"
            else:
                st.subheader("🔗 Correlation Analysis")
                x_label = "Variable X"
                y_label = "Variable Y"
                method_label = "Correlation Method"
                result_title = "📈 Analysis Result"
                interp_title = "📋 Correlation Interpretation"
            
            if numeric_cols:
                col1, col2 = st.columns(2)
                with col1:
                    var_x = st.selectbox(x_label, numeric_cols)
                with col2:
                    other_cols = [col for col in numeric_cols if col != var_x]
                    if other_cols:
                        var_y = st.selectbox(y_label, other_cols, index=0)
                    else:
                        var_y = None
                        st.warning("Hanya satu variabel numerik tersedia" if language == "Indonesia" else "Only one numeric variable available")
                
                method = st.radio(
                    method_label,
                    ["Pearson", "Spearman"],
                    index=0
                )
                
                if var_x and var_y:
                    data = df[[var_x, var_y]].dropna()
                    x = data[var_x]
                    y = data[var_y]
                    
                    if len(x) < 2:
                        st.warning("Data tidak cukup untuk analisis korelasi" if language == "Indonesia" else "Insufficient data for correlation analysis")
                    else:
                        if method == "Pearson":
                            corr, p_value = pearsonr(x, y)
                        else:
                            corr, p_value = spearmanr(x, y)
                        
                        # Tampilkan hasil
                        st.markdown(f"### {result_title}")
                        
                        col_res1, col_res2, col_res3 = st.columns(3)
                        with col_res1:
                            st.metric("Metode" if language == "Indonesia" else "Method", method)
                        with col_res2:
                            st.metric("Koefisien Korelasi" if language == "Indonesia" else "Correlation Coefficient", f"{corr:.4f}")
                        with col_res3:
                            st.metric("Nilai-p" if language == "Indonesia" else "P-value", f"{p_value:.4f}")
                        
                        # Interpretasi
                        st.markdown(f"### {interp_title}")
                        
                        abs_corr = abs(corr)
                        if abs_corr < 0.2:
                            strength = "Sangat lemah" if language == "Indonesia" else "Very weak"
                        elif abs_corr < 0.4:
                            strength = "Lemah" if language == "Indonesia" else "Weak"
                        elif abs_corr < 0.6:
                            strength = "Sedang" if language == "Indonesia" else "Moderate"
                        elif abs_corr < 0.8:
                            strength = "Kuat" if language == "Indonesia" else "Strong"
                        else:
                            strength = "Sangat kuat" if language == "Indonesia" else "Very strong"
                        
                        if corr > 0:
                            direction = "Positif" if language == "Indonesia" else "Positive"
                        elif corr < 0:
                            direction = "Negatif" if language == "Indonesia" else "Negative"
                        else:
                            direction = "Tidak ada" if language == "Indonesia" else "No"
                        
                        if p_value < 0.05:
                            significance = "Signifikan (p < 0.05)" if language == "Indonesia" else "Significant (p < 0.05)"
                        else:
                            significance = "Tidak signifikan" if language == "Indonesia" else "Not significant"
                        
                        col_int1, col_int2, col_int3 = st.columns(3)
                        with col_int1:
                            st.metric("Kekuatan" if language == "Indonesia" else "Strength", strength)
                        with col_int2:
                            st.metric("Arah" if language == "Indonesia" else "Direction", direction)
                        with col_int3:
                            st.metric("Signifikansi" if language == "Indonesia" else "Significance", significance)
                        
                        # Visualisasi
                        st.markdown("#### 📊 Visualisasi Hubungan")
                        chart_data = pd.DataFrame({
                            var_x: x,
                            var_y: y
                        })
                        st.scatter_chart(chart_data)
                        
        except Exception as e:
            if language == "Indonesia":
                st.error(f"❌ Terjadi kesalahan: {str(e)}")
                st.info("""
                **Penyebab mungkin:**
                1. File rusak atau format tidak sesuai
                2. Encoding file CSV tidak UTF-8
                3. Sheet Excel kosong
                4. Data tidak konsisten
                """)
            else:
                st.error(f"❌ Error occurred: {str(e)}")
                st.info("""
                **Possible causes:**
                1. File is corrupted or format mismatch
                2. CSV encoding is not UTF-8
                3. Excel sheet is empty
                4. Inconsistent data
                """)