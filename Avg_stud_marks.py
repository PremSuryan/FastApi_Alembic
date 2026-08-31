data = {
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "student_name": ["Amit", "Neha", "Rahul", "Amit", "Neha", "Rahul", "Amit", "Neha"],
    "class": ["10A", "10A", "10A", "10B", "10B", "10B", "10A", "10B"],
    "subject": ["Math", "Math", "Science", "Math", "Science", "Math", "Science", "Science"],
    "marks": [78, 85, 72, 88, 91, 67, 80, 76]
}


# this method 1:


from collections import defaultdict
count=0
# dic= defaultdict(list)
dic = {}
for i in sorted(zip(data["class"],data["student_name"],data["subject"],data["marks"])):
    print(i)
    if i[0] not in dic:
        dic[i[0]] = []

    dic[i[0]].append(i[1])
    
# print(dic)

for key, values in dic.items():
    avg = sum(values) / len(values)
    maximum = max(values)

    # print(key)
    # print("Average:", avg)
    # print("Maximum:", maximum)

    print(f"For the Class {key} :  the Avg is {avg} and the max mark is {maximum}")



#Method 2:

# Average marks for each class
class_marks = {}

for i in range(len(data["student_id"])):
    class_name = data["class"][i]
    marks = data["marks"][i]

    if class_name not in class_marks:
        class_marks[class_name] = []

    class_marks[class_name].append(marks)

# print("Average marks for each class:")

for class_name in class_marks:
    total = sum(class_marks[class_name])
    count = len(class_marks[class_name])
    average = total / count

    # print(class_name, ":", average)


# Highest marks for each subject
subject_highest = {}

for i in range(len(data["student_id"])):
    subject = data["subject"][i]
    marks = data["marks"][i]

    if subject not in subject_highest:
        subject_highest[subject] = marks
    elif marks > subject_highest[subject]:
        subject_highest[subject] = marks

# print("\nHighest marks for each subject:")

for subject in subject_highest:
    # print(subject, ":", subject_highest[subject])

    pass

