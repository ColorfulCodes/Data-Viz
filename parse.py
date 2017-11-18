import csv
from collections import Counter
#import matplotlib.pyplot as plt
#import numpy as np
MY_FILE = "../Data-Viz/sample_sfpd_incident_all.csv"

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
"""
def visualize_days():
    #Visualize data by day of week

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

    # Assign labels to plot
    plt.xticks(range(len(day_tuple)), day_tuple)
    # parameter1 = [0,1,2,3,4,5,6] as len() returns numbers
    # parameter2 = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun")

    #Save the plot
    #You can give it any name
    plt.savefig("Days.png")

    #Close figure
    plt.clf()
    plt.show()


"""
def visualize_type():
    """Visualize data by category in a bar graph"""
    # grab parsed data
    data_file = parse(MY_FILE, ",")

    # This returns a dict where it sums the total
    # incidents per category
    counter = Counter(item["Category"] for item in data_file)

    # Set the labels which are based on the keys of our counter
    # Since order does not matter, just use counter.keys()

    labels = tuple(counter.keys())

    # Set where the labels hit the x-axis
    # arange create a list of ints like range but
    # here we add 0.5 to each element of the list
    xlocations = np.arange(len(labels)) + 0.5

    #Width of each bar
    width = 0.5

    # Assign data to bar plot
    plt.bar(xlocations, counter.values(), width= width)
    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width/ 2, labels, rotation=90)

    # This gives more room so the labels are not cut off in the graph
    plt.subplots_adjust(bottom=0.4)

    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    # Save plot
    plt.savefig("Type.png")

    # Close figure
    plt.clf()
    plt.show()


"""
def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(MY_FILE, ",")

    print (new_data)


def main():
    visualize_days()
    new_data = parse(MY_FILE, ',')
    print (new_data)
"""

def main():
    visualize_type()

if __name__ == "__main__":
    main()
