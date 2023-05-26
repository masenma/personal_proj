import matplotlib.pyplot as plt


with open("analytics.txt", "r") as f:
    values = [float(x) for x in f.read().split(",")[:-1]]


bins = [0, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20]

counts, edges, patches = plt.hist(values, bins=bins, edgecolor='black')


plt.xlabel("Multipliers")
plt.ylabel("Number of occurrences")
plt.title("Results of 10,000 Crash Games")


for i, count in enumerate(counts):
    plt.text(edges[i] + 0.5, count + 5, str(int(count)))


plt.show()


total_count = len(values)
percent_1 = sum(1 for x in values if x == 1) / total_count * 100
percent_1_to_2 = sum(1 for x in values if 1 < x <= 2) / total_count * 100
percent_2_to_3 = sum(1 for x in values if 2 < x <= 3) / total_count * 100
percent_3_to_10 = sum(1 for x in values if 3 < x <= 10) / total_count * 100
percent_above_10 = sum(1 for x in values if x > 10) / total_count * 100


largest_num = max(values)


print(f"Percentage of results that are 1: {percent_1:.2f}%")
print(f"Percentage of results between 1 and 2: {percent_1_to_2:.2f}%")
print(f"Percentage of results between 2 and 3: {percent_2_to_3:.2f}%")
print(f"Percentage of results between 3 and 10: {percent_3_to_10:.2f}%")
print(f"Percentage of results above 10: {percent_above_10:.2f}%")
print(f"The largest number is: {largest_num}x")

plt.show()