import csv
freq = {"min_frequency" : "2535", "max_frequency": "2555"}
with open('freq.csv', mode='a') as csvfile:    #in mode (a means append,r means read, w means write, r+ means read and write, w+ means write and read)
   # fieldnames = ['min_frequency', 'max_frequency']
   fieldnames = freq.keys()
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   writer.writerows(freq)
    #writer.writerow( {"min_frequency" : "2535", "max_frequency": "2555"})