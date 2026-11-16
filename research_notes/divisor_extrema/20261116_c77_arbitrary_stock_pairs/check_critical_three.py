"""Exact excluded-box volumes for the critical three-stock limit."""
from fractions import Fraction as F
from itertools import combinations, product
import json


def psi3(J):
    rows = [tuple(map(F, row)) for row in J]
    if len(rows) != 3 or any(len(row) != 2 for row in rows):
        raise ValueError("a three-by-two matrix is required")
    for (a,b),(c,d) in combinations(rows,2):
        det=a*d-b*c
        if det:
            left=int((abs(d)+abs(b))/abs(det))
            right=int((abs(c)+abs(a))/abs(det))
            break
    else:
        raise ValueError("full column rank required")
    boxes=[]
    for k,l in product(range(-left,left+1),range(-right,right+1)):
        if not (k or l):
            continue
        shift=[a*k+b*l for a,b in rows]
        if max(map(abs,shift)) >= 1:
            continue
        boxes.append(tuple((max(F(0),-r),min(F(1),1-r)) for r in shift))
    def union(active, dimension):
        if not active:
            return F(0)
        if dimension == 3:
            return F(1)
        divisions=sorted({v for box in active for v in box[dimension]})
        return sum(((hi-lo)*union([box for box in active
                                    if box[dimension][0]<=lo and hi<=box[dimension][1]],
                                  dimension+1)
                    for lo,hi in zip(divisions,divisions[1:])),F(0))
    return 1-union(boxes,0)


def check():
    matrices=[
        ([(F(3,4),0),(0,F(4,5)),(0,0)],F(3,10)),
        ([(1,0),(0,1),(1,1)],F(1)),
        ([(F(1,2),0),(0,F(1,2)),(F(1,2),F(1,2))],F(1,4)),
        ([(F(3,4),0),(0,F(4,5)),(F(1,2),F(1,3))],F(11,20))]
    results=[]
    for rows,known in matrices:
        ans=psi3(rows)
        assert known is None or ans==known
        assert ans==psi3(rows[::-1])==psi3([(a,a+b) for a,b in rows])
        assert ans==psi3([(-a,-b) for a,b in rows])
        results.append(dict(J=[[str(a),str(b)] for a,b in rows],phase=str(ans)))
    return results


if __name__=='__main__':
    print(json.dumps(check(),indent=2))
