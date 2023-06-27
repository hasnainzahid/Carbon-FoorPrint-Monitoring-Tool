import matplotlib.pyplot as plt

class CarbonCalculator:
    def __init__(self):
        self.constant = 12

    def get_valid_positive_float_input(self, prompt, error_message):
        """
        To get a valid input from the user.
        Will keep prompting the user until a valid input is provided.
        """
        while True:
            try:
                value = float(input(prompt))
                if value >= 0:
                    return value
                else:
                    print(error_message)
            except ValueError:
                print(error_message)

    def calculate_energy_usage(self):
        # Get input values from the user and check for valid input
        electric_bill = self.get_valid_positive_float_input("\nAvg Monthly Electric bill: ",
                                                            "Invalid input. Please enter a valid number.")
        gas_bill = self.get_valid_positive_float_input("Avg Monthly Gas bill: ",
                                                       "Invalid input. Please enter a valid number.")
        fuel_bill = self.get_valid_positive_float_input("Avg Monthly Fuel bill: ",
                                                        "Invalid input. Please enter a valid number.")

        # Perform separate calculations
        electric_bill_calc = electric_bill * 0.0005 * self.constant
        gas_bill_calc = gas_bill * 0.0053 * self.constant
        fuel_bill_calc = fuel_bill * 2.32 * self.constant

        # Final calculation
        result = electric_bill_calc + gas_bill_calc + fuel_bill_calc
        return round(result, 2)

    def calculate_waste_emissions(self):
        # Get input values from the user and check for valid input
        waste_amount = self.get_valid_positive_float_input("\nAvg Monthly Waste: ",
                                                           "Invalid input. Please enter a valid number.")
        while True:
            waste_recycled_percentage = self.get_valid_positive_float_input("Avg Monthly Waste Recycled Percentage: ",
                                                                            "Invalid input. Please enter a valid number.")
            if waste_recycled_percentage <= 100:
                break
            print("Invalid input. Please enter a value between 0 and 100.")

        # Perform separate calculations
        waste_amount_calc = waste_amount * self.constant
        waste_recycled_percentage_calc = 0.57 - (waste_recycled_percentage / 100)

        # Final calculation
        result = waste_amount_calc * waste_recycled_percentage_calc
        return round(result, 2)

    def calculate_business_travel(self):
        # Get input values from the user and check for valid input
        km_traveled_yearly = self.get_valid_positive_float_input("\nKM travelled per year for Business purposes: ",
                                                                 "Invalid input. Please enter a valid number.")
        avg_fuel_efficiency = self.get_valid_positive_float_input("Avg fuel efficiency of car per 100 KM: ",
                                                                  "Invalid input. Please enter a valid number.")
        if avg_fuel_efficiency == 0:
            raise ValueError("Invalid input. Fuel efficiency cannot be 0.")

        # Perform calculations
        avg_fuel_efficiency_calc = 1 / avg_fuel_efficiency

        # Final calculation
        result = km_traveled_yearly * avg_fuel_efficiency_calc * 2.31
        return round(result, 2)


def generate_pie_chart(energy_usage, waste_emissions, business_travel):

    # Create the data for the pie chart
    labels = ['Energy Usage', 'Waste Emissions', 'Business Travel']
    sizes = [energy_usage, waste_emissions, business_travel]

    # Find the index of the highest value
    max_index = sizes.index(max(sizes))

    # Generate the pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    # Set the font size for the labels
    plt.rcParams['font.size'] = 12
    plt.title('Carbon Emission', fontsize=16)

    # Adding comments on reducing higher values
    comments = [
        "Energy Usage - Consider reducing energy consumption by using energy-efficient appliances and renewable energy sources.",
        "Waste Emission - Increase waste recycling efforts and reduce waste generation to minimize emissions.",
        "Business Travel - Explore alternatives to business travel, such as video conferencing, to reduce carbon emissions."
    ]
    plt.text(0.1, -1.5, comments[max_index], wrap=True, horizontalalignment='center', fontsize=10)

    plt.show()


def main():
    carbon_calculator = CarbonCalculator()

    while True:
        print("\nWelcome to Carbon FootPrint Monitoring Tool")
        print("1. Calculate Energy Usage")
        print("2. Calculate Waste Emissions")
        print("3. Calculate Business Travel")
        print("4. All Calculations with Pie Chart")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            energy_usage = carbon_calculator.calculate_energy_usage()
            print("\nEnergy Carbon Emission is:", energy_usage, "KgCO2")

        elif choice == '2':
            waste_emissions = carbon_calculator.calculate_waste_emissions()
            print("\nWaste Carbon Emission is:", waste_emissions, "KgCO2")

        elif choice == '3':
            business_travel = carbon_calculator.calculate_business_travel()
            print("\nBusiness Travel Carbon Emission is:", business_travel, "KgCO2")

        elif choice == '4':
            energy_usage = carbon_calculator.calculate_energy_usage()
            print("Energy Carbon Emission is:", energy_usage, "KgCO2")
            waste_emissions = carbon_calculator.calculate_waste_emissions()
            print("Waste Carbon Emission is:", waste_emissions, "KgCO2")
            business_travel = carbon_calculator.calculate_business_travel()
            print("Business Travel Carbon Emission is:", business_travel, "KgCO2")

            # Generate and display the pie chart
            generate_pie_chart(energy_usage, waste_emissions, business_travel)

        elif choice == '5':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the main function
if __name__ == '__main__':
    main()

