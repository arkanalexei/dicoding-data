# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import plotly.express as px

# Assuming this is a typo and meant to use @st.cache
@st.cache_data
def load_data():
    df = pd.read_csv("./main_data.csv")
    df["product_id"] = df["product_id"].str[:5]
    return df

def run():
    st.set_page_config(
        page_title="Dashboard",
        page_icon="📈",
    )

    st.write("# Welcome to the Dashboard! 📊")
    st.caption("Hover on each bar to find more information!")

    df = load_data()

    n = st.sidebar.number_input('Enter the number of top products:', min_value=1, value=5)  # Default to 5

    # Ambil top n produk
    top_n_products = df.nlargest(n, 'total_quantity_sold')

    # Plot
    fig = px.bar(top_n_products, x='product_id', y='total_quantity_sold',
                 hover_data=['price', 'product_category_name_english', 'product_description_lenght', 'product_photos_qty'],  # Fixed typo in 'product_description_length'
                 labels={'total_quantity_sold': 'Total Quantity Sold', 'product_id': 'Product ID'},
                 title=f'Top {n} Products by Total Quantity Sold')

    # Tampilkan plot
    st.plotly_chart(fig)

if __name__ == "__main__":
    run()
