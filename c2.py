import csv
Freq_Bands=[{'Start_Frequency':'935','Stop_Frequency': '960', 'Noise_Bandwidth':'200', 'Dwell_Time':'50000'},
            {"Start_Frequency":"1805","Stop_Frequency":"1880", "Noise_Bandwidth":"200", "Dwell_Time":"50000"},
            {"Start_Frequency":"2110","Stop_Frequency":"2170", "Noise_Bandwidth":"200", "Dwell_Time":"50000"},
              {"Start_Frequency":"869","Stop_Frequency":"894", "Noise_Bandwidth":"200", "Dwell_Time":"50000"},
              {"Start_Frequency":"1805","Stop_Frequency":"1880", "Noise_Bandwidth":"200", "Dwell_Time":"50000"},
             {"Start_Frequency":"2300","Stop_Frequency":"2400", "Noise_Bandwidth":"200", "Dwell_Time":"50000"},
              {"Start_Frequency":"2535","Stop_Frequency":"2655", "Noise_Bandwidth":"200", "Dwell_Time":"50000"}]
fields=["Start_Frequency","Stop_Frequency", "Noise_Bandwidth", "Dwell_Time"]
filename = "freq1.csv"


with open(filename, "w") as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=fields,lineterminator="\n")
    writer.writeheader()
    writer.writerows(Freq_Bands)