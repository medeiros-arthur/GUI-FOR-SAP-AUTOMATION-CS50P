# PROJECT TITLE: GUI FOR SAP AUTOMATION - CS50P FINAL PROJECT
# CREATED BY: ARTHUR MEDEIROS
# GITHUB PROFILE: https://github.com/medeiros-arthur
# GITHUB REPOSITOTY: https://github.com/medeiros-arthur/GUI-FOR-SAP-AUTOMATION-CS50P
# DATE THAT THE VIDEO WAS RECORDED: 03/06/2024
# DATE THAT THE VIDEO WAS EDITED: 13/06/2024



import PySimpleGUI as sg
import win32com.client
import sys
import subprocess
import time
from datetime import datetime
import calendar
import sapCred # SAP CREDENTIALS
import os


exportPath = sapCred.exportPath # FOLDER TO EXTRACT FILES




mes = datetime.now().strftime("%m")
ano = datetime.now().strftime("%Y")



# Define the layout of your window
layout = [[sg.Button('Login Sap')],
          [sg.Button('Export CE34 Production'),sg.Text('Month:'),sg.Combo(['01','02','03','04','05','06','07','08','09','10','11','12'], default_value=mes)],
          [sg.Button('Export CE37 Production'),sg.Text('Year:'),sg.Combo(['2020','2021','2023','2024','2025'], default_value=ano)],
          [sg.Button('Launch Dashboard')],

          ]

sg.theme('DarkAmber')

# Create the window
window = sg.Window('AUXÍLIO SAP', layout)


class SapGui():
    def open_sap(self):
        self.path = sapCred.sapExePath
        subprocess.Popen(self.path)
        time.sleep(5)




    def sapLogin(self):
        self.open_sap()
        self.SapGuiAuto = win32com.client.GetObject('SAPGUI')
        if not type(self.SapGuiAuto) == win32com.client.CDispatch:
            return

        application = self.SapGuiAuto.GetScriptingEngine
        self.connection = application.OpenConnection("RIOPET [PRD]", True)
        time.sleep(3)

        self.session = self.connection.Children(0)
        self.session.findById("wnd[0]").maximize


        try:
            self.session.findById("wnd[0]/usr/txtRSYST-MANDT").text = "600"
            self.session.findById("wnd[0]/usr/txtRSYST-BNAME").text = sapCred.login
            self.session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = sapCred.password
            self.session.findById("wnd[0]/usr/txtRSYST-LANGU").text = "PT"
            self.session.findById("wnd[0]").sendVKey(0)


        except:
            print(sys.exec_info()[0])
            time.sleep(2)
        else:
            sg.popup("Login succesfully")


    def connect_sap(self):
        SapGuiAuto = win32com.client.GetObject('SAPGUI')
        application = SapGuiAuto.GetScriptingEngine
        self.connection = application.Children(0)
        self.session = self.connection.Children(0)
        self.session.findById("wnd[0]").maximize
        time.sleep(2)

    def ce34(self):
        self.connect_sap()

        self.session.findById("wnd[0]").maximize
        self.session.findById("wnd[0]/tbar[0]/okcd").text = "zpp002"
        self.session.findById("wnd[0]").sendVKey(0)
        self.session.findById("wnd[0]/usr/ctxtP_WERKS").text = "ce34"
        self.session.findById("wnd[0]/usr/ctxtS_ISDD-LOW").text = f"01.{mes_selected}.{ano_selected}"
        self.session.findById("wnd[0]/usr/ctxtS_ISDD-HIGH").text = f"{dia}.{mes_selected}.{ano_selected}"
        time.sleep(2)
        self.session.findById("wnd[0]/usr/ctxtS_ISDD-HIGH").setFocus()
        self.session.findById("wnd[0]/usr/ctxtS_ISDD-HIGH").caretPosition = 10
        self.session.findById("wnd[0]/tbar[1]/btn[8]").press()

        self.session.findById("wnd[0]").sendVKey(0)
        time.sleep(1)
        self.session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[2]").select()
        time.sleep(1)
        self.session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").select()
        time.sleep(1)
        self.session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").setFocus()
        time.sleep(1)
        self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        time.sleep(1)
        self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = exportPath + r'\CE34'
        self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = f"CE34 {values[0]} {values[1]}.csv"

        self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        time.sleep(1)
        self.session.findById("wnd[0]/tbar[0]/btn[12]").press()
        time.sleep(1)
        self.session.findById("wnd[0]/tbar[0]/btn[12]").press()
        time.sleep(1)
        self.session.findById("wnd[0]/tbar[0]/btn[12]").press()
        time.sleep(0.2)
        sg.popup("CE34 Production extracted")


    def ce37(self):
        self.connect_sap()

        self.session.findById("wnd[0]").maximize
        self.session.findById("wnd[0]/tbar[0]/okcd").text = "zpp002"
        self.session.findById("wnd[0]").sendVKey(0)
        self.session.findById("wnd[0]/usr/ctxtP_WERKS").text = "ce37"
        self.session.findById("wnd[0]/usr/ctxtS_ISDD-LOW").text = f"01.{mes_selected}.{ano_selected}"
        self.session.findById("wnd[0]/usr/ctxtS_ISDD-HIGH").text = f"{dia}.{mes_selected}.{ano_selected}"
        time.sleep(2)
        self.session.findById("wnd[0]/usr/ctxtS_ISDD-HIGH").setFocus()
        self.session.findById("wnd[0]/usr/ctxtS_ISDD-HIGH").caretPosition = 10
        self.session.findById("wnd[0]/tbar[1]/btn[8]").press()

        self.session.findById("wnd[0]").sendVKey(0)
        time.sleep(1)
        self.session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[2]").select()
        time.sleep(1)
        self.session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").select()
        time.sleep(1)
        self.session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").setFocus()
        time.sleep(1)
        self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        time.sleep(1)
        self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = exportPath + r'\CE37'
        self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = f"CE37 {values[0]} {values[1]}.csv"

        self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        time.sleep(0.2)
        self.session.findById("wnd[0]/tbar[0]/btn[12]").press()
        time.sleep(0.2)
        self.session.findById("wnd[0]/tbar[0]/btn[12]").press()
        time.sleep(0.2)
        self.session.findById("wnd[0]/tbar[0]/btn[12]").press()
        time.sleep(0.2)
        sg.popup("CE37 Production extracted")




#! Event loop to process events and get values
def main():
    while True:
        event, values = window.read()



        mes_selected = values[0]
        ano_selected = values[1]
        dia = calendar.monthrange(int(ano_selected), int(mes_selected))[1]

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Login Sap':
            SapGui().sapLogin()


        if event == 'Export CE34 Production':
            SapGui().ce34()


        if event == 'Export CE37 Production':
            SapGui().ce37()







        if event == 'Launch Dashboard':

            try:
            # Run the Streamlit command
                subprocess.run(["streamlit", "run", "streamlit.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"An error occurred: {e}")









    # Close the window
    window.close()

if __name__ == "__main__":
    main()
