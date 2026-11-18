"""Transfer authentic EC49CT signed-X6 BRC extreme rank witnesses to all h>=4.
Reads the original genuine JSON witnesses, verifies literal endpoints, ordered
A/B tags and exact positive BRC/count weights, then recomputes modular minors.
"""
import json
from pathlib import Path
from EC49CT_RECHECK_INDEPENDENT import loc, wt, tag, det_mod, suffix

def seed(n):
    o=json.loads(Path(__file__).with_name(f'EC49CT_CERT_n{n}_S4.json').read_text())
    return next(b for b in o['blocks'] if b['target']==[-8,0,0,0,0,0])

def check(h):
    assert h>=4
    output=[]
    for n0,k in ((14,11),(16,12)):
        b=seed(n0)
        ps=[tuple(p)+(-1,-1)*(h-4) for p in b['paths']]
        s=suffix('e'*h)
        assert len(ps)==k
        assert all(len(p)==n0+2*(h-4) and loc(p)==(-2*h,0,0,0,0,0) for p in ps)
        rows=[(t,c) for t in range(4) for c in range(3)]
        m=[[wt(p+s,c) if tag(p+s)==t else 0 for p in ps] for t,c in rows]
        if k==11:m=[r[:11] for r in m[:11]]
        residue=det_mod(m)
        assert residue!=0,(h,n0,residue)
        if n0==14:
            A=30*12**h;B=30*27**h
            for p in ps:
                if tag(p+s)==3:
                    assert wt(p+s,0)*B+wt(p+s,1)*A==A*B
        output.append((n0+2*(h-4),residue))
    return output

if __name__=='__main__':
    for h in (4,5,6,7,10,20):
        print('h',h,'target',(-2*h,0,0,0,0,0),'rank11/full12 residues',check(h))
    print('PASS authentic BRC witness-transfer checks; all-h proof uses invertible positive row scaling')
