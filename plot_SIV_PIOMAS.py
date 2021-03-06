"""
Plots PIOMAS daily Sea Ice Volume for 1979-2016

Website   : http://psc.apl.uw.edu/research/projects/arctic-sea-ice-volume-
            anomaly/data/
Author    : Zachary M. Labe
Date      : 15 July 2016
"""

### Import modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as c
import datetime

### Directory and time
directorydata = '...'                    # enter directory
directoryfigure = '...'                  # enter directory

day = map(int,day)
now = datetime.datetime.now()
currentmn = str(now.month-1)
currentdy = str(now.day)
currentyr = str(now.year)
years = np.arange(1979,2017,1)

### Read data
year,day,volume = np.loadtxt(directorydata + \
                          'PIOMAS.vol.daily.1979.2016.Current.v2.1.dat.gz',
                          skiprows=1,unpack=True)

### Reshape sea ice volumes arrays
currentyear = volume.copy()[-day[-1]:]
volumen = volume[:-day[-1]]

volumen = np.reshape(volumen,(volumen.shape[0]/365,365))

### Calculate mean volume
mean = np.nanmean(volumen,axis=0)

### x-coordinates
doy = np.arange(0,np.nanmax(day))

### Calculate minimum
minsiv = np.nanmin(volumen[:,day[-1]])
minyear = np.where(volumen[:,day[-1]] == minsiv)[0]
timeyr = years[minyear][0]

### Make plot
plt.rc('savefig', facecolor='black')
plt.rc('axes', edgecolor='white')
plt.rc('xtick', color='white')
plt.rc('ytick', color='white')
plt.rc('axes', labelcolor='white')
plt.rc('axes', facecolor='black')
plt.rc('text',usetex=True)
plt.rc('font',**{'family':'sans-serif','sans-serif':['Avant Garde']}) 

### Return information
print '\n' 'PIOMAS -- Sea Ice Volume --', now.strftime("%Y-%m-%d %H:%M"), '\n' '\n' 
print 'Completed: Reading Data!'
print 'Completed: Reshaping Data!' '\n' '\n' 
print 'Current Sea Ice Volume = %s [x1000 km^3]' % currentyear[-1]
print 'Lowest previous record = %s --> %s [x1000 km^3]' % (timeyr,minsiv) 

### Plot Arctic sea ice volume
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
        
### Plot mean sea ice volume        
plt.plot(doy,mean,color='white',linewidth=3,label='Average Volume',
         zorder=3,linestyle='-')

### Use colormap for each year 
color=iter(plt.cm.magma(np.linspace(0,1,volumen.shape[0])))
for i in xrange(volumen.shape[0]):
    if i == 33:
        c = 'r'
        l = 2
        plt.plot(doy,volumen[i,:],c=c,zorder=2,linewidth=l,label='Year 2012')
    else:
        c=next(color)
        l = 0.4
        plt.plot(doy,volumen[i,:],c=c,zorder=1,linewidth=l)

### Plot current year sea ice volume
plt.plot(doy[:day[-1]],currentyear,color='lime',linewidth=2,
         label='Year 2016',zorder=6)
plt.scatter(day[-1],currentyear[-1],
            s=6,color='lime',zorder=4,marker='o')
 
### Adjust legend and axes                      
le = plt.legend(shadow=False,fontsize=8,loc='upper right',fancybox=True)
for text in le.get_texts():
    text.set_color('w')
                       
ax.tick_params('both',length=7.5,width=2,which='major')             
adjust_spines(ax, ['left','bottom'])            
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
plt.ylabel(r'\textbf{Sea Ice Volume [$\times$1000 km$^{3}$]}',fontsize=11)

### x-ticks
xlabels = [r'Jan',r'Feb',r'Mar',r'Apr',r'May',r'June',r'July',
          r'Aug',r'Sept',r'Oct',r'Nov',r'Dec',r'Jan']
plt.xticks(np.arange(0,361,30),xlabels,rotation=0)
plt.xlim([0,360])

### y-ticks
plt.yticks(np.arange(int(np.nanmin(volume)-1),int(np.nanmax(volume)+2),2),
           map(str,np.arange(int(np.nanmin(volume)-1),
                             int(np.nanmax(volume)+2),2)),fontsize=11)
plt.ylim([int(np.nanmin(volume)-1),int(np.nanmax(volume)+1)])

### Add text
plt.subplots_adjust(bottom=0.15)  

plt.text(0.5,4.7,r'\textbf{DATA:} PIOMAS [Zhang and Rothrock, 2003]',
         fontsize=7,rotation='horizontal',ha='left',color='w')
plt.text(0.5,3.4,r'\textbf{CSV:} http://psc.apl.washington.edu/zhang/IDAO/',
         fontsize=7,rotation='horizontal',ha='left',color='w')
plt.text(0.5,2.1,r'\textbf{GRAPHIC:} Zachary Labe (@ZLabe)',
         fontsize=7,rotation='horizontal',ha='left',color='w')

fig.suptitle(r'\textbf{PIOMAS Arctic Sea Ice Volume (1979-%s)}' % currentyr,
                       fontsize=18,color='w') 

plt.savefig(directoryfigure + 'SIV_PIOMAS_sample.png',dpi=900)

print '\n' '\n' 'Completed: Figure plotted!'
