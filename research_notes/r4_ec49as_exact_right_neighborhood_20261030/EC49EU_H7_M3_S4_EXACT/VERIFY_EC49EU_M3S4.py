#!/usr/bin/env python3
"""Exact finite 7-operation H7/M3/S4 optimization with original signed-native X6 paths.

Research numerical crosscheck: SciPy/HiGHS MILP. Full three-assignment coverage from
analytic interval reduction; exact lower bounds only where solver provides gap=0
(or separately certified exact integer DP). Nothing here is formal admission.
"""
import json,time,sys,math
from itertools import product
from collections import defaultdict
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
from scipy.optimize import milp,Bounds,LinearConstraint
from MODEL_EC49EU import words,T4_fibers,signature,T4,P0,BASE,path,PAID_BASE,rank_mod,poscount

P3=(4,2,1,0,0,0)
P5s=[(5,4,1,0,0,0),(6,3,1,0,0,0),(6,4,1,0,0,0)]


def assignments():
    # complete T4 case enumeration (all h>=3 must use 4 native seam matrices)
    dom={h:set(T4_fibers(h)) for h in range(3,8)}
    out=[]
    for p3 in sorted(dom[3]):
        for p4 in sorted(dom[4]):
            for p5 in sorted(dom[5]):
                for p6 in sorted(dom[6]):
                    for p7 in sorted(dom[7]):
                        ps=(p3,p4,p5,p6,p7)
                        if len(set(ps)|{P0})==3:out.append(ps)
    return out


def case_word_map(ps):
    sigs=sorted(T4)
    result={}
    for h,p in zip(range(3,8),ps):
        eligible={w:signature(w) for w in words(h,p) if signature(w) in T4}
        assert set(eligible.values())==T4,(h,p)
        result[h]=eligible
    return result


def make_milp(eligible):
    nodes={():0};prefixes=[()];parent=[-1];children=[];colors=defaultdict(set)
    def add(w):
        pre=()
        for s in path(w):
            pre=pre+(s,)
            if pre not in nodes:
                nodes[pre]=len(prefixes);prefixes.append(pre)
                parent.append(nodes[pre[:-1]])
        return nodes[pre]
    for w in BASE:add(w)
    base_nodes={nodes[pr] for pr in PAID_BASE}
    assert len(base_nodes)==28
    colors_index={(h,s):4*(h-3)+i for h in eligible for i,s in enumerate(sorted(T4))}
    for h,ww in eligible.items():
        for w,s in ww.items():
            colors[colors_index[h,s]].add(add(w))
    assert set(colors)==set(range(4*len(eligible)))
    n=len(prefixes); edges=n-1
    rows=[];cols=[];vals=[]
    for i in range(1,n):
        rows.extend((i-1,i-1)); cols.extend((i,parent[i]));vals.extend((1.,-1.))
    for k in range(4*len(eligible)):
        for v in colors[k]:
            rows.append(edges+k);cols.append(v);vals.append(1.)
    A=coo_matrix((vals,(rows,cols)),shape=(edges+4*len(eligible),n)).tocsr()
    lo=np.r_[np.full(edges,-np.inf),np.ones(4*len(eligible))]
    hi=np.r_[np.zeros(edges),np.full(4*len(eligible),np.inf)]
    cost=np.ones(n);cost[0]=0
    for v in base_nodes:cost[v]=0
    lb=np.zeros(n);ub=np.ones(n)
    lb[list(base_nodes)]=1
    return {'prefixes':prefixes,'parent':parent,'base':base_nodes,'matrix':A,'lo':lo,'hi':hi,'cost':cost,'lb':lb,'ub':ub,'colors':colors,'word_map':eligible}


def optimize(ps,seconds=130):
    t=time.perf_counter();fw=case_word_map(ps);m=make_milp(fw)
    n=len(m['prefixes']);cnt={h:len(d) for h,d in fw.items()}
    print('START',ps[2][:3], 'nodes',n,'terminal_candidates',cnt,flush=True)
    result=milp(m['cost'],integrality=np.ones(n),bounds=Bounds(m['lb'],m['ub']),constraints=LinearConstraint(m['matrix'],m['lo'],m['hi']),options={'time_limit':seconds,'mip_rel_gap':0.,'disp':False})
    out={'p3_to_p7':[list(x) for x in ps],'nodes':n,'eligible_counts':cnt,'solver_status':int(result.status),'solver_message':result.message,'seconds':round(time.perf_counter()-t,3)}
    if result.x is not None:
        chosen={i for i,x in enumerate(result.x) if x>0.5}
        covered={}
        for h,ww in fw.items():
            covered[str(h)]=sorted(w for w in ww if m['prefixes'].index(path(w)) in chosen)
        all_words=[*BASE]+[w for ws in covered.values() for w in ws]
        used={path(w)[:k] for w in all_words for k in range(1,len(path(w))+1)}
        sig={signature(w) for w in all_words}
        p={poscount(w) for w in all_words}
        rr={h:rank_mod(set(signature(w) for w in selected)) for h,selected in covered.items()}
        assert len(p)==3 and len(sig)==4 and len(used)==len(chosen)-1
        assert all(rank==9 for rank in rr.values())
        out.update({'E':len(used),'M':len(p),'S':len(sig),'attaining_words':covered,'ranks':rr,'objective_extra':float(result.fun),'dual_bound_extra':float(result.mip_dual_bound),'mip_gap':float(result.mip_gap),'mip_nodes':int(result.mip_node_count)})
    return out

if __name__=='__main__':
  ps=assignments()
  print('FULL_M3_S4_ASSIGNMENTS',len(ps),[[list(p[:3]) for p in q] for q in ps],flush=True)
  assert len(ps)==3
  results=[]
  for p in ps:
      x=optimize(p,float(sys.argv[1]) if len(sys.argv)>1 else 90.)
      print('RESULT',x['p3_to_p7'][2][:3],x.get('E'),x.get('dual_bound_extra'),x['solver_status'],x['seconds'],flush=True)
      results.append(x)
      Path('EC49EU_M3S4_PARTIAL.json').write_text(json.dumps({'cases':results},indent=2)+'\n')
  Path('EC49EU_M3S4_EXECUTED.json').write_text(json.dumps({'cases':results},indent=2)+'\n')
