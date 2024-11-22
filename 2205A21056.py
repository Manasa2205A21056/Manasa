import streamlit as st
import math

# Function to calculate resistance and reactance
def Tran_Eff(V0, I0, W0):
    NPF = W0 / (V0 * I0)
    Iμ = I0 * math.sqrt(1 - NPF**2)
    Iw = I0 * NPF
    R0 = V0 / Iw
    X0 = V0 / Iμ
    return R0, X0

# Web application title
st.title('2205A21056-PS7')
st.write("calculate the resistance R0(and reactance X0 of a transformer based on open cirvuit measurements like V0,I0 and W0)")

# Input fields
V0 = st.number_input('Voltage (V0)', value=230)
I0 = st.number_input('Current (I0) in Amps', value=5)
W0 = st.number_input('Power (W0) in Watts', value=100)

# Calculate resistance and reactance
if st.button('Calculate'):
    R0, X0 = Tran_Eff(V0, I0, W0)
    R0_kohms = R0 / 1000
    X0_kohms = X0 / 1000
    st.write(f'Resistance (R0): {R0_kohms:.2f} kΩ')
    st.write(f'Reactance (X0): {X0_kohms:.2f} kΩ')