#!/usr/bin/env python3
"""PREFIX-601-R2 complete symbolic native phase-basis Krylov certificate.
Frozen science f42f2906d77f24085c123f3ccfe9667d41caa96d.
Reconstruct 48 native phase tail from original STAR phase graph; prove all z>=0.
"""
import json
from pathlib import Path
import sympy as sp

z=sp.symbols("z")
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
phases=tuple((a,p,sgn*k) for a in range(4) for k in STAR[a]
             for sgn in (-1,1) for p in near(a,sgn*k))
idx={a:i for i,a in enumerate(phases)}
def suc(i):
    a,p,c=phases[i]
    b=next(k for k in range(4) if k!=a and abs(c) in STAR[k])
    return tuple(idx[v] for v in ([(a,c,q) for q in near(a,c) if q!=p]
                                 +[(b,c,q) for q in near(b,c)]))
N=tuple(suc(i) for i in range(48))
g=idx[(0,1,-3)]
assert len(idx)==48 and g==4
Q=sp.zeros(48)
for i,ns in enumerate(N):
    if abs(phases[i][2])>4:continue
    for j in ns:
        Q[i,j]=1 if i==g else (3+z if j==g else 2)
powers=[sp.eye(48)]
for k in range(1,11):powers.append(Q*powers[-1])
s=4*z+12
poly={
 "zero":powers[1],
 "base5":powers[5]-16*powers[1],
 "gate5":powers[5]-s*powers[1],
 "base6":powers[6]-16*powers[2],
 "full10":powers[10]-(16+s)*powers[6]+16*s*powers[2]
}
classes={
 "zero":{"indices":[1,3,5,7,13,15,17,19,25,27,29,31,37,39,41,43],"degree":1,"poly":"t"},
 "base5":{"indices":[0,2,6,12,16,18,24,28,30,36,38,42],"degree":5,"poly":"t*(t^4-16)"},
 "gate5":{"indices":[4,14,26,40],"degree":5,"poly":"t*(t^4-4z-12)"},
 "base6":{"indices":[9,10,21,22,33,34,45,46],"degree":6,"poly":"t^2*(t^4-16)"},
 "full10":{"indices":[8,11,20,23,32,35,44,47],"degree":10,
           "poly":"t^2*(t^4-16)*(t^4-4z-12)"}
}
record=[]
for kind,d in classes.items():
    order=d["degree"]
    for j in d["indices"]:
        assert all(sp.expand(poly[kind][i,j])==0 for i in range(48)),(kind,j)
        T=sp.Matrix.hstack(*(powers[k][:,j] for k in range(order)))
        pivot=list(T.subs(z,0).T.rref()[1])
        assert len(pivot)==order
        minor=sp.factor(T.extract(pivot,range(order)).det())
        c,factors=sp.factor_list(minor)
        assert c!=0
        assert all(sp.expand(f-(z+1*3))==0 or sp.expand(f-(z-1))==0 for f,p in factors)
        if kind=="full10":
            assert any(sp.expand(f-(z-1))==0 and p==4 for f,p in factors)
        else:
            assert all(sp.expand(f-(z-1))!=0 for f,p in factors)
        rec={"phase":j,"kind":kind,"degree_nonunit":order,
             "pivot_rows":pivot,"sharp_lower_minor":str(minor)}
        if kind=="full10":
            assert all(sp.expand(poly["base6"][i,j].subs(z,1))==0 for i in range(48))
            mat=sp.Matrix.hstack(*(powers[k][:,j] for k in range(6))).subs(z,1)
            piv1=list(mat.T.rref()[1])
            assert len(piv1)==6
            det1=mat.extract(piv1,range(6)).det()
            assert det1!=0
            rec["z1_degree"]=6
            rec["z1_pivot_rows"]=piv1
            rec["z1_lower_minor"]=str(det1)
        record.append(rec)
assert sorted(r["phase"] for r in record)==list(range(48))
result={
 "science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "model":"existing native 48-phase positive tail from original 96 bit-ports and 576 typed actions",
 "scope":"all 48 phase basis inputs and all real nonnegative gates",
 "classes":classes,
 "sharp_distribution_nonunit":{"degree_1":16,"degree_5":16,"degree_6":8,"degree_10":8},
 "sharp_distribution_z1":{"degree_1":16,"degree_5":16,"degree_6":16},
 "all_48_symbolic_minor_certificates":record,
 "status":"AUTHOR_SIDE_EXACT_VERIFICATION_PASSED_UNREVIEWED"
}
out=Path(__file__).with_name("PREFIX601_R2_native_phase_basis_krylov_results.json")
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("ALL 48 EXACT BASIS CERTIFICATES PASS; distinct source types:",list(classes))
