import streamlit as st
import helper
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Custom CSS for sky-like soothing background and borders
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #b3e0ff 0%, #e6f7ff 100%);
    }
    .stTextInput>div>div>input {
        border: 1.5px solid #b6c6e0;
        border-radius: 8px;
        padding: 0.5rem;
        background-color: #f7fafc;
    }
    .stButton>button {
        background-color: #6a82fb;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        border: none;
        font-size: 1rem;
        font-weight: 500;
        margin-top: 1rem;
    }
    .stButton>button:hover {
        background-color: #5a6ee5;
    }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #3a3a3a;'>Duplicate Question Detector</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: #5a6ee5;'>Enter two questions below. The model will predict if they are duplicates and show its confidence.</p>",
        unsafe_allow_html=True
    )

    q1 = st.text_input('Enter Question 1')
    q2 = st.text_input('Enter Question 2')

    if st.button('Check Duplicate'):
        if not q1.strip() or not q2.strip():
            st.warning("Please enter both questions.")
        else:
            query = helper.query_point_creator(q1, q2)
            proba = model.predict_proba(query)[0]
            result = model.predict(query)[0]
            confidence = proba[result]
            if result:
                st.success(f'✅ These questions are likely duplicates.\n\n**Confidence:** {confidence:.2%}')
            else:
                st.info(f'❌ These questions are not duplicates.\n\n**Confidence:** {confidence:.2%}')

    st.markdown('</div>', unsafe_allow_html=True)
