"""
Plots Arctic sea ice extent from June 2002-present using JAXA metadata
Website   : https://ads.nipr.ac.jp/vishop/vishop-extent.html
Author    : Zachary M. Labe
Date      : 9 August 2016
"""

### Import modules
import numpy as np
import urllib2
import datetime
import matplotlib.pyplot as plt

### Directory and time
directory = '...'                        # add working directory
now = datetime.datetime.now()
currentmn = str(now.month)
currentdy = str(now.day)
currentyr = str(now.year)
currenttime = currentmn + '_' + currentdy + '_' + currentyr

### Load url
url = 'https://ads.nipr.ac.jp/vishop.ver1/data/graph/plot_extent_n_v2.csv'

### Read file
raw_data = urllib2.urlopen(url)
dataset = np.genfromtxt(raw_data, skip_header=0,delimiter=",",)

### Set missing data to nan
dataset[np.where(dataset==-9999)] = np.nan

### Variables
month     = dataset[1:,0]        # 1-12, nan as month[0]
day       = dataset[1:,1]        # 1-31, nan as day[0]
mean1980  = dataset[1:,2]        # km^2, nan as mean1980[0]
mean1990  = dataset[1:,3]        # km^2, nan as mean1990[0]
mean2000  = dataset[1:,4]        # km^2, nan as mean2000[0]
years     = dataset[1:,5:]
doy       = np.arange(0,len(day),1)

### Change units to million km^2
years = years/1e6

### Recent day of current year
currentyear = years[:,-1]
lastday = np.where(np.isnan(currentyear))[0][0] - 1
currentice = currentyear[lastday]

### Changes in sea ice
weekchange = currentice - currentyear[lastday-7]
daychange = currentice - currentyear[lastday-1]

print '--- JAXA Arctic Sea Ice Extent Min Years ---'
print '\nCurrent Date =', now.strftime("%Y-%m-%d %H:%M")
print 'Current SIE = %s km^2 \n' % (currentice*1e6)

### Calculate minimums
mins = np.empty((years.shape[1]))
for i in xrange(years.shape[1]):
    mins[i] = np.nanmin(years[:,i])
    
### Add current year
currentline = [currentice]*len(mins)

### Define parameters (dark)
plt.rc('text',usetex=True)
plt.rc('font',**{'family':'sans-serif','sans-serif':['Avant Garde']}) 
plt.rc('savefig',facecolor='black')
plt.rc('axes',edgecolor='white')
plt.rc('xtick',color='white')
plt.rc('ytick',color='white')
plt.rc('axes',labelcolor='white')
plt.rc('axes',facecolor='black')

### Plot sea ice extent
fig = plt.figure()
ax = plt.subplot(111)

N = len(mins)
ind = np.arange(N)
width = 0.9

### Adjust axes in time series plots 
def adjust_spines(ax, spines):
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 15))
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
adjust_spines(ax, ['left', 'bottom'])
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.tick_params('both',length=8.5,width=2,which='major')
ax.tick_params(labelbottom='off')
plt.setp(ax.get_xticklines()[0:-1],visible=False)

rects = ax.bar(ind,mins,width,color='steelblue',alpha=1,
               zorder=1)
line = ax.plot(currentline,linestyle='--',color='y',
               linewidth=2,zorder=3)

### Check mins
belowyr = np.where(mins >= currentice)[0]

### Set color
for i in xrange(len(belowyr)):
    rects[belowyr[i]].set_color('indianred')
    rects[belowyr[i]].set_edgecolor('black')
rects[-1].set_color('y')

### Set y-axis labels
plt.yticks(np.arange(0,7,1),map(str,np.arange(0,7,1)))
plt.ylabel(r'SIE ($\times$10$^6$ km$^2)$',fontsize=16)

### Set font styles
plt.text(0.135,-0.34,'02',color='w',fontsize=13)
plt.text(1.135,-0.34,'03',color='w',fontsize=13)
plt.text(2.135,-0.34,'04',color='w',fontsize=13)
plt.text(3.135,-0.34,'05',color='w',fontsize=13)
plt.text(4.135,-0.34,'06',color='w',fontsize=13)
plt.text(5.135,-0.34,r'\textbf{07}',color='w',fontsize=13)
plt.text(6.136,-0.34,'08',color='w',fontsize=13)
plt.text(7.135,-0.34,'09',color='w',fontsize=13)
plt.text(8.135,-0.34,'10',color='w',fontsize=13)
plt.text(9.135,-0.34,'11',color='w',fontsize=13)
plt.text(10.135,-0.34,r'\textbf{12}',color='w',fontsize=13)
plt.text(11.135,-0.34,'13',color='w',fontsize=13)
plt.text(12.135,-0.34,'14',color='w',fontsize=13)
plt.text(13.135,-0.34,'15',color='w',fontsize=13)
plt.text(14.135,-0.34,'16',color='y',fontsize=13)
plt.text(0.03,-0.6,r'\textbf{DATA:} JAXA (Arctic Data archive System, NIPR)',
         fontsize=6,rotation='horizontal',ha='left',color='w')
plt.text(0.03,-0.8,r'\textbf{CSV:} https://ads.nipr.ac.jp/vishop/vishop-extent.html',
         fontsize=6,rotation='horizontal',ha='left',color='w')
plt.text(15,-0.6,r'\textbf{GRAPHIC:} Zachary Labe (@ZLabe)',
         fontsize=6,rotation='horizontal',ha='right',color='w') 
plt.text(13.6,currentice+0.1,r'Current',color='y')
plt.text(-0.55,6.3,r'\textbf{Arctic Sea Ice Min Extent (2002-%s)}' % currentyr,
                       fontsize=18,color='w') 

### Save figure 
plt.savefig(directory + 'MinSeaIceExtent_JAXA_sample.png',dpi=500)              

print 'Completed script!'    