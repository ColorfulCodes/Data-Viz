import csv
MY_FILE = "../dataviz/sample_sfpd_incident_all.csv"

def parse(raw_file,delimiter):
    # Doc string
    """ Parses a raw CSV file to a JSON-like object"""
    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter = delimiter)

    #Build a data structure to return parsed_data

    parsed_data = []
    # Skip over the first line of the file for the headers
    fields = csv_data.next()
    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    #Close CSV file
    opened_file.close()


    return parsed_data

def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(MY_FILE, "-")

    print new_data

def visualize_days():
    """Visualize data by day of week"""

    # grab parsed data
    data_file = parse(MY_FILE, ",")

    # create variable counter by iterating
    # through each line of data  in the parsed data,
    # and count how many incidents occur on each day of week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # separate the x-axis data (days of the week) from the
    # 'counter' variable from the y-axis data (the number of incidents
    # for each day)
    data_list = [counter["Monday"], counter["Tuesday"],
    counter["Wednesday"], counter["Thursday"], counter["Friday"],
    counter["Saturday"], counter["Sunday"]
    ]

    day_tuple = tuple(["Mon","Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Assign y-axis data to matplotlib plot instance
    plt.plot(data_list)


























if __name__ == "__main__":
    main()
