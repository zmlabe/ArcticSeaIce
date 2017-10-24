# ArcticSeaIce
Repository contains scripts for plotting routines of Arctic sea ice and atmospheric parameters ```[Python 2.7]```.

###### Under construction...

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

## Data
###### Reanalysis Data 
+ NCEP/NCAR Reanalysis 1 : [[DATA]](https://www.esrl.noaa.gov/psd/data/gridded/data.ncep.reanalysis.html)
    + Kalnay, E., and co-authors, 1996: The NCEP/NCAR 40-year reanalysis project. Bulletin of the American meteorological Society, 77(3), 437-471 [[Publication]](http://journals.ametsoc.org/doi/abs/10.1175/1520-0477(1996)077%3C0437:TNYRP%3E2.0.CO;2)
###### Sea Ice Concentration/Extent
+ AMSR2 (JAXA Arctic Data archive System, NIPR) : [[DATA]](https://ads.nipr.ac.jp/vishop/#/monitor)
+ Sea Ice Index, Version 3 : [[DATA]](https://nsidc.org/data/seaice_index/)
    + Fetterer, F., K. Knowles, W. Meier, M. Savoie, and A. K. Windnagel, 2017: updated daily. Sea Ice Index, Version 3. Boulder, Colorado USA. NSIDC: National Snow and Ice Data Center. doi:http: //dx.doi.org/10.7265/N5K072F8. [[Documentation]](http://nsidc.org/data/g02135)
+ SSMIS Sea Ice Concentration (EUMETSAT OSI SAF) : [[DATA]](http://osisaf.met.no/p/ice/#conc_details)
###### Sea Ice Volume
+ Pan-Arctic Ice Ocean Modeling and Assimilation System (PIOMAS) : [[DATA]](http://psc.apl.uw.edu/research/projects/arctic-sea-ice-volume-anomaly/data/model_grid)
    + Zhang, J., and D. A. Rothrock, 2003: Modeling Global Sea Ice with a Thickness and Enthalpy Distribution Model in Generalized Curvilinear Coordinates. Monthly Weather Review, 131 (5), 845–861, doi:10.1175/1520-0493(2003)131<0845:MGSIWA>2.0.CO;2 [[Publication]](http://journals.ametsoc.org/doi/abs/10.1175/1520-0493%282003%29131%3C0845%3AMGSIWA%3E2.0.CO%3B2)
