# Identification of Exoplanets Using NASA Kepler Light Curve Data

## Project Description
NASA recorded the brightness of stars in an attempt to find planets outside of our solar system through missions titled Kepler and K2. Exoplanets can be identified by looking for dips in brightness which typically means a planet is crossing in front of the star (called a transit). The light curves for thousands of stars were recorded along with contextual information such as whether the transit is a true planet, candidate, or false positive. The motive for this project will be to categorize transits into one of these fields. To interact with the final results, a conversational agent will be released.

## General Understanding
For an overview of the project objective, methodology, and findings refer to the *Report* folder which contains information for each milestone.

## Data Collection
To download the data required, refer to *data_access_info.txt* in the *Data* folder. Then, run *data_collection.ipynb* from *Scripts*. This will fetch the required SQLite database and CSV file. A copy of the required CSV file, *KOI_cumulative.csv*, was provided but the SQLite database will have to be generated through *data_collection.ipynb* due to the large size of the database.

## Data Processing
The report for the first milestone has a macro view of the process. For a more detailed view, there are markdown cells in *data_processing.ipynb*. To replicate results, reading the markdown cells is highly encouraged.
