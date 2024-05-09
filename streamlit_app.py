import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Simple Chart Titles",
    page_icon=":bar_chart:",
)


@st.cache_data
def load_col_data():
    return pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
    )


@st.cache_data
def load_data():
    return pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])


st.subheader("Customizing Chart Titles for Streamlit's Simple Charts")

with st.expander("Context :books:"):
    st.write(
        """
    Streamlit's [simple charts](https://docs.streamlit.io/develop/api-reference/charts#simple-chart-elements) (line, area, bar, scatter) have a `title` parameter that allows you to customize the chart title.

    | Parameter | Description |
    | --- | --- |
    | `title` *(str or None)* | The title of the chart. If a string, it will be used as the descriptive title text. If None (default), no title will be displayed. |


    """
    )

    st.write(
        """


    """
    )

    st.write(
        """
    - Notion project: [Built-in charts: Chart title](https://www.notion.so/snowflake-corp/Product-Spec-92cad2ef99814a1a87a4ecd26c72be42)
    - Download the [wheel file](https://github.com/snehankekre/streamlit-simple-chart-titles/raw/main/streamlit-1.33.0-py2.py3-none-any.whl)
    - See the PoC implementation: https://github.com/streamlit/streamlit/compare/develop...snehan/feature/chart-titles
    """
    )

# chart_data = load_col_data()

# st.area_chart(
#     chart_data,
#     x="col1",
#     y="col2",
#     color="col3",
#     use_container_width=True,
#     x_title="This is the x-axis title",
# )


chart_data = load_data()

title = st.text_input(label="Enter the chart title", value="This is the chart title", help="This is the chart title that will be displayed on the top-left corner of the chart.")

tab1, tab2, tab3, tab4 = st.tabs(["Line Chart", "Area Chart", "Bar Chart", "Scatter Chart"])

with tab1:
    st.line_chart(
        chart_data,
        x="a",
        y="b",
        use_container_width=True,
        title=title,
    )
    st.code(
    f"""
    st.line_chart(
        chart_data,
        x="a",
        y="b",
        use_container_width=True,
        title="{title}",
    )
    """
    )

with tab2:
    st.area_chart(
        chart_data,
        use_container_width=True,
        title=title,
    )
    st.code(
    f"""
    st.area_chart(
        chart_data,
        use_container_width=True,
        title="{title}",
    )
    """
    )

with tab3:
    st.bar_chart(
        chart_data,
        use_container_width=True,
        title=title,
    )

    st.code(
    f"""
    st.bar_chart(
        chart_data,
        use_container_width=True,
        title="{title}",
    )
    """
    )
with tab4:
    st.scatter_chart(
        chart_data,
        use_container_width=True,
        title=title,
    )
    st.code(
    f"""
    st.scatter_chart(
        chart_data,
        use_container_width=True,
        title="{title}",
    )
    """
    )



