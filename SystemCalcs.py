# Methodology at: https://www.gogreensolar.com/pages/sizing-solar-systems#:~:text=%20How%20to%20Size%20a%20Solar%20System%20in,Your%20Solar%20Panels%20Will%20Receive%0ASunlight%20availability...%20More%20

# Determine your Average Monthly kWh Usage
avgMnthlyUsage = 970 # kWh per month

# Calculate your daily kWh usage
dailyUsage = round(avgMnthlyUsage / 30.41, 2) 

# Estimate the amount of sunlight your solar panels can recieve
sunhoursPerDay = 5.25 

# Size of Solar Array needed:
solarArraySize = round(dailyUsage / sunhoursPerDay, 2)

# Account for inefficiencies (assuming degradation to 80% after 25 years)
adjustedArraySize = round(solarArraySize * 1.2, 2)

# Supposing that I only want to offset part of my electric bill initially. 
pctOffset = 82 # percent
solarArraySize = round(pctOffset * solarArraySize /100.0, 2)
adjustedArraySize = round(pctOffset * adjustedArraySize / 100.0, 2)

# Determine how many Solar Panels needed
panelRatedWattage = 460 # watts
numberOfPanels = round(adjustedArraySize * 1000.00 / panelRatedWattage, 0)

# Cost of panels from Signature Solar
panelPrice = 271.40 # dollars each
panelsCost = round(numberOfPanels * panelPrice * 1.0825, 2)

# Output:
print("\nAvg Monthly kWh Usage: ", avgMnthlyUsage, " kWh per month")
print("Daily kWh Usage: ", dailyUsage, " kWh per day")
print("Hours of sunlight per day at my location: ", sunhoursPerDay, " hrs per day") 
print("Percent of electric bill being offset by solar system: ", pctOffset, " %")
print("Size of Solar Array needed : ", solarArraySize, " kW of panels") 
print("Adjusted Size of Solar Array needed : ", adjustedArraySize, " kW of panels") 
print("\nNumber of ", panelRatedWattage, " Watt panels needed: ", numberOfPanels)
print("Cost of the solar panels from Signature Solar: $", panelsCost, " including taxes")