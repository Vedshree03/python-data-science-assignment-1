# List of dictionaries with id
data = [{"id": 1}, {"id": 2}, {"id": 1}]

seen_ids = set()
result = []

# Remove duplicates based on id
for d in data:
    if d["id"] not in seen_ids:
        seen_ids.add(d["id"])
        result.append(d)

print(result)