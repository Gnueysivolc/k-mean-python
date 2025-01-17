import plotly.graph_objects as go
import numpy as np

# Set the circle properties
circle_x = 250
circle_y = 250
circle_radius = 150

# Create the figure
fig = go.Figure()
# Draw the circle
thetta = np.linspace(0, 2 * np.pi, 200)
x = circle_x + circle_radius * np.cos(thetta)
y = circle_y + circle_radius * np.sin(thetta)
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='black', width=2)))

# Function to generate and draw random points
def generate_points():
    # Generate random points
    x = np.random.randint(0, 500, 1)
    y = np.random.randint(0, 500, 1)

    # Check if the point is inside the circle
    distance = np.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= circle_radius:
        # Point is inside the circle, display it in green
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='green', size=2)))
    else:
        # Point is outside the circle, display it in red
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='red', size=2)))

    # Update the figure
    fig.update_layout(
    title='circle data', 
    xaxis=dict(
            range=[0, 819.1],
            anchor='x',
            showgrid=False,
            zeroline=False
        ),
        yaxis=dict(
            range=[0, 500],
            anchor='y',
            showgrid=False,
            zeroline=False
        ),
    barmode='overlay', 
    plot_bgcolor='rgb(245,245,245)',
    legend=dict(
        x=0.02,
        y=0.95),
    margin=dict(t=0, b=0, l=0, r=0)
)

    


# Generate and display points continuously
for i in range(10000):
    generate_points()


fig.show(config={'displayModeBar': False})
fig.write_html('circle_in_square.html')
