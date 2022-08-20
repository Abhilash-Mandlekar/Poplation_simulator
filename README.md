# Population Simulator

## Overview
This similation is about how the population of the city will increase from 50 to 100K with progressing years.

It works as follows:

1) The program initializes with the 50 people with random genders and random age (between 18 to 50).

2) The population keeps on getting added based on the reproduce functioanlity which adds a new person into the population. (Based on the constraints). A female can reproces with the chance of 20% if she is in the age between 18 to 35. This will add a new person into the simulation model.

3) Harvest method tracks the food resources available for the city.

4) The person will die at an age of 80.

5) Natural disasters can occur with 10% chances every year. This method call needs to uncomment in the code (runYear method) if you want this functionality. 5-15% individuals can be dead.

6) Infant mortality is the rate by which an individual can die if he/she is between 0-1 year old. It has 5% chance. This method call needs to uncomment in the code (runYear method) if you want this functionality.

7) This simulation model keeps on running till the population reaches either 0 or till 100K.

## Check the <B>screenshots</B> to see how the model will run and to see the graphs of population growth

The population growth is exponential in both the cases that is with or without the natural disaster and infant mortality. 

Please check the screenshot or the pbix (PowerBI file) that shows the same.

## Future Scope

The model is not currently tested for edge cases. 
Need to create a new directory to write unit tests and integration tests.

## Results

1) When ran the model <B> without </B> natural disaster and infant mortality - it took <B> 345 days </B> to reach the population of 100K. The whole_log.csv in "Logs" folder has the same. 

2) When ran the model <B> with </B> natural disaster and infant mortality - it took <B> 626 days </B> to reach the population of 100K. The whole_log2.csv in "Logs" folder has the same. 


### Note: The results are subject to change as the model uses random functions to initialize the population.


