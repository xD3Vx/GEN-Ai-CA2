# 2. Parse the dataset to fill the dictionary with available symptoms
for index, row in base_data_set_full.iterrows():
    symptom_dict['Symptom 1'].append(row['Symptoms - 1'])
    symptom_dict['Symptom 2'].append(row['Symptoms - 2'])
    symptom_dict['Symptom 3'].append(row['Symptoms - 3'])

# Check for missing data
# Identify columns with missing data (Loss)
missing_columns = base_data_set_full.columns[base_data_set_full.isnull().any()]
# Printing out the "Loss" (columns with missing values)
print("Loss - Columns with missing data:")
print(missing_columns)

# Define the list of other symptoms that need to be added
other_symptoms = ['Body Ache', 'Shivering', 'Head Ache', 'Nausia', 'Sickness', 'Vertigo', 'Head Ache', 'Nausia', 'Sickness', 'Vertigo, Nausia']

# Adding other symptoms to the dictionary as a new symptom set
symptom_dict['Other Symptoms'] = set(other_symptoms)  # Using set to ensure uniqueness

# Enhancing the Dictionary with data from the dataset
# We'll check for any data in the 'Other Symptoms' column and dynamically add it
for index, row in base_data_set_full.iterrows():
    if pd.notna(row['Other Symptoms']):
        symptom_dict[f'S{len(symptom_dict)}'] = {row['Other Symptoms']}

# Print the enhanced dictionary with the required format
print("\nEnhanced Symptom Dictionary with Other Symptoms included:")
for key, value in symptom_dict.items():
    print(f"{key}: {value}")
