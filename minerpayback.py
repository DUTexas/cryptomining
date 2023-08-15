def calculate_roi(initial_investment, cash_flows, discount_rate):
    """
    Calculate ROI using discounted cash flows.
    
    Parameters:
    - initial_investment (float): The initial investment.
    - cash_flows (list of float): The estimated future cash flows.
    - discount_rate (float): The discount rate (e.g., 0.07 for 7%).
    
    Returns:
    - float: ROI as a decimal (e.g., 0.1 for 10% ROI).
    """
    npv = 0
    for t, cf in enumerate(cash_flows, 1):
        npv += cf / ((1 + discount_rate) ** t)
    
    roi = (npv - initial_investment) / initial_investment
    return roi

# Example usage:
initial_investment = 100000  # Initial investment of $100,000
cash_flows = [30000, 35000, 40000, 45000]  # Estimated cash flows for the next 4 years
discount_rate = 0.07  # 7% discount rate

roi = calculate_roi(initial_investment, cash_flows, discount_rate)
print(f"ROI: {roi * 100:.2f}%")

