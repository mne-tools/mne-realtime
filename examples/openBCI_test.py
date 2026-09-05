# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:51:27 2021

@author: ICN_admin
"""

from mne_realtime import LSLClient
import matplotlib.pyplot as plt

# this is the max wait time in seconds until client connection
wait_max = 5


if __name__ == '__main__': 
    plt.ion()  # make plot interactive
    _, ax = plt.subplots(1)
    with LSLClient(host="openbci_eeg_id127", wait_max=wait_max) as client:
        print("client initialized")
        client_info = client.get_measurement_info()
        sfreq = int(client_info['sfreq'])    
        epoch = client.get_data_as_epoch(n_samples=sfreq)
        
        # let's observe ten seconds of data
        for ii in range(100):
            print(ii)
            plt.cla()
            epoch = client.get_data_as_epoch(n_samples=sfreq)
            epoch.average().plot(axes=ax)
            print(epoch.average().shape)
            plt.pause(1)
        
    plt.draw()

