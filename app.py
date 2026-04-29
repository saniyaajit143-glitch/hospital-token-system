import streamlit as st

# १. पेज सेटिंग
st.set_page_config(page_title="Smart Token System", page_icon="🏥", layout="wide")

# २. टोकन डेटा मेंटेन करण्यासाठी (Database येईपर्यंत तात्पुरते)
if 'current_token' not in st.session_state:
    st.session_state.current_token = 0
if 'total_tokens' not in st.session_state:
    st.session_state.total_tokens = 5

# ३. मुख्य डिझाइन
st.title("🏥 हॉस्पिटल टोकन मॅनेजमेंट सिस्टीम")
st.markdown("---")

# ४. दोन मुख्य विभाग: पेशंट आणि डॉक्टर
tab1, tab2 = st.tabs(["👋 पेशंट विभाग", "🔐 डॉक्टर पॅनेल"])

with tab1:
    st.header("लाईव्ह टोकन स्टेटस")
    c1, c2 = st.columns(2)
    
    with c1:
        st.metric(label="सध्या तपासणी सुरू असलेला नंबर", value=f"#{st.session_state.current_token}")
    
    with c2:
        st.metric(label="एकूण टोकन संख्या", value=st.session_state.total_tokens)
    
    # प्रोग्रेस बार
    progress = st.session_state.current_token / st.session_state.total_tokens if st.session_state.total_tokens > 0 else 0
    st.progress(progress)
    
    st.info("💡 कृपया तुमचा नंबर येईपर्यंत शांतता राखा. नंबर जवळ आला की असिस्टंट तुम्हाला कळवतील.")

with tab2:
    st.header("👨‍⚕️ डॉक्टर/असिस्टंट लॉगिन")
    # सोपा पासवर्ड प्रोटेक्शन
    pwd = st.text_input("पासवर्ड टाका", type="password")
    
    if pwd == "7890": # तुम्ही हा पासवर्ड बदलू शकता
        st.success("लॉगिन यशस्वी!")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("पुढचा पेशंट (Next Patient) ➡️"):
                if st.session_state.current_token < st.session_state.total_tokens:
                    st.session_state.current_token += 1
                    st.rerun()
                else:
                    st.warning("सर्व टोकन तपासून झाले आहेत!")

        with col_b:
            if st.button("टोकन रिसेट करा (Reset All) 🔄"):
                st.session_state.current_token = 0
                st.rerun()

        st.markdown("---")
        new_tk = st.number_input("नवीन टोकन ॲड करा", min_value=1, step=1)
        if st.button("टोकन लिस्ट वाढवा ➕"):
            st.session_state.total_tokens += new_tk
            st.success(f"{new_tk} नवीन टोकन ॲड केले!")
            st.rerun()
    else:
        st.info("डॉक्टर पॅनेल वापरण्यासाठी पासवर्ड टाका.")

# ५. फुटर
st.markdown("---")
st.caption("Developed by Ajit Bhau | Smart City Dharashiv Initiative 🇮🇳")
