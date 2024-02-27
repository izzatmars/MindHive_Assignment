import streamlit as st
import requests
import folium
from streamlit_folium import folium_static

def fetch_outlets():
    response = requests.get("http://127.0.0.1:5000/outlets")  # Adjust URL as needed
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch outlet data")
        return []
    
def main():
    st.title("Outlet Map")

    # Fetch outlet data
    outlets = fetch_outlets()

    # Create a map centered at Kuala Lumpur
    m = folium.Map(location=[3.139, 101.6869], zoom_start=12)

    # Add markers for each outlet
    for outlet in outlets:
        folium.Marker(location=[outlet['latitude'], outlet['longitude']],
                      popup=outlet['name']).add_to(m)

    # Render the map
    folium_static(m)

if __name__ == "__main__":
    main()