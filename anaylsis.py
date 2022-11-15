import csv


list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)

# 0. Print out how many rows your data contains
print(len(list_data)) 

# 1. Filter a state in "list_data" to only contain that state
CA_state_data = [row for row in list_data if row["STATE"] == "CALIFORNIA"]
print(len(CA_state_data))

# 2. Decide which one of these columns you want to analyze -> California 
# 3. Filter out 'state-data' to only contain dictionaries that contain values for 'AVG_MATH_4_SCORE'
CA_AVG_MATH_SCORE = [float(row["AVG_MATH_4_SCORE"]) for row in CA_state_data if row["AVG_MATH_4_SCORE"]]
print(CA_AVG_MATH_SCORE)
# 4. Print out how many rows your data contains after filtering 
print(len(CA_AVG_MATH_SCORE))
# 5. Document your code 

# average of CA math 4 score
print(sum(CA_AVG_MATH_SCORE)/(len(CA_AVG_MATH_SCORE))) # sum divided by the number of rows the data contains after filtering




# Get Available Years

years = [row["YEAR"] for row in CA_state_data if row["STATE"] == "CALIFORNIA" and row["AVG_MATH_4_SCORE"]]

# Percent Change
def percent_change(data, year1, year2, column):
    """ Calculate percent change 
    
    Parameters
    ----------
    data: list
        Education data throughout the U.S.
    year1: str
        A year that you're comparing it to, initial year
    year2: str 
        Secondary year value
    column: str
        column describingf actual score for year 

    Returns
    -------
    float 
        percent change 
    
    """
    old = 0
    new = 0
    for row in data:
        if row["YEAR"] == year1:
            old = row[column]
        if row["YEAR"] == year2:
            new = row[column]
            
    return ((float(old) - float(new))/float(old))*100

# test code 
print(percent_change(CA_state_data,"2017","2019","AVG_MATH_4_SCORE"))

# Applying Percent Change

for i in range(len(years) - 1):
    year1 = years[i]
    year2 = years[i+1]
    change = percent_change(CA_state_data, year1, year2,"AVG_MATH_4_SCORE")
    # Calculate the percent change by calling percent change function
    print(f"CA percent change from {year1} - {year2} is {round(change,2)}")

    

