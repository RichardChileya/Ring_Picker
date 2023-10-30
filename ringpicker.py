# Define the rings
rings = ['agate', 'diamond', 'diamond', 'citrine']

# Define the ring fingers
fingers = ['thumb', 'index', 'middle', 'ring', 'pinky']

# Come up  all possible combinations of wearing rings on different fingers
combinations = []
for i in range(len(fingers)):
    for j in range(len(rings)):
        if i == 3 and j != 1 and j != 2:
            continue 
        if i == 0 or (i == 3 and j == 1):
            continue  
        if j == 1 and rings.count('diamond') == 2:
            continue 
        combinations.append((fingers[i], rings[j]))

for combo in combinations:
    print(f"Wearing {combo[1]} ring on {combo[0]} finger")
