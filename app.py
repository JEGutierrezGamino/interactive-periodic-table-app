import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Setup
st.set_page_config(page_title="Interactive Table of Elements", layout="wide")
st.title("Interactive Table of Elements")
st.markdown("Filter by **Period** (rows) or **Group** (columns) to explore chemical trends across all 118 elements.")

# 2. Data Dictionary for all 118 Elements
# Grid_X and Grid_Y ensure Lanthanides & Actinides don't stack on top of Group 3
data = {
    "Atomic Number": list(range(1, 119)),
    "Symbol": [
        "H", "He",
        "Li", "Be", "B", "C", "N", "O", "F", "Ne",
        "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
        "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
        "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
        "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
        "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
        "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
        "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
    ],
    "Name": [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
        "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium",
        "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
        "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
        "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin",
        "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
        "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
        "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
        "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium",
        "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
        "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium",
        "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"
    ],
    "Group": [
        1, 18,
        1, 2, 13, 14, 15, 16, 17, 18,
        1, 2, 13, 14, 15, 16, 17, 18,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
    ],
    "Period": [
        1, 1,
        2, 2, 2, 2, 2, 2, 2, 2,
        3, 3, 3, 3, 3, 3, 3, 3,
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
        6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
        7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
    ],
    "Category": [
        "Nonmetal", "Noble Gas",
        "Alkali Metal", "Alkaline Earth", "Metalloid", "Nonmetal", "Nonmetal", "Nonmetal", "Halogen", "Noble Gas",
        "Alkali Metal", "Alkaline Earth", "Post-transition Metal", "Metalloid", "Nonmetal", "Nonmetal", "Halogen", "Noble Gas",
        "Alkali Metal", "Alkaline Earth", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Post-transition Metal", "Metalloid", "Metalloid", "Nonmetal", "Halogen", "Noble Gas",
        "Alkali Metal", "Alkaline Earth", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Post-transition Metal", "Post-transition Metal", "Metalloid", "Metalloid", "Halogen", "Noble Gas",
        "Alkali Metal", "Alkaline Earth", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Lanthanide", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Post-transition Metal", "Post-transition Metal", "Post-transition Metal", "Post-transition Metal", "Halogen", "Noble Gas",
        "Alkali Metal", "Alkaline Earth", "Actinide", "Actinide", "Actinide", "Actinide", "Actinide", "Actinide", "Actinide", "Actinide", "Actinide", "Actinide", "Actinide", "Actinide", "Actinide", "Actinide", "Actinide", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Transition Metal", "Post-transition Metal", "Post-transition Metal", "Post-transition Metal", "Post-transition Metal", "Halogen", "Noble Gas"
    ],
    "Grid_X": [
        1, 18,
        1, 2, 13, 14, 15, 16, 17, 18,
        1, 2, 13, 14, 15, 16, 17, 18,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
    ],
    "Grid_Y": [
        1, 1,
        2, 2, 2, 2, 2, 2, 2, 2,
        3, 3, 3, 3, 3, 3, 3, 3,
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
        6, 6, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
        7, 7, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
    ]
}

df = pd.DataFrame(data)

# 3. Sidebar UI Controls
st.sidebar.header("Filter Elements")
selected_period = st.sidebar.selectbox("Select Period (Rows)", ["All"] + list(range(1, 8)))
selected_group = st.sidebar.selectbox("Select Group (Columns)", ["All"] + list(range(1, 19)))

# 4. Apply User Filters
filtered_df = df.copy()
if selected_period != "All":
    filtered_df = filtered_df[filtered_df["Period"] == selected_period]
if selected_group != "All":
    filtered_df = filtered_df[filtered_df["Group"] == selected_group]

# 5. Build Interactive Scatter Grid
fig = px.scatter(
    filtered_df,
    x="Grid_X",
    y="Grid_Y",
    text="Symbol",
    color="Category",
    hover_name="Name",
    hover_data={"Atomic Number": True, "Group": True, "Period": True, "Category": True, "Grid_X": False, "Grid_Y": False},
    height=600
)

# Style markers to look like periodic table tiles
fig.update_traces(
    marker=dict(size=32, symbol="square"),
    textposition="middle center",
    textfont=dict(color="white", size=11)
)

# Lock axes to mimic periodic table grid layout
fig.update_layout(
    yaxis=dict(
        autorange="reversed",
        tickmode="array",
        tickvals=[1, 2, 3, 4, 5, 6, 7, 8.5, 9.5],
        ticktext=["1", "2", "3", "4", "5", "6", "7", "La", "Ac"],
        title="Period (Electron Shells)",
        range=[0, 10.5]
    ),
    xaxis=dict(
        tickmode="linear",
        dtick=1,
        title="Group (Valence Electrons)",
        side="top",
        range=[0, 19]
    ),
    plot_bgcolor="rgba(0,0,0,0)",
    hovermode="closest"
)

# 6. Render Chart & Selected Elements Table
st.plotly_chart(fig, use_container_width=True)

st.subheader("Selected Elements Data")
st.dataframe(
    filtered_df[["Atomic Number", "Symbol", "Name", "Group", "Period", "Category"]],
    use_container_width=True,
    hide_index=True
)
