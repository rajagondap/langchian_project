import streamlit as st
import pandas as pd
import numpy as np


# Set the title of the app
st.title("DataFrame Manipulation App")


#create simple dataframe
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
})
# Display the dataframe in the app  
st.write("Original DataFrame")
st.dataframe(df)

## Create line chart
st.write("Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)