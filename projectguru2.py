import csv


# Function to read CSV file and return emissions data
def read_csv(filename):
    emissions_data = {}
    with open(filename, "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header row
        years = header[1:]  # Extract years from the header
        for row in reader:
            country = row[0]
            data = {year: float(emission) for year, emission in zip(years, row[1:])}
            emissions_data[country] = data
    return emissions_data


# Function to perform analysis for a given year
def analyze_year(emissions_data, year):
    try:
        if (
            year in emissions_data[next(iter(emissions_data))]
        ):  # Check if year is in the data
            year_data = {
                country: emissions_data[country][year] for country in emissions_data
            }

            if year_data:
                min_value = min(year_data.values())
                max_value = max(year_data.values())
                average_value = sum(year_data.values()) / len(year_data)

                return min_value, max_value, average_value
    except (KeyError, StopIteration):
        pass

    return None


# Function to take input from the user and perform analysis
def main():
    # Get user input for the CSV filename
    csv_filename = input("Enter the CSV filename: ")

    # Read emissions data from CSV file
    emissions_data = read_csv(csv_filename)

    # Get user input for the year
    year = input("Enter a year: ")

    # Perform analysis
    analysis_result = analyze_year(emissions_data, year)

    # Print the results
    if analysis_result:
        min_value, max_value, average_value = analysis_result
        print(f"Analysis for {year} worldwide emissions data:")
        print(f"Minimum value: {min_value:.6f}")
        print(f"Maximum value: {max_value:.6f}")
        print(f"Average value: {average_value:.6f}")
    else:
        print(f"No data found for {year}. Cannot perform analysis.")


if __name__ == "__main__":
    main()
