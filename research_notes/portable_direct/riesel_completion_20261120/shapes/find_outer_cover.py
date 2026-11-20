"""Find a square-compatible odd cover outside the v4 phase family.

SciPy/HiGHS is only a candidate finder. Every returned solution is checked
using exact integer coverage; an infeasibility status is not a proof here.
"""
from pathlib import Path
import json
import sys
import time
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix

ROOT = next(p for p in Path(__file__).resolve().parents
            if (p/'research_notes/portable_direct/riesel_families_20261119').is_dir())
sys.path.insert(0, str(ROOT/'research_notes/portable_direct/riesel_families_20261119/phase'))
from prepare_family import PRIMES, PERIODS, PHASES, membership, root_for_phase, M


def main():
    start = time.monotonic()
    offsets = np.cumsum([0]+PERIODS).tolist()
    count = offsets[-1]
    row, col, value = [], [], []
    lo, hi = [], []
    for i,e in enumerate(PERIODS):
        for c in range(e):
            row.append(i);col.append(offsets[i]+c);value.append(1.)
        lo.append(1.);hi.append(1.)
    for u in range(3360):
        for i,e in enumerate(PERIODS):
            row.append(20+u);col.append(offsets[i]+u%e);value.append(1.)
        lo.append(1.);hi.append(np.inf)
    # Normalization of the mutually coprime periods 3 and 16.
    lower=np.zeros(count);upper=np.ones(count)
    for p in [7,65537]:
        i=PRIMES.index(p);upper[offsets[i]:offsets[i+1]]=0
        lower[offsets[i]]=1;upper[offsets[i]]=1
    # All v4 family members in this normalization have these three phases.
    target={17:2,241:1,257:4}
    r=len(lo)
    for p,c in target.items():
        row.append(r);col.append(offsets[PRIMES.index(p)]+c);value.append(1.)
    lo.append(-np.inf);hi.append(2.)
    matrix=coo_matrix((value,(row,col)),shape=(len(lo),count)).tocsc()
    ans=milp(np.zeros(count),integrality=np.ones(count),bounds=Bounds(lower,upper),
             constraints=LinearConstraint(matrix,np.array(lo),np.array(hi)),
             options={'disp':True})
    report={'status':int(ans.status),'message':str(ans.message),'seconds':time.monotonic()-start,
            'candidate_finder_only':True,'variables':count,'constraints':len(lo)}
    if ans.x is not None:
        vector=[]
        for i,e in enumerate(PERIODS):
            selected=[c for c in range(e) if ans.x[offsets[i]+c]>.5]
            assert len(selected)==1
            vector.append(selected[0])
        assert all(any(u%e==c for c,e in zip(vector,PERIODS)) for u in range(3360))
        assert vector[PRIMES.index(7)]==vector[PRIMES.index(65537)]==0
        shifts=[t for t in range(3360) if membership([(c-t)%e for c,e in zip(vector,PERIODS)])]
        assert not shifts
        residues=[root_for_phase(p,c) for p,c in zip(PRIMES,vector)]
        a=sum((M//p)*pow(M//p,-1,p)*r for p,r in zip(PRIMES,residues))%M
        if a%2==0:a+=M
        assert all(a%p==r for p,r in zip(PRIMES,residues))
        report.update(phases=vector,prime_channels=PRIMES,periods=PERIODS,
                      outside_v4_family_all_translations=True,a=str(a),k=str(a*a),
                      all_odd_phases_covered=True,root_residues=residues)
    out=Path(__file__).with_name('outer_cover_result.json')
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))


if __name__=='__main__':main()
