#!/usr/bin/env python3
"""R034 exact FCC/HCP propagation-sphere laboratory.

The hot path uses integer path counts and rational/surd arithmetic only.
Floating point is used only in optional presentation helpers, never theorem-critical
path counting, local covariance, or rational radial moments.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from typing import Dict, Iterable, Iterator, List, Mapping, Sequence, Tuple
import json
import math

P3 = Tuple[int,int,int]
Mon = Tuple[int,int,int]

# ---------- Q(sqrt(2),sqrt(3)) ----------
@dataclass(frozen=True)
class Q23:
    a: F = F(0)   # 1
    b: F = F(0)   # sqrt2
    c: F = F(0)   # sqrt3
    d: F = F(0)   # sqrt6

    @staticmethod
    def q(x=0) -> "Q23":
        return Q23(F(x))

    def __add__(self, other):
        other = other if isinstance(other,Q23) else Q23.q(other)
        return Q23(self.a+other.a,self.b+other.b,self.c+other.c,self.d+other.d)
    __radd__ = __add__
    def __neg__(self): return Q23(-self.a,-self.b,-self.c,-self.d)
    def __sub__(self, other): return self + (-other if isinstance(other,Q23) else -Q23.q(other))
    def __rsub__(self, other): return Q23.q(other)-self
    def __mul__(self, other):
        other = other if isinstance(other,Q23) else Q23.q(other)
        a,b,c,d=self.a,self.b,self.c,self.d
        e,f,g,h=other.a,other.b,other.c,other.d
        return Q23(
            a*e + 2*b*f + 3*c*g + 6*d*h,
            a*f+b*e+3*c*h+3*d*g,
            a*g+c*e+2*b*h+2*d*f,
            a*h+d*e+b*g+c*f,
        )
    __rmul__ = __mul__
    def inv(self):
        if self.b or self.c or self.d: raise ValueError("non-rational inverse not implemented")
        return Q23(F(1,1)/self.a)
    def __truediv__(self, other):
        other = other if isinstance(other,Q23) else Q23.q(other)
        return self * other.inv()
    def is_zero(self): return not (self.a or self.b or self.c or self.d)
    def to_json(self):
        def fs(q:F): return str(q.numerator) if q.denominator==1 else f"{q.numerator}/{q.denominator}"
        return {name:fs(q) for name,q in (("1",self.a),("sqrt2",self.b),("sqrt3",self.c),("sqrt6",self.d)) if q}
    def __str__(self):
        terms=[]
        for q,n in ((self.a,""),(self.b,"sqrt2"),(self.c,"sqrt3"),(self.d,"sqrt6")):
            if q: terms.append(f"{q}*{n}" if n else f"{q}")
        return " + ".join(terms) if terms else "0"

SQ2=Q23(F(0),F(1)); SQ3=Q23(F(0),F(0),F(1)); SQ6=Q23(F(0),F(0),F(0),F(1))

Poly = Dict[Mon,Q23]
def poly_add(a:Poly,b:Poly)->Poly:
    out=dict(a)
    for m,c in b.items(): out[m]=out.get(m,Q23())+c
    return {m:c for m,c in out.items() if not c.is_zero()}
def poly_mul(a:Poly,b:Poly)->Poly:
    out:Poly={}
    for (i,j,k),u in a.items():
        for (p,q,r),v in b.items():
            m=(i+p,j+q,k+r); out[m]=out.get(m,Q23())+u*v
    return {m:c for m,c in out.items() if not c.is_zero()}
def poly_pow(a:Poly,n:int)->Poly:
    out={(0,0,0):Q23.q(1)}; base=a
    while n:
        if n&1: out=poly_mul(out,base)
        base=poly_mul(base,base); n//=2
    return out
def linpoly(v:Tuple[Q23,Q23,Q23])->Poly:
    return {(1,0,0):v[0],(0,1,0):v[1],(0,0,1):v[2]}
def moment_poly(steps:Sequence[Tuple[Q23,Q23,Q23]],m:int)->Poly:
    out:Poly={}
    for v in steps: out=poly_add(out,poly_pow(linpoly(v),m))
    return {mon:c/12 for mon,c in out.items()}
def poly_scale(p:Poly,q)->Poly:
    return {m:c*q for m,c in p.items() if not (c*q).is_zero()}
def cumulant_polys(steps):
    m={j:moment_poly(steps,j) for j in range(1,7)}
    k={1:m[1],2:m[2],3:m[3]}
    k[4]=poly_add(m[4],poly_scale(poly_mul(m[2],m[2]),-3))
    k[5]=poly_add(m[5],poly_scale(poly_mul(m[3],m[2]),-10))
    k[6]=poly_add(m[6],poly_add(poly_scale(poly_mul(m[4],m[2]),-15),poly_add(poly_scale(poly_mul(m[3],m[3]),-10),poly_scale(poly_mul(poly_mul(m[2],m[2]),m[2]),30))))
    return k
def poly_json(p:Poly):
    return {f"x^{i} y^{j} z^{k}":c.to_json() for (i,j,k),c in sorted(p.items(),reverse=True)}

# ---------- graph models ----------
FCC_DIRS=(
    (0,-1,-1),(0,-1,1),(0,1,-1),(0,1,1),
    (-1,0,-1),(-1,0,1),(1,0,-1),(1,0,1),
    (-1,-1,0),(-1,1,0),(1,-1,0),(1,1,0),
)
TRI_DIRS=((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))

def fcc_neighbors(p:P3)->Tuple[P3,...]:
    x,y,z=p
    return tuple((x+a,y+b,z+c) for a,b,c in FCC_DIRS)

def hcp_neighbors(p:P3)->Tuple[P3,...]:
    i,j,k=p
    same=[(i+a,j+b,k) for a,b in TRI_DIRS]
    shifts=((0,0),(1,0),(0,1)) if (k&1) else ((0,0),(-1,0),(0,-1))
    lower=[(i+a,j+b,k-1) for a,b in shifts]
    upper=[(i+a,j+b,k+1) for a,b in shifts]
    return tuple(same+lower+upper)

def hcp_center(p:P3)->Tuple[F,F,F]:
    i,j,k=p; s=F(1,3) if k&1 else F(0)
    return F(i)+s,F(j)+s,F(k)

FCC_G=((F(1,2),F(0),F(0)),(F(0),F(1,2),F(0)),(F(0),F(0),F(1,2)))
HCP_G=((F(1),F(1,2),F(0)),(F(1,2),F(1),F(0)),(F(0),F(0),F(2,3)))

def qform(G, v:Tuple[F,F,F])->F:
    return sum(v[i]*sum(G[i][j]*v[j] for j in range(3)) for i in range(3))
def fcc_r2(p:P3)->F: return qform(FCC_G, tuple(F(x) for x in p))
def hcp_r2(p:P3)->F: return qform(HCP_G, hcp_center(p))

def fcc_orbit_key(p:P3):
    return tuple(sorted((abs(p[0]),abs(p[1]),abs(p[2]))))

def _hcp_r120(v):
    u,w,z=v; return -u-w,u,z
def _hcp_reflect(v):
    u,w,z=v; return w,u,z
def _hcp_zflip(v):
    u,w,z=v; return u,w,-z
def _hcp_coeff_to_state(v):
    u,w,z=v; k=int(z); assert F(k)==z
    shift=F(1,3) if (k&1) else F(0)
    i=u-shift; j=w-shift; assert i.denominator==j.denominator==1
    return int(i),int(j),k
def hcp_orbit_key(p:P3):
    v=hcp_center(p); imgs=[]
    for rot in range(3):
        vr=v
        for _ in range(rot): vr=_hcp_r120(vr)
        for refl in (False,True):
            w=_hcp_reflect(vr) if refl else vr
            for zf in (False,True):
                q=_hcp_zflip(w) if zf else w
                imgs.append(_hcp_coeff_to_state(q))
    return min(imgs)

def angular_orbit_summary(counts,world):
    keyfn=fcc_orbit_key if world=="fcc" else hcp_orbit_key
    groups=defaultdict(list)
    for p,c in counts.items(): groups[keyfn(p)].append((p,c))
    assert all(len({c for _,c in vals})==1 for vals in groups.values())
    return {
      "orbit_count":len(groups),
      "orbit_size_histogram":{str(k):v for k,v in sorted(Counter(len(vals) for vals in groups.values()).items())},
      "orbit_path_count_histogram":{str(k):v for k,v in sorted(Counter(vals[0][1] for vals in groups.values()).items())}
    }

# ---------- physical unit-step vectors in orthonormal coordinates ----------
def fcc_steps_physical():
    a=SQ2/2
    return tuple((Q23.q(x)*a,Q23.q(y)*a,Q23.q(z)*a) for x,y,z in FCC_DIRS)

def hcp_steps_physical(parity:int):
    half=Q23.q(F(1,2)); rt3_2=SQ3/2; rt3_6=SQ3/6; rt3_3=SQ3/3; h=SQ6/3
    same=(
        (Q23.q(1),Q23.q(0),Q23.q(0)),(Q23.q(-1),Q23.q(0),Q23.q(0)),
        (half,rt3_2,Q23.q(0)),(-half,-rt3_2,Q23.q(0)),
        (half,-rt3_2,Q23.q(0)),(-half,rt3_2,Q23.q(0)),
    )
    P=((half,rt3_6),( -half,rt3_6),(Q23.q(0),-rt3_3))
    if parity: P=tuple((-x,-y) for x,y in P)
    inter=[]
    for z in (-h,h):
        inter.extend((x,y,z) for x,y in P)
    return tuple(same)+tuple(inter)

# ---------- exact local mean/covariance in coefficient coordinates ----------
def coeff_displacements(world:str,parity:int=0):
    if world=="fcc": return [tuple(F(x) for x in d) for d in FCC_DIRS], FCC_G
    p=(0,0,parity); c=hcp_center(p); ds=[]
    for q in hcp_neighbors(p):
        cq=hcp_center(q); ds.append(tuple(cq[i]-c[i] for i in range(3)))
    return ds,HCP_G

def mat_inverse_3(G):
    A=[list(G[i])+[F(int(i==j)) for j in range(3)] for i in range(3)]
    for c in range(3):
        p=next(r for r in range(c,3) if A[r][c])
        A[c],A[p]=A[p],A[c]
        z=A[c][c]; A[c]=[x/z for x in A[c]]
        for r in range(3):
            if r==c: continue
            z=A[r][c]
            if z: A[r]=[A[r][j]-z*A[c][j] for j in range(6)]
    return tuple(tuple(A[i][j+3] for j in range(3)) for i in range(3))

def local_mean_cov(world:str,parity:int=0):
    ds,G=coeff_displacements(world,parity)
    mean=tuple(sum(d[i] for d in ds)/12 for i in range(3))
    C=tuple(tuple(sum(d[i]*d[j] for d in ds)/12 for j in range(3)) for i in range(3))
    target=tuple(tuple(mat_inverse_3(G)[i][j]/3 for j in range(3)) for i in range(3))
    return mean,C,target

# ---------- path counts ----------
def path_counts(neighbors, n:int, origin:P3=(0,0,0))->Dict[P3,int]:
    d={origin:1}
    for _ in range(n):
        nxt=defaultdict(int)
        for p,c in d.items():
            for q in neighbors(p): nxt[q]+=c
        d=dict(nxt)
    return d

def path_layers(neighbors,N:int,origin:P3=(0,0,0))->Iterator[Tuple[int,Dict[P3,int]]]:
    d={origin:1}; yield 0,d
    for n in range(1,N+1):
        nxt=defaultdict(int)
        for p,c in d.items():
            for q in neighbors(p): nxt[q]+=c
        d=dict(nxt); yield n,d

def radial_hist(counts:Mapping[P3,int], r2fn):
    h=defaultdict(int)
    for p,c in counts.items(): h[r2fn(p)]+=c
    return dict(sorted(h.items()))
def count_hist(counts:Mapping[P3,int]): return dict(sorted(Counter(counts.values()).items()))
def fracstr(q:F): return str(q.numerator) if q.denominator==1 else f"{q.numerator}/{q.denominator}"

def radial_moment(counts,r2fn,power:int)->F:
    total=sum(counts.values())
    return sum(F(c)*r2fn(p)**power for p,c in counts.items())/total

def same_radius_witness(counts,r2fn):
    by=defaultdict(lambda:defaultdict(list))
    for p,c in counts.items(): by[r2fn(p)][c].append(p)
    for r2,cs in sorted(by.items()):
        if len(cs)>1:
            vals=sorted(cs)
            return {"r2":fracstr(r2),"count_a":vals[0],"state_a":list(cs[vals[0]][0]),
                    "count_b":vals[-1],"state_b":list(cs[vals[-1]][0])}
    return None

# ---------- exact closed formulas discovered in R034 ----------
def radial2(n:int)->F: return F(n)
def radial4(n:int)->F: return F(5*n*n-2*n,3)
def radial6_fcc(n:int)->F: return F(n*(35*n*n-42*n+16),9)
def radial6_hcp(n:int)->F:
    if n==0:return F(0)
    return F(210*n**3-252*n**2+95*n+1,54)

def fourth_components_fcc(n:int):
    return {"x4":F(n*(2*n-1),6),"x2y2":F(n*(4*n-1),36)}
def fourth_components_hcp(n:int):
    return {"x4=y4":F(n*(8*n-3),24),"z4":F(n*(3*n-1),9),
            "x2y2":F(n*(8*n-3),72),"x2z2=y2z2":F(n*(2*n-1),18)}

# ---------- spectral formulas (exact closed forms) ----------
SPECTRAL={
 "fcc":{
  "lambda2":"-(x^2+y^2+z^2)/6",
  "lambda4":"(x^4+3*x^2*y^2+3*x^2*z^2+y^4+3*y^2*z^2+z^4)/144",
  "lambda6":"-(2*x^6+15*x^4*y^2+15*x^4*z^2+15*x^2*y^4+15*x^2*z^4+2*y^6+15*y^4*z^2+15*y^2*z^4+2*z^6)/17280",
  "log2":"-(x^2+y^2+z^2)/6",
  "log4":"-(x^4+x^2*y^2+x^2*z^2+y^4+y^2*z^2+z^4)/144",
  "log6":"-(26*x^6+45*x^4*y^2+45*x^4*z^2+45*x^2*y^4-60*x^2*y^2*z^2+45*x^2*z^4+26*y^6+45*y^4*z^2+45*y^2*z^4+26*z^6)/51840",
  "quartic_unit_direction_range":["-1/144","-1/216"],
  "spectral_anisotropy_spread":"q^4/(432*n)+O(n^-2)"
 },
 "hcp_principal":{
  "lambda2":"-(x^2+y^2+z^2)/6",
  "lambda4":"(15*x^4+30*x^2*y^2+24*x^2*z^2+15*y^4+24*y^2*z^2+16*z^4)/1728",
  "lambda6":"-(153*x^6+135*x^4*y^2+180*x^4*z^2+675*x^2*y^4+360*x^2*y^2*z^2+480*x^2*z^4+117*y^6+180*y^4*z^2+480*y^2*z^4+128*z^6)/622080",
  "log2":"-(x^2+y^2+z^2)/6",
  "log4":"-(9*x^4+18*x^2*y^2+24*x^2*z^2+9*y^4+24*y^2*z^2+8*z^4)/1728",
  "log6":"-(213*x^6+315*x^4*y^2+720*x^4*z^2+855*x^2*y^4+1440*x^2*y^2*z^2+960*x^2*z^4+177*y^6+720*y^4*z^2+960*y^2*z^4+128*z^6)/622080",
  "quartic_unit_direction_range":["-1/168","-1/216"],
  "spectral_anisotropy_spread":"q^4/(756*n)+O(n^-2)"
 },
 "hcp_optical":{
  "lambda0":"0",
  "lambda2":"-(x^2+y^2-2*z^2)/12",
  "note":"separated from principal lambda=1 band at k=0"
 },
 "hcp_closed_symbol":{
   "C":"cos(x)+2*cos(x/2)*cos(sqrt(3)*y/2)",
   "S":"2*cos(x/2)*exp(i*sqrt(3)*y/6)+exp(-i*sqrt(3)*y/3)",
   "h":"sqrt(2/3)",
   "P":"[[C/6, cos(h*z)*S/6],[cos(h*z)*conj(S)/6,C/6]]",
   "bands":"lambda_±=C/6 ± cos(h*z)*sqrt(3+2*C)/6 near k=0"
 },
 "fcc_closed_symbol": "(cos(x/sqrt(2))*cos(y/sqrt(2))+cos(x/sqrt(2))*cos(z/sqrt(2))+cos(y/sqrt(2))*cos(z/sqrt(2)))/3",
 "stacking_aligned_quartic_difference":"log4_FCC-log4_HCP = -sqrt(2)*y*z*(3*x^2-y^2)/432"
}

# ---------- atlas builders ----------
def local_tensor_atlas():
    out={"schema":"R034_LOCAL_MOMENT_TENSORS_V1","nn_length":1,"worlds":{}}
    for world,parities in (("fcc",[0]),("hcp",[0,1])):
        for parity in parities:
            mean,C,target=local_mean_cov(world,parity)
            steps=fcc_steps_physical() if world=="fcc" else hcp_steps_physical(parity)
            key=world if world=="fcc" else f"hcp_{'A' if parity==0 else 'B'}"
            out["worlds"][key]={
                "coefficient_mean":[fracstr(x) for x in mean],
                "coefficient_covariance":[[fracstr(x) for x in row] for row in C],
                "isotropy_target_one_third_G_inverse":[[fracstr(x) for x in row] for row in target],
                "covariance_is_I_over_3": C==target,
                "moment_contractions":{str(m):poly_json(moment_poly(steps,m)) for m in range(1,7)},
                "cumulant_contractions":{str(m):poly_json(cumulant_polys(steps)[m]) for m in range(1,7)}
            }
    out["first_memory_orders"]={
        "rooted_one_step_physical_tensor":3,
        "A_B_averaged_or_principal_band":4,
        "scalar_radial_even_moment":6,
        "return_probability":"none: exact Barlow gauge universality theorem candidate"
    }
    return out

def finite_atlas(full_N=2,summary_N=12,return_N=12):
    out={"schema":"R034_FINITE_N_PROPAGATION_ATLAS_V1","full_distribution_N":full_N,
         "summary_N":summary_N,"return_N":return_N,"worlds":{},"comparison":{}}
    worldspec={"fcc":(fcc_neighbors,fcc_r2),"hcp":(hcp_neighbors,hcp_r2)}
    returns={}
    heat={}
    heat_ns={4,8,12}
    for world,(neigh,r2fn) in worldspec.items():
        summaries=[]; full=[]; return_counts=[]; first_nonuniform=None; heat_rows=[]
        for n,counts in path_layers(neigh,return_N):
            if n<=summary_N:
                s={"n":n,"support_size":len(counts),"return_count":counts.get((0,0,0),0),
                   "total_paths":12**n,
                   "Er2":fracstr(radial_moment(counts,r2fn,1)),
                   "Er4":fracstr(radial_moment(counts,r2fn,2)),
                   "Er6":fracstr(radial_moment(counts,r2fn,3)),
                   "path_count_histogram":{str(k):v for k,v in count_hist(counts).items()} if n<=4 else None,
                   "angular_orbits":angular_orbit_summary(counts,world) if n<=4 else None}
                w=same_radius_witness(counts,r2fn)
                if w and first_nonuniform is None: first_nonuniform={"n":n,**w}
                summaries.append(s)
            return_counts.append(counts.get((0,0,0),0))
            if n in heat_ns and n<=return_N:
                c0=counts[(0,0,0)]
                for th in (F(1,2),F(1,10)):
                    inside=[r2fn(p) for p,c in counts.items() if c*th.denominator>=c0*th.numerator]
                    outside=[r2fn(p) for p,c in counts.items() if c*th.denominator<c0*th.numerator]
                    heat_rows.append({"n":n,"threshold_of_origin":fracstr(th),
                                      "max_inside_r2":fracstr(max(inside)),"min_excluded_r2":fracstr(min(outside)),
                                      "radial_interface_width_r2":fracstr(min(outside)-max(inside))})
            if n<=full_N:
                rows=[]
                for p,c in sorted(counts.items()):
                    rr=r2fn(p)
                    rows.append([p[0],p[1],p[2],c,rr.numerator,rr.denominator])
                full.append({"n":n,"columns":["i","j","k","count","r2_num","r2_den"],"rows":rows})
        out["worlds"][world]={"summaries":summaries,"full_distributions":full,
                              "return_counts_0_to_N":return_counts,
                              "first_same_radius_nonuniformity":first_nonuniform}
        returns[world]=return_counts
        heat[world]=heat_rows
    f2=path_counts(fcc_neighbors,2); h2=path_counts(hcp_neighbors,2)
    out["comparison"]={
      "first_unlabeled_path_count_distribution_witness":{
        "n":2,"fcc_support":len(f2),"hcp_support":len(h2),
        "fcc_count_histogram":{str(k):v for k,v in count_hist(f2).items()},
        "hcp_count_histogram":{str(k):v for k,v in count_hist(h2).items()}
      },
      "n2_radial_histograms":{
        "fcc":{fracstr(r):c for r,c in radial_hist(f2,fcc_r2).items()},
        "hcp":{fracstr(r):c for r,c in radial_hist(h2,hcp_r2).items()},
      },
      "return_counts_identical_through_N":returns["fcc"]==returns["hcp"],
      "return_count_N":return_N,
      "radial_moment_closed_forms":{
        "Er2_both":"n",
        "Er4_both":"(5*n^2-2*n)/3",
        "Er6_fcc":"n*(35*n^2-42*n+16)/9",
        "Er6_hcp":"(210*n^3-252*n^2+95*n+1)/54 for n>=1",
        "Er6_hcp_minus_fcc":"-(n-1)/54"
      },
      "global_coordinate_moment_closed_forms":{
        "fcc_4th":{"Ex4":"n*(2*n-1)/6","Ex2y2":"n*(4*n-1)/36","permutations":"cubic symmetry"},
        "hcp_4th":{"Ex4=Ey4":"n*(8*n-3)/24","Ez4":"n*(3*n-1)/9","Ex2y2":"n*(8*n-3)/72","Ex2z2=Ey2z2":"n*(2*n-1)/18"},
        "hcp_3rd_harmonic":{"H":"Y*(3*X^2-Y^2)","E[H(X_n)]":"sqrt(3)/18 for n>=1 from A origin","fcc":"0"}
      }
    }
    out["heat_ball_threshold_atlas"]={"definition":"H_{n,theta}={x:c_n(x)>=theta*c_n(0)} for even n",
                                      "rows":heat,
                                      "interpretation":"finite-n level sets are not exact radial balls; interface width in r^2 stays microscopic over the sampled range while radius^2 is O(n)"}
    return out

def compact_finite_atlas():
    p=finite_atlas()
    return {
      "schema":p["schema"],"full_distribution_N":p["full_distribution_N"],
      "summary_N":p["summary_N"],"return_N":p["return_N"],
      "full_distributions":{w:p["worlds"][w]["full_distributions"] for w in ("fcc","hcp")},
      "summary_rows":{w:[{k:x[k] for k in ("n","support_size","return_count","Er2","Er4","Er6")}
                         for x in p["worlds"][w]["summaries"]] for w in ("fcc","hcp")},
      "small_time_angular_orbits":{w:[{"n":x["n"],"path_count_histogram":x["path_count_histogram"],
                                        "angular_orbits":x["angular_orbits"]}
                                      for x in p["worlds"][w]["summaries"] if x["n"]<=4]
                                   for w in ("fcc","hcp")},
      "first_same_radius_nonuniformity":{w:p["worlds"][w]["first_same_radius_nonuniformity"] for w in ("fcc","hcp")},
      "comparison":p["comparison"],"heat_ball_threshold_atlas":p["heat_ball_threshold_atlas"]
    }

def semantics_matrix():
    return {
      "schema":"R034_PROPAGATION_SEMANTICS_MATRIX_V1",
      "rows":[
       {"semantics":"word_metric_ball","scale":"r","fcc_macro":"cuboctahedral polytope","hcp_macro":"18-vertex stable velocity polytope","fcc_hcp_universal":False,"isotropic":False,"memory":"leading order"},
       {"semantics":"uniform_NN_second_moment","scale":"n","fcc_macro":"n I/3 covariance","hcp_macro":"n I/3 covariance","fcc_hcp_universal":True,"isotropic":True,"memory":"forgotten exactly at rank-2"},
       {"semantics":"uniform_NN_diffusive_CLT","scale":"sqrt(n)","fcc_macro":"Gaussian covariance I/3","hcp_macro":"same Gaussian covariance I/3","fcc_hcp_universal":True,"isotropic":True,"memory":"subleading"},
       {"semantics":"principal_spectral_band","scale":"k=q/sqrt(n)","fcc_macro":"-|q|^2/6 + O(1/n)","hcp_macro":"same quadratic + O(1/n)","fcc_hcp_universal":True,"isotropic":True,"memory":"quartic O(1/n)"},
       {"semantics":"finite_time_full_kernel","scale":"finite n","fcc_macro":"angularly anisotropic","hcp_macro":"angularly anisotropic","fcc_hcp_universal":False,"isotropic":False,"memory":"physical distribution differs at n=1; unlabeled count distribution at n=2"},
       {"semantics":"return_probability","scale":"n","fcc_macro":"same return sequence","hcp_macro":"same return sequence","fcc_hcp_universal":True,"isotropic":None,"memory":"conjecturally/exactly forgotten for all Barlow stackings by layer-Fourier gauge theorem"}
      ]
    }

def barlow_atlas():
    return {
      "schema":"R034_BARLOW_EXTENSION_V1",
      "local_theorem":{
        "hypotheses":"legal close-packed triangular-layer Barlow stacking; uniform 12-neighbor walk; ideal NN geometry normalized to 1",
        "zero_drift":True,
        "conditional_covariance":"I/3 at every cell",
        "proof_certificate":{
          "same_layer_sum_outer":"diag(3,3,0)",
          "each_interlayer_triangle_planar_sum_outer":"(1/2) I_2",
          "above_plus_below_total":"diag(1,1,4)",
          "all_12_sum_outer":"4 I_3"
        }
      },
      "leading_diffusion":{
        "periodic": "same Brownian leading covariance I/3",
        "arbitrary_nonperiodic":"bounded martingale differences + deterministic predictable quadratic variation n I/3 -> martingale functional CLT route",
        "pointwise_nonperiodic_heat_kernel":"OPEN; FCLT does not itself imply a local CLT"
      },
      "local_higher_memory":{
        "ABA_turnback":"nonzero basal cubic third tensor; A/B sign reversal",
        "ABC_continuation":"cubic cancels; quartic stacking-chirality harmonic survives"
      },
      "return_gauge_theorem_candidate":{
        "statement":"after basal Fourier transform, interlayer hopping phases live on a one-dimensional layer chain and are removable by a diagonal layer gauge; all legal Barlow NN transition fibers are unitarily equivalent to a stacking-independent constant-magnitude Jacobi fiber",
        "consequences":["same return probability at every n","same root local spectral measure","same integrated NN adjacency/transition spectrum"],
        "boundary":"q-dependent gauge is not a physical-coordinate vertex permutation and does not erase physical wavevector-labelled angular dispersion or heat-kernel corrections"
      }
    }

def hypothesis_atlas():
    return {
      "schema":"R034_HYPOTHESIS_DISPOSITIONS_V1",
      "H1":{"status":"PASS","result":"exact zero drift FCC/HCP A/B"},
      "H2":{"status":"PASS","result":"exact local covariance I/3 FCC/HCP A/B"},
      "H3":{"status":"PASS","result":"E[X_n X_n^T]=n I/3 exact for all n"},
      "H4":{"status":"PASS","result":"common isotropic Gaussian/Brownian leading diffusive geometry"},
      "H5":{"status":"PASS_REFINED","result":"memory orders: rooted local m=3; principal/even m=4; radial scalar m=6; return probability forgets stacking"},
      "H6":{"status":"PASS","result":"same cell world supports polyhedral ballistic and Euclidean-leading diffusive spheres"},
      "H7":{"status":"DIRECT_LINK_KILLED","result":"exposed-face equality and covariance equality are distinct coarse-memory-loss observables; no derivation connecting them found"},
      "H8":{"status":"PASS","result":"arbitrary legal Barlow local zero drift and covariance I/3"},
      "H9":{"status":"PASS_LEADING_OPEN_LOCAL","result":"arbitrary Barlow martingale FCLT leading universality; nonperiodic pointwise heat-kernel local CLT remains open"},
      "H10":{"status":"PASS","result":"pi absent from microscopic rule; enters only Gaussian normalization/Fourier inversion"},
      "H11":{"status":"PASS_ASYMPTOTIC","result":"spectral angular spread FCC q^4/(432n), HCP q^4/(756n), plus O(n^-2)"},
      "H12":{"status":"PASS_ASYMPTOTIC_CERTIFICATE","result":"at n=1e36 quartic spectral angular corrections are ~2.31e-39 FCC and ~1.32e-39 HCP for q=1; sixth order O(1e-72)"}
    }

if __name__=="__main__":
    import argparse, pathlib
    ap=argparse.ArgumentParser(); ap.add_argument("--atlas-dir",default=None); args=ap.parse_args()
    if args.atlas_dir:
        d=pathlib.Path(args.atlas_dir); d.mkdir(parents=True,exist_ok=True)
        payloads={
          "R034_LOCAL_MOMENT_TENSORS.json":local_tensor_atlas(),
          "R034_FINITE_N_PROPAGATION_ATLAS.json":compact_finite_atlas(),
          "R034_SPECTRAL_EXPANSION.json":{"schema":"R034_SPECTRAL_EXPANSION_V1",**SPECTRAL},
          "R034_PROPAGATION_SEMANTICS_MATRIX.json":semantics_matrix(),
          "R034_BARLOW_EXTENSION.json":barlow_atlas(),
          "R034_HYPOTHESIS_DISPOSITIONS.json":hypothesis_atlas(),
        }
        for fn,obj in payloads.items():
            (d/fn).write_text(json.dumps(obj,separators=(",",":"),sort_keys=True)+"\n",encoding="utf-8")
        print("wrote",len(payloads),"atlases to",d)
    else:
        print(json.dumps({"local":local_tensor_atlas()["first_memory_orders"],"hypotheses":hypothesis_atlas()},indent=2))
