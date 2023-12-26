#  class SwissRandom
The class generates a (random) set of coordinates in the common Swiss LV95 system within the borders of Switzerland and/or checks if they are in the country.

~~It also supports WSG84 and the obsolete LV03 coordinate system.~~ The class can also be used to check if existing coordinates are within Switzerland.

## Swiss coordinate system
The Swiss coordinate system (or Swiss grid) is a geographic coordinate system used in Switzerland
and Liechtenstein for maps and surveying by the Swiss Federal Office of Topography (Swisstopo).

<Read more: https://www.swisstopo.admin.ch/en/knowledge-facts/surveying-geodesy/reference-frames/local.html

## List of extreme points in Switzerland
| Points | LV95 E | LV95 N | WGS84 Lat | WGS84 Lon |
| --- | --- | --- | --- | --- |
| Northernmost point in Switzerland | 2'684'602 | 1'295'934 | 47.80845 | 8.56803 |
| Most easterly point in Switzerland | 2'833'859 | 1'166'962 | 46.61296 | 10.49219 |
| Southernmost point of Switzerland | 2'722'707 | 1'075'269 | 45.81796 | 9.01734 |
| Westernmost point of Switzerland | 2'485'410 | 1'110'070 | 46.13236 | 5.95590 |

>Source: [Wikipedia DE](https://de.wikipedia.org/wiki/Geographische_Extrempunkte_der_Schweiz)

>Verified and also converted to the outdated LV03 coordinate system on https://map.geo.admin.ch/

## Missing features:

- A set of user-defined minimum and maximum coordinates to limit the result to a specific area.
- Support for WSG84 and the old LV03 coordinate systems.
- Conversion between the three coordinate systems.

## Shape file
File: *..data/swissBOUNDARIES3D_1_5_TLM_LANDESGEBIET.shp*

Source: [Bundesamt für Landestopografie swisstopo](https://www.swisstopo.admin.ch/de/geodata/landscape/boundaries3d.html)

Downloaded: 26. December 2023

## Requirements

- geopandas==0.14.1
- shapely==2.0.2

## Version

Version 0.5 / chme / 2023-12-26
