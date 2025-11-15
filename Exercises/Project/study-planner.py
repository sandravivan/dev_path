#ask about subject
subjects_input = input("What subjects do you want to study?")

#split whit comma
subjects_raw = subjects_input.split(",")

#empty list
subjects = []

#for all raw list
for item in subjects_raw:

    #final list
    clean_item = item.strip()
    subjects.append(clean_item)

    print(subjects)






