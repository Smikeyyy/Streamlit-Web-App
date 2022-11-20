# Import libraries penting
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model dengan pickle
# model = pickle.load(open("mymodel.sav", "rb"))
model = joblib.load("newmodel.sav")

# Display title webpage
st.title("Apakah Webpage Efektif :money_with_wings:")

# Menerima input fitur dari user
Administrative = st.text_input("Masukkan jumlah interaksi pada bagian web administrasi dalam satu sesi", "10")
Administrative_Duration = st.text_input("Masukkan durasi jumlah semua interaksi pada bagian web administrasi dalam satu sesi (dalam detik)", "10")
Informational = st.text_input("Masukkan jumlah interaksi pada bagian web informasi dalam satu sesi", "10")
Informational_Duration = st.text_input("Masukkan durasi jumlah semua interaksi pada bagian web informasi dalam satu sesi (dalam detik)", "10")
ProductRelated = st.text_input("Masukkan jumlah interaksi pada bagian web produk dalam satu sesi", "10")
ProductRelated_Duration = st.text_input("Masukkan durasi jumlah semua interaksi pada bagian web produk dalam satu sesi (dalam detik)", "10")
BounceRates = st.text_input("Masukkan bouncerate dalam seluruh sesi", "0.1")
ExitRates = st.text_input("Masukkan exitrate dalam sesi terakhir", "0.1")
PageValues = st.text_input("Masukkan pagevalue", "0.1")
SpecialDay = st.select_slider("Pilih tingkat kedekatan dengan hari spesial (0: bukan hari spesial, 1: hari spesial)", [0, 0.2, 0.4, 0.6, 0.8, 1])
Month = st.selectbox("Pilih bulan kapan web diakses", ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"])
OperatingSystems = st.selectbox("Pilih operating system yang dipakai untuk mengakses web", [str(i) for i in range(1, 9)])
Browser = st.selectbox("Pilih browser yang dipakai untuk mengakses web", [str(i) for i in range(1, 14)])
Region = st.selectbox("Pilih daerah dimana web diakses", [str(i) for i in range(1, 10)])
TrafficType = st.selectbox("Pilih traffic type yang terjadi sehingga sampai mengakses web", [str(i) for i in range(1, 21)])
VisitorType = st.selectbox("Pilih tipe pengunjung yang mengakses web", ["Lama", "Baru", "Lain"])
Weekend = st.selectbox("Apakah web diakses pada saat weekend?", ["Iya", "Tidak"])

# Fungsi untuk melakukan preprocessing
def preprocess():
    columns_new = ['SpecialDay_0.2', 'SpecialDay_0.4', 'SpecialDay_0.6', 'SpecialDay_0.8',
       'SpecialDay_1.0', 'Month_Dec', 'Month_Feb', 'Month_Jul', 'Month_June',
       'Month_Mar', 'Month_May', 'Month_Nov', 'Month_Oct', 'Month_Sep',
       'OperatingSystems_2', 'OperatingSystems_3', 'OperatingSystems_4',
       'OperatingSystems_5', 'OperatingSystems_6', 'OperatingSystems_7',
       'OperatingSystems_8', 'Browser_2', 'Browser_3', 'Browser_4',
       'Browser_5', 'Browser_6', 'Browser_7', 'Browser_8', 'Browser_9',
       'Browser_10', 'Browser_11', 'Browser_12', 'Browser_13', 'Region_2',
       'Region_3', 'Region_4', 'Region_5', 'Region_6', 'Region_7', 'Region_8',
       'Region_9', 'TrafficType_2', 'TrafficType_3', 'TrafficType_4',
       'TrafficType_5', 'TrafficType_6', 'TrafficType_7', 'TrafficType_8',
       'TrafficType_9', 'TrafficType_10', 'TrafficType_11', 'TrafficType_12',
       'TrafficType_13', 'TrafficType_14', 'TrafficType_15', 'TrafficType_16',
       'TrafficType_17', 'TrafficType_18', 'TrafficType_19', 'TrafficType_20',
       'VisitorType_Other', 'VisitorType_Returning_Visitor', 'Administrative',
       'Administrative_Duration', 'Informational', 'Informational_Duration',
       'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates',
       'PageValues', 'Weekend']
    
    mycolumns = {}
    for i in columns_new:
        mycolumns[i] = 0
    mycolumns = pd.DataFrame([mycolumns]) 
    
    # Onehot encode kolom SpecialDay
    if SpecialDay == 0:
        mycolumns["SpecialDay_0.2"] = 0
        mycolumns["SpecialDay_0.4"] = 0
        mycolumns["SpecialDay_0.6"] = 0
        mycolumns["SpecialDay_0.8"] = 0
        mycolumns["SpecialDay_1.0"] = 0
    elif SpecialDay == 0.2:
        mycolumns["SpecialDay_0.2"] = 1
        mycolumns["SpecialDay_0.4"] = 0
        mycolumns["SpecialDay_0.6"] = 0
        mycolumns["SpecialDay_0.8"] = 0
        mycolumns["SpecialDay_1.0"] = 0  
    elif SpecialDay == 0.4:
        mycolumns["SpecialDay_0.2"] = 0
        mycolumns["SpecialDay_0.4"] = 1
        mycolumns["SpecialDay_0.6"] = 0
        mycolumns["SpecialDay_0.8"] = 0
        mycolumns["SpecialDay_1.0"] = 0
    elif SpecialDay == 0.6:
        mycolumns["SpecialDay_0.2"] = 0
        mycolumns["SpecialDay_0.4"] = 0
        mycolumns["SpecialDay_0.6"] = 1
        mycolumns["SpecialDay_0.8"] = 0
        mycolumns["SpecialDay_1.0"] = 0
    elif SpecialDay == 0.8:
        mycolumns["SpecialDay_0.2"] = 0
        mycolumns["SpecialDay_0.4"] = 0
        mycolumns["SpecialDay_0.6"] = 0
        mycolumns["SpecialDay_0.8"] = 1
        mycolumns["SpecialDay_1.0"] = 0
    elif SpecialDay == 1.0:
        mycolumns["SpecialDay_0.2"] = 0
        mycolumns["SpecialDay_0.4"] = 0
        mycolumns["SpecialDay_0.6"] = 0
        mycolumns["SpecialDay_0.8"] = 0
        mycolumns["SpecialDay_1.0"] = 1
    else:
        print("Error")
    
    # Onehot encode kolom Month
    if Month in ["Januari", "April", "Agustus"]:
        mycolumns["Month_Dec"] = 0
        mycolumns["Month_Feb"] = 0
        mycolumns["Month_Jul"] = 0
        mycolumns["Month_June"] = 0
        mycolumns["Month_Mar"] = 0
        mycolumns["Month_May"] = 0
        mycolumns["Month_Nov"] = 0
        mycolumns["Month_Oct"] = 0
        mycolumns["Month_Sep"] = 0
    elif Month == "Februari":
        mycolumns["Month_Dec"] = 0
        mycolumns["Month_Feb"] = 1
        mycolumns["Month_Jul"] = 0
        mycolumns["Month_June"] = 0
        mycolumns["Month_Mar"] = 0
        mycolumns["Month_May"] = 0
        mycolumns["Month_Nov"] = 0
        mycolumns["Month_Oct"] = 0
        mycolumns["Month_Sep"] = 0 
    elif Month == "Maret":
        mycolumns["Month_Dec"] = 0
        mycolumns["Month_Feb"] = 0
        mycolumns["Month_Jul"] = 0
        mycolumns["Month_June"] = 0
        mycolumns["Month_Mar"] = 1
        mycolumns["Month_May"] = 0
        mycolumns["Month_Nov"] = 0
        mycolumns["Month_Oct"] = 0
        mycolumns["Month_Sep"] = 0 
    elif Month == "Juni":
        mycolumns["Month_Dec"] = 0
        mycolumns["Month_Feb"] = 0
        mycolumns["Month_Jul"] = 0
        mycolumns["Month_June"] = 1
        mycolumns["Month_Mar"] = 0
        mycolumns["Month_May"] = 0
        mycolumns["Month_Nov"] = 0
        mycolumns["Month_Oct"] = 0
        mycolumns["Month_Sep"] = 0 
    elif Month == "Juli":
        mycolumns["Month_Dec"] = 0
        mycolumns["Month_Feb"] = 0
        mycolumns["Month_Jul"] = 1
        mycolumns["Month_June"] = 0
        mycolumns["Month_Mar"] = 0
        mycolumns["Month_May"] = 0
        mycolumns["Month_Nov"] = 0
        mycolumns["Month_Oct"] = 0
        mycolumns["Month_Sep"] = 0 
    elif Month == "September":
        mycolumns["Month_Dec"] = 0
        mycolumns["Month_Feb"] = 0
        mycolumns["Month_Jul"] = 0
        mycolumns["Month_June"] = 0
        mycolumns["Month_Mar"] = 0
        mycolumns["Month_May"] = 0
        mycolumns["Month_Nov"] = 0
        mycolumns["Month_Oct"] = 0
        mycolumns["Month_Sep"] = 1 
    elif Month == "Oktober":
        mycolumns["Month_Dec"] = 0
        mycolumns["Month_Feb"] = 0
        mycolumns["Month_Jul"] = 0
        mycolumns["Month_June"] = 0
        mycolumns["Month_Mar"] = 0
        mycolumns["Month_May"] = 0
        mycolumns["Month_Nov"] = 0
        mycolumns["Month_Oct"] = 1
        mycolumns["Month_Sep"] = 0
    elif Month == "November":
        mycolumns["Month_Dec"] = 0
        mycolumns["Month_Feb"] = 0
        mycolumns["Month_Jul"] = 0
        mycolumns["Month_June"] = 0
        mycolumns["Month_Mar"] = 0
        mycolumns["Month_May"] = 0
        mycolumns["Month_Nov"] = 1
        mycolumns["Month_Oct"] = 0
        mycolumns["Month_Sep"] = 0
    elif Month == "Desember":
        mycolumns["Month_Dec"] = 1
        mycolumns["Month_Feb"] = 0
        mycolumns["Month_Jul"] = 0
        mycolumns["Month_June"] = 0
        mycolumns["Month_Mar"] = 0
        mycolumns["Month_May"] = 0
        mycolumns["Month_Nov"] = 0
        mycolumns["Month_Oct"] = 0
        mycolumns["Month_Sep"] = 0       
    else:
        print("Error")   

    # Onehot encode Operating Systems
    if OperatingSystems == "1":
        mycolumns["OperatingSystems_2"] = 0
        mycolumns["OperatingSystems_3"] = 0
        mycolumns["OperatingSystems_4"] = 0
        mycolumns["OperatingSystems_5"] = 0
        mycolumns["OperatingSystems_6"] = 0
        mycolumns["OperatingSystems_7"] = 0
        mycolumns["OperatingSystems_8"] = 0
    elif OperatingSystems == "2":
        mycolumns["OperatingSystems_2"] = 1
        mycolumns["OperatingSystems_3"] = 0
        mycolumns["OperatingSystems_4"] = 0
        mycolumns["OperatingSystems_5"] = 0
        mycolumns["OperatingSystems_6"] = 0
        mycolumns["OperatingSystems_7"] = 0
        mycolumns["OperatingSystems_8"] = 0
    elif OperatingSystems == "3":
        mycolumns["OperatingSystems_2"] = 0
        mycolumns["OperatingSystems_3"] = 1
        mycolumns["OperatingSystems_4"] = 0
        mycolumns["OperatingSystems_5"] = 0
        mycolumns["OperatingSystems_6"] = 0
        mycolumns["OperatingSystems_7"] = 0
        mycolumns["OperatingSystems_8"] = 0
    elif OperatingSystems == "4":
        mycolumns["OperatingSystems_2"] = 0
        mycolumns["OperatingSystems_3"] = 0
        mycolumns["OperatingSystems_4"] = 1
        mycolumns["OperatingSystems_5"] = 0
        mycolumns["OperatingSystems_6"] = 0
        mycolumns["OperatingSystems_7"] = 0
        mycolumns["OperatingSystems_8"] = 0        
    elif OperatingSystems == "5":
        mycolumns["OperatingSystems_2"] = 0
        mycolumns["OperatingSystems_3"] = 0
        mycolumns["OperatingSystems_4"] = 0
        mycolumns["OperatingSystems_5"] = 1
        mycolumns["OperatingSystems_6"] = 0
        mycolumns["OperatingSystems_7"] = 0
        mycolumns["OperatingSystems_8"] = 0
    elif OperatingSystems == "6":
        mycolumns["OperatingSystems_2"] = 0
        mycolumns["OperatingSystems_3"] = 0
        mycolumns["OperatingSystems_4"] = 0
        mycolumns["OperatingSystems_5"] = 0
        mycolumns["OperatingSystems_6"] = 1
        mycolumns["OperatingSystems_7"] = 0
        mycolumns["OperatingSystems_8"] = 0
    elif OperatingSystems == "7":
        mycolumns["OperatingSystems_2"] = 0
        mycolumns["OperatingSystems_3"] = 0
        mycolumns["OperatingSystems_4"] = 0
        mycolumns["OperatingSystems_5"] = 0
        mycolumns["OperatingSystems_6"] = 0
        mycolumns["OperatingSystems_7"] = 1
        mycolumns["OperatingSystems_8"] = 0
    elif OperatingSystems == "8":
        mycolumns["OperatingSystems_2"] = 0
        mycolumns["OperatingSystems_3"] = 0
        mycolumns["OperatingSystems_4"] = 0
        mycolumns["OperatingSystems_5"] = 0
        mycolumns["OperatingSystems_6"] = 0
        mycolumns["OperatingSystems_7"] = 0
        mycolumns["OperatingSystems_8"] = 1
    else:
        print("Error")
    
    # Onehot encode Browser
    if Browser == "1":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 0
    elif Browser == "2":
        mycolumns["Browser_2"] = 1
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 0
    elif Browser == "3":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 1
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 0
    elif Browser == "4":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 1
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 0
    elif Browser == "5":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 1
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 0
    elif Browser == "6":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 1
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 0
    elif Browser == "7":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 1
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 0
    elif Browser == "8":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 1
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 0
    elif Browser == "9":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 1
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 0
    elif Browser == "10":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 1
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 0
    elif Browser == "11":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 1
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 0
    elif Browser == "12":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 1
        mycolumns["Browser_13"] = 0
    elif Browser == "13":
        mycolumns["Browser_2"] = 0
        mycolumns["Browser_3"] = 0
        mycolumns["Browser_4"] = 0
        mycolumns["Browser_5"] = 0
        mycolumns["Browser_6"] = 0
        mycolumns["Browser_7"] = 0
        mycolumns["Browser_8"] = 0
        mycolumns["Browser_9"] = 0
        mycolumns["Browser_10"] = 0
        mycolumns["Browser_11"] = 0
        mycolumns["Browser_12"] = 0
        mycolumns["Browser_13"] = 1
    else:
        print("Error")
    
    if Region == "1":
        mycolumns["Region_2"] = 0
        mycolumns["Region_3"] = 0
        mycolumns["Region_4"] = 0
        mycolumns["Region_5"] = 0
        mycolumns["Region_6"] = 0
        mycolumns["Region_7"] = 0
        mycolumns["Region_8"] = 0
        mycolumns["Region_9"] = 0
    elif Region == "2":
        mycolumns["Region_2"] = 1
        mycolumns["Region_3"] = 0
        mycolumns["Region_4"] = 0
        mycolumns["Region_5"] = 0
        mycolumns["Region_6"] = 0
        mycolumns["Region_7"] = 0
        mycolumns["Region_8"] = 0
        mycolumns["Region_9"] = 0        
    elif Region == "3":
        mycolumns["Region_2"] = 0
        mycolumns["Region_3"] = 1
        mycolumns["Region_4"] = 0
        mycolumns["Region_5"] = 0
        mycolumns["Region_6"] = 0
        mycolumns["Region_7"] = 0
        mycolumns["Region_8"] = 0
        mycolumns["Region_9"] = 0
    elif Region == "4":
        mycolumns["Region_2"] = 0
        mycolumns["Region_3"] = 0
        mycolumns["Region_4"] = 1
        mycolumns["Region_5"] = 0
        mycolumns["Region_6"] = 0
        mycolumns["Region_7"] = 0
        mycolumns["Region_8"] = 0
        mycolumns["Region_9"] = 0
    elif Region == "5":
        mycolumns["Region_2"] = 0
        mycolumns["Region_3"] = 0
        mycolumns["Region_4"] = 0
        mycolumns["Region_5"] = 1
        mycolumns["Region_6"] = 0
        mycolumns["Region_7"] = 0
        mycolumns["Region_8"] = 0
        mycolumns["Region_9"] = 0
    elif Region == "6":
        mycolumns["Region_2"] = 0
        mycolumns["Region_3"] = 0
        mycolumns["Region_4"] = 0
        mycolumns["Region_5"] = 0
        mycolumns["Region_6"] = 1
        mycolumns["Region_7"] = 0
        mycolumns["Region_8"] = 0
        mycolumns["Region_9"] = 0
    elif Region == "7":
        mycolumns["Region_2"] = 0
        mycolumns["Region_3"] = 0
        mycolumns["Region_4"] = 0
        mycolumns["Region_5"] = 0
        mycolumns["Region_6"] = 0
        mycolumns["Region_7"] = 1
        mycolumns["Region_8"] = 0
        mycolumns["Region_9"] = 0
    elif Region == "8":
        mycolumns["Region_2"] = 0
        mycolumns["Region_3"] = 0
        mycolumns["Region_4"] = 0
        mycolumns["Region_5"] = 0
        mycolumns["Region_6"] = 0
        mycolumns["Region_7"] = 0
        mycolumns["Region_8"] = 1
        mycolumns["Region_9"] = 0
    elif Region == "9":
        mycolumns["Region_2"] = 0
        mycolumns["Region_3"] = 0
        mycolumns["Region_4"] = 0
        mycolumns["Region_5"] = 0
        mycolumns["Region_6"] = 0
        mycolumns["Region_7"] = 0
        mycolumns["Region_8"] = 0
        mycolumns["Region_9"] = 1
    else:
        print("Error")

    # Onehote encode kolom TrafficType
    if TrafficType == "1":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "2":
        mycolumns["TrafficType_2"] = 1
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "3":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 1
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "4":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 1
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "5":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 1
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "6":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 1
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "7":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 1
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "8":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 1
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "9":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 1 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "10":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 1
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "11":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 1
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "12":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 1
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "13":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 1
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "14":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 1
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "15":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 1
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "16":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 1
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "17":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 1
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "18":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 1
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "19":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 1
        mycolumns["TrafficType_20"] = 0
    elif TrafficType == "20":
        mycolumns["TrafficType_2"] = 0
        mycolumns["TrafficType_3"] = 0
        mycolumns["TrafficType_4"] = 0
        mycolumns["TrafficType_5"] = 0
        mycolumns["TrafficType_6"] = 0
        mycolumns["TrafficType_7"] = 0
        mycolumns["TrafficType_8"] = 0
        mycolumns["TrafficType_9"] = 0 
        mycolumns["TrafficType_10"] = 0
        mycolumns["TrafficType_11"] = 0
        mycolumns["TrafficType_12"] = 0
        mycolumns["TrafficType_13"] = 0
        mycolumns["TrafficType_14"] = 0
        mycolumns["TrafficType_15"] = 0
        mycolumns["TrafficType_16"] = 0
        mycolumns["TrafficType_17"] = 0
        mycolumns["TrafficType_18"] = 0
        mycolumns["TrafficType_19"] = 0
        mycolumns["TrafficType_20"] = 1
    else:
        print("Error")

    # Onehot encode VisitorType
    if VisitorType == "Baru":
        mycolumns["VisitorType_Other"] = 0
        mycolumns["VisitorType_Returning_Visitor"] = 0
    elif VisitorType == "Lama":
        mycolumns["VisitorType_Other"] = 0
        mycolumns["VisitorType_Returning_Visitor"] = 1
    elif VisitorType == "Lain":
        mycolumns["VisitorType_Other"] = 1
        mycolumns["VisitorType_Returning_Visitor"] = 0
    else:
        print("Error")

    # Label encode Weekend
    if Weekend == "Iya":
        mycolumns["Weekend"] = 1
    elif Weekend == "Tidak":
        mycolumns["Weekend"] = 0
    else:
        print("Error")

    return mycolumns

# Fungsi untuk melakukan prediksi
def predicts():
    row = np.array([Administrative, Administrative_Duration, Informational,
       Informational_Duration, ProductRelated, ProductRelated_Duration,
       BounceRates, ExitRates, PageValues])
    
    columns = ['Administrative', 'Administrative_Duration', 'Informational',
       'Informational_Duration', 'ProductRelated', 'ProductRelated_Duration',
       'BounceRates', 'ExitRates', 'PageValues']
    
    X = pd.DataFrame([row], columns = columns)
    X_prep = preprocess()
    X_prep[columns] = X

    prediction = model.predict(X_prep)[0]
    
    if prediction == 1:
        st.success("Webpage Effective :thumbsup:")
    else:
        st.error("Webpage Tidak Effective :thumbsdown:")

st.button("Predict", on_click = predicts)