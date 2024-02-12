import csv
import re

# Clean a cell by removing non-ASCII characters.
def clean_cell(cell, unwanted_chars):
    return re.sub(unwanted_chars, '', cell)

# Clean and filter a CSV file.
def clean_and_filter_csv(input_file, output_file, min_length=12, unwanted_chars=r'[,\."\'\n\r:]'):
    clean_pattern = re.compile(unwanted_chars, re.VERBOSE)

    with open(input_file, 'r', newline='', encoding='utf-8') as csv_input, \
        open(output_file, 'w', newline='', encoding='utf-8') as csv_output:

        reader = csv.reader(csv_input)
        writer = csv.writer(csv_output)

        for row in reader:
            cleaned_row = [clean_cell(element, clean_pattern) for element in row]
            filtered_row = [cell for cell in cleaned_row if len(cell) >= min_length]
            writer.writerow(filtered_row)

    print(f"Cleaning and filtering completed. Cleaned data saved to {output_file}")

# Example usage:
clean_and_filter_csv(r'E:\1.csv', 'output_cleaned_filtered.csv', min_length=12)

