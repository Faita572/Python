# A dictionary where the value for "scores" is a list
student_data = {
    "name": "Jordan",
    "scores": [85, 92, 78, 90]
}

#To calculate Jordan's average score... we need to; i) grab the list of scores from the dictionary, ii) add all the scores together, and iii) divide by the total number of scores.
student_data = {
    "name": "Jordan",
    "scores": [85, 92, 78, 90]
}

# 1. Pull the list of scores out of the dictionary 
all_scores = student_data["scores"]

# 2. Initialize a running total
total_sum = 0

# 3. Add all the scores together by looping
for score in all_scores:
    total_sum = total_sum + score

# 4. Calculate the average
number_of_tests = len(all_scores)
average_score = total_sum / number_of_tests

# 5. Print the final result
print(student_data["name"] + " has an average score of " + str(average_score))