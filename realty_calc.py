def calculate_monthly_mortgage(principal: float, annual_rate: float, years: int) -> float:
    """Calculates monthly mortgage payment given loan principal, interest rate, and term."""
    monthly_rate = (annual_rate / 100) / 12
    total_payments = years * 12
    if monthly_rate == 0:
        return principal / total_payments
    return principal * (monthly_rate * (1 + monthly_rate)**total_payments) / ((1 + monthly_rate)**total_payments - 1)

def calculate_gross_yield(annual_rent: float, property_price: float) -> float:
    """Calculates gross rental yield percentage."""
    return (annual_rent / property_price) * 100

def calculate_future_value(current_value: float, annual_appreciation_rate: float, years: int) -> float:
    """Calculates estimated future property value based on annual appreciation rate."""
    return current_value * ((1 + (annual_appreciation_rate / 100)) ** years)

if __name__ == "__main__":
    property_price = 350000.0
    down_payment = 70000.0
    loan_amount = property_price - down_payment
    interest_rate = 6.5  # 6.5%
    loan_years = 30
    expected_monthly_rent = 2400.0
    appreciation_rate = 4.0  # 4% annual growth
    holding_period = 10  # 10 years

    monthly_payment = calculate_monthly_mortgage(loan_amount, interest_rate, loan_years)
    rental_yield = calculate_gross_yield(expected_monthly_rent * 12, property_price)
    future_val = calculate_future_value(property_price, appreciation_rate, holding_period)

    print(f"🏠 Property Value: ${property_price:,.2f}")
    print(f"💵 Monthly Mortgage: ${monthly_payment:,.2f}")
    print(f"📈 Gross Rental Yield: {rental_yield:.2f}%")
    print(f"🚀 Estimated Value in {holding_period} Years: ${future_val:,.2f}")
