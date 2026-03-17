""""
Brandon Yang

CSCI1380

LAB 4.5
"""
#data of names and scores
names = ["Alice", "Ben", "Chloe", "Daniel", "Ella", "Felix", "Grace", "Hannah", "Isaac", "Jade"]
scores = [8, 9, 6, 9, 7, 10, 8, 10, 5, 9]

print("---------Today's scores---------")

#runs through both names and score list and ties them to their respective values
for x in range(len(names)):
    for y in range(len(scores)):
        if x == y:
            print(f"{names[x]}: {scores[y]}/10 pts")
print()

#starts at first position in scores list
max = scores[0]

#puts current position into a variable
#checks to see if its bigger than the max value
#if it is, store it into the max variable

for i in range(len(scores)):
    current_max = scores[i]
    if current_max > max:
        max = current_max

print("---------Winner(s)---------")

#runs through score list
#if score is the same as max you are a winner
for i in range(len(scores)):
    if scores[i] == max:
        print(names[i])

print()

#makes a file named 'official_report'
Official_Report = open("Official_report.txt", "w")

Official_Report.write("Official Report of todays winners")
Official_Report.write("\n___________________________________")

#writes names and scores
for x in range(len(names)):
    for y in range(len(scores)):
        if x == y:
            Official_Report.write(f"\n{names[x]}: {scores[y]}/10 pts")
print()

#writes winners
Official_Report.write("\n---------Winner(s)---------")
for i in range(len(scores)):
    if scores[i] == max:
        Official_Report.write(f"\n{names[i]}")

#closes file
Official_Report.close()

#opens file in read only
Official_Report = open("Official_report.txt", "r")

content = Official_Report.read()

print("\n----contents of document----")

print(content)

Official_Report.close()

print("___________________________________")
print("That concludes the python bake off contest.")
