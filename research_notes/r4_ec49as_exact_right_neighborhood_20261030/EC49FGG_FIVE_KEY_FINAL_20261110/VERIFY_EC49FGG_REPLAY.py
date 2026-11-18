#!/usr/bin/env python3
"""EC49FGG: reproduce fixed-branch exact integer LP-dual proof (36 leaves).
Frozen model pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Floats propose duals; final lower bounds are recomputed using integers.
"""
from pathlib import Path
import sys, json
import numpy as np
from scipy.optimize import linprog
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'EC49FGF_EXACT_16_CLASS_DUAL_20261110'))
from VERIFY_EC49FGF import build,BASE,EARLY,LATE
SCALE=131072
PATHS=(
    "116:1 143:1 4966:1",
    "116:1 143:1 4966:0 4961:1",
    "116:1 143:1 4966:0 4961:0 47:1",
    "116:1 143:1 4966:0 4961:0 47:0 118:0",
    "116:1 143:1 4966:0 4961:0 47:0 118:1",
    "116:1 143:0 413:1 107:1 753:1",
    "116:1 143:0 413:1 107:1 753:0",
    "116:1 143:0 413:1 107:0 4961:1",
    "116:1 143:0 413:1 107:0 4961:0 4966:1",
    "116:1 143:0 413:1 107:0 4961:0 4966:0 6027:1",
    "116:1 143:0 413:1 107:0 4961:0 4966:0 6027:0 6022:1",
    "116:1 143:0 413:1 107:0 4961:0 4966:0 6027:0 6022:0",
    "116:1 143:0 413:0 4966:1 47:1",
    "116:1 143:0 413:0 4966:1 47:0",
    "116:1 143:0 413:0 4966:0 47:1 406:1",
    "116:1 143:0 413:0 4966:0 47:1 406:0",
    "116:1 143:0 413:0 4966:0 47:0 4961:1",
    "116:1 143:0 413:0 4966:0 47:0 4961:0 107:0 6022:1",
    "116:1 143:0 413:0 4966:0 47:0 4961:0 107:0 6022:0 6027:1",
    "116:1 143:0 413:0 4966:0 47:0 4961:0 107:0 6022:0 6027:0",
    "116:1 143:0 413:0 4966:0 47:0 4961:0 107:1",
    "116:0 107:1 753:1",
    "116:0 107:1 753:0",
    "116:0 107:0 4982:1",
    "116:0 107:0 4982:0 413:1 143:1 4987:1",
    "116:0 107:0 4982:0 413:1 143:1 4987:0",
    "116:0 107:0 4982:0 413:1 143:0 4987:1",
    "116:0 107:0 4982:0 413:1 143:0 4987:0",
    "116:0 107:0 4982:0 413:0 143:1 4987:1",
    "116:0 107:0 4982:0 413:0 143:1 4987:0 6006:1",
    "116:0 107:0 4982:0 413:0 143:1 4987:0 6006:0 6001:1",
    "116:0 107:0 4982:0 413:0 143:1 4987:0 6006:0 6001:0",
    "116:0 107:0 4982:0 413:0 143:0 4987:1",
    "116:0 107:0 4982:0 413:0 143:0 4987:0 6022:1",
    "116:0 107:0 4982:0 413:0 143:0 4987:0 6022:0 6027:1",
    "116:0 107:0 4982:0 413:0 143:0 4987:0 6022:0 6027:0",
)
def leaves_cover_full_boolean_tree(paths):
    root={}
    for path in paths:
        branch=root
        for idx,bit in path:
            assert '_leaf' not in branch
            if '_var' in branch:assert branch['_var']==idx
            else:branch['_var']=idx
            branch=branch.setdefault(bit,{})
        assert not branch
        branch['_leaf']=True
    def rec(node):
        if '_leaf' in node:
            assert len(node)==1
            return 1,0
        assert set(node)=={'_var',0,1}
        a,da=rec(node[0]);b,db=rec(node[1])
        return a+b,max(da,db)+1
    return rec(root)

def main():
    paths=[[(int(e.split(':')[0]),int(e.split(':')[1])) for e in s.split()] for s in PATHS]
    count,depth=leaves_cover_full_boolean_tree(paths)
    assert count==36 and depth==9
    keys=set(BASE)|{EARLY[1],LATE[1]}
    c,G,h,n,d=build(keys)
    assert n==10901 and d==1904 and len(c)==12805 and G.shape==(14728,12805)
    report=[];min_bound=None
    for index,path in enumerate(paths):
        fix=dict(path);assert len(fix)==len(path)
        lb=np.zeros(len(c));ub=np.ones(len(c))
        for j,b in fix.items():
            assert 0<=j<len(c) and b in (0,1)
            lb[j]=b;ub[j]=b
        fit=linprog(c.astype(float),A_ub=G,b_ub=h,bounds=list(zip(lb,ub)),method='highs')
        assert fit.success,(index,fit.status,fit.message)
        z=np.minimum(np.rint(np.asarray(fit.ineqlin.marginals)*SCALE).astype(np.int64),0)
        r=SCALE*c-G.transpose()@z
        assert np.all(z<=0)
        # For every feasible binary x with Gx<=h and z<=0:
        # SCALE*c*x >= z*h + sum_j min(r_j*lb_j,r_j*ub_j).
        low=int(z@h)+sum(int(v)*int(lb[j] if v>=0 else ub[j]) for j,v in enumerate(r))
        assert low>111*SCALE,(index,low)
        min_bound=low if min_bound is None else min(min_bound,low)
        report.append({'index':index,'branch':PATHS[index],
                       'integer_dual_bound_numerator':low,
                       'nz_integer_dual':int(np.count_nonzero(z))})
    print(json.dumps({'schema':'EC49FGG_BRANCH_DUAL_REPLAY_V1',
      'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
      'key_profile':sorted(keys),'branch_leaves':count,'depth':depth,
      'exact_min_dual_numerator':int(min_bound),'scale':SCALE,
      'conclusion':'C_native >= 112 for this sole competitive five-key class',
      'leaves':report},indent=2))
if __name__=='__main__':main()
