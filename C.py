import altair as alt
import pandas as pd

# 1. Configuration
A = 7
limit = 100
output_filename = "altair_multiples_perfect.png"

# 2. Prepare the Data
df = pd.DataFrame({
    'number': range(1, limit + 1),
    'is_multiple': [(i % A == 0) for i in range(1, limit + 1)]
})

# 3. Create the Base Block Chart
blocks = alt.Chart(df).mark_rect().encode(
    y=alt.Y('number:O', 
            title=None, 
            sort='descending', 
            # FIXED: 'labelPadding' is the correct parameter name
            axis=alt.Axis(labelFontSize=8, tickSize=0, labelPadding=15)),
    x=alt.value(25), 
    x2=alt.value(65), 
    color=alt.condition(
        alt.datum.is_multiple,
        alt.Color('number:Q', scale=alt.Scale(scheme='rainbow'), legend=None),
        alt.value('white')
    ),
    tooltip=['number']
)

# 4. Add the Dot Layer
dots = alt.Chart(df.query('is_multiple')).mark_point(
    filled=True, 
    color='#8B4513', 
    size=40
).encode(
    y=alt.Y('number:O', sort='descending'),
    x=alt.value(45) 
)

# 5. Combine and Style
final_plot = (blocks + dots).properties(
    width=100,
    height=alt.Step(18) 
).configure_view(
    strokeWidth=0
).configure_axis(
    grid=False,
    domain=False
)

# --- THE SAVE LOGIC ---
try:
    final_plot.save(output_filename, engine="vl-convert")
    print(f"✨ Success! Plot is now flipped (1 at bottom) and saved as {output_filename}")
except Exception as e:
    print(f"❌ Error saving: {e}")
