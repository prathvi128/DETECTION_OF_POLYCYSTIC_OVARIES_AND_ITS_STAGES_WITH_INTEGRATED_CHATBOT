import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

def pco_prediction_page():
    st.image(r'C:/Users/harinijayanth/Downloads/shutterstock_1790187350-1.jpg', width=800)  
    model = load_model(r'C:/Users/harinijayanth/Desktop/2/pco_prediction.h5') 
    icons = ['activity']

    st.title("DETECTION OF POLYCYSTIC OVARIES")

    age = st.number_input('Enter your age')
    weight = st.number_input('Enter your weight')
    height = st.number_input('Enter your height')
    bmi = st.number_input('Enter your BMI count')
    hb = st.number_input('Enter your haemoglobin value')
    cycle_length = st.number_input('Enter your menstruation cycle length')
    pregnant = st.number_input('pregnant? (yes(1)/no(0))')
    abortions = st.number_input('Enter the number of abortions')
    hip = st.number_input('Enter your hip size in inches')
    waist = st.number_input('Enter your waist size in inches')
    waist_hip_ratio = st.number_input('Enter waist hip ratio')
    weight_gain = st.number_input('Any sudden gain in weight is observed? (yes(1)/no(0))')
    hair_growth = st.number_input('Any abnormal hair growth? (yes(1)/no(0))')
    skin_darkening = st.number_input('Skindarkening?')
    hair_loss = st.number_input('Any abnormal hair loss observed? (yes(1)/no(0))')
    pimples = st.number_input('Pimples?(yes(1)/no(0))')
    fast_food = st.number_input('Do you consume fast food regularly? (yes(1)/no(0))')
    Regular_exercise = st.number_input('Do you practice regular exercise? (yes(1)/no(0))')

    if st.button('Predict'):
        input_data = np.array([[age, weight, height, bmi, hb, cycle_length, pregnant, abortions, hip, waist, waist_hip_ratio, weight_gain, hair_growth, skin_darkening, hair_loss, pimples, fast_food, Regular_exercise]])
        prediction = model.predict(input_data)
        if prediction[0][0] == 1:
            st.write("You are detected with polycystic ovarian disease. Consult a doctor and follow their inputs.")
            st.write('Scroll down, add up more data to know about your stages and its medication')
        else:
            st.write("You are not having polycystic ovaries.")
            st.write('Have a good day and good health!')

def stages_page():
    st.image(r'C:/Users/harinijayanth/Downloads/1679642750_Polycystic-Ovarian-Syndrome.webp', width=700) 
    model = load_model(r'C:/Users/harinijayanth/Desktop/2/pco_stages.h5') 
    icons = ['activity']

    st.title("DETECTION OF PCO STAGES")

    SI_NO = st.number_input('Enter your serial no')
    Patient_file_no = st.number_input('Enter your fileno')
    a = st.number_input('AGE:')
    b = st.number_input('WEIGHT:')
    c = st.number_input('HEIGHT:')
    d = st.number_input('BMI:')
    e = st.number_input('Pregnant:')
    f = st.number_input('NO OF ABORTIONS:')
    g = st.number_input('MENSTRUATION CYCLE LENGTH:')
    I_beta = st.number_input('1ST-BETA:')
    h = st.number_input('ABNORMAL HAIR GROWTH:')
    j = st.number_input('SKIN DARKENING:')
    k = st.number_input('HAIR LOSS:')
    l = st.number_input('LH COUNT:')
    m = st.number_input('FSH COUNT:')
    vit = st.number_input('VITD3:')
    fsh_lh_ratio = st.number_input('Enter fsh-lh ratio')
    endometrium = st.number_input('Enter your endometrium thickness value')
    anovulation = st.number_input('Are you getting periods regularly? (yes(1)/no(0))')

    if st.button('Predict STAGES'):
        input_data = np.array([[SI_NO, Patient_file_no, a, b, c, d, e, f, g, I_beta, h, j, k, l, m, vit, fsh_lh_ratio, endometrium, anovulation]])
        prediction = model.predict(input_data)
        if prediction[0][0] == 1:
            st.write("Detected with STAGE 2-PCOS")
            st.write('TIPS TO OVERCOME THE DISEASE:')
            st.write('1. Intake of balanced diet (Nuts, Wholegrains, Legumes, Leafy greens etc)')
            st.write('2. Reduce intake of coffee as it may result in hormonal imbalance')
            st.write('3. Increase iron (Spinach, Broccoli etc) and magnesium (Almonds, cashews etc) intake')
            st.write('4. Maintain a healthy weight')
            st.write('5. Practice regular exercises')
            st.write('6. Maintain good sleep')
            st.write('In addition to all these, since it may lead to many dangerous health risks like High BP, Thyroid, Diabetes, Heart disease, Endometrium cancer, it is advisable to consult a doctor and schedule regular checkups')
        else:
            st.write("Detected with STAGE1-PCOD")
            st.write('TIPS TO OVERCOME THE DISEASE:')
            st.write('1. Intake of balanced diet (Nuts, Wholegrains, Legumes, Leafy greens etc)')
            st.write('2. Reduce intake of coffee as it may result in hormonal imbalance')
            st.write('3. Increase iron (Spinach, Broccoli etc) and magnesium (Almonds, cashews etc) intake')
            st.write('4. Maintain a healthy weight')
            st.write('5. Practice regular exercises')
            st.write('6. Maintain good sleep')
            st.write('In addition to following the above tips, consider consulting a doctor for further guidance')

def pcod_chatbot():
    st.title("PCOD Chatbot")
    st.write("Hello! I am your PCOD Chatbot. Ask me anything about PCOD.")

    user_input = st.text_input("You:", "")

    if st.button("Let me know"):
        response = chatbot_response(user_input)
        st.text_area("PCOD ChatBot:", value=response, height=1000)

def chatbot_response(user_input):
    responses = {
        "Hi": "Hello! What's up ?",
        "I wanted to know about PCOD": "Sure! Ask me exactly what you want to know about PCOD?",
        "What is polycystic ovaries": "Polycystic ovaries is a hormonal disorder causing enlarged ovaries with small cysts on the outer edges. There are two stages which you should know. Polycystic Ovarian Disease (PCOD) and Polycystic Ovarian Syndrome (PCOS). In PCOD, the ovaries release immature eggs, secretion of male hormones, and the ovaries become enlarged. But PCOS is a syndrome which is an endocrine disorder causing dangerous health issues.",
        "What are its symptoms": "The symptoms for PCOD mainly include irregular periods, abnormal changes in weight, acne, abnormal growth of body hairs, hair loss on the scalp. PCOS symptoms mainly include anovulation, irregular periods, weight gain or loss issues, acne, growth of body hairs, hirsutism (abnormal body hair growth). But comparatively PCOS leads to serious health issues.",
        "Treatments for PCOD": "Without consulting your doctor, consumption of any drugs may lead to serious issues. But a few lifestyle changes may help with this which include maintaining a healthy diet that is having intake of proteins, iron, magnesium-rich foods, reduce sugars and carbohydrates as it may lead to insulin resistance, managing weight if obese, regular physical exercise. Aim for anti-inflammatory. Adding iron-rich foods such as spinach, eggs, and broccoli to your diet. Cut out coffee as caffeine consumption may be linked to changes in estrogen levels and hormone behavior. Consume herbs like Ashwagandha and tulsi as they maintain cortisol levels and metabolic stress. Apart from these food intakes, maintain a healthy weight and follow regular exercise.",
        "Treatments for PCOS": "PCOS is an endocrine disorder which may lead to serious health issues like infertility, diabetes, heart disease and may end up with endometrium cancer. Lifestyle changes like maintaining a healthy diet that is having intake of proteins, reduce sugars and carbohydrates as it may lead to insulin resistance, managing weight , regular exercise may help. Aim for anti-inflammatory. Adding iron-rich foods such as spinach, eggs, and broccoli to your diet. Cut out coffee as caffeine consumption may be linked to changes in estrogen levels and hormone behavior. Consume herbs like Ashwagandha and tulsi as they maintain cortisol levels and metabolic stress. Apart from these food intakes, maintain a healthy weight and follow regular exercise. Consider visiting your doctor and follow up with regular health checkups.",
        "Causes of PCOD": "Its causes mainly include genetics, unhealthy diet, sedentary lifestyle, hormone-altering medication, over-the-counter supplements and medications, insulin resistance, high androgen levels and many other hormonal changes",
        "Causes of PCOS": "Its causes serious complications compared to PCOD. But the causes are related which include genetics, unhealthy diet, sedentary lifestyle, hormone-altering medication, over-the-counter supplements and medications, insulin resistance, high androgen levels and many other hormonal changes."
        
    }

    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I don't understand that. Please ask me anything about polycystic ovaries."

def main():
    st.sidebar.title("PCOD/PCOS Prediction and Chatbot")
    options = ["PCOD Prediction", "PCOD Stages Detection", "PCOD Chatbot"]
    choice = st.sidebar.selectbox("Select", options)

    if choice == "PCOD Prediction":
        pco_prediction_page()
    elif choice == "PCOD Stages Detection":
        stages_page()
    elif choice == "PCOD Chatbot":
        pcod_chatbot()

if __name__ == '__main__':
    main()
