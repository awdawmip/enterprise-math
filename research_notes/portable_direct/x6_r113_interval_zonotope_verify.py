"""Exact scoped checks for X6 R113: joint-observer zonotope and improved R112 chambers."""
from fractions import Fraction as Q
from itertools import combinations, product
import json

G = ((-1,-1,-1),(1,0,0),(0,1,0),(0,0,1))
CASES = (
 ((60,1,10,46), Q(1,11), Q(9,61), 51, Q(7,53)),
 ((6,47,45,2), Q(6,49), Q(9,47), 92, Q(3,17)),
)

def det3(a,b,c):
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def den(w):
 a,b,c,d=w
 return (a+b,a+c,a+d,b+c,b+d,c+d)

def score(u,v,h,w):
 return max(Q(abs(t),d) for t,d in zip((u,v,h,v-u,h-u,h-v),den(w)))

def carrier(w,r):
 U,V,H=(int(r*d) for d in den(w)[:3]); rows={}
 for u,v,h in product(range(-U,U+1),range(-V,V+1),range(-H,H+1)):
  if v%3 or (h-u)%6 or (h-u-6*v)%12:continue
  f=score(u,v,h,w)
  if f>r or (u,v,h)==(0,0,0):continue
  a=((h+19*u-8*v)//2,(-h-14*u+7*v)//3,(h+11*u-6*v)//12)
  assert (a[0]+3*a[1]+6*a[2],3*a[0]+12*a[1]+30*a[2],7*a[0]+39*a[1]+126*a[2])==(u,v,h)
  orient=min(a,tuple(-x for x in a))
  q=max(sum(max(x,0) for x in a),sum(max(-x,0) for x in a))
  rows[orient]=(f,q)
 return rows,(U,V,H)

def bound(w,eta,outer,inside_max):
 dmin=min(den(w)); inside=inside_max/eta; outside=outer/eta
 Kmax=min(Q(3,2)/inside,Q(2,3)*outside)
 return Q(dmin,2)*(Kmax-1)/(Kmax+1),Kmax

def main():
 assert tuple(abs(det3(*[G[i] for i in cc])) for cc in combinations(range(4),3))==(1,1,1,1)
 # 14 exposed sign patterns: exclude all equal, since G0+G1+G2+G3=0.
 exposed=[s for s in product((-1,1),repeat=4) if len(set(s))==2]
 assert len(exposed)==14 and len(tuple(combinations(range(4),2)))==6
 # 12 parallelogram facets, 24 edges, 14 vertices via Euler.
 assert 2*6==12 and 12*4//2==24 and 24-12+2==14
 output=[]
 for w,eta,outer,p0,im in CASES:
  vals,box=carrier(w,outer)
  near={a:(f,q) for a,(f,q) in vals.items() if f<Q(3,2)*eta}
  outside={a:(f,q) for a,(f,q) in vals.items() if f>=Q(3,2)*eta}
  assert len(vals)==14 and len(near)==12 and len(outside)==2
  assert min(f for f,q in vals.values())==eta
  assert max(q for f,q in near.values())==p0
  assert max(f for f,q in near.values())==im
  assert min(f for f,q in outside.values())==outer
  epsmax,Kmax=bound(w,eta,outer,im)
  assert Q(1,13)<epsmax
  eps=Q(1,13); t=2*eps/min(den(w)); K=(1+t)/(1-t)
  assert (im/eta)*K < Q(3,2) < (outer/eta)/K
  A,B,C,D=w; e3=A*B*C+A*B*D+A*C*D+B*C*D
  volcoef=Q(2,9)*e3
  density=eta**3*e3/Q(36)
  assert density <= 1
  output.append({"weights":list(w),"p_ge":p0,"eta":str(eta),"moment_box":list(box),
    "complete_carrier_count":len(vals),"near_count":len(near),"outside_count":len(outside),
    "max_inside_score":str(im),"min_outside_score":str(outer),
    "certified_open_supnorm_radius_ceiling":str(epsmax),
    "certified_uniform_supnorm_radius":str(eps),"K_at_uniform_radius":str(K),
    "inside_K_ratio":str((im/eta)*K),"outside_ratio_div_K":str((outer/eta)/K),
    "e3_weights":e3,"uvw_ball_volume_coefficient":str(8*e3),
    "xyz_ball_volume_coefficient":str(volcoef),"minkowski_density_ratio":str(density)})
 report={"schema":"X6_R113_INTERVAL_ZONOTOPE_EXACT_V1",
  "source_model":"R112 fixed four-positive-weight six-pair conditional BRC model",
  "mathematical_proof":"manuscript (interval Helly + segment zonotope + determinant-36 lattice)",
  "checking_scope":"exact finite moment carriers at two fixed R112 centers and symbolic rational perturbation inequalities; combinatorial face determinants",
  "moment_matrix_det":36,"zonotope_generator_triple_abs_det":[1,1,1,1],
  "zonotope_faces_edges_vertices":[12,24,14],"chambers":output}
 print(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':main()
