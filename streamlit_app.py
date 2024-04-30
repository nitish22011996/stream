{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f18e77dc-ed9f-41ff-a5a8-6ae6d69d862e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import folium\n",
    "\n",
    "# Load your CSV file\n",
    "def load_data():\n",
    "    df = pd.read_csv(\"F:/Downloads/Lakes_ndti.csv\")\n",
    "    return df\n",
    "\n",
    "# Title of the web application\n",
    "st.title('Lake Location Visualization')\n",
    "\n",
    "# Adding dropdowns for selecting columns\n",
    "selected_column = st.selectbox('Select a column', load_data().columns)\n",
    "\n",
    "# Adding sliders for selecting ranges\n",
    "min_value = st.slider('Select minimum value', float(load_data()[selected_column].min()), float(load_data()[selected_column].max()))\n",
    "max_value = st.slider('Select maximum value', float(load_data()[selected_column].min()), float(load_data()[selected_column].max()))\n",
    "\n",
    "# Filter the data based on selected range\n",
    "filtered_df = load_data()[(load_data()[selected_column] >= min_value) & (load_data()[selected_column] <= max_value)]\n",
    "\n",
    "# Calculate mean of latitudes and longitudes\n",
    "mean_lat = filtered_df['MEAN_X'].mean()\n",
    "mean_long = filtered_df['MEAN_Y'].mean()\n",
    "\n",
    "# Create a map centered at the mean latitude and longitude\n",
    "m = folium.Map(location=[mean_lat, mean_long], zoom_start=10)\n",
    "\n",
    "# Add markers for each location in the filtered dataframe\n",
    "for index, row in filtered_df.iterrows():\n",
    "    folium.Marker(location=[float(row['MEAN_X']), float(row['MEAN_Y'])], popup=row['Result_fie']).add_to(m)\n",
    "\n",
    "# Display the map\n",
    "st.write(m)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "4f2c0d33-c23c-4bf0-9517-665f7f84b57d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

