"""Enumerate the unique affine-drift-immune contrasts on the twenty triples.
Requires only scalar_contrast_survey.py next to this file, and the stdlib.
"""
from fractions import Fraction
from itertools import product,combinations
from math import gcd
from pathlib import Path
import json
import scalar_contrast_survey as s

def tail_half():
    # Uniform bound <1/2 on |Y-P/36|. The 300 polynomial inequalities and
    # the binomial-coefficient argument are as in scalar_contrast_survey.py.
    for q0 in range(s.BASE,s.BASE+6):
        for e,d,sign in product(s.choices,s.choices,(-1,1)):
            def val(t):
                q=q0+6*t
                D=s.C[q]+d
                return 54*D+sign*(108*q**3*(s.T[q]+e)-(s.bpoly(q)+3*s.P[q%6])*D)
            coeff=s.diffs([val(t) for t in range(10)])
            assert coeff[0]>0 and all(z>=0 for z in coeff)
    assert s.C[s.BASE]>s.BUDGET

def main():
    s.BASE=8000
    s.C,s.T=s.counts(s.BASE+72)
    tail_half()
    s.tail_certificate=lambda:None # replaced by uniform, stronger proof above
    rows=[]
    for J in combinations(range(6),3):
        i,j,k=J
        w=(k-j,i-k,j-i);d=gcd(*w)
        s.A=tuple(x//d for x in w);s.J=J
        s.S=tuple(sum(v*s.P[(a+h)%6] for h,v in zip(s.J,s.A)) for a in range(6))
        s.order=sorted(s.S)
        gap=min(y-x for x,y in zip(s.order,s.order[1:]))
        row=dict(J=J,weights=s.A,S=s.S,box_radius=str(Fraction(gap,72*sum(map(abs,s.A)))))
        if gap:
            assert gap>=36*sum(map(abs,s.A))
            d=s.compute()
            row.update(thresholds=d['thresholds_denominator_rows_numerator_columns'],witnesses=d['last_failure_witnesses'])
            print(J,row['thresholds'][0][0],row['thresholds'][4][4],flush=True)
        else:
            row['identical_phases']=next((a,b) for a,b in combinations(range(6),2) if s.S[a]==s.S[b])
        rows.append(row)
    Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':main()
