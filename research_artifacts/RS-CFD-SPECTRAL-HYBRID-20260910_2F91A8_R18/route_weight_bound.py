#!/usr/bin/env python3
"""Exact route-count / dense-call heterogeneity envelope for CFD hybrid R18."""
from __future__ import annotations
from fractions import Fraction
import json
ROUTES={"91001":{"n":20,"k_sparse":2},"91003":{"n":20,"k_sparse":2},"91007":{"n":20,"k_sparse":1}}
ALPHA=Fraction(7,10)
TARGET_SPEEDUPS=[Fraction(21,20),Fraction(11,10),Fraction(6,5)]
RHO_EXAMPLES=[Fraction(1),Fraction(2),Fraction(3),Fraction(5)]
def sparse_weight_bounds(n:int,k:int,rho:Fraction)->tuple[Fraction,Fraction]:
    if not (0<k<n): raise ValueError("require 0 < k < n")
    if rho<1: raise ValueError("rho must be >= 1")
    return Fraction(k,1)/(Fraction(k,1)+Fraction(n-k,1)*rho), Fraction(k,1)*rho/(Fraction(k,1)*rho+Fraction(n-k,1))
def ideal_total_ceiling(alpha:Fraction,w:Fraction)->Fraction:
    return Fraction(1,1)/(Fraction(1,1)-alpha*w)
def required_weight(alpha:Fraction,target_speedup:Fraction)->Fraction:
    if target_speedup<=1: return Fraction(0)
    return (Fraction(1)-Fraction(1,1)/target_speedup)/alpha
def minimum_rho_for_target(n:int,k:int,alpha:Fraction,target_speedup:Fraction)->Fraction|None:
    w=required_weight(alpha,target_speedup)
    if w>=1: return None
    if w<=0: return Fraction(1)
    return w*Fraction(n-k,1)/(Fraction(k,1)*(Fraction(1,1)-w))
def frac_obj(x:Fraction)->dict[str,object]:
    return {"exact":f"{x.numerator}/{x.denominator}","float":float(x)}
def main()->None:
    result={"schema":"CFD_ROUTE_WEIGHT_HETEROGENEITY_BOUND_V1","alpha_example":frac_obj(ALPHA),"routes":{},"claims":{"unbounded_rho":"route count alone gives no nontrivial upper bound on weighted sparse share w_sparse when dense per-call cost heterogeneity is unbounded","finite_rho_upper":"w_sparse <= k*rho/(k*rho+n-k)","finite_rho_lower":"w_sparse >= k/(k+(n-k)*rho)","full_trajectory_ceiling":"S_total <= 1/(1-alpha*w_sparse)"}}
    for seed,route in ROUTES.items():
        n,k=route["n"],route["k_sparse"]
        entry={"n":n,"k_sparse":k,"count_fraction":frac_obj(Fraction(k,n)),"rho_examples":{},"minimum_rho_for_target_speedup_at_alpha_0p7":{}}
        for rho in RHO_EXAMPLES:
            lo,hi=sparse_weight_bounds(n,k,rho); assert lo<=Fraction(k,n)<=hi
            entry["rho_examples"][str(rho)]={"w_lower":frac_obj(lo),"w_upper":frac_obj(hi),"ideal_total_ceiling_lower_weight":frac_obj(ideal_total_ceiling(ALPHA,lo)),"ideal_total_ceiling_upper_weight":frac_obj(ideal_total_ceiling(ALPHA,hi))}
        for target in TARGET_SPEEDUPS:
            rho_req=minimum_rho_for_target(n,k,ALPHA,target)
            entry["minimum_rho_for_target_speedup_at_alpha_0p7"][f"{float(target):.2f}x"]=None if rho_req is None else frac_obj(rho_req)
        result["routes"][seed]=entry
    assert [(ROUTES[s]["k_sparse"],ROUTES[s]["n"]-ROUTES[s]["k_sparse"]) for s in ROUTES]==[(2,18),(2,18),(1,19)]
    assert sparse_weight_bounds(20,2,Fraction(2))==(Fraction(1,19),Fraction(2,11))
    assert sparse_weight_bounds(20,1,Fraction(2))==(Fraction(1,39),Fraction(2,21))
    assert minimum_rho_for_target(20,2,ALPHA,Fraction(11,10))==Fraction(90,67)
    assert minimum_rho_for_target(20,1,ALPHA,Fraction(11,10))==Fraction(190,67)
    for route in ROUTES.values():
        bounds=[sparse_weight_bounds(route["n"],route["k_sparse"],r) for r in RHO_EXAMPLES]
        assert all(bounds[i][0]>=bounds[i+1][0] for i in range(len(bounds)-1))
        assert all(bounds[i][1]<=bounds[i+1][1] for i in range(len(bounds)-1))
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=="__main__": main()
