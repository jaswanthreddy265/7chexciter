import sys
import csv
import os.path
from PyQt5.QtWidgets import QMainWindow, QApplication

from Freq import Ui_MainWindow

class prob(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(prob, self).__init__()
        self.setupUi(self)
        self.Save.clicked.connect(self.mainfile)

    def mainfile(self):

        fields = ["Start_Frequency", "Stop_Frequency", "Noise_Bandwidth", "Dwell_Time"]
        #fields = ["Start_Frequency(MHz)", "Stop_Frequency(MHz)", "Noise_Bandwidth(Hz)", "Dwell_Time(s)"]
        filename = "frequency.csv"

        start_freq = self.Start_Frequency.text()
        stop_freq = self.Stop_Frequency.text()
        bw = self.CB_Bandwidth.currentText()
        dt = self.Dwell_Time.text()
        Freq_Bands = {'Start_Frequency': start_freq, 'Stop_Frequency': stop_freq, 'Noise_Bandwidth': bw,
                      'Dwell_Time': dt}
        file_exist = os.path.isfile(filename)
        with open(filename, "a") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields, lineterminator="\n")
            if not file_exist:
                writer.writeheader()
            writer.writerow(Freq_Bands)

if __name__=="__main__":
    app=QApplication(sys.argv)
    sol=prob()
    sol.show()
    sys.exit(app.exec_())