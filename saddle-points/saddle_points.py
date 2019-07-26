def saddle_points(matrix):
    if len({len(i) for i in matrix})!=1 and matrix:
        raise ValueError(".+")
    saddle=[]
    columnwise=list(zip(*matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] >= max(matrix[i]) and matrix[i][j]<=min(columnwise[j]):
                saddle.append({"row": i + 1, "column": j + 1})
    return ( [{}]  if not matrix or not saddle else saddle)