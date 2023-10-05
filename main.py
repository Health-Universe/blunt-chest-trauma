# Streamlit App for NEXUS Chest Decision Instrument for Blunt Chest Trauma

import streamlit as st

st.title('NEXUS Chest Decision Instrument for Blunt Chest Trauma')

# Clinical Criteria for NEXUS Chest
st.markdown('''
Please answer the following questions related to the patient's symptoms and signs:
''')

age_gt_60 = st.checkbox("Is the patient's age >60 years?")
rapid_deceleration_mechanism = st.checkbox("Was there a rapid deceleration mechanism, e.g., a fall from height >20 feet?")
intoxication = st.checkbox("Is the patient intoxicated?")
altered_alertness_or_distraction = st.checkbox("Does the patient have altered alertness or distracting painful injury?")
tenderness_to_chest_wall_palpation = st.checkbox("Is there tenderness to chest wall palpation?")
painful_thoracic_spine_or_sternum_exam = st.checkbox("Is there a painful thoracic spine or sternum exam?")

criteria = [
    age_gt_60,
    rapid_deceleration_mechanism,
    intoxication,
    altered_alertness_or_distraction,
    tenderness_to_chest_wall_palpation,
    painful_thoracic_spine_or_sternum_exam
]

# NEXUS Chest Decision
if any(criteria):
    st.warning('Consider imaging. Patient does NOT meet the NEXUS low-risk criteria.')
else:
    st.success('Patient meets the NEXUS low-risk criteria. Imaging may not be necessary.')

st.markdown('''
**Disclaimer:** This tool is meant for educational purposes only and not for clinical decision making. Please consult with a medical professional before making any clinical decisions.
''')

# To run the app, you'll need to have Streamlit installed:
# pip install streamlit

# After writing the code in a .py file, you can run the app using:
# streamlit run your_file_name.py
