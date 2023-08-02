import numpy as np

student_scores = np.array([
    [85, 90, 78, 92],
    [70, 88, 81, 85],
    [92, 78, 84, 82],
    [94, 80, 83, 83],
   [90,  87, 92, 87],
    [80, 82, 88, 78],
    [92, 78, 84, 80],
    [94, 74, 87, 89],
    [85, 90, 78, 92],
    [70, 78, 86, 85],
    [92, 78, 84, 83],
    [94, 80, 82, 78],
    [72, 81, 95, 81],
    [95, 85, 88, 78],
    [88, 76, 84, 91],
    [90, 87, 92, 87],
    [85, 90, 78, 92],
  [88, 76, 84, 91],
    [90, 79, 92, 77],
    [80, 84, 83, 78],
   [72, 60, 95, 81],
    [95, 85, 85, 78],
    [88, 76, 84, 91],
    [90, 89, 92, 87],
    [85, 90, 78, 92],
    [72, 70, 95, 81],
    [95, 85, 89, 78],
    [88, 76, 84, 91],
   [95, 85, 81, 78],
    [88, 76, 84, 60],
    [90, 89, 92, 87],
    [80, 82, 83, 78],
])
average_scores = np.mean(student_scores, axis=0)

highest_avg_subject_index = np.argmax(average_scores)

subjects = ['Math', 'Science', 'English', 'History']

print("Average scores for each subject:")
for i, subject in enumerate(subjects):
    print(f"{subject}: {average_scores[i]:.2f}")

print(f"\nThe subject with the highest average score is: {subjects[highest_avg_subject_index]}")



