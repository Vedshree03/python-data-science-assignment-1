# List of coordinate points
points = [(1,2), (-1,3), (-2,-2), (3,-1)]

quadrants = {1:0, 2:0, 3:0, 4:0}

# Check quadrant of each point
for x, y in points:
    if x > 0 and y > 0:
        quadrants[1] += 1
    elif x < 0 and y > 0:
        quadrants[2] += 1
    elif x < 0 and y < 0:
        quadrants[3] += 1
    elif x > 0 and y < 0:
        quadrants[4] += 1

print(quadrants)