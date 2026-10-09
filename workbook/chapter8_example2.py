participant_ids=["A1","A3","A2","A4","A5"]
unique_ids = set(participant_ids)
print(sorted(unique_ids))
print("A3" in unique_ids)
print(unique_ids & {"A1","A6"})

