import pandas as pd
import json

# Step 1: Function to read data in various formats (CSV, TSV, JSON, XML, Excel)
def read_data(file_path, file_type):
    if file_type == 'excel':
        return pd.read_excel(file_path, sheet_name=None)  # Read all sheets into a dictionary
    elif file_type == 'csv':
        return pd.read_csv(file_path)
    elif file_type == 'tsv':
        return pd.read_csv(file_path, sep='\t')
    elif file_type == 'json':
        return pd.read_json(file_path)
    elif file_type == 'xml':
        return pd.read_xml(file_path)
    else:
        raise ValueError("Unsupported file type")

# Step 2: Function to enhance the dictionary based on new data
def enhance_dictionary(base_dict, new_data):
    for _, row in new_data.iterrows():
        # Ensure the column name is correct
        symptoms = row['Observation'].split(', ') if 'Observation' in row else []
        for symptom in symptoms:
            if symptom not in base_dict:
                base_dict[symptom] = {}  # Initialize empty dict for new symptoms
            # Here you could add further attributes if necessary
    return base_dict

# Step 3: Function to print the data sets
def print_data_sets(data):
    print(data)

# Step 4: Function to dump the dictionary to a file
def dump_dictionary(base_dict, file_name):
    # Convert sets to lists
    dict_to_dump = {key: list(value) for key, value in base_dict.items()}
    with open(file_name, 'w') as file:
        json.dump(dict_to_dump, file, indent=4)


# Step 5: Function for manual editing of the dictionary
def edit_dictionary(base_dict, symptom, attributes):
    if symptom in base_dict:
        base_dict[symptom].update(attributes)
    else:
        print(f"Symptom {symptom} not found in the dictionary.")

# Example usage
base_dictionary = {
    'S1': {'Fever: mild', 'Fever: low', 'Fever: high'},
    'S2': {'Cough: mild', 'Cough: low', 'Cough: high'},
    'S3': {'Cold: mild', 'Cold: low', 'Cold: high'},
    'S4': {'Body Ache'},
    'S5': {'Cold'},
    'S6': {'Shivering: mild', 'Shivering: high', 'Shivering: Intermittent'}
}

# Specify the correct file path and file type
file_path = 'Auto_Regressive_Model_Diffusion_Model_V_1.0.xlsx'  # Path to your file
file_type = 'excel'  # Specify file type as 'excel'

# Read the data from the Excel file
data = read_data(file_path, file_type)

# Assuming the first sheet is where the relevant data is
sheet_name = list(data.keys())[0]  # Get the first sheet name
new_data = data[sheet_name]  # Extract the DataFrame from the sheet

# Print the columns of the DataFrame to check for 'Observation'
print("Columns in the DataFrame:")
print(new_data.columns)

# Enhance the dictionary
enhanced_dictionary = enhance_dictionary(base_dictionary, new_data)

# Print the enhanced dictionary
print("\nEnhanced Dictionary:")
print(enhanced_dictionary)

# Print the data sets
print("\nData Sets:")
print_data_sets(new_data)

# Dump the dictionary to a JSON file
dump_dictionary(enhanced_dictionary, 'enhanced_dictionary.json')

# Example of manual editing
edit_dictionary(enhanced_dictionary, 'Fever: mild', {'Severity': 'Medium'})
print("\nDictionary after manual editing:")
print(enhanced_dictionary)

# Manual re-parsing of data could be done by re-running read_data and enhance_dictionary functions
