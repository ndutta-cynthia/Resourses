
emergency_resources = [
    {"name": "Medical Team", "longitude": -122.1215}, 
    {"name": "Food Supplies", "longitude": -121.9552},  
]

def allocate_resources(disaster_location_longitude):
    allocated_resources = []
    for resource in emergency_resources:
        resource_longitude = resource["longitude"]
        distance = abs(resource_longitude - disaster_location_longitude)
        if distance <= 1.0:
            allocated_resources.append(resource["name"])
    return allocated_resources

disaster_longitude = -122.3321 
allocated_resources = allocate_resources(disaster_longitude)

if allocated_resources:
    print("Allocated resources:")
    for resource in allocated_resources:
        print(f"- {resource}")
else:
    print("No resources allocated for the given location.")
