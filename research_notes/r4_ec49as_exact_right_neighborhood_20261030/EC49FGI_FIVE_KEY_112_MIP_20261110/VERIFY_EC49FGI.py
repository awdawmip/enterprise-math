#!/usr/bin/env python3
"""Five-key 24-label BRC integer optimum; MIP-backed, no formal UNSAT certificate."""
from pathlib import Path
import sys
sibling=Path(__file__).resolve().parent.parent/"EC49FGF_EXACT_16_CLASS_DUAL_20261110"
if (sibling/"VERIFY_EC49FGF.py").exists(): sys.path.insert(0,str(sibling))
from VERIFY_EC49FGF import BASE,model
import numpy as np,json,time
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import vstack,csr_matrix
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
 (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
 (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
K=set(BASE)|{(4,2,1),(6,4,1)}
W={
 2:{16:'fe',32:'ge'},3:{16:'feg',32:'gef'},
 4:{1:'gefd',2:'fegd',4:'fegc',8:'gefc'},
 5:{16:'feggf',32:'geffg'},
 6:{1:'gefddd',2:'fegddd',4:'fegccc',8:'gefccc'},
 7:{1:'gefddgf',2:'fegddgf',4:'fegccfg',8:'gefccfg'},
 8:{1:'geffgfgd',2:'feggfgfd',4:'feggfgfc',8:'geffgfgc'},
 9:{16:'feggfgffg',32:'geffgfggf'}}

def witness():
    keys=set();seen=set();ndemands=0
    for h,labels in W.items():
        for sig,w in labels.items():
            assert len(w)==h and sig in REQ[h]
            q=0;prefix=();pos=[0]*6
            for ch in w:
                q=T[q]['acdefg'.index(ch)]
                assert q!=8
                for n in STEPS[ch]:
                    prefix=prefix+(n,);seen.add(prefix)
                    pos[abs(n)-1]+=1 if n>0 else -1
            assert SIG[q]==sig and pos==[2,0,0,0,0,0]
            flat=[n for ch in w for n in STEPS[ch]]
            keys.add(tuple(sum(n==axis for n in flat) for axis in (1,2,3)))
            ndemands+=1
    assert ndemands==24 and keys==K and len(seen)==112
    return {'demands':ndemands,'keys':sorted(keys),'native_prefixes':len(seen),'family':W}

def run():
    c,G,h,stats=model(K)
    print('model',stats,flush=True)
    bounds=Bounds(0,1);integrality=np.ones(len(c),dtype=int)
    opt=milp(c=c.astype(float),integrality=integrality,bounds=bounds,
        constraints=LinearConstraint(G,np.full(len(h),-np.inf),h),
        options={'time_limit':80,'mip_rel_gap':0.,'presolve':True,'disp':False})
    assert opt.success and opt.fun==112 and opt.mip_dual_bound==112 and opt.mip_gap==0
    A=vstack([G,csr_matrix(c.reshape(1,-1))],format='csr');rhs=np.r_[h,111]
    status=[]
    for presolve in (True,False):
        decision=milp(c=np.zeros(len(c)),integrality=integrality,bounds=bounds,
          constraints=LinearConstraint(A,np.full(len(rhs),-np.inf),rhs),
          options={'time_limit':80,'mip_rel_gap':0.,'presolve':presolve,'disp':False})
        assert decision.status==2,decision.message
        status.append({'presolve':presolve,'status':int(decision.status),'message':decision.message})
    val=witness()
    out={'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
        'class':sorted(K),'model':stats,'optimum':opt.fun,'dual_bound':opt.mip_dual_bound,
        'mip_gap':opt.mip_gap,'mip_nodes':opt.mip_node_count,'cap_111':status,'witness':val,
        'limitation':'No independently checkable rational/Boolean UNSAT proof exported by HiGHS.'}
    Path('EXACT_SOLVER_AUDIT_112.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('MIN_OPTIMUM',opt.fun,'DUAL_BOUND',opt.mip_dual_bound,'GAP',opt.mip_gap,flush=True)
    print('CAP_111_INFEASIBLE',status,flush=True)
    print('INDEPENDENT_WITNESS_PASS',val['native_prefixes'],flush=True)

if __name__=='__main__':run()
