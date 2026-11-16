import json
from crosscheck import brute
from quotient_exact import TRIP
labels = {"012":True,"01|2":(0,1),"02|1":(0,2),"12|0":(1,2),"0|1|2":False}
rows = [json.loads(l) for l in open("table.jsonl")]
assert len(rows) == 25
for row in rows:
    N = row["threshold"]
    for r in (N-1,N,N+1):
        assert brute(r,TRIP,labels[row["col"]],labels[row["row"]]) == (r==N-1), row
print("PASS: 75 direct all-errors independent comparisons at all 25 thresholds")
