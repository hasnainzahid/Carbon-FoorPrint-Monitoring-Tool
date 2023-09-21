import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CarbonEmissionCalculator:
    def __init__(self):
        self.constant = 12

    def calculate_energy_emission(self, electric_bill, gas_bill, fuel_bill):
        electric_carbon_emission = max(electric_bill, 0) * 0.0005 * self.constant
        gas_carbon_emission = max(gas_bill, 0) * 0.0053 * self.constant
        fuel_carbon_emission = max(fuel_bill, 0) * 2.32 * self.constant
        total_carbon_emission = electric_carbon_emission + gas_carbon_emission + fuel_carbon_emission
        return round(total_carbon_emission, 2)

    def calculate_waste_emission(self, waste_amount, recycling_percentage):
        waste_carbon_emission = max(waste_amount, 0) * self.constant * (0.57 - (max(recycling_percentage, 0) / 100))
        return round(waste_carbon_emission, 2)

    def calculate_travel_emission(self, kilometers_traveled_per_year, average_fuel_efficiency):
        average_fuel_efficiency_calc = 1 / max(average_fuel_efficiency, 0.001)
        total_carbon_emission = max(kilometers_traveled_per_year, 0) * average_fuel_efficiency_calc * 2.31
        return round(total_carbon_emission, 2)


class CarbonEmissionApp:
    def __init__(self, master):
        self.master = master
        master.title("Carbon Emission Calculator")
        self.emission_calculator = CarbonEmissionCalculator()
        self.create_layout()

    def create_layout(self):
        # Input box
        self.input_frame = tk.Frame(self.master, padx=20, pady=10, bd=1, relief=tk.RIDGE)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)

        # Energy Emission Section
        tk.Label(self.input_frame, text="Energy Emission", font=("Arial", 14, "bold")).grid(row=0, column=0,
                                                                                            columnspan=2, pady=(0, 10))

        tk.Label(self.input_frame, text="Electric Bill:").grid(row=1, column=0)
        self.electric_bill_entry = tk.Entry(self.input_frame)
        self.electric_bill_entry.grid(row=1, column=1)

        tk.Label(self.input_frame, text="Gas Bill:").grid(row=2, column=0)
        self.gas_bill_entry = tk.Entry(self.input_frame)
        self.gas_bill_entry.grid(row=2, column=1)

        tk.Label(self.input_frame, text="Fuel Bill:").grid(row=3, column=0)
        self.fuel_bill_entry = tk.Entry(self.input_frame)
        self.fuel_bill_entry.grid(row=3, column=1)

        self.calculate_energy_button = tk.Button(self.input_frame, text="Calculate Energy Emission",
                                                 command=self.calculate_energy)
        self.calculate_energy_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

        # Waste Emission Section
        tk.Label(self.input_frame, text="Waste Emission", font=("Arial", 14, "bold")).grid(row=5, column=0,
                                                                                           columnspan=2, pady=(20, 10))

        tk.Label(self.input_frame, text="Waste Amount:").grid(row=6, column=0)
        self.waste_amount_entry = tk.Entry(self.input_frame)
        self.waste_amount_entry.grid(row=6, column=1)

        tk.Label(self.input_frame, text="Recycling Percentage:").grid(row=7, column=0)
        self.recycling_percentage_entry = tk.Entry(self.input_frame)
        self.recycling_percentage_entry.grid(row=7, column=1)

        self.calculate_waste_button = tk.Button(self.input_frame, text="Calculate Waste Emission",
                                                command=self.calculate_waste)
        self.calculate_waste_button.grid(row=8, column=0, columnspan=2, pady=(10, 0))

        # Travel Emission Section
        tk.Label(self.input_frame, text="Travel Emission", font=("Arial", 14, "bold")).grid(row=9, column=0,
                                                                                            columnspan=2, pady=(20, 10))

        tk.Label(self.input_frame, text="Kilometers Traveled:").grid(row=10, column=0)
        self.kilometers_entry = tk.Entry(self.input_frame)
        self.kilometers_entry.grid(row=10, column=1)

        tk.Label(self.input_frame, text="Fuel Efficiency:").grid(row=11, column=0)
        self.fuel_efficiency_entry = tk.Entry(self.input_frame)
        self.fuel_efficiency_entry.grid(row=11, column=1)

        self.calculate_travel_button = tk.Button(self.input_frame, text="Calculate Travel Emission",
                                                 command=self.calculate_travel)
        self.calculate_travel_button.grid(row=12, column=0, columnspan=2, pady=(10, 0))

        # Calculate All Button
        self.calculate_all_button = tk.Button(self.input_frame, text="Calculate All Emissions",
                                              command=self.calculate_all_emissions)
        self.calculate_all_button.grid(row=15, column=0, columnspan=2, pady=(10, 0))

        # Pie Chart Display Box
        self.pie_chart_frame = tk.Frame(self.master, padx=20, pady=10, bd=1, relief=tk.RIDGE)
        self.pie_chart_frame.grid(row=0, column=1, padx=10, pady=(0, 10), sticky=tk.NSEW)

        # Result box
        self.result_frame = tk.Frame(self.master, padx=20, pady=10, bd=1, relief=tk.RIDGE)
        self.result_frame.grid(row=1, column=1, padx=10, pady=(10, 0), sticky=tk.NSEW)

        tk.Label(self.result_frame, text="Results", font=("Arial", 14, "bold")).pack(pady=(0, 10))

        self.result_label = tk.Label(self.result_frame, text="")
        self.result_label.pack(fill=tk.BOTH, expand=True)

        # Configure the result box to have a maximum height of 100 pixels
        self.result_frame.update_idletasks()  # Update the display to get accurate height
        self.result_frame.config(
            height=min(10, self.result_frame.winfo_height()))

    def calculate_energy(self):
        try:
            electric_bill = float(self.electric_bill_entry.get())
            if electric_bill < 0:
                raise ValueError("Electric Bill should be non-negative")
            gas_bill = float(self.gas_bill_entry.get())
            if gas_bill < 0:
                raise ValueError("Gas Bill should be non-negative")
            fuel_bill = float(self.fuel_bill_entry.get())
            if fuel_bill < 0:
                raise ValueError("Fuel Bill should be non-negative")
            energy_emission = self.emission_calculator.calculate_energy_emission(electric_bill, gas_bill, fuel_bill)
            self.result_label.config(text=f"Energy Carbon Emission: {energy_emission} KgCO2")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for energy calculation.")

    def calculate_waste(self):
        try:
            waste_amount = float(self.waste_amount_entry.get())
            if waste_amount < 0:
                raise ValueError("Waste Amount should be non-negative")
            recycling_percentage = float(self.recycling_percentage_entry.get())
            if recycling_percentage < 0 or recycling_percentage > 100:
                raise ValueError("Recycling Percentage should be between 0 and 100")
            waste_emission = self.emission_calculator.calculate_waste_emission(waste_amount, recycling_percentage)
            self.result_label.config(text=f"Waste Carbon Emission: {waste_emission} KgCO2")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for waste calculation.")

    def calculate_travel(self):
        try:
            kilometers_traveled = float(self.kilometers_entry.get())
            if kilometers_traveled < 0:
                raise ValueError("Kilometers Amount should be non-negative")
            fuel_efficiency = float(self.fuel_efficiency_entry.get())
            if fuel_efficiency < 0:
                raise ValueError("Fuel Efficiency Amount should be non-negative")
            travel_emission = self.emission_calculator.calculate_travel_emission(kilometers_traveled, fuel_efficiency)
            self.result_label.config(text=f"Travel Carbon Emission: {travel_emission} KgCO2")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for travel calculation.")

    def display_pie_chart(self, emission_data):
        labels = ['Energy', 'Waste', 'Travel']
        sizes = [emission_data['energy'], emission_data['waste'], emission_data['travel']]
        colors = ['#ff9999', '#66b3ff', '#99ff99']
        explode = (0.1, 0, 0)  # explode the 1st slice (i.e., 'Energy')

        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        pie_chart_canvas = FigureCanvasTkAgg(fig, master=self.pie_chart_frame)
        pie_chart_canvas.draw()
        pie_chart_canvas.get_tk_widget().grid(row=0, column=0)

    def calculate_all_emissions(self):
        try:
            electric_bill = float(self.electric_bill_entry.get())
            gas_bill = float(self.gas_bill_entry.get())
            fuel_bill = float(self.fuel_bill_entry.get())
            waste_amount = float(self.waste_amount_entry.get())
            recycling_percentage = float(self.recycling_percentage_entry.get())
            kilometers_traveled = float(self.kilometers_entry.get())
            fuel_efficiency = float(self.fuel_efficiency_entry.get())

            energy_emission = self.emission_calculator.calculate_energy_emission(electric_bill, gas_bill, fuel_bill)
            waste_emission = self.emission_calculator.calculate_waste_emission(waste_amount, recycling_percentage)
            travel_emission = self.emission_calculator.calculate_travel_emission(kilometers_traveled, fuel_efficiency)

            # Display results and pie chart
            emission_data = {'energy': energy_emission, 'waste': waste_emission, 'travel': travel_emission}
            self.result_label.config(text=f"Energy Carbon Emission: {energy_emission} KgCO2\n"
                                          f"Waste Carbon Emission: {waste_emission} KgCO2\n"
                                          f"Travel Carbon Emission: {travel_emission} KgCO2")
            self.display_pie_chart(emission_data)

        except ValueError as e:
            messagebox.showerror("Error", f"Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CarbonEmissionApp(root)
    root.mainloop()
