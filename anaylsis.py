import csv

list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)

# Step 5
# 0. Print out how many rows your data contains
print(len(list_data)) 

# 1. Filter a state in "list_data" to only contain that state
CA_state_data = [row for row in list_data if row["STATE"] == "CALIFORNIA"]
print(len(CA_state_data))

# 2. Decide which one of these columns you want to analyze -> California 
# 3. Filter out 'state-data' to only contain dictionaries that contain values for 'AVG_MATH_4_SCORE'
CA_AVG_MATH_SCORE = [float(row["AVG_MATH_4_SCORE"]) for row in CA_state_data if row["AVG_MATH_4_SCORE"]]

# 4. Print out how many rows your data contains after filtering 
print(len(CA_AVG_MATH_SCORE))
# 5. Document your code 

# average of CA math 4 score
print(sum(CA_AVG_MATH_SCORE)/(len(CA_AVG_MATH_SCORE))) # sum divided by the number of rows the data contains after filtering



