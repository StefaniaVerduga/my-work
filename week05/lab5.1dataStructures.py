# lab5.1dataStructures.py
# We are creating a tuple that stores the months of the year,
# from that tuple, create another tuple with just the summer months.
# The program will print out the summer months one at a time.
# Author: Stefania Verduga

months = ("January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
)
summer = months[4:7]
for month in summer:
    print(month)