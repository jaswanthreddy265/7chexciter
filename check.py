"""import csv
n = open("fre.csv", 'a', newline='')
Start_Frequency=input("Enter the Start Frequency")
Stop_Frequency=input("Enter the Stop Frequency")
Noise_Bandwidth=input("Enter the Noise Bandwidth")
Dwell_Time=input("Enter the Dwell Time")
j={"Start_Frequency":Start_Frequency,"Stop_Frequency":Stop_Frequency, "Noise_Bandwidth":Noise_Bandwidth, "Dwell_Time":Dwell_Time}
row = ["Start_Frequency","Stop_Frequency", "Noise_Bandwidth", "Dwell_Time" ]
writer = csv.writer(n,)
writer.writerow(row)
writer.writerows(j)
n.close()"""


#############################################################################################################################
"""import csv
with open("fre.csv", 'a', newline='') as n:
    writer = csv.writer(n)
    row = ["Start_Frequency", "Stop_Frequency", "Noise_Bandwidth", "Dwell_Time"]
    writer.writerow(row)
    """
