import csv
import re

def clean_and_filter_csv(input_file, output_file, min_length=12):
    # Define the regular expression pattern to remove unwanted characters
    clean_pattern = re.compile('[,."\'\n\r:]')

    with open(input_file, 'r', newline='', encoding='utf-8') as csv_input:
        # Create a CSV reader
        reader = csv.reader(csv_input)

        with open(output_file, 'w', newline='', encoding='utf-8') as csv_output:
            # Create a CSV writer
            writer = csv.writer(csv_output)

            # Iterate through each row in the input CSV
            for row in reader:
                # Apply the clean_pattern to each element in the row
                cleaned_row = [clean_pattern.sub('', element) for element in row]

                # Check if the length of the cleaned cell is greater than or equal to min_length
                filtered_row = [cell for cell in cleaned_row if len(cell) >= min_length]

                # Write the filtered row to the output CSV
                writer.writerow(filtered_row)

    print(f"Cleaning and filtering completed. Cleaned data saved to {output_file}")

# Replace 'input.csv' and 'output_cleaned_filtered.csv' with your file names
clean_and_filter_csv(r'E:\1.csv', 'output_cleaned_filtered.csv', min_length=12)


"""
import csv
import re

def clean_csv(input_file, output_file):
    # Define the regular expression pattern to remove unwanted characters
    clean_pattern = re.compile('[,."\'\n\r]')

    with open(input_file, 'r', newline='', encoding='utf-8') as csv_input:
        # Create a CSV reader
        reader = csv.reader(csv_input)

        with open(output_file, 'w', newline='', encoding='utf-8') as csv_output:
            # Create a CSV writer
            writer = csv.writer(csv_output)

            # Iterate through each row in the input CSV
            for row in reader:
                # Apply the clean_pattern to each element in the row
                cleaned_row = [clean_pattern.sub('', element) for element in row]

                # Write the cleaned row to the output CSV
                writer.writerow(cleaned_row)

    print(f"Cleaning completed. Cleaned data saved to {output_file}")

# Replace 'input.csv' and 'output_cleaned.csv' with your file names
clean_csv(r'E:\1.csv', 'output_cleaned.csv')
"""

