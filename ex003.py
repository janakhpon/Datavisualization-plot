import matplotlib.pyplot as plt

labels = 'Python', 'Rust', 'Javascript', 'Go', 'Ruby', 'Java', 'Shell', 'C++', 'C'
sizes = [38, 20, 37.5, 17, 10, 27, 8, 10, 5]
separated = (.1, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(sizes, labels=labels, autopct='%1.2f%%', explode=separated)
plt.axis('equal')
plt.show()

