import tkinter as tk
import datetime
import time

class Clock():
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("In_Time v.3.0tk by ldlolcl")
        self.label = tk.Label(text="", font=('Helvetica', 15), fg='green2', background='black')
        self.label.pack()
        self.update_clock()
        self.Dolg()
        self.Time()
        self.root.mainloop()

    def update_clock(self):
        now = self.Time()
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

    def Dolg(self):
        nachalo = datetime.date(2021, 10, 15)
        t_data = datetime.date.today()
        d_kontrakt = datetime.date(2024, 7, 31)
        d_proshlo = int((str((nachalo - t_data) * -1).split()[0]))
        d_vsego = int(str(d_kontrakt - nachalo).split()[0])
        d_ostalos = d_vsego - d_proshlo
        dolg_1 = 32214
        dolg_2 = round(dolg_1 / d_vsego * d_ostalos)
        dolg_3 = str(dolg_2)[::-1]
        dolg_4 = ('.'.join(dolg_3[i:i+3] for i in range(0, len(dolg_3), 3))[::-1])
        return str(dolg_4)

    def Time(self):
        dt  = datetime.datetime
        start_date = dt.today()
        end_date = dt(year=2024,month=7,day=31)
        timer = end_date - start_date
        now = dt.now()
        timer2 = str(end_date - datetime.datetime(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute))
        timer2 = timer2.split()
        timer3 = timer2[2].split(':')
        timer2 = int(timer2[0])
        seconds = timer.total_seconds()
        years = int(timer2 // 365.3)
        months = int((timer2 % 365.3) // 30.4)
        days = int((timer2 % 365.3) % 30.4)
        hours = int(timer3[0])
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        o = ' • '
        if years < 10:
            years2 = '000'+str(years)
        else:
            years2 = str(years)
        if months < 10:
            months2 = '0'+str(months)
        else:
            months2 = str(months)
        if days < 10:
            days2 = '0'+str(days)
        else:
            days2 = str(days)
        if hours < 10:
            hours2 = '0'+str(hours)
        else:
            hours2 = str(hours)
        if minutes < 10:
            minutes2 = '0'+str(minutes)
        else:
            minutes2 = str(minutes)
        if seconds < 10:
            seconds2 = '0'+str(seconds)
        else:
            seconds2 = str(seconds)
        dolgi = self.Dolg()
        return (dolgi + ' BYN' + o + years2 + o + months2 + o + days2 + o + hours2 + o + minutes2 + o + seconds2)
        time.sleep(1)
app=Clock()

# pyinstaller -w -F -i"D:\Python\In_Time\ldlolcl.ico" In_Time_v.3.0tk.py 