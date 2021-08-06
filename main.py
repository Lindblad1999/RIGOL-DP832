import schedule
from datetime import datetime
import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
dp832_1 = rm.open_resource(rm.list_resources()[0]) #'USB0::6833::3601::DP8C173003282::0::INSTR'
dp832_2 = rm.open_resource(rm.list_resources()[1]) #'USB0::6833::3601::DP8C230300199::0::INSTR'
log = open("log.txt", "a")

def job():
    logTime = datetime.now().strftime("%d/%m/%y %H:%M:%S")
    ps1_ch1 = dp832_1.query('MEAS:ALL? CH1')
    ps1_ch2 = dp832_1.query('MEAS:ALL? CH2')
    ps2_ch1 = dp832_2.query('MEAS:ALL? CH1')
    ps2_ch2 = dp832_2.query('MEAS:ALL? CH2')
    d = "{},{},{},{},{}".format(logTime, ps1_ch1.strip(), ps1_ch2.strip(), ps2_ch1.strip(), ps2_ch2.strip())
    print(d)
    log.write(d)


schedule.every(10).seconds.do(job)

try:
    while True:
        schedule.run_pending()
except KeyboardInterrupt:
    log.close()
    dp832_1.close()
    dp832_2.close()
    rm.close()
    print("Program successfully ended")
