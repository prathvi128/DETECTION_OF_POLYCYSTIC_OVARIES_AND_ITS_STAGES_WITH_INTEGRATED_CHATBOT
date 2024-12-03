

https://github.com/user-attachments/assets/be664e51-332f-4497-a659-11c0f7fe66ab

<B> DETECTION-OF-POLYCYSTIC-OVARIES-AND-ITS-STAGES-WITH-CHATBOT </B> <br>
 A comprehensive PCOS (Polycystic Ovary Syndrome) prediction and assistance system, designed to provide accurate diagnosis and stage detection of PCOS. 
 The application integrates neural network models and chatbot technology, deployed using Streamlit for user-friendly interaction.<br><br>
<B>1. Objectives</B><br>
-PCOD Detection: Identifies the likelihood of Polycystic Ovary Disease using user input data.<br>
-Stage Detection: Determines the severity (Stage 1 or Stage 2) of PCOS based on medical data.<br>
-Health Education: Offers lifestyle recommendations and health management tips.<br>
-Interactive Support: Provides an AI-driven chatbot for user queries about PCOD/PCOS.<br><br>
<B>2. Key Features</B><br>
Streamlit Interface:<br>
-Simplifies data input through an intuitive GUI.<br>
-Visual aids (images) enhance usability.<br>
-Sidebar navigation for quick access to different functionalities.<br>
Chatbot Integration:<br>
-Offers predefined, context-sensitive responses to common questions about PCOS.<br>
-Educates users on symptoms, causes, and treatments.<br>
Health Insights:<br>
-Provides actionable advice tailored to the prediction results, focusing on diet, exercise, and medical care.<br><br>
<B>3. Workflow</B><br>
PCOD Prediction:<br>
-Accepts personal and health-related data.<br>
-Processes the input through the pco_prediction.h5 model.<br>
-Displays results and next-step advice.<br>
PCOS Stages Detection:<br>
-Requires additional clinical data.<br>
-Processes the input through the pco_stages.h5 model.<br>
-Identifies the stage and suggests lifestyle adjustments.<br>
Chatbot:<br>
-Engages users in natural conversations about PCOD/PCOS.<br>
-Offers quick access to information.<br><br>
<B>4. Implementation</B><br>
Technology Stack:<br>
-Backend: Python (TensorFlow, NumPy).<br>
-Frontend: Streamlit.<br>
Models:<br>
-PCOD prediction (pco_prediction.h5).<br>
-Stage detection (pco_stages.h5).<br>
Input Handling:<br>
-Numeric input fields for user health data.<br>
-Prediction results displayed interactively.<br>
