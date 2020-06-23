import requests
import numpy as np
import json
import pickle
import glob
import os
from pathlib import Path
import tempfile

import pandas as pd

ip_ws1 = '192.168.0.4'
ip_ws2 = '192.168.0.5'


def createWspString(wsFreq, wsAttn, wsPhase, wsPort):
    wsAttn[np.isnan(wsAttn)] = 60
    wsPhase[np.isnan(wsPhase)] = 0
    wsAttn[wsAttn > 60] = 60
    wsAttn[wsAttn <= 0] = 0
    wspString = ''

    for i in range(len(wsFreq)):
        wspString = '%s%.4f\t%.4f\t%.4f\t%d\n' % (wspString, wsFreq[i], wsAttn[i], wsPhase[i], wsPort[i])
    return wspString


def get_device_info():
    device_info = requests.get('http://' + ip + '/waveshaper/devinfo').json()

    print("ip:", device_info["ip"],
          "\nmodel:", device_info["model"],
          "\npartno:", device_info["partno"],
          "\nportcount:", device_info["portcount"],
          "\nsno:", device_info["sno"],
          "\nstartfreq:", device_info["startfreq"],
          "\nstopfreq:", device_info["stopfreq"],
          "\n")


def getprofile():
    device_profile = requests.get('http://' + ip + '/waveshaper/getprofile').content.decode("utf-8")
    # splitFile = device_profile.replace('\t', ',').split('\n')
    splitFile = device_profile.split('\n')
    # print(splitFile)

    # pickle_out = open("dict2.pickle", "wb") #Writing to pickle
    # pickle.dump(device_profile, pickle_out)
    # pickle_out.close()

    pickle_in = open("dict2.pickle", "rb")
    wsp_pickle = pickle.load(pickle_in)
    print(wsp_pickle)


# cols = ['wsFreq', 'wsAttn','wsPhase', 'wsPort']
# lst = []
# for index in  splitFile:

#     p0 = index.replace('\t', ',').split(',')


#    dataset1 = p0[0]
#    dataset2 = str(p0[1: 2])[2:-2]
#     dataset3 = str(p0[2: 3])[2:-2]
#   dataset4 = str(p0[3: 4])[2:-2]

#      lst.append([dataset1,  dataset2,  dataset3, dataset4])

#  df1 = pd.DataFrame(lst, columns=cols)
# df1.to_csv("data.csv", index=False)

#  print(df1)


def uploadProfile(ip, wsFreq, wsAttn, wsPhase, wsPort, timeout=20):
    data = {'type': 'wsp', 'wsp': createWspString(wsFreq, wsAttn, wsPhase, wsPort)}
    r = requests.post('http://' + ip + '/waveshaper/loadprofile', json.dumps(data), timeout=timeout)
    return r


########################################
#  Save and Retrieve config
########################################
WSFilenameText = ''
WSSaveConfig1Button = ''
WSSaveConfig2Button = ''
WSListConfigButton = ''
WSLoadConfig1Button = ''
WSLoadConfig2Button = ''
WSListConfigSelect = ''

def ws1_save_to_disk(a):
    filepathname = './WS Configs/' + WSFilenameText.value
    try:
        Path(filepathname).touch()
    except OSError:
        print('Could not create file')
        return False
    # initialize list of lists

    profile = requests.get('http://' + ip_ws1 + '/waveshaper/getprofile').content.decode("utf-8")

    f = tempfile.TemporaryFile(mode='w+')
    f.write('Frequency,Attenuation,Phase,Port\n')
    for i in profile.split('/n'):
        f.write(i.replace('\t', ','), )
    f.seek(0)
    df = pd.read_csv(f)
    f.close()
    print(df)
    try:
        df.to_pickle(filepathname, compression='gzip')
    except OSError:
        print('Could not write configuration to file')
        return False

def ws2_save_to_disk(a):
    filepathname = './WS Configs/' + WSFilenameText.value
    try:
        Path(filepathname).touch()
    except OSError:
        print('Could not create file')
        return False
    # initialize list of lists

    profile = requests.get('http://' + ip_ws2 + '/waveshaper/getprofile').content.decode("utf-8")

    f = tempfile.TemporaryFile(mode='w+')
    f.write('Frequency,Attenuation,Phase,Port\n')
    for i in profile.split('/n'):
        f.write(i.replace('\t', ','), )
    f.seek(0)
    df = pd.read_csv(f)
    print(df)
    try:
        df.to_pickle(filepathname, compression='gzip')
    except OSError:
        print('Could not write configuration to file')
        return False


def ws_load1_from_disk(a):
    try:
        fd = os.open(WSListConfigSelect.value, os.O_RDONLY)
    except OSError:
        print('Could not open file:', WSListConfigSelect.value)
        return False
    try:
        df = pd.read_pickle(WSListConfigSelect.value, compression='gzip')
    except OSError:
        print('Could not read configuration from file:', WSListConfigSelect.value)
        return False
    print(df)
    uploadProfile(ip_ws1,
                  df['Frequency'].values,
                  df['Attenuation'].values,
                  df['Phase'].values,
                  df['Port'].values,
                  timeout=20)
    os.close( fd )


def ws_load2_from_disk(a):
    try:
        fd = os.open(WSListConfigSelect.value, os.O_RDONLY)
    except OSError:
        print('Could not open file:', WSListConfigSelect.value)
        return False
    try:
        df = pd.read_pickle(WSListConfigSelect.value, compression='gzip')
    except OSError:
        print('Could not read configuration from file:', WSListConfigSelect.value)
        return False
    print(df)
    uploadProfile(ip_ws2,
                  df['Frequency'].values,
                  df['Attenuation'].values,
                  df['Phase'].values,
                  df['Port'].values,
                  timeout=20)
    os.close(fd)

def ws_list_config(a):
    WSListConfigSelect.options = glob.glob("./WS Configs/*")
