#!/usr/bin/env python3
"""Author-side executable exact positive-rational BRC semantic witness.

This checks the typed CWM/port/recurrent relations from immutable Source,
using standalone Fraction arithmetic. It is NOT a native heartbeat Phi run
and does not import the canonical enterprise_math package.
"""
from fractions import Fraction as F
from json import dumps

ZERO=F(0)
ONE=F(1)
HALF=F(1,2)

def edge(w):
    assert w>0
    return (1,w,w)

def propagate(a,b):
    return (a[0]*b[0],a[1]*b[1],a[2]*b[2])

def port_collapse(full,hidden=1):
    ports=[i for i in range(len(full)) if i!=hidden]
    a=full[hidden][hidden]
    assert 0<=a<1
    star=ONE/(ONE-a)
    effective=[[full[i][j]+full[i][hidden]*star*full[hidden][j] for j in ports] for i in ports]
    return ports,effective,star

def positive_recurrent_two_ports(W):
    a,b=W[0];c,d=W[1]
    det=(ONE-a)*(ONE-d)-b*c
    if det==0: return {"stable":False,"det":det,"star":None}
    star=[[(ONE-d)/det,b/det],[c/det,(ONE-a)/det]]
    h=[sum(row,ZERO) for row in star]
    stable=all(x>0 for x in h) and all(x>=0 for row in star for x in row)
    if stable:
        assert all(sum((W[i][j]*h[j] for j in range(2)),ZERO)==h[i]-ONE for i in range(2))
    return {"stable":stable,"det":det,"star":star if stable else None}

def encode(obj):
    if isinstance(obj,F): return str(obj.numerator) if obj.denominator==1 else f"{obj.numerator}/{obj.denominator}"
    if isinstance(obj,dict):return {k:encode(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):return [encode(v) for v in obj]
    return obj

def run():
    A=[[ZERO,HALF,ZERO],[ZERO,ZERO,HALF],[ZERO,ZERO,ZERO]]
    B=[[ZERO,HALF,ZERO],[HALF,ZERO,ZERO],[ZERO,ZERO,ZERO]]
    ia,Wa,za=port_collapse(A)
    ib,Wb,zb=port_collapse(B)
    assert ia==ib==[0,2] and za==zb==ONE
    assert Wa==[[ZERO,F(1,4)],[ZERO,ZERO]]
    assert Wb==[[F(1,4),ZERO],[ZERO,ZERO]]
    br=propagate(edge(HALF),edge(HALF))
    assert br==(1,F(1,4),F(1,4))
    assert sum(map(sum,Wa),ZERO)==sum(map(sum,Wb),ZERO)==F(1,4)
    K=[[ZERO,ZERO],[F(4),ZERO]]
    ua=[[Wa[i][j]+K[i][j] for j in range(2)] for i in range(2)]
    ub=[[Wb[i][j]+K[i][j] for j in range(2)] for i in range(2)]
    qa=positive_recurrent_two_ports(ua)
    qb=positive_recurrent_two_ports(ub)
    assert not qa["stable"] and qa["det"]==0
    assert qb["stable"] and qb["det"]==F(3,4)
    assert qb["star"]==[[F(4,3),ZERO],[F(16,3),ONE]]
    assert ua[0][1]*ua[1][0]==ONE
    cert=[ONE,F(5)]
    assert all(sum((ub[i][j]*cert[j] for j in range(2)),ZERO)<cert[i] for i in range(2))
    out={
      "schema":"PREFIX269_POSITIVE_BRC_PORT_WITNESS_V1",
      "status":"AUTHOR_SIDE_STANDALONE_SEMANTIC_CHECK_PASS",
      "actual_source_import_test":"NOT_EXECUTED",
      "native_physical_heartbeat_Phi":"NOT_DEFINED_OR_EXECUTED",
      "full_A":A, "full_B":B, "effective_A":Wa,"effective_B":Wb,
      "same_target_forget_CWM":br,
      "hidden_loop_zeta":[za,zb],
      "future_port_context":K,"context_A":ua,"context_B":ub,
      "result_A":qa,"result_B":qb,"stable_B_integer_potential":[1,5],
      "unit_positive_recurrent_cycle_A":ua[0][1]*ua[1][0],
      "minimal_labeled_port_count_for_declared_observer":2
    }
    print(dumps(encode(out),indent=2,ensure_ascii=False,sort_keys=True))

if __name__=="__main__":
    run()
