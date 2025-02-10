# Exercise 5. Find the highest score
# Create a Python function named find_max_score that takes a dictionary of names and scores as an argument.
# The function should return the name and score of the person with the highest score in the form of a dictionary.
def find_max_score(scores_dict):
    result = {}
    max_score = 0
    for name, score in scores_dict.items():
        if score >= max_score:
            max_score = score
            result = {name: score}

    return result
# Sample test_scores dictionary
test_scores = {
  'James': 83,
  'Julia': 91,
  'Ryan': 90,
  'Maria': 80,
  'David': 79,
  'Adam': 96,
  'Jennifer': 97,
  'Susan': 77
}
highest_scorer = find_max_score(test_scores)
print(highest_scorer)
#  Find the person with the highest test score and display both their name and score

# Steps:
# - Define a function called find_max_score that takes one argument, scores_dict, which is a dictionary of names
#   (as keys) and scores (as values).
# - Create an empty result variable
# - Assume the initial maximum score is 0
# - Iterate over each key-value pair in the test_scores, using the .items() method
# - Check if the current score (v) is >= to the current maximum score
# - If so, update the max score and assign the key-value pair to the result
# - Return result and test the function