# ArcticSeaIce
Repository contains scripts for plotting routines of Arctic sea ice and atmospheric parameters ```[Python 2.7]```.

######Under construction...

## Contact
Zachary Labe - [Research Website](http://sites.uci.edu/zlabe/) - [@ZLabe](https://twitter.com/ZLabe)

## Description

`plot_MinYears_JAXA.py` --
Bar graph of minimum Arctic sea ice extents over the 2002-present period. Comparison looks at the current sea ice extent versus the minimum years. Data is available by the Japan Aerospace Exploration Agency (JAXA) and through the [Arctic Data archive System (NiPR)](https://ads.nipr.ac.jp/vishop.ver1/vishop-extent.html).

`plot_SeaIceExtent_JAXA.py` --
Daily Arctic sea extent over the 2002-2016 (to-date) is available by the Japan Aerospace Exploration Agency (JAXA) and through the [Arctic Data archive System (NiPR)](https://ads.nipr.ac.jp/vishop.ver1/vishop-extent.html).

`plot_SeaIceExtent_NSIDC.py` --
Daily Arctic sea ice extent is calculated and plotted for the current year (to-date) through the [National Snow & Ice Data Center](https://nsidc.org/arcticseaicenews/) SSM/I-SSMIS F-18 satellite. Climatology (1981-2010) is plotted in addition to two standard deviations from the mean.

`plot_SeaIceConc_SSMIS.py` --
Daily Arctic sea concentration data is available through the [Ocean and Sea Ice SAF](http://osisaf.met.no/p/ice/) F-18 satellite. Data is provisional from the DMSP F-18 satellite as a result of F-17 satellite errors [(for more information)](https://nsidc.org/arcticseaicenews/2016/05/daily-sea-ice-extent-updates-resume-with-provisional-data/).

`plot_SIV_PIOMAS.py` --
Daily Arctic sea ice volume (SIV) is available through [PIOMAS (Zhang and Rothrock, 2003)](http://psc.apl.uw.edu/research/projects/arctic-sea-ice-volume-anomaly/) at the beginning of each month. Sea ice volume is available from 1979 to present and averaged over the entire Arctic. Gridded products are also [available](http://psc.apl.washington.edu/zhang/IDAO/). 

`plot_ZonalTAS_NCEP.py` --
Mean zonal surface temperatures over the Arctic Circle (north of 66°) through NCEP reanalysis. Data available using the [ESRL toolbox](http://www.esrl.noaa.gov/psd/cgi-bin/data/timeseries/timeseries1.pl). Grid cells are weighted and data available for yearly (January - to-date, monthly) time frames.
