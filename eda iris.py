import streamlit as st
import pandas as pd
import seaborn as sns

# load iris dataset
col_names = ['sepal_length','sepal_width','petal_length','petal_width','target']
iris = pd.read_csv("iris.csv", names=col_names)
iris_df = pd.DataFrame(iris)

st.set_page_config(layout="wide")

# create sidebar
st.sidebar.title('Exploratory Data Analysis')
plot_type = st.sidebar.selectbox('Pilih tipe grafik', ('Histogram', 'Boxplot', 'Scatterplot'))

# create main panel
st.title('Dataset Iris')
col1, col2 = st.columns(2)
with col1:
    st.subheader('Dataset Iris (10 Data Awal)')
    st.write(iris_df[:10])
with col2:
    st.subheader('Statistik Dataset Iris')
    st.write(iris_df.describe())

if plot_type == 'Histogram':
    st.subheader('Grafik Histogram')
    feature = st.selectbox('Pilih feature', iris_df.columns[:-1])
    hist_plot = sns.histplot(data=iris_df, x=feature, hue='target', kde=True)
    st.pyplot(hist_plot.figure)

elif plot_type == 'Boxplot':
    st.subheader('Grafik Boxplot')
    feature = st.selectbox('Pilih feature', iris_df.columns[:-1])
    box_plot = sns.boxplot(data=iris_df, x='target', y=feature)
    st.pyplot(box_plot.figure)

else:
    st.subheader('Grafik Scatterplot')
    x_feature = st.selectbox('Pilih x-axis feature', iris_df.columns[:-1])
    y_feature = st.selectbox('Pilih y-axis feature', iris_df.columns[:-1])
    scatter_plot = sns.scatterplot(data=iris_df, x=x_feature, y=y_feature, hue='target')
    st.pyplot(scatter_plot.figure)
