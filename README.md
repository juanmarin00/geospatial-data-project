# geospatial-data-project
Fourth project for IronHack Data Analytics BootCamp: https://github.com/ironhack-datalabs/datamad1020-rev/tree/master/projects/W4-geospatial-data-project

In this project we had to use our newly gained skills in MongoDB and geoqueries together with our existing knowledge of Python, APIs, NumPy and Pandas to find the best location for an office based on a certain criteria.

I queried all the required data from MongoDb using PyMogno and then used FourSquare's API to do the rest of the filtering and ordering. To order the chosen locations I created a model which computed the sum of the distance between each office location and key places such as airports and schools and then whichever location had the leasr value would be chosen as the perfect location.

In this Notebook you can find the final cleaned and ordered dataset (sorted_companies.csv), the notebook where all the work took place and a functions .py file which contains the functions used in the previously mentioned notebook.

**I hope you enjoy my project!**
