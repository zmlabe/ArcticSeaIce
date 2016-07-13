"""
Plots Arctic sea ice extent from June 2002-present using JAXA metadata
Website   : https://ads.nipr.ac.jp/vishop/vishop-extent.html
Author    : Zachary M. Labe
Date      : 13 June 2016
"""

### Import modules
import numpy as np
import urllib2
import datetime
import matplotlib.pyplot as plt

### Directory and time
directory = '...'                        # enter present working directory
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
currentanom = currentice - (mean1980[lastday]/1e6)

### Changes in sea ice
weekchange = currentice - currentyear[lastday-7]
daychange = currentice - currentyear[lastday-1]

print 'JAXA Arctic Sea Ice Extent'
print '\nCurrent Date =', now.strftime("%Y-%m-%d %H:%M"), '\n'
print 'Current SIE = %s km^2' % (currentice*1e6)
print 'Current Anomaly = %s km^2 \n' % (currentanom*1e6)
print '1-day SIE Change = %s km^2' % (daychange*1e6)
print '7-day SIE Change = %s km^2 \n' % (weekchange*1e6)

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

### x-labels
xlabels = [r'Jan',r'Feb',r'Mar',r'Apr',r'May',r'June',r'July',
          r'Aug',r'Sept',r'Oct',r'Nov',r'Dec',r'Jan']
plt.xticks(np.arange(0,361,30),xlabels,rotation=0)

### y-labels
ylabels = map(str,np.arange(2,18,2))
plt.yticks(np.arange(2,18,2),ylabels)

plt.ylim([2,16])
plt.xlim([0,360])

### Define date
strmonth = xlabels[int(currentmn)-1]
asof = strmonth + ' ' + currentdy + ', ' + currentyr

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

### Adjust axes spines
adjust_spines(ax, ['left', 'bottom'])
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
plt.setp(ax.get_xticklines()[1:-2],visible=False)
plt.grid(color='w',zorder=1,alpha=0.3)
plt.tick_params('both', length=5, width=2, which='major') 

### Set labels
plt.ylabel(r'\textbf{SIE [$\bf{\times 10^{6}\ km^2}$]}',fontsize=20)
fig.suptitle(r'\textbf{JAXA Arctic Sea Ice Extent (2002-%s)}' % currentyr,
                       fontsize=20,color='w') 

### Color scheme for time series years
color=iter(plt.cm.PuBuGn(np.linspace(0,1,years.shape[1])))
for i in xrange(years.shape[1]):
    if i == (years.shape[1]-1):
        c = 'red'
    else:
        c=next(color)
    plt.plot(doy,years[:,i],c=c,zorder=1)

plt.scatter(doy[lastday],currentyear[lastday],
            s=5,color='r',zorder=2)

### Insert sea ice text                        
if lastday <= 250:
    xcord = lastday - 5
    ycord = round(currentice)-1.3
    plt.text(xcord,ycord,r'\textbf{%s}' '\n' r'\textbf{%s} $\bf{km^2}$' \
    % (asof,format(currentice*1e6,",f")[:-7]),fontsize=11,rotation='horizontal',ha='right',color='r')
else:    
    xcord = lastday + 8
    ycord = round(currentice)-1.5
    plt.text(xcord,ycord,r'\textbf{%s}' '\n' r'\textbf{%s} $\bf{km^2}$' \
    % round(currentice,3),fontsize=11,rotation='horizontal',ha='left') 

if lastday <= 150:
    plt.text(xcord,ycord-2.5,r'\textbf{7--day change}'\
        '\n' r'\textbf{%s} $\bf{km^2}$'\
        % (format(weekchange*1e6,",f")[:-7]),fontsize=10,
        rotation='horizontal',ha='right') 
    plt.text(xcord,ycord-4.2,r'\textbf{1--day change}' \
        '\n' r'\textbf{%s} $\bf{km^2}$'\
        % (format((daychange*1e6),",f")[:-7]),fontsize=10,
        rotation='horizontal',ha='right') 

plt.text(0.5,2.7,r'\textbf{DATA:} JAXA (Arctic Data archive System, NIPR)',
         fontsize=7,rotation='horizontal',ha='left',color='w')
plt.text(0.5,2.2,r'\textbf{CSV:} https://ads.nipr.ac.jp/vishop/vishop-extent.html',
         fontsize=7,rotation='horizontal',ha='left',color='w')
plt.text(0.5,1.7,r'\textbf{GRAPHIC:} Zachary Labe (@ZLabe)',
         fontsize=7,rotation='horizontal',ha='left',color='w')
         
### Create subplot         
a = plt.axes([.55, .61, .25, .25], axisbg='w')
        
ylimsu = round(currentice)+1
ylimsb = round(currentice)-1
xlimsu = lastday+15
xlimsb = lastday-15
color=plt.cm.PuBuGn(np.linspace(0,1,years.shape[1]))
for i,c in zip(xrange(years.shape[1]),color):
    if i == (years.shape[1]-1):
        c = 'red'
        l = 3
    else:
        l = 2   
    plt.plot(doy, years[:,i],c=c,linewidth=l,zorder=1)
plt.scatter(doy[lastday],currentyear[lastday],
            s=15,color='k',zorder=2)
plt.title(r'\textbf{Anomaly [1980] = %s' % round(currentanom,3),fontsize=10)
plt.xlim([xlimsb,xlimsu])
plt.ylim([ylimsb,ylimsu])
plt.grid(alpha=0.4)
labelsx2 = map(str,np.arange(xlimsb+1,xlimsu+2,15))
labelsy2 = map(str,np.arange(int(ylimsb),int(ylimsu+1),0.5))
plt.xticks(np.arange(xlimsb,xlimsu+1,15),labelsx2,fontsize=8)
plt.yticks(np.arange(ylimsb,ylimsu+1,0.5),labelsy2,fontsize=8)
plt.ylabel(r'$\bf{\times 10^{6}\ km^2}$',fontsize=8)
plt.xlabel(r'\textbf{day of year}',fontsize=8)

### Save figure 
plt.savefig(directory + 'JAXAseaice_%s.png' % currenttime,dpi=500)              

print 'Completed script!'    