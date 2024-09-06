#Dictionary data type containing various marketing channels and their associated budgets
mkt_channel_bgts = {"Social Media": 5000,
                    "Email Marketing": 5000,
                    "Advertising": 20000}

#Array data type containing different target audiences based upon generations
target_audience = ["Gen Z", "Millennials", "Gen X"]

#Array data type containing different campaign goals
campaign_goal = ["Brand Awareness", "Lead Generation", "Sales"]

#Takes inputs from the user regarding target audience and campaign goals
user_target_audience = input("Enter your target audience (Gen Z, Millennials, Gen X): ")
user_campaign_goal = input("Enter your campaign goal (Brand Awareness, Lead Generation, Sales): ")

#If-else statements to adjust budgets according to campaign goals
if user_campaign_goal == "Brand Awareness":
  mkt_channel_bgts["Social Media"] *= 1.15
elif user_campaign_goal == "Lead Generation":
  mkt_channel_bgts["Email Marketing"] *= 1.1
else:
  mkt_channel_bgts["Social Media"] *= 1.05
  mkt_channel_bgts["Email Marketing"] *= 1.05
  mkt_channel_bgts["Advertising"] *= 1.05

#Function to calculate adjusted budgets
def calculate_budget(channel, base_budget):
  if user_target_audience == "Gen Z" and channel == "Social Media":
    base_budget *= 1.05
  elif user_target_audience == "Millennials" and channel == "Email Marketing":
    base_budget *= 1.05
  elif user_target_audience == "Gen X" and channel == "Advertising":
    base_budget *= 1.05

  return base_budget

#Empty list to define all allocated budgets
allocated_bgts = []

#For loop for calculating adjusted budgets
for channel, base_budget in mkt_channel_bgts.items():
  adj_budget = calculate_budget(channel, base_budget)
  allocated_bgts.append(adj_budget)

#Prints budget overview
print("\nBUDGET OVERVIEW ---\n")

print("Initial Budgets")
for i,j in mkt_channel_bgts.items():
  print(f"{i}: ${j}")

print("\nAllocated Budgets")
print(f"Social Media: ${allocated_bgts[0]}")
print(f"Email Marketing: ${allocated_bgts[1]}")
print(f"Advertising: ${allocated_bgts[2]}")

print("\nRemaining Budgets")
print(f"Social Media: ${mkt_channel_bgts['Social Media'] - allocated_bgts[0]}")
print(f"Email Marketing: ${mkt_channel_bgts['Email Marketing'] - allocated_bgts[1]}")
print(f"Advertising: ${mkt_channel_bgts['Advertising'] - allocated_bgts[2]}")

