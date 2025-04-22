# Identification of Exoplanets Using NASA Kepler Light Curve Data

## Project Description
NASA recorded the brightness of stars in an attempt to find planets outside of our solar system through missions titled Kepler and K2. Exoplanets can be identified by looking for dips in brightness which typically means a planet is crossing in front of the star (called a transit). The light curves for thousands of stars were recorded along with contextual information such as whether the transit is a true planet, candidate, or false positive. The motive for this project will be to categorize transits as either true planets or non-planets (false positives). To interact with the final results, a conversational agent will be released.

## General Understanding
For an overview of the project objective, methodology, and findings refer to the *Report* folder which contains information for each milestone. To run the code, ensure files in the *Data* and *Scripts* folders are extracted to your working directory.

## Data Collection
To download the data required, refer to *data_access_info.txt* in the *Data* folder. Then, run *data_collection.ipynb* from *Scripts*. This will fetch the required SQLite database and CSV file. A copy of the required CSV file, *KOI_cumulative.csv*, was provided but the SQLite database will have to be generated through *data_collection.ipynb* due to the large size of the database.

## Data Processing
The report for the first milestone has a macro view of the process. For a more detailed view, there are markdown cells in *data_processing.ipynb* from *Scripts*. To replicate results, reading the markdown cells is highly encouraged. The cleaned version *KOI_cumulative.csv* is saved as *KOI_cumulative_cleaned.csv* in the *Data* folder.

## Feature Selection/Engineering and Model Training
This process is covered in *training.ipynb* from *Scripts*. Three contextual features from *KOI_cumulative.csv* were selected and 30 time steps from a given light curve, centered around the first detected transit, were used (from the SQL database of light curves). For each time step, the associated time, PDC SAP flux (corrected star brightness), etc. were saved as *transits.csv* which can be found in the *Data* folder. A random forest classifier, logistic regression model, and RNN were hyperparameter tuned for precision. This is explained in detail in the Jupyter Notebook and the second milestone report. The trained models are saved as *.pkl* files in the *Models* folder; the RNN also has its history and a dictionary of the chosen hyperparameters saved.

## Testing
The models were evaluated on the test set in *testing.ipynb* from *Scripts*. Potential biases were explored.

## Chatbot
*chatbot_dev.ipynb* from *Scripts* covers the development of the chatbot to answer project-related questions. Unlike the other scripts, the directory structure of the GitHub is used and files generally do not need to be extracted to the working space as long as the working directory is *Scripts*. To use the chatbot, simply run the *chatbot_app.py* in *Scripts*.

## Video Demonstrations
- **Project Overview**: https://youtu.be/yYLAPwx-Lss
- **Chatbot Demo**: https://youtu.be/BpDTeVWMHE4
