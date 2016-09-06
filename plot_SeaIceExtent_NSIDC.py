"""
Reads in current year's Arctic sea ice extent from Sea Ice Index 2 (NSIDC)

Website   : ftp://sidads.colorado.edu/DATASETS/NOAA/G02135/north/daily/data/
Author    : Zachary M. Labe
Date      : 5 September 2016
"""

### Import modules
import numpy as np
import urllib2
import datetime
import matplotlib.pyplot as plt

### Directory and time
directory = '...'                        # enter working directory
now = datetime.datetime.now()
currentmn = str(now.month)
currentdy = str(now.day)
currentyr = str(now.year)
currenttime = currentmn + '_' + currentdy + '_' + currentyr
currentdoy = now.timetuple().tm_yday

### Load url
url = 'ftp://sidads.colorado.edu/DATASETS/NOAA/G02135/north/daily/' \
        'data/NH_seaice_extent_nrt_v2.csv'

### Read file
raw_data = urllib2.urlopen(url)
dataset = np.genfromtxt(raw_data, skip_header=2,delimiter=',',
                        usecols=[0,1,2,3,4])
                        
print '\nCompleted: Read sea ice data!'                        

### Set missing data to nan
dataset[np.where(dataset==-9999)] = np.nan

### Variables
year = dataset[:,0]
month = dataset[:,1]
day = dataset[:,2]
ice = dataset[:,3]
missing = dataset[:,4]

### Ice Conversion
iceval = ice * 1e6

### Printing
print '\n----- NSIDC Arctic Sea Ice -----'
print 'Current Date =', now.strftime("%Y-%m-%d %H:%M"), '\n'

print 'SIE Date    = %s/%s/%s' % (int(month[-1]),int(day[-1]),int(year[-1]))
print 'Current SIE = %s km^2 \n' % (iceval[-1])

print '1-day change SIE = %s km^2' % (iceval[-1]-iceval[-2])
print '7-day change SIE = %s km^2 \n' % (iceval[-1]-iceval[-8])
    
###########################################################################
###########################################################################
###########################################################################
### Reads in 1981-2010 climatology
### Load url
url2 = 'ftp://sidads.colorado.edu/DATASETS/NOAA/G02135/north/daily/data/' \
       'NH_seaice_extent_climatology_1981-2010_v2.csv'

### Read file
raw_data2 = urllib2.urlopen(url2)
dataset2 = np.genfromtxt(raw_data2, skip_header=2,delimiter=',',
                        usecols=[0,1,2])
                        
### Create variables
doy = dataset2[:,0]
meanice = dataset2[:,1] * 1e6
std = dataset2[:,2]

### Anomalies
currentanom = iceval[-1]-meanice[currentdoy-2]

### Printing
print 'Current anomaly = %s km^2 \n' % currentanom   

###########################################################################
###########################################################################
###########################################################################
### Define parameters
plt.rc('text',usetex=True)
plt.rc('font',**{'family':'sans-serif','sans-serif':['Avant Garde']}) 
plt.rc('savefig',facecolor='black')
plt.rc('axes',edgecolor='white')
plt.rc('xtick',color='white')
plt.rc('ytick',color='white')
plt.rc('axes',labelcolor='white')
plt.rc('axes',facecolor='black')

### Create plot
fig = plt.figure()
ax = plt.subplot(111)

### Set x/y ticks and labels
xlabels = [r'Jan',r'Feb',r'Mar',r'Apr',r'May',r'Jun',r'Jul',
          r'Aug',r'Sep',r'Oct',r'Nov',r'Dec',r'Jan']
plt.xticks(np.arange(0,361,30),xlabels,rotation=0)
ylabels = map(str,np.arange(2,19,2))
plt.yticks(np.arange(2,19,2),ylabels)

### Set x/y limits
plt.xlim([0,360])
plt.ylim([2,18])

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
  
### Adjust borders of figure      
ax.tick_params('both',length=7.5,width=2,which='major')             
adjust_spines(ax, ['left','bottom'])            
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')  

### Define 2 standard deviations
upper2std = (meanice/1e6)+(std*2)
lower2std = (meanice/1e6)-(std*2)

### Add a grid
ax.grid(zorder=1,color='w',alpha=0.25)

### Plot lines
plt.plot(doy,meanice/1e6,linewidth=2,color='y',zorder=5)
plt.plot(doy,upper2std,color='white',alpha=0.7,zorder=3)
plt.plot(doy,lower2std,color='white',alpha=1,zorder=4,linewidth=2)
ax.fill_between(doy, lower2std, upper2std, facecolor='white', alpha=0.5,
                label=r'$\pm$2 standard deviations',zorder=2)
plt.plot(ice,linewidth=1.3,color='r',zorder=6) 
plt.scatter(doy[currentdoy-2],ice[-1],s=10,color='r')

### Add legend and labels
plt.ylabel(r'\textbf{SIE} [$\times$10$^{6}$ km$^2$]',fontsize=15)
le = plt.legend(shadow=False,fontsize=6,loc='upper left',
           bbox_to_anchor=(0.73, 1.011),fancybox=True)
for text in le.get_texts():
    text.set_color('w')   
    
### Define title
plt.title(r'\textbf{NSIDC Arctic Sea Ice Extent (%s)}' % int(year[-1]),
                       fontsize=14,color='w')         

### Add text box information
plt.text(0.5,3.1,r'\textbf{DATA:} National Snow \& Ice Data Center, Boulder CO',
         fontsize=6,rotation='horizontal',ha='left',color='w')
plt.text(0.5,2.6,r'\textbf{CSV:} ftp://sidads.colorado.edu/DATASETS/NOAA/G02135/',
         fontsize=6,rotation='horizontal',ha='left',color='w')
plt.text(0.5,2.1,r'\textbf{GRAPHIC:} Zachary Labe (@ZLabe)',
         fontsize=6,rotation='horizontal',ha='left',color='w') 
         
### Adjust figure sizing
fig.subplots_adjust(top=0.91)
   
### Save figure     
plt.savefig(directory + 'SeaIceExtent_NSIDC_sample.png',dpi=300)     

print 'Completed script!'     
                  
                        