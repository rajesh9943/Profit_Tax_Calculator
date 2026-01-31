import streamlit as st

st.set_page_config(page_title="Trading Tax & Profit Calculator", layout="centered")

# ===== Custom Button Styling =====
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        background-color: #1f77ff;
        color: white;
        font-size: 18px;
        font-weight: 600;
        padding: 0.6em 1em;
        border-radius: 8px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #155dcc;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Trading Capital & Profit Tax Calculator")
st.markdown("Calculate required capital, profit, tax, and net returns of your trade.")

# ================= ENTRY SECTION =================
st.header("Entry Details")

cmp = st.number_input("Entry Market Price", min_value=0.0, step=0.1)
quantity = st.number_input("Quantity", min_value=0, step=1)

# ================= EXIT SECTION =================
st.header("Exit & Tax Calculator (Optional)")

exit_price = st.number_input("Exit Price", min_value=0.0, step=0.1)
tax_percent = st.number_input("Tax Percentage (%)", min_value=0.0, max_value=100.0, step=0.1)

# ================= CALCULATE BUTTON =================
calculate = st.button("Calculate", use_container_width=True)

# ================= CALCULATIONS =================
if calculate:

    # Case 1: Only Entry Data
    if cmp > 0 and quantity > 0 and exit_price == 0:
        capital_required = cmp * quantity

        st.header("Results")
        st.write(f"**Capital Required:** ₹ {capital_required:,.2f}")
        st.info("Enter Exit Price to calculate profit.")

    # Case 2: Entry + Exit Price (Before Tax)
    elif cmp > 0 and quantity > 0 and exit_price > 0 and tax_percent == 0:
        capital_required = cmp * quantity
        gross_profit = (exit_price - cmp) * quantity
        profit_percent = (gross_profit / capital_required) * 100 if capital_required > 0 else 0

        st.header("Results")
        st.write(f"**Capital Required:** ₹ {capital_required:,.2f}")
        st.write(f"**Gross Profit:** ₹ {gross_profit:,.2f}")
        st.write(f"**Profit Percentage (Before Tax):** {profit_percent:.2f}%")
        st.info("Enter tax % to see net profit after tax.")

    # Case 3: Entry + Exit + Tax
    elif cmp > 0 and quantity > 0 and exit_price > 0 and tax_percent > 0:
        capital_required = cmp * quantity
        gross_profit = (exit_price - cmp) * quantity
        tax_amount = gross_profit * (tax_percent / 100)
        net_profit = gross_profit - tax_amount
        profit_percent = (net_profit / capital_required) * 100 if capital_required > 0 else 0

        st.header("Results")
        st.write(f"**Capital Required:** ₹ {capital_required:,.2f}")
        st.write(f"**Gross Profit:** ₹ {gross_profit:,.2f}")
        st.write(f"**Tax Amount:** ₹ {tax_amount:,.2f}")
        st.write(f"**Net Profit After Tax:** ₹ {net_profit:,.2f}")
        st.write(f"**Net Profit Percentage:** {profit_percent:.2f}%")

        if net_profit > 0:
            st.success("✅ This trade is profitable after tax.")
        elif net_profit < 0:
            st.error("❌ This trade results in a loss.")
        else:
            st.info("⚖️ Break-even trade.")

    else:
        st.warning("Please enter at least Current Market Price and Quantity.")
