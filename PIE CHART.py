import matplotlib.pyplot as plt

slices=[7,2,2,13]
activities=['sleeping','eating','working','playing']
colors=['c','m','r','b']

plt.pie(
    slices,
    labels=activities,
    colors=colors,
    startangle=270,
    shadow=True,
    explode=(0.1,0.1,0.1,0.1),
    autopct='%0.2f%%'
    )
plt.title("PIE CHART EXAMPLE")
plt.show()
