# type: ignore
# flake8: noqa
# Step 1: Remove 'k' and multiply those values by 1000
def convert_k_to_numeric(val):
    if isinstance(val, str) and 'k' in val.lower():
        return float(val.lower().replace('k', '')) * 1000
    return val  # return original value if no 'k'

# Step 2: Apply the function to the column
panel["gdp_pcapita"] = panel["gdp_pcapita"].apply(convert_k_to_numeric)


