# Import the AP1000 class from the Apex Driver
import glob
import os
from pathlib import Path
import pandas as pd
from PyApex import AP1000

# Move these to globals inside sunlab

apexIP = "192.168.0.3"

# Connection to your AP1000 *** SET THE GOOD IP ADDRESS ***
# MyAP1000 = AP1000(apexIP)

# Display the modules of the AP1000
# for i in range(1, 8):
# 	print("Slot", i, "->", MyAP1000.SlotType(i))


########################################
#  SLOT 1
########################################

# These variable must be initialised as GUI widgets
Slot1PowerSetBFT = ""
Slot1PowerGetBFT = ""
Slot1PowerSetButton = ""
Slot1PowerGetButton = ""


# Set the TLS Power parameters
def apex_tls_pset(a):
    MyAP1000 = AP1000(apexIP)
    MyTLS = MyAP1000.TunableLaser(1)
    # Initialize the TLS powermeter and  wavelength
    MyTLS.SetPower(Slot1PowerSetBFT.value)
    Slot1PowerSetButton.icon = "check"
    Slot1PowerGetButton.icon = ""


# Get the TLS Power parameters
def apex_tls_pget(a):
    MyAP1000 = AP1000(apexIP)
    MyTLS = MyAP1000.TunableLaser(1)
    # Do some measurement
    Slot1PowerGetBFT.value = MyTLS.GetPower()
    Slot1PowerGetButton.icon = "check"
    Slot1PowerSetButton.icon = ""


# These variable must be initialised as GUI widgets
Slot1WavelenSetBFT = ""
Slot1WavelenGetBFT = ""
Slot1WavelenSetButton = ""
Slot1WavelenGetButton = ""


# Set the TLS Wavelength parameters
def apex_tls_wset(a):
    MyAP1000 = AP1000(apexIP)
    MyTLS = MyAP1000.TunableLaser(1)
    # Initialize the TLS powermeter and  wavelength
    MyTLS.SetWavelength(Slot1WavelenSetBFT.value)
    Slot1WavelenSetButton.icon = "check"
    Slot1WavelenGetButton.icon = ""


# Get the TLS Wavelength parameters
def apex_tls_wget(a):
    MyAP1000 = AP1000(apexIP)
    MyTLS = MyAP1000.TunableLaser(1)
    # Do some measurement
    Slot1WavelenGetBFT.value = MyTLS.GetWavelength()
    Slot1WavelenGetButton.icon = "check"
    Slot1WavelenSetButton.icon = ""


# These variable must be initialised as GUI widgets
Slot1LaserOnButton = ""
Slot1LaserOffButton = ""


# Turn on the Laser Source
def apex_tls_laseron(a):
    MyAP1000 = AP1000(apexIP)
    MyTLS = MyAP1000.TunableLaser(1)
    # Switch on the TLS output
    MyTLS.On()
    Slot1LaserOnButton.icon = "check"
    Slot1LaserOffButton.icon = ""


# Turn off the Lase Source
def apex_tls_laseroff(a):
    MyAP1000 = AP1000(apexIP)
    MyTLS = MyAP1000.TunableLaser(1)
    # Switch off the TLS output
    MyTLS.Off()
    Slot1LaserOffButton.icon = "check"
    Slot1LaserOnButton.icon = ""


########################################
#  SLOT 2
########################################

# These variable must be initialised as GUI widgets
Slot2OAT1SetBFT = ""
Slot2OAT1SetButton = ""
Slot2OAT1GetBFT = ""
Slot2OAT1GetButton = ""


# Get the ATTN Channel #1 parameters
def apex_attn1_get(a):
    MyAP1000 = AP1000(apexIP)
    MyATTN = MyAP1000.Attenuator(2)
    Slot2OAT1GetBFT.value = MyATTN.GetAttenuation(1)
    Slot2OAT1GetButton.icon = "check"
    Slot2OAT1SetButton.icon = ""


# Set the ATTN Channel #1 parameters
def apex_attn1_set(a):
    MyAP1000 = AP1000(apexIP)
    MyATTN = MyAP1000.Attenuator(2)
    MyATTN.SetAttenuation(Slot2OAT1SetBFT.value, 1)
    Slot2OAT1GetButton.icon = ""
    Slot2OAT1SetButton.icon = "check"


# These variable must be initialised as GUI widgets
Slot2OAT2SetBFT = ""
Slot2OAT2SetButton = ""
Slot2OAT2GetBFT = ""
Slot2OAT2GetButton = ""


# Get the ATTN Channel #2 parameters
def apex_attn2_get(a):
    MyAP1000 = AP1000(apexIP)
    MyATTN = MyAP1000.Attenuator(2)
    Slot2OAT2GetBFT.value = MyATTN.GetAttenuation(2)
    Slot2OAT2GetButton.icon = "check"
    Slot2OAT2SetButton.icon = ""


# Set the ATTN Channel #2 parameters
def apex_attn2_set(a):
    MyAP1000 = AP1000(apexIP)
    MyATTN = MyAP1000.Attenuator(2)
    # Initialize ATTN
    MyATTN.SetAttenuation(Slot2OAT2SetBFT.value, 2)
    Slot2OAT2GetButton.icon = ""
    Slot2OAT2SetButton.icon = "check"


########################################
#  SLOT 3
########################################

Slot3ManModeButton = ""
Slot3AutoPowerModeButton = ""
Slot3CurrentSetBFT = ""
Slot3CurrentSetButton = ""
Slot3PowerSetBFT = ""
Slot3PowerGetBFT = ""
Slot3PowerSetButton = ""
Slot3PowerGetButton = ""
Slot3AmpOnButton = ""
Slot3AmpOffButton = ""


def apex_efda1_manmode(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(3)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(0)
    Slot3ManModeButton.icon = 'check'
    Slot3AutoPowerModeButton.icon = ''
    Slot3AmpOnButton.icon = 'check'
    Slot3AmpOffButton.icon = ''


def apex_efda1_apmode(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(3)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(1, Slot3PowerSetBFT.value)
    Slot3ManModeButton.icon = ''
    Slot3AutoPowerModeButton.icon = 'check'
    Slot3AmpOnButton.icon = 'check'
    Slot3AmpOffButton.icon = ''


# Set up the EFDA parameters

def apex_efda1_iset(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(3)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(0)
    print('About to write: ', Slot3CurrentSetBFT.value)
    MyErbiumAmplifier.SetIPump(Slot3CurrentSetBFT.value)
    Slot3CurrentSetButton.icon = 'check'
    Slot3AmpOnButton.icon = 'check'
    Slot3AmpOffButton.icon = ''
    Slot3PowerSetButton.icon = ''
    Slot3PowerGetButton.icon = ''


# Set up the EFDA parameters

def apex_efda1_pset(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(3)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(1, Slot3PowerSetBFT.value)
    Slot3ManModeButton.icon = ''
    Slot3AutoPowerModeButton.icon = 'check'
    Slot3PowerSetButton.icon = 'check'
    Slot3PowerGetButton.icon = ''
    Slot3AmpOnButton.icon = 'check'
    Slot3AmpOffButton.icon = ''
    Slot3CurrentSetButton.icon = ''


# Get the EFDA parameters

def apex_efda1_get(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(3)
    MyErbiumAmplifier.On()
    # Do some measurement
    Slot3PowerGetBFT.value = MyErbiumAmplifier.GetOutPower()
    Slot3PowerGetButton.icon = 'check'
    Slot3PowerSetButton.icon = ''
    Slot3CurrentSetButton.icon = ''


# Turn the EFDA on
def apex_efda1_on(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(3)
    MyErbiumAmplifier.On()
    Slot3AmpOnButton.icon = 'check'
    Slot3AmpOffButton.icon = ''


# Turn the EFDA on
def apex_efda1_off(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(3)
    MyErbiumAmplifier.Off()
    Slot3AmpOffButton.icon = 'check'
    Slot3AmpOnButton.icon = ''


########################################
#  SLOT 4
########################################
Slot4ManModeButton = ""
Slot4AutoPowerModeButton = ""
Slot4CurrentSetBFT = ""
Slot4CurrentSetButton = ""
Slot4PowerSetBFT = ""
Slot4PowerGetBFT = ""
Slot4PowerSetButton = ""
Slot4PowerGetButton = ""
Slot4AmpOnButton = ""
Slot4AmpOffButton = ""


def apex_efda2_manmode(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(4)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(0)
    Slot4ManModeButton.icon = 'check'
    Slot4AutoPowerModeButton.icon = ''
    Slot4AmpOnButton.icon = 'check'
    Slot4AmpOffButton.icon = ''


def apex_efda2_apmode(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(4)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(1, Slot4PowerSetBFT.value)
    Slot4ManModeButton.icon = ''
    Slot4AutoPowerModeButton.icon = 'check'
    Slot4AmpOnButton.icon = 'check'
    Slot4AmpOffButton.icon = ''


# Set up the EFDA parameters

def apex_efda2_iset(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(4)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(0)
    print('About to write: ', Slot4CurrentSetBFT.value)
    MyErbiumAmplifier.SetIPump(Slot4CurrentSetBFT.value)
    Slot4CurrentSetButton.icon = 'check'
    Slot4AmpOnButton.icon = 'check'
    Slot4AmpOffButton.icon = ''
    Slot4PowerSetButton.icon = ''
    Slot4PowerGetButton.icon = ''


# Set up the EFDA parameters

def apex_efda2_pset(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(4)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(1, Slot4PowerSetBFT.value)
    Slot4ManModeButton.icon = ''
    Slot4AutoPowerModeButton.icon = 'check'
    Slot4PowerSetButton.icon = 'check'
    Slot4PowerGetButton.icon = ''
    Slot4AmpOnButton.icon = 'check'
    Slot4AmpOffButton.icon = ''
    Slot4CurrentSetButton.icon = ''


# Get the EFDA parameters

def apex_efda2_get(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(4)
    MyErbiumAmplifier.On()
    # Do some measurement
    Slot4PowerGetBFT.value = MyErbiumAmplifier.GetOutPower()
    Slot4PowerGetButton.icon = 'check'
    Slot4PowerSetButton.icon = ''
    Slot4CurrentSetButton.icon = ''


# Turn the EFDA on
def apex_efda2_on(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(4)
    MyErbiumAmplifier.On()
    Slot4AmpOnButton.icon = 'check'
    Slot4AmpOffButton.icon = ''


# Turn the EFDA on
def apex_efda2_off(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(4)
    MyErbiumAmplifier.Off()
    Slot4AmpOffButton.icon = 'check'
    Slot4AmpOnButton.icon = ''

########################################
#  SLOT 5
########################################

Slot5ManModeButton = ""
Slot5AutoPowerModeButton = ""
Slot5CurrentSetBFT = ""
Slot5CurrentSetButton = ""
Slot5PowerSetBFT = ""
Slot5PowerGetBFT = ""
Slot5PowerSetButton = ""
Slot5PowerGetButton = ""
Slot5AmpOnButton = ""
Slot5AmpOffButton = ""


def apex_efdba1_manmode(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(5)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(0)
    Slot5ManModeButton.icon = 'check'
    Slot5AutoPowerModeButton.icon = ''
    Slot5AmpOnButton.icon = 'check'
    Slot5AmpOffButton.icon = ''


def apex_efdba1_apmode(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(5)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(1, Slot5PowerSetBFT.value)
    Slot5ManModeButton.icon = ''
    Slot5AutoPowerModeButton.icon = 'check'
    Slot5AmpOnButton.icon = 'check'
    Slot5AmpOffButton.icon = ''


# Set up the EFDA parameters

def apex_efdba1_iset(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(5)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(0)
    print('About to write: ', Slot5CurrentSetBFT.value)
    MyErbiumAmplifier.SetIPump(Slot5CurrentSetBFT.value)
    Slot5CurrentSetButton.icon = 'check'
    Slot5AmpOnButton.icon = 'check'
    Slot5AmpOffButton.icon = ''
    Slot5PowerSetButton.icon = ''
    Slot5PowerGetButton.icon = ''


# Set up the EFDA parameters

def apex_efdba1_pset(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(5)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(1, Slot5PowerSetBFT.value)
    Slot5ManModeButton.icon = ''
    Slot5AutoPowerModeButton.icon = 'check'
    Slot5PowerSetButton.icon = 'check'
    Slot5PowerGetButton.icon = ''
    Slot5AmpOnButton.icon = 'check'
    Slot5AmpOffButton.icon = ''
    Slot5CurrentSetButton.icon = ''


# Get the EFDA parameters

def apex_efdba1_get(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(5)
    MyErbiumAmplifier.On()
    # Do some measurement
    Slot5PowerGetBFT.value = MyErbiumAmplifier.GetOutPower()
    Slot5PowerGetButton.icon = 'check'
    Slot5PowerSetButton.icon = ''
    Slot5CurrentSetButton.icon = ''


# Turn the EFDA on
def apex_efdba1_on(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(5)
    MyErbiumAmplifier.On()
    Slot5AmpOnButton.icon = 'check'
    Slot5AmpOffButton.icon = ''


# Turn the EFDA on
def apex_efdba1_off(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(5)
    MyErbiumAmplifier.Off()
    Slot5AmpOffButton.icon = 'check'
    Slot5AmpOnButton.icon = ''


########################################
#  SLOT 6
########################################

Slot6ManModeButton = ""
Slot6AutoPowerModeButton = ""
Slot6CurrentSetBFT = ""
Slot6CurrentSetButton = ""
Slot6PowerSetBFT = ""
Slot6PowerGetBFT = ""
Slot6PowerSetButton = ""
Slot6PowerGetButton = ""
Slot6AmpOnButton = ""
Slot6AmpOffButton = ""


def apex_efdba2_manmode(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(6)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(0)
    Slot5ManModeButton.icon = 'check'
    Slot5AutoPowerModeButton.icon = ''
    Slot5AmpOnButton.icon = 'check'
    Slot5AmpOffButton.icon = ''


def apex_efdba2_apmode(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(6)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(1, Slot6PowerSetBFT.value)
    Slot5ManModeButton.icon = ''
    Slot5AutoPowerModeButton.icon = 'check'
    Slot5AmpOnButton.icon = 'check'
    Slot5AmpOffButton.icon = ''


# Set up the EFDA parameters

def apex_efdba2_iset(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(6)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(0)
    print('About to write: ', Slot6CurrentSetBFT.value)
    MyErbiumAmplifier.SetIPump(Slot6CurrentSetBFT.value)
    Slot6CurrentSetButton.icon = 'check'
    Slot6AmpOnButton.icon = 'check'
    Slot6AmpOffButton.icon = ''
    Slot6PowerSetButton.icon = ''
    Slot6PowerGetButton.icon = ''


# Set up the EFDA parameters

def apex_efdba2_pset(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(6)
    MyErbiumAmplifier.On()
    MyErbiumAmplifier.SetMode(1, Slot6PowerSetBFT.value)
    Slot6ManModeButton.icon = ''
    Slot6AutoPowerModeButton.icon = 'check'
    Slot6PowerSetButton.icon = 'check'
    Slot6PowerGetButton.icon = ''
    Slot6AmpOnButton.icon = 'check'
    Slot6AmpOffButton.icon = ''
    Slot6CurrentSetButton.icon = ''


# Get the EFDA parameters

def apex_efdba2_get(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(6)
    MyErbiumAmplifier.On()
    # Do some measurement
    Slot6PowerGetBFT.value = MyErbiumAmplifier.GetOutPower()
    Slot6PowerGetButton.icon = 'check'
    Slot6PowerSetButton.icon = ''
    Slot6CurrentSetButton.icon = ''


# Turn the EFDA on
def apex_efdba2_on(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(6)
    MyErbiumAmplifier.On()
    Slot6AmpOnButton.icon = 'check'
    Slot6AmpOffButton.icon = ''


# Turn the EFDA on
def apex_efdba2_off(a):
    MyAP1000 = AP1000(apexIP)
    MyErbiumAmplifier = MyAP1000.ErbiumAmplifier(6)
    MyErbiumAmplifier.Off()
    Slot6AmpOffButton.icon = 'check'
    Slot6AmpOnButton.icon = ''


########################################
#  SLOT 7
########################################

Slot7PowerCh1BFT = ''
Slot7PowerCh2BFT = ''
Slot7GetPowerCh1Button = ''
Slot7GetPowerCh2Button = ''


def apex_opa1_get(a):
    MyAP1000 = AP1000(apexIP)
    MyPowerMeter = MyAP1000.PowerMeter(7)
    # Do some measurement
    Slot7PowerCh1BFT.value = MyPowerMeter.GetPower(1)
    Slot7GetPowerCh1Button.icon = 'check'
    Slot7GetPowerCh2Button.icon = ''


def apex_opa2_get(a):
    MyAP1000 = AP1000(apexIP)
    MyPowerMeter = MyAP1000.PowerMeter(7)
    # Do some measurement
    Slot7PowerCh2BFT.value = MyPowerMeter.GetPower(2)
    Slot7GetPowerCh2Button.icon = 'check'
    Slot7GetPowerCh1Button.icon = ''


########################################
#  Save and Retrieve config
########################################
FilenameText = ''
SaveConfigButton = ''
ListConfigSelect = ''
ListConfigButton = ''
LoadConfigButton = ''


def apex_save_to_disk(a):

    filepathname = './Apex Configs/' + FilenameText.value
    print("Trying to create file:", filepathname)
    try:
        Path(filepathname).touch()
    except OSError:
        print('Could not create file')
        return False
    # initialize list of lists
    data = [['1', 'TLS', 'Wavelength', Slot1WavelenSetBFT.value],
            ['1', 'TLS', 'Power', Slot1PowerSetBFT.value],
            ['2', 'OAM CH1', 'Attenuation', Slot2OAT1SetBFT.value],
            ['2', 'OAM CH2', 'Attenuation', Slot2OAT2SetBFT.value],
            ['3', 'EFDA #1', 'Power Setpoint', Slot3PowerSetBFT.value],
            ['3', 'EFDA #1', 'Pump Current', Slot3CurrentSetBFT.value],
            ['4', 'EFDA #2', 'Power Setpoint', Slot4PowerSetBFT.value],
            ['4', 'EFDA #2', 'Pump Current', Slot4CurrentSetBFT.value],
            ['5', 'EFDBA #1', 'Power Setpoint', Slot5PowerSetBFT.value],
            ['5', 'EFDBA #1', 'Pump Current', Slot5CurrentSetBFT.value],
            ['6', 'EFDBA #1', 'Power Setpoint', Slot6PowerSetBFT.value],
            ['6', 'EFDBA #1', 'Pump Current', Slot6CurrentSetBFT.value]]

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Slot #', 'Device Type', 'Parameter', 'Value'])
    print(df)
    try:
        df.to_pickle(filepathname)
    except OSError:
        print('Could not write configuration to file')
        return False


def apex_load_from_disk(a):

    try:
        os.open(ListConfigSelect.value, os.O_RDONLY)
    except OSError:
        print('Could not open file:', ListConfigSelect.value)
        return False
    try:
        df = pd.read_pickle(ListConfigSelect.value)
    except OSError:
        print('Could not read configuration from file:', ListConfigSelect.value)
        return False

    print('Slot1WavelenSetBFT.value = ', df.loc[0].Value)
    Slot1WavelenSetBFT.value = df.loc[0].Value
    print('Slot1PowerSetBFT.value = ', df.loc[1].Value)
    Slot1PowerSetBFT.value = df.loc[1].Value
    print('Slot2OAT1SetBFT.value = ', df.loc[2].Value)
    Slot2OAT1SetBFT.value = df.loc[2].Value
    print('Slot2OAT2SetBFT.value = ', df.loc[3].Value)
    Slot2OAT2SetBFT.value = df.loc[3].Value
    print('Slot3PowerSetBFT.value = ', df.loc[4].Value)
    Slot3PowerSetBFT.value = df.loc[4].Value
    print('Slot3CurrentSetBFT.value = ', df.loc[5].Value)
    Slot3CurrentSetBFT.value = df.loc[5].Value
    print('Slot4PowerSetBFT.value = ', df.loc[6].Value)
    Slot4PowerSetBFT.value = df.loc[6].Value
    print('Slot4CurrentSetBFT.value = ', df.loc[7].Value)
    Slot4CurrentSetBFT.value = df.loc[7].Value
    print('Slot5PowerSetBFT.value = ', df.loc[8].Value)
    Slot5PowerSetBFT.value = df.loc[8].Value
    print('Slot5CurrentSetBFT.value = ', df.loc[9].Value)
    Slot5CurrentSetBFT.value = df.loc[9].Value
    print('Slot6PowerSetBFT.value = ', df.loc[10].Value)
    Slot6PowerSetBFT.value = df.loc[10].Value
    print('Slot6CurrentSetBFT.value = ', df.loc[11].Value)
    Slot6CurrentSetBFT.value = df.loc[11].Value

def apex_list_config(a):
    ListConfigSelect.options = glob.glob("./Apex Configs/*")




