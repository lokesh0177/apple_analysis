import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import Helper

# Read the dataset
df = pd.read_csv("apple_quality.csv")
df.dropna(inplace=True)
df = df.drop(['A_id'], axis=1)

# Set page title and favicon
st.set_page_config(page_title="Apple Quality Analysis", page_icon=":apple:")

# Title and subheader
st.title("Apple Quality Analysis")

# Markdown text
st.markdown("### Quality VS Size")
st.markdown("This box plot shows the distribution of apple sizes based on quality.")

# Box plot
st.subheader("Quality VS Size")
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="Quality", y="Size")
plt.xlabel("Quality")
plt.ylabel("Size")
box_fig = plt.gcf()  # Get the current figure
st.pyplot(box_fig)

# Line plot
st.subheader("Sweetness VS Size by Quality")
st.markdown("This line plot shows the relationship between sweetness and size for each quality category.")
plt.figure(figsize=(8, 6))
sns.lineplot(data=df, x="Sweetness", y="Size", hue="Quality", marker='o')
plt.xlabel("Sweetness")
plt.ylabel("Size")
line_fig = plt.gcf()  # Get the current figure
st.pyplot(line_fig)

# Bar plot
st.subheader("Mean Juiciness by Quality")
st.markdown("This bar plot shows the mean juiciness for each quality category.")
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x="Quality", y="Juiciness", ci=None)
plt.xlabel("Quality")
plt.ylabel("Mean Juiciness")
bar_fig = plt.gcf()  # Get the current figure
st.pyplot(bar_fig)

# Heatmap
df_corr = Helper.heatmap(df)
st.subheader("Correlation Heatmap")
st.markdown("This heatmap shows the correlation between different variables.")
plt.figure(figsize=(8, 6))
sns.heatmap(df_corr.corr(), annot=True, fmt='.2f', cmap='Blues')
plt.title("Correlation Heatmap")
heatmap_fig = plt.gcf()  # Get the current figure
st.pyplot(heatmap_fig)

# Bar plot for Sweetness across different Quality categories
st.subheader("Mean Sweetness by Quality")
st.markdown("This bar plot shows the mean sweetness for each quality category.")
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x="Quality", y="Sweetness", ci=None)
plt.xlabel("Quality")
plt.ylabel("Mean Sweetness")
sweetness_bar_fig = plt.gcf()  # Get the current figure
st.pyplot(sweetness_bar_fig)  # Pass the specific figure object to st.pyplot()
