import csv
import os.path

fields=["Start_Frequency","Stop_Frequency", "Noise_Bandwidth", "Dwell_Time"]
filename = "freq.csv"

start_freq=int(input("Enter Start Frequency"))
stop_freq=int(input("Enter Stop Frequency"))
bw=int(input("Enter bandwidth"))
dt=int(input("Enter Dwell Time"))
Freq_Bands={'Start_Frequency':start_freq,'Stop_Frequency':stop_freq , 'Noise_Bandwidth':bw, 'Dwell_Time':dt}
file_exist=os.path.isfile(filename)
with open(filename, "a") as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=fields,lineterminator="\n")
    if not file_exist:
        writer.writeheader()
    writer.writerow(Freq_Bands)