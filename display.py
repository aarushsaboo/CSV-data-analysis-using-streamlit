import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def display_selected_chart(dataframe, x_axis_column,y_axis_column):
    chart_type =st.selectbox('Select the type of chart you want', 
                        ('Line chart', 'Area chart', 'Bar graph', 'Pie chart','Scatter plot'))
    if(chart_type == 'Line chart'):
        st.line_chart(dataframe, x=x_axis_column, y= y_axis_column, color = "#ffaa00")
    elif(chart_type == 'Area chart'):
        st.area_chart(dataframe, x=x_axis_column, y= y_axis_column)
    elif(chart_type == 'Bar graph'):
        st.bar_chart(dataframe, x= x_axis_column, y=y_axis_column)
    elif(chart_type == 'Pie chart'):
        fig = px.pie(dataframe, names=x_axis_column, values= y_axis_column)
        st.plotly_chart(fig)
    elif(chart_type == 'Scatter plot'):
        st.scatter_chart(dataframe, x=x_axis_column, y=y_axis_column)
    
def compute_correlation(dataframe, x_axis_column, y_axis_column):
    # dataframe.dtypes
    dataframe[x_axis_column] = pd.to_numeric(dataframe[x_axis_column], errors = 'coerce')
    dataframe[y_axis_column] = pd.to_numeric(dataframe[y_axis_column], errors = 'coerce')
    # dataframe.dtypes
    clean_data = dataframe.dropna(subset=[x_axis_column, y_axis_column], inplace = False)
    # dataframe
    correlation = clean_data[x_axis_column].corr(clean_data[y_axis_column])

    if not np.isnan(correlation):
        st.write(f"The correlation between the columns {x_axis_column} and {y_axis_column} is **:blue[{correlation}]**")
        if correlation == 1:
            st.write("*Perfect positive* correlation: as one variable increases, the other also increases.")
        elif correlation == -1:
            st.write("*Perfect negative* correlation: as one variable increases, the other decreases.")
        elif correlation == 0:
            st.write("*No correlation*: there is no relationship between the variables.")
        elif correlation > 0:
            st.write("*Positive correlation*: as one variable increases, the other tends to increase.")
        else:
            st.write("*Negative correlation*: as one variable increases, the other tends to decrease.")
    else:
        st.write("The correlation could not be calculated due to **insufficient data** or **non-numeric values.**")



st.title('CSV Data analysis tool')

csv_file = st.file_uploader('Please upload a csv file.', type="csv")



if csv_file != None:
    dataframe = pd.read_csv(csv_file)
    st.success('Data file loaded successfully')

    st.markdown('## **Options**')
    st.markdown('*Choose an option below to interact with the data*')

    choice = st.radio('Choose an option', ('View dataframe', 'Display charts', 'Calculate correlation'))

    st.markdown('---')

    if choice == 'View dataframe':
        st.header('Dataframe content')
        st.dataframe(dataframe)

    elif choice == 'Display charts':
        st.header('Chart visualization')
        st.markdown('*Select the columns to calculate the correlation:*')
        x_axis_column = st.selectbox('Select the X-axis column', dataframe.columns)
        y_axis_column = st.selectbox('Select the Y-axis column', dataframe.columns )
        display_selected_chart(dataframe, x_axis_column, y_axis_column)

    elif choice == 'Calculate correlation':
        st.header('Correlation Calculation')
        st.markdown('*Select the columns to calculate the correlation:*')
        x_axis_column = st.selectbox('Select the first column', dataframe.columns)
        y_axis_column = st.selectbox('Select the second column', dataframe.columns )
        compute_correlation(dataframe, x_axis_column, y_axis_column)

else:
    st.info('Please upload a CSV file to get started')

