import csv 

def save_to_file(uniInfo):
    file = open("curriculum.csv", mode = "w", newline='')
    writer = csv.writer(file)
    writer.writerow(["University Name", "Course", "Link"])

    for uniGroup in uniInfo:
        for uni in uniGroup:
            writer.writerow(list(uni.values()))