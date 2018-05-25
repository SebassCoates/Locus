# Dynamic Locus Display

The objective of this project was to better utilize data on Locus users, in 
order to enhance their user experience. Currently, users have to spent a lot of
time and waste many clicks in order to find the pages that they need. 
Understanding the history of individual users and the relationships between 
users presents an opportunity to make Locus much more efficient.

## Results

According to test data (a 90/10 train-test-split), the page-links displayed
on the homepage have a 70% chance of containing the exact link a user wants
when they access Locus. With access to more features, and more analysis tools,
this can only get better. 

## Running The Code and Replicating the Results
unzip the training data from the .zip file in /data
Run parser.py to analyze the data and produce data for 
multi-class classification algorithms. Once this has been 
run, model\_selection.py can be run to determine the most
effective model for the data.   
Similarly timeseries\_parser.py produces time-based data
to be trained with RNN.py.
Moving the produced .txt files and the produced models to
the /webapp folder, allows the full mockup to use the models
in its prediction.
Start the webserver with:
```
python3 -m flask run
```
