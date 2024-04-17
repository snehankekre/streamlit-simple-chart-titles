import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


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


st.subheader("Customizing Chart Titles for Streamlit's simple charts")

with st.expander("Context :books:"):
    st.write(
        """
    Streamlit's [simple charts](https://docs.streamlit.io/develop/api-reference/charts#simple-chart-elements) (line, area, bar, scatter) have a `title` parameter that allows you to customize the chart title.

    | Parameter | Description |
    | --- | --- |
    | `title` *(str, alt.TitleParams, or None)* | The title of the chart. If a string, it will be used as the title text. To further customize the title (e.g. add a subtitle, change font size, etc.), pass an [`alt.TitleParams`](https://altair-viz.github.io/user_guide/generated/core/altair.TitleParams.html) object. If None, no title will be displayed. |


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
#     title_x="This is the x-axis title",
# )


chart_data = load_data()


container1 = st.container(border=True)
container1.line_chart(
    chart_data,
    use_container_width=True,
    title="Line Chart with Default Title",
)

st.code(
    """
st.line_chart(
    chart_data,
    use_container_width=True,
    title="Line Chart with Default Title",
)
"""
)

container2 = st.container(border=True)

container2.line_chart(
    chart_data,
    use_container_width=True,
    title=alt.TitleParams(
        text="Line Chart title",
        subtitle="With a subtitle below",
    ),
)

st.code(
    """
st.line_chart(
    chart_data,
    use_container_width=True,
    title=alt.TitleParams(
        text="Line Chart title",
        subtitle="With a subtitle below",
    ),
)
"""
)

container3 = st.container(border=True)

container3.area_chart(
    chart_data,
    use_container_width=True,
    title=alt.TitleParams(
        text="Centered title with custom font, size, color, and anchor",
        fontSize=14,
        font="Comic Sans MS",
        anchor="middle",
        color="steelblue",
    ),
)

st.code(
    """
st.area_chart(
    chart_data,
    use_container_width=True,
    title=alt.TitleParams(
        text="Centered title with custom font, size, color, and anchor",
        fontSize=14,
        font="Comic Sans MS",
        anchor="middle",
        color="steelblue",
    ),
)
"""
)

container4 = st.container(border=True)

container4.bar_chart(
    chart_data,
    use_container_width=True,
    title=alt.TitleParams(
        text="Bar Chart title centered at the bottom",
        orient="bottom",
        anchor="middle",
    ),
)

st.code(
    """
st.bar_chart(
    chart_data,
    use_container_width=True,
    title=alt.TitleParams(
        text="Bar Chart title centered at the bottom",
        orient="bottom",
        anchor="middle",
    ),
)
"""
)
