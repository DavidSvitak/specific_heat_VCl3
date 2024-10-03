import json
import os
from urllib.request import urlopen
from download import download
import numpy as np
import matplotlib.pyplot as plt
from LongHCPulse import LongHCPulse 
from periodictable import formula

BASE_URL = 'https://api.figshare.com/v2'
ITEM_ID = 27151218   # https://doi.org/10.6084/m9.figshare.27151218.v1
#Retrieve public metadata from the endpoint
r=urlopen(f'{BASE_URL}/articles/{ITEM_ID}')
metadata=json.loads(r.read())
for f in metadata["files"]:
    download(f["download_url"], f["name"])

mm = formula('VCl3').mass

datafile = "20240530_VCl3_HC_pulses.raw"
DRcalfile = "Puck921.cal"
# find out correct mass
vcl = LongHCPulse(datafile=datafile,calfile=DRcalfile,
    sampmass=2.93,molarmass=mm, useRawTemp=True)  

vcl.heatcapacity()

vcl.labels=[]
vcl.shortpulselabels=[]
f,ax = plt.subplots(1,1)

vcl.lineplot(ax,"All", demag=False)  

ax.set_ylabel("$C$ $(\\rm{J\\> K^{-1} mol^{-1}})$")
ax.set_xlabel("$T$ (K)")

# Show legend
short_legend=ax.legend(handles=vcl.shortpulselabels,labelspacing = 0,handlelength=1.4,
    fontsize=11,frameon=False, bbox_to_anchor=(0.97, 1.0),numpoints=1)
long_legend=ax.legend(handles=vcl.labels,labelspacing = 0,handlelength=1.4,fontsize=11,
    frameon=False, bbox_to_anchor=(0.9, 0.42))
ax.add_artist(short_legend)

#FIX that
plt.ylim(0,7)
plt.xlim(16,25)
plt.savefig("fig1.pdf")