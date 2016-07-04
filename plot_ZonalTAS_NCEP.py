"""
Plots Arctic mean surface temperature (1948-2016) for Jan-month

Website   : http://www.esrl.noaa.gov/psd/cgi-bin/data/timeseries/timeseries1.pl
Author    : Zachary M. Labe
Date      : 15 May 2016
"""

### Import modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as c

### Directory and time
directoryfigure = '/home/zlabe/Documents/Projects/GlobalTemperature/Results/'
directorydata = '/home/zlabe/Documents/Projects/GlobalTemperature/Data/'

### Insert month
month = 'June'

### Retrieve Data
year,temp = np.genfromtxt(directorydata + 'Arctic_Tsurf_Jan%s.txt' % month,
                          unpack=True)

currentyear = int(year[-1])

### Define parameters (dark)
plt.rc('savefig', facecolor='black')
plt.rc('axes', edgecolor='white')
plt.rc('xtick', color='white')
plt.rc('ytick', color='white')
plt.rc('axes', labelcolor='white')
plt.rc('axes', facecolor='black')
plt.rc('text',usetex=True)
plt.rc('font',**{'family':'sans-serif','sans-serif':['Avant Garde']}) 

### Plot for zonal mean temperature
fig = plt.figure()
ax = plt.subplot(111)

### Adjust axes in time series plots 
def adjust_spines(ax, spines):
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))
        else:
            spine.set_color('none')  
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        ax.xaxis.set_ticks([])

### Set colormap
cmap = plt.get_cmap('YlGn_r')
cmap2 = plt.get_cmap('PuBuGn')
cmap3 = plt.get_cmap('YlOrBr')
cmaplist = [cmap(i) for i in xrange(cmap.N)]
cmaplist2 = [cmap2(i) for i in xrange(100,cmap2.N)]
cmaplist3 = [cmap3(i) for i in xrange(cmap3.N)]
cms = c.ListedColormap(cmaplist2 + cmaplist + cmaplist3)

cm = plt.get_cmap(cms)
no_points = len(year)
ax.set_color_cycle([cm(1.*i/(no_points-1)) 
                     for i in range(no_points-1)])
                     
for i in range(no_points-1):
    bar = ax.plot(year[i:i+2],temp[i:i+2],linewidth=3.5,zorder=1)
plt.scatter(year[-1],temp[-1],
            s=40,color='r',zorder=2)
            
ax.tick_params('both',length=7.5,width=2,which='major')             
adjust_spines(ax, ['left', 'bottom'])            
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
plt.subplots_adjust(bottom=0.15)

### y-ticks
plt.yticks(np.arange(int(min(temp))-1,int(max(temp))+1,1),
           map(str,np.arange(int(min(temp))-1,int(max(temp))+1,1)),
           fontsize=11)
plt.ylabel(r'\textbf{Surface Temperature [$^{\circ}$C]}',fontsize=11)
plt.ylim([int(min(temp))-1,int(max(temp))])

### x-ticks
plt.xticks(np.arange(1950,2021,10),map(str,np.arange(1950,2021,10)),
           fontsize=11)
plt.xlabel(r'\textbf{NCEP/NCAR Reanalysis : [Jan-%s] : Arctic, 66N+}' % month,
           fontsize=11)
plt.xlim([1948,2020])

### Insert text            
plt.text(currentyear-8,int(max(temp)),r'\textbf{You are here!}',
             fontsize=11,rotation='horizontal',ha='left',color='r')
plt.text(1999.8,int(min(temp))-0.5,r'Zachary Labe (@ZLabe)',
             fontsize=8,rotation='horizontal',ha='left',color='w',
             bbox=dict(boxstyle='square,pad=0.3',fc='k',
                       edgecolor='w',linewidth=0.2))             

### Save figure
plt.savefig(directoryfigure + 'ZonalTAS_NCEP_sample.png',dpi=900)
