# Here are some statistics about the city of Houston
# Complete the print() statements to answer the questions.
my_city = {
   'name' : 'Houston',
   'demographics_pct' : {
       'hispanic' : 44.0,
       'white' : 23.7,
       'black' : 22.1,
       'asian' : 7.1
   },
   'airports' : [
       'George Bush Intercontinental',
       'William P. Hobby'
   ]
}

# What is the name of the city?
print(my_city['name'])

# How would you print the percentage of the Hispanic population?
print(my_city['demographics_pct']['hispanic'])

# What is the last airport of the list of airports?
print(my_city['airports'][-1])
