from quotient_exact import TRIP, failure
import json
labels = ("012","01|2","02|1","12|0","0|1|2")
parts = (True,(0,1),(0,2),(1,2),False)
# Independent / independent already proven globally correct for r >= 447.
# Every coupled partition permits only a subset of those error assignments.
for i,dc in enumerate(parts):
    for j,ec in enumerate(parts):
        for r in range(446,0,-1):
            w = failure(r,TRIP,ec,dc)
            if w:
                print(json.dumps(dict(row=labels[i],col=labels[j],threshold=r+1,witness=w)),flush=True)
                break
