# gist-604b-assignment2
GIST 604B Assignment 2: QGIS Desktop GIS Projects

## Overview
This repository contains QGIS project files and screenshot outputs from ten completed tutorials on qgistutorials.com. The tutorials cover foundational desktop GIS skills including map creation, coordinate reference systems, attribute and spatial data management, vector and raster styling, and spatial analysis operations. Each tutorial was completed in QGIS and saved as a `.qgz` project file alongside a screenshot capturing the layers panel and map canvas. Together, these projects demonstrate a working proficiency in core QGIS workflows applicable to real-world GIS analysis tasks.

## Software Environment
- **QGIS Version:** QGIS 3.34 LTR
- **Operating System:** macOS
- **Plugins:** No additional plugins required for the completed tutorials

## Completed Tutorials
- Learning
- [Making a Map](https://www.qgistutorials.com/en/docs/3/making_a_map.html)
- [Working with Projections](https://www.qgistutorials.com/en/docs/3/working_with_projections.html)
- [Working with Attributes](https://www.qgistutorials.com/en/docs/3/working_with_attributes.html)
- [Importing Spreadsheets or CSV Files](https://www.qgistutorials.com/en/docs/3/importing_spreadsheets_csv.html)
- [Basic Vector Styling](https://www.qgistutorials.com/en/docs/3/basic_vector_styling.html)
- [Basic Raster Styling and Analysis](https://www.qgistutorials.com/en/docs/3/basic_raster_styling.html)
- [Performing Table Joins](https://www.qgistutorials.com/en/docs/3/performing_table_joins.html)
- [Performing Spatial Joins](https://www.qgistutorials.com/en/docs/3/performing_spatial_joins.html)
- [Performing Spatial Queries](https://www.qgistutorials.com/en/docs/3/performing_spatial_queries.html)
- [Interpolating Point Data](https://www.qgistutorials.com/en/docs/3/interpolating_point_data.html)

## Skills Demonstrated
- Creating and exporting print-ready maps with titles, legends, and scale bars
- Working with coordinate reference systems (CRS) and on-the-fly reprojection
- Editing and querying attribute tables using expressions
- Importing CSV and spreadsheet data and plotting point locations
- Applying vector symbology including categorized and graduated styles
- Loading and styling raster data with custom color ramps
- Performing table joins to link non-spatial data to spatial layers
- Running spatial joins to transfer attributes between overlapping features
- Executing spatial queries to select features by location and attribute
- Interpolating point data to create continuous raster surfaces

## Reflection
Working through these tutorials reinforced how fundamental coordinate reference systems are to every GIS workflow — understanding when and why to reproject data became much clearer through hands-on experimentation. The attribute table editing and join tutorials highlighted the close relationship between spatial and tabular data that underpins most real-world GIS analysis. The most challenging part was managing data sources across multiple tutorials, particularly ensuring that file paths in QGIS project files remained valid after moving or reorganizing data. Spatial queries and spatial joins required careful attention to layer order and join type, concepts that were easier to grasp visually in QGIS than in purely written explanations. I also found raster styling more nuanced than expected, since small adjustments to the color ramp or stretch settings could dramatically change how patterns appeared in the map. These skills directly support my work in spatial analysis and remote sensing, where combining vector and raster data sources is a routine requirement. I anticipate using QGIS alongside Python-based tools like GeoPandas and Rasterio, treating each as complementary parts of an open source GIS workflow.
