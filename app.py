# Import the Streamlit library and alias it as 'st' for easier use
import streamlit as st
# Import the convert_temperature function from the converter module
from converter import convert_temperature

# Configure the Streamlit page with a custom title and icon
# page_title: Sets the title that appears in the browser tab
# page_icon: Sets the emoji icon that appears in the browser tab
st.set_page_config(page_title="Konwerter jednostek v1.01", page_icon="🌡️")

# Display a main heading on the page with an emoji and text
st.title("🌡️ Konwerter temperatury v1.01")

# Create a number input widget for users to enter temperature values
# This creates a text field that only accepts numerical input
value = st.number_input("Wprowadź wartość temperatury:")

# Create a dropdown selection box for the source temperature unit
# Users can choose from Celsius, Fahrenheit, or Kelvin
from_unit = st.selectbox("Z jednostki:", ["Celsius", "Fahrenheit", "Kelvin"])

# Create a dropdown selection box for the target temperature unit
# Users can choose from Celsius, Fahrenheit, or Kelvin
to_unit = st.selectbox("Na jednostkę:", ["Celsius", "Fahrenheit", "Kelvin"])

# Check if the "Konwertuj" (Convert) button has been clicked
if st.button("Konwertuj"):
    # If button is clicked, call the convert_temperature function with the user's inputs
    # This function takes the value and converts it from from_unit to to_unit
    result = convert_temperature(value, from_unit, to_unit)
    
    # Display the conversion result in a success message box
    # f-string formatting is used to show the original value, units, and converted result
    # .2f formats the result to show only 2 decimal places
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")