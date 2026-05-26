import matplotlib.pyplot as plt
import plotly.express as px
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent / "src"))

from data_wrangling import (
    sale_stores_for_graph,
)

sales_graph = px.scatter(
    sale_stores_for_graph,
    x='store_id',
    y='total_sales',
    title='Revenue by Store',
    labels={'store_id': 'Store ID', 'total_sales': 'Total Sales'},
)

sales_graph.show()