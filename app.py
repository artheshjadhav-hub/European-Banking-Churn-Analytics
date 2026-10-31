
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="European Banking Churn", layout="wide")

st.title("European Banking Customer Churn Analytics")

uploaded = st.file_uploader("Upload Customer CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)

    st.subheader("Customer Overview")

    total = len(df)
    churned = df["Exited"].sum()
    retained = total - churned
    rate = churned / total * 100 if total else 0

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Total Customers", total)
    c2.metric("Churned", int(churned))
    c3.metric("Retained", int(retained))
    c4.metric("Churn Rate", f"{rate:.2f}%")

    st.subheader("Geography-wise Churn")

    geo = df.groupby("Geography")["Exited"].mean()*100
    st.bar_chart(geo)

    st.subheader("Age-wise Churn")

    df["AgeGroup"] = pd.cut(
        df["Age"],
        bins=[0,29,45,60,float("inf")],
        labels=["Under 30","30-45","46-60","60+"]
    )

    age = df.groupby("AgeGroup", observed=False)["Exited"].mean()*100
    st.bar_chart(age)

    st.subheader("Gender-wise Churn")
    gender = df.groupby("Gender")["Exited"].mean()*100
    st.bar_chart(gender)

    st.subheader("Tenure Analysis")
    tenure = df.groupby("Tenure")["Exited"].mean()*100
    st.line_chart(tenure)

    st.subheader("Customer Data")
    st.dataframe(df, use_container_width=True)

    st.download_button(
        "Download Customer Data",
        df.to_csv(index=False),
        "customer_data.csv"
    )
else:
    st.info("Please upload your customer churn CSV file.")
