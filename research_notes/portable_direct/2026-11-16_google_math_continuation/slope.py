"""Exact breakpoints for classifying six ideal signatures with common linear drift."""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

P=tuple(Fraction(x,36) for x in (455,-295,-25,185,-25,-295))
J=(0,1,5)
S=[tuple(P[(a+j)%6] for j in J) for a in range(6)]
def rays(sign):
    output={}
    for a,b in product(range(6),repeat=2):
        if a==b:
            continue
        deltas=[x-y for x,y in zip(S[a],S[b])]
        critical=Fraction()
        for i,j in product(range(3),repeat=2):
            diff=deltas[i]-deltas[j]
            divisor=5-sign*(J[i]-J[j])
            if divisor==0 and diff>0:
                critical=None
                break
            if divisor:
                critical=max(critical,diff/divisor)
        output[a,b]=critical
    return output
records={}
for sign in (1,-1):
    table=rays(sign)
    critical=min(v for v in table.values() if v is not None)
    assert critical==Fraction(40,27)
    ordered=sorted((t,a,b) for (a,b),t in table.items() if t is not None)
    assert ordered[:2]==([(critical,3,4),(Fraction(5,2),0,3)] if sign==1
                         else [(critical,4,3),(Fraction(5,2),1,4)])
    records[str(sign)]=[[None if table.get((a,b)) is None else str(table[a,b]) for b in range(6)] for a in range(6)]
print(json.dumps(records,indent=2))
