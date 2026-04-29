import streamlit as st

st.set_page_config(page_title="Smart Hospital System", page_icon="🏥", layout="wide")

if 'current_token' not in st.session_state:
    st.session_state.current_token = 0
if 'patients_data' not in st.session_state:
    st.session_state.patients_data = []

st.title("🏥 स्मार्ट हॉस्पिटल मॅनेजमेंट सिस्टीम")
st.markdown("---")

tab1, tab2 = st.tabs(["👋 पेशंट विभाग", "🔐 डॉक्टर पॅनेल (लॉगिन)"])

with tab1:
    st.header("लाईव्ह टोकन स्टेटस")
    if st.session_state.current_token == 0:
        st.info("तपासणी अजून सुरू झालेली नाही.")
    else:
        st.success(f"सध्या सुरू असलेला नंबर: #{st.session_state.current_token}")
    
    st.markdown("---")
    st.caption("Developed by Ajit Bhau | Smart City Dharashiv 🇮🇳")

with tab2:
    pwd = st.text_input("पासवर्ड टाका", type="password")
    if pwd == "7890":
        st.success("लॉगिन यशस्वी!")
        
        # नवीन पेशंट नोंदणी फॉर्म
        st.subheader("📝 नवीन पेशंट नोंदणी")
        with st.form("patient_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("पेशंटचे नाव")
                village = st.text_input("गाव")
                age = st.number_input("वय", min_value=0)
            with col2:
                weight = st.text_input("वजन (उदा. 60kg)")
                opd = st.number_input("OPD चार्जेस", min_value=0)
                other = st.number_input("इतर चार्जेस", min_value=0)
            
            total = opd + other
            st.write(f"**एकूण बिल: ₹{total}**")
            
            submit = st.form_submit_button("टोकन जनरेट करा")
            if submit:
                new_token = len(st.session_state.patients_data) + 1
                st.session_state.patients_data.append({
                    "token": new_token, "name": name, "village": village, 
                    "age": age, "weight": weight, "total": total
                })
                st.success(f"टोकन #{new_token} तयार झाले!")

        st.markdown("---")
        # डॉक्टर कंट्रोल
        st.subheader("⚙️ कंट्रोल पॅनेल")
        if st.button("पुढचा पेशंट बोलवा ➡️"):
            if st.session_state.current_token < len(st.session_state.patients_data):
                st.session_state.current_token += 1
                st.rerun()
        
        # नोंदणीकृत पेशंटची यादी
        if st.session_state.patients_data:
            st.subheader("📋 आजची पेशंट लिस्ट")
            st.table(st.session_state.patients_data)
            
