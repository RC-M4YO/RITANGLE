fixed = [(0,3),(2,1),(4,0)]

def check(points):
  distances = []
  print(points)
  for i in range(6):
    for j in range(i,6):
      point1 = points[i]
      point2 = points[j]
      if point1 == point2:
        continue
      distance = (point1[0]-point2[0])**2+(point1[1]-point2[1])**2
      print(point1,point2, distance) 
      if distance in distances:
        print(f"current distances is {distances} and {distance} was already in it\n")
        return False
      distances.append(distance)
  print(f"the points are {points}")
  print("DONE")
  exit()

for x1 in range(6):
  for y1 in range(6):
    if (x1,y1) in fixed:
      continue
    for x2 in range(6):
      for y2 in range(6):
        if (x2,y2) == (x1,y1) or (x2,y2) in fixed:
          continue
        for x3 in range(6):
          for y3 in range(6):
            points = [fixed[0],fixed[1],fixed[2],(x1,y1),(x2,y2),(x3,y3)]
            if (x3,y3) in fixed or (x2,y2) == (x3,y3) or (x1,y1) == (x3,y3):
              continue
            check(points)
