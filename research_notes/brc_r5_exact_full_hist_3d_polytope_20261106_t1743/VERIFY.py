#!/usr/bin/env python3
"""R5 exact rational H/V certificate: FULL_HIST (TQ,TP,D) projection."""
from fractions import Fraction as Q
from itertools import product, combinations
T=[(-323,282,0,-41),(-188,216,0,139),(-160,160,0,41),(-1,2,0,4),
   (3,-2,0,4),(80,-80,0,23),(123,-146,0,-23),(274,-236,0,179)]
B=[(-444824,376149,184500,-68675),(-27912,17792,136000,3887),
   (-12234,7979,29500,-4255),(-2912,-3128,53000,-5455),
   (-360,0,40000,9843),(-26,1,200,-25),(-13,-112,1000,-125),
   (1063,-2288,9000,-1225),(3984,-8904,52000,-2007),
   (15671,-21076,23000,-5405)]
H=T+[(a,b,c*s,h) for a,b,c,h in B for s in (-1,1)]
q=((Q(13,20),Q(1,5),Q(3,20)),(Q(1,40),Q(9,20),Q(21,40)))
def det(a,b,c):
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def solve3(rows):
 a,b,c=(r[:3] for r in rows);d=det(a,b,c)
 if not d:return None
 v=[r[3] for r in rows]
 return tuple(Q(det([v[0] if i==j else a[i] for i in range(3)],
                    [v[1] if i==j else b[i] for i in range(3)],
                    [v[2] if i==j else c[i] for i in range(3)]),d) for j in range(3))
def solve2(a,b):
 p,q0,_,r=a;s,t,_,u=b; d=p*t-q0*s
 return (Q(r*t-q0*u,d),Q(p*u-r*s,d)) if d else None
def inside(x):return all(sum(f[i]*x[i] for i in range(3))<=f[3] for f in H)
def main():
 stop=set()
 for g,v0,v1 in product((Q(0),Q(1)),repeat=3):
  u0,u1=g*v0,g*v1
  cap=[[u*q[i][j]/2 for j in range(3)] for i,u in enumerate((u0,u1))]
  for z in product((0,1),repeat=6):
   x=[[cap[i][j]*z[3*i+j] for j in range(3)] for i in range(2)]
   X=[x[0][j]+x[1][j] for j in range(3)]
   V=[cap[0][j]+cap[1][j] for j in range(3)]
   J=Q(47,180)*x[0][1]+Q(67,162)*x[1][1]
   m={Q(1,10):(509*X[0]+9*X[2])/900+J,
      Q(1,2):V[0]-X[0], Q(3,4):(g-u0)/2,
      Q(1):1-g+V[1]+Q(382,900)*(X[0]+X[2])-2*J,
      Q(5,4):(g-u1)/2,Q(3,2):V[2]-X[2],
      Q(19,10):(9*X[0]+509*X[2])/900+J}
   assert min(m.values())>=0 and sum(m.values())==1
   assert sum(r*v for r,v in m.items())==1
   tq=1+g+(u0+u1)/2+sum(X)
   tp=1+g+(3*u0+5*u1)/8+X[0]/2+X[1]+3*X[2]/2
   S=sum((1-r)*v for r,v in m.items() if r<1)
   assert S==g/8+3*u0/80+u1/160+Q(9,1000)*(X[0]+X[2])+Q(9,10)*J
   stop.add((tq,tp,S))
 pts={(tq,tp,s*S) for tq,tp,S in stop for s in (-1,1)}
 assert len(stop)==82 and len(pts)==163 and all(inside(p) for p in pts)
 for row in H:
  tight=[p for p in pts if sum(row[i]*p[i] for i in range(3))==row[3]]
  assert any(det(tuple(v[i]-tight[0][i] for i in range(3)),
                 tuple(w[i]-tight[0][i] for i in range(3)),row[:3])!=0
             for v,w in combinations(tight[1:],2))
 vertices={v for rows in combinations(H,3) if (v:=solve3(rows)) is not None and inside(v)}
 assert len(vertices)==23 and vertices<=pts
 tv={v for rows in combinations(T,2) if (v:=solve2(*rows)) is not None
     and all(a*v[0]+b*v[1]<=h for a,b,_,h in T)}
 assert len(tv)==8 and tv<={(p[0],p[1]) for p in pts}
 for s,t in ((1,0),(-1,0),(0,1),(0,-1)):
  assert any((lambda d: d and Q(s*b[1]-t*b[0],d)>=0 and Q(a[0]*t-a[1]*s,d)>=0)
             (a[0]*b[1]-a[1]*b[0]) for a,b in combinations(T,2))
 upper=min(Q(h-(a+b)*Q(5,2),c) for a,b,c,h in B)
 assert upper==Q(1929,10600)
 assert (Q(2),Q(2),Q(1,8)) in stop
 assert (Q(133,40),Q(133,40),Q(69,250)) in stop
 assert Q(33,53)/8+Q(20,53)*Q(69,250)==upper<Q(3,16)
 assert inside((Q(5,2),Q(5,2),upper))
 assert not inside((Q(5,2),Q(5,2),Q(3,16)))
 print('PASS_EXACT_R5_FULL_HIST_3D_PROJECTION_28_FACETS')
 print('stop_encodings=512 distinct_stop=',len(stop),'signed_threshold_points=',len(pts))
 print('timing_facets=',len(T),'support_pairs=',len(B),'polytope_vertices=',len(vertices))
 print('timing_octagon_vertices=',len(tv))
 print('at TQ=TP=5/2 sharp |D|=',upper,'old_bound=',Q(3,16),
       'improvement=',Q(3,16)-upper)
 print('attainment_mixture=(33/53,20/53)')
if __name__=='__main__':main()
