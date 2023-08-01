
import pickle
import streamlit as st

# Loading the trained model
pickle_in = open('classifier9.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache_data
def prediction(tenure, Contract, PaperlessBilling, MonthlyCharges, gender, SeniorCitizen, Partner, Dependents,
               PaymentMethod, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
               StreamingTV, StreamingMovies, MultipleLines,TotalCharges):

    # Pre-processing user input
    if PaperlessBilling == "Yes":
        PaperlessBilling = 1
    else:
        PaperlessBilling = 0

    if gender == 'Male':
        gender = 1
    else:
        gender = 0

    if Contract == "Month-to-month":
        Contract = 0
    elif Contract == "One_year":
        Contract = 1
    else:
        Contract = 2

    if SeniorCitizen == 'Yes':
        SeniorCitizen = 1
    else:
        SeniorCitizen = 0

    if Partner == 'Yes':
        Partner = 1
    else:
        Partner = 0

    if Dependents == "Yes":
        Dependents = 1
    else:
        Dependents = 0

    if InternetService == 'DSL':
        InternetService = 1
    elif InternetService == 'Fiber optic':
        InternetService = 2
    else:
        InternetService = 0
        OnlineSecurity = 0
        OnlineBackup = 0
        DeviceProtection = 0
        TechSupport = 0
        StreamingTV = 0
        StreamingMovies = 0

    if OnlineSecurity == "Yes":
        OnlineSecurity = 1
    else:
        OnlineSecurity = 0

    if OnlineBackup == "Yes":
        OnlineBackup = 1
    else:
        OnlineBackup = 0

    if DeviceProtection == "Yes":
        DeviceProtection = 1
    else:
        DeviceProtection = 0

    if TechSupport == "Yes":
        TechSupport = 1
    else:
        TechSupport = 0

    if StreamingTV == "Yes":
        StreamingTV = 1
    else:
        StreamingTV = 0

    if StreamingMovies == "Yes":
        StreamingMovies = 1
    else:
        StreamingMovies = 0

    if PaymentMethod == "Electronic check":
        PaymentMethod = 0
    elif PaymentMethod == "Mailed check":
        PaymentMethod = 1
    elif PaymentMethod == "Bank transfer (automatic)":
        PaymentMethod = 2
    else:
        PaymentMethod = 3

    if MultipleLines == "No phone service":
        MultipleLines = 0
    elif MultipleLines == "No":
        MultipleLines = 1
    else:
        MultipleLines = 2

    prediction = classifier.predict([[tenure, Contract, MonthlyCharges, PaperlessBilling, gender, SeniorCitizen,
                                      Partner, Dependents, PaymentMethod, InternetService, OnlineSecurity,
                                      OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies,
                                      MultipleLines,TotalCharges]])

    if prediction == 0:
        pred = 'will not Churn'
    else:
        pred = 'is likely to Churn'

    return pred


def main():
    # Front-end elements of the web page
    st.title("Churn Prediction")
    st.markdown("This app predicts customer churn.")

    # User input fields
    tenure = st.sidebar.number_input("Tenure", min_value=0, max_value=100)
    Contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One_year", "Two_year"])
    PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check",
                                                            "Bank transfer (automatic)", "Credit card (automatic)"])
    MonthlyCharges = st.sidebar.number_input("Monthly Charges",min_value=0, max_value=300)
    TotalCharges = st.sidebar.number_input("TotalCharges",min_value=0, max_value=10000)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.sidebar.selectbox("Senior Citizen", ["Yes", "No"])
    Partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
    Dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
    MultipleLines = st.sidebar.selectbox("Multiple Lines", ["No phone service", "No - Single Line", "Yes"])

    InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    if InternetService == "No":
        OnlineSecurity = 0
        OnlineBackup = 0
        DeviceProtection = 0
        TechSupport = 0
        StreamingTV = 0
        StreamingMovies = 0
    else:
        OnlineSecurity = st.sidebar.selectbox("Online Security", ["Yes", "No"])
        OnlineBackup = st.sidebar.selectbox("Online Backup", ["Yes", "No"])
        DeviceProtection = st.sidebar.selectbox("Device Protection", ["Yes", "No"])
        TechSupport = st.sidebar.selectbox("Tech Support", ["Yes", "No"])
        StreamingTV = st.sidebar.selectbox("Streaming TV", ["Yes", "No"])
        StreamingMovies = st.sidebar.selectbox("Streaming Movies", ["Yes", "No"])


    result = ""

    if st.button("Predict"):
        result = prediction(tenure, Contract, PaperlessBilling, MonthlyCharges, gender, SeniorCitizen, Partner,
                            Dependents, PaymentMethod, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection,
                            TechSupport, StreamingTV, StreamingMovies, MultipleLines,TotalCharges)
        st.success('Customer {}'.format(result))

        print(result)

if __name__ == '__main__':
    main()
