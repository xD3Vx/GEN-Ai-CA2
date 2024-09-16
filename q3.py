class VehicleInsurance:
    def __init__(self, vehicle_value, insurance_years, monthly_rate):
        self.initial_value = vehicle_value
        self.years = insurance_years
        self.monthly_rate = monthly_rate

    def calculate_depreciation(self, year):
        
        depreciated_value = self.initial_value * ((1 - 0.07) ** year)
        return depreciated_value

    def premium_chart(self):
        
        chart = []
        for year in range(1, self.years + 1):
            yearly_value = self.calculate_depreciation(year)
            yearly_premium = yearly_value * self.monthly_rate * 12
            quarterly_premium = yearly_premium / 4
            monthly_premium = yearly_premium / 12

            chart.append({
                "Year": year,
                "Depreciated Vehicle Value": round(yearly_value, 2),
                "Monthly Premium": round(monthly_premium, 2),
                "Quarterly Premium": round(quarterly_premium, 2),
                "Yearly Premium": round(yearly_premium, 2)
            })
        return chart
