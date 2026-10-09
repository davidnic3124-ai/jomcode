workshop = [
    {"id":"A1", "capacity": 2},
    {"id":"A2", "capacity": 5},
    {"id":"A3", "capacity": 2},
    {"id":"A4", "capacity": 3},
]
open_ids = [row["id"] for row in workshop if row["capacity"] > 5]
print(open_ids)
