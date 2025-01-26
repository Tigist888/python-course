# Create an empty list and add the following elements about your location, in this order:
# - City
# - State or Province
# - A list with the temperatures the last three days
# - Your favorite animal

my_list=[]
my_list.append("Nashville")
my_list.append("Tn")
my_list.append("45,50,60")
my_list.append("dog")

# Then, remove the State, without using the indexes.
my_list.remove("Tn")

# Bonus: Remove the last element, using a negative index.
del my_list[-1]
