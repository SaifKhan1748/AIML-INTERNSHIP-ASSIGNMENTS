'''
Assignment (28/02/2026)
Assignment Name : Storytelling with Graphs
Description : Create bar chart, pie chart, histogram and 
write a short data story explaining trends..
'''

import matplotlib.pyplot as plt
import numpy as np

# Sample Data
subjects = ['Math', 'Science', 'English', 'Computer']
marks = [85, 90, 75, 95]


# Bar Chart

plt.figure()
plt.bar(subjects, marks)
plt.title("Marks in Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Pie Chart

plt.figure()
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.show()

# Histogram

data = [55, 60, 65, 70, 75, 80, 85, 90, 95, 88, 92, 78, 74, 69]

plt.figure()
plt.hist(data, bins=5)
plt.title("Marks Frequency Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()