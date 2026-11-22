#!/usr/bin/env python3
"""Exact R125 D-line six-pair BRC replay: no floating point."""
from fractions import Fraction
import json

D_VALUES = ["3","29","30","31","32","101/3","34","47","48","70","71","72","100"]
PORTS = (11,17,18)
U=(10,-5,1); V=(4,-1,0); B=(6,-4,1); E=(16,-9,2)

def port(a):
    return max(sum(max(t,0) for t in a),sum(max(-t,0) for t in a))

def directions(p):
    for x in range(-p,p+1):
        for y in range(-p,p+1):
            for z in range(-p,p+1):
                if not (x or y or z) or next(t for t in (x,y,z) if t)!=abs(next(t for t in (x,y,z) if t)):
                    continue
                a=(x,y,z)
                if port(a)<=p: yield a

def score(a,d):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    w=(Fraction(1),Fraction(3),Fraction(4),d)
    return max(Fraction(abs(h[i]-h[j]),1)/(w[i]+w[j]) for i in range(4) for j in range(i+1,4))

def expected(d,p):
    if d<=29: return {U}
    if d<=31: return {U,V}
    if d<=Fraction(101,3): return {U,V,B}
    if d<71: return {U,V,B}|({E} if p>=18 else set())
    return {B}

def optimum(d):
    return min(Fraction(1,4),Fraction(12,1)/(d+1))

def replay():
    rows=[]; total=0
    for dtext in D_VALUES:
        d=Fraction(dtext); cases={}
        for p in PORTS:
            items=list(directions(p))
            vals=[score(a,d) for a in items]
            eta=min(vals)
            near={a for a,v in zip(items,vals) if 2*v<3*eta}
            assert eta==optimum(d),(d,p,eta)
            assert near==expected(d,p),(d,p,near,expected(d,p))
            assert len(items)=={11:2541,17:8942,18:10563}[p],(d,p,len(items))
            cases[str(p)]={"checked_unoriented":len(items),
                            "eta":str(eta),
                            "near":[list(a) for a in sorted(near)],
                            "near_count":len(near)}
            total+=len(items)
        rows.append({"D":dtext,"port_results":cases})
    return {"scope":"R125 finite replay; analytic theorem covers all real D>=3 and integer p>=11",
            "checks":len(D_VALUES)*len(PORTS),"vector_parameter_cases":total,
            "arithmetic":"Python fractions.Fraction exact",
            "status":"PASS","rows":rows}

if __name__=="__main__": print(json.dumps(replay(),ensure_ascii=False,indent=2))
