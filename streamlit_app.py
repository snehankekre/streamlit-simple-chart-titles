import altair as alt
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
title = container1.text_input(
    "Enter a title for the chart", "Line Chart with Default Title"
)
st.write(
    """

    """
)
container1.line_chart(
    chart_data,
    use_container_width=True,
    title=title,
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
title = container2.text_input("Enter a title for the chart", "Line Chart title")
subtitle = container2.text_input(
    "Enter a subtitle for the chart", "With a subtitle below", help="Subtitles are displayed below the title. They are optional."
)
container2.line_chart(
    chart_data,
    use_container_width=True,
    title=alt.TitleParams(
        text=title,
        subtitle=subtitle,
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
title = container3.text_input(
    "Enter a title for the chart",
    "Centered title with custom font, size, color, and anchor",
)
fontSize = container3.slider("Font size", 1, 50, 14)
font = container3.selectbox("Font", ["Comic Sans MS", "Times New Roman", "Courier New"])
anchor = container3.selectbox(
    "Anchor",
    ["middle", "start", "end"],
    help="The anchor position for the title relative to the chart. One of 'start', 'middle', or 'end'.",
)
color = container3.selectbox(
    "Color",
    [
        "steelblue",
        "black",
        "silver",
        "gray",
        "white",
        "maroon",
        "red",
        "purple",
        "fuchsia",
        "green",
        "lime",
        "olive",
        "yellow",
        "navy",
        "blue",
        "teal",
        "aqua",
        "orange",
        "aliceblue",
        "antiquewhite",
        "aquamarine",
        "azure",
        "beige",
        "bisque",
        "blanchedalmond",
        "blueviolet",
        "brown",
        "burlywood",
        "cadetblue",
        "chartreuse",
        "chocolate",
        "coral",
        "cornflowerblue",
        "cornsilk",
        "crimson",
        "cyan",
        "darkblue",
        "darkcyan",
        "darkgoldenrod",
        "darkgray",
        "darkgreen",
        "darkgrey",
        "darkkhaki",
        "darkmagenta",
        "darkolivegreen",
        "darkorange",
        "darkorchid",
        "darkred",
        "darksalmon",
        "darkseagreen",
        "darkslateblue",
        "darkslategray",
        "darkslategrey",
        "darkturquoise",
        "darkviolet",
        "deeppink",
        "deepskyblue",
        "dimgray",
        "dimgrey",
        "dodgerblue",
        "firebrick",
        "floralwhite",
        "forestgreen",
        "gainsboro",
        "ghostwhite",
        "gold",
        "goldenrod",
        "greenyellow",
        "grey",
        "honeydew",
        "hotpink",
        "indianred",
        "indigo",
        "ivory",
        "khaki",
        "lavender",
        "lavenderblush",
        "lawngreen",
        "lemonchiffon",
        "lightblue",
        "lightcoral",
        "lightcyan",
        "lightgoldenrodyellow",
        "lightgray",
        "lightgreen",
        "lightgrey",
        "lightpink",
        "lightsalmon",
        "lightseagreen",
        "lightskyblue",
        "lightslategray",
        "lightslategrey",
        "lightsteelblue",
        "lightyellow",
        "limegreen",
        "linen",
        "magenta",
        "mediumaquamarine",
        "mediumblue",
        "mediumorchid",
        "mediumpurple",
        "mediumseagreen",
        "mediumslateblue",
        "mediumspringgreen",
        "mediumturquoise",
        "mediumvioletred",
        "midnightblue",
        "mintcream",
        "mistyrose",
        "moccasin",
        "navajowhite",
        "oldlace",
        "olivedrab",
        "orangered",
        "orchid",
        "palegoldenrod",
        "palegreen",
        "paleturquoise",
        "palevioletred",
        "papayawhip",
        "peachpuff",
        "peru",
        "pink",
        "plum",
        "powderblue",
        "rosybrown",
        "royalblue",
        "saddlebrown",
        "salmon",
        "sandybrown",
        "seagreen",
        "seashell",
        "sienna",
        "skyblue",
        "slateblue",
        "slategray",
        "slategrey",
        "snow",
        "springgreen",
        "steelblue",
        "tan",
        "thistle",
        "tomato",
        "turquoise",
        "violet",
        "wheat",
        "whitesmoke",
        "yellowgreen",
        "rebeccapurple",
    ],
)
container3.area_chart(
    chart_data,
    use_container_width=True,
    title=alt.TitleParams(
        text=title,
        fontSize=fontSize,
        font=font,
        anchor=anchor,
        color=color,
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
