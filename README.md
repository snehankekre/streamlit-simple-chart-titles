# streamlit-simple-chart-titles

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://simple-chart-titles-demo.streamlit.app)

Streamlit's [simple charts](https://docs.streamlit.io/develop/api-reference/charts#simple-chart-elements) (line, area, bar, scatter) have a `title` parameter that allows you to customize the chart title.

| Parameter | Description |
| --- | --- |
| `title` | The title of the chart. If a string, it will be used as the title text. To further customize the title (e.g. add a subtitle, change font size, etc.), pass an [`alt.TitleParams`](https://altair-viz.github.io/user_guide/generated/core/altair.TitleParams.html) object. If None, no title will be displayed. |

See the [PoC implementation](https://github.com/streamlit/streamlit/compare/develop...snehan/feature/chart-titles)



