#!/usr/bin/env python3
"""Exact ninth-trit q=9 six-branch moving-orbit BRC period certificate.

Use: python3 R762FJ_ORBIT_PERIOD_CERTIFICATE_VERIFY.py --h 7 8 9 --scan-end 42 --output R762FJ_EVIDENCE.json
All arithmetic is integer; no third-party packages.
"""
import argparse
import json

Q=9
STEPS=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
# Exact 33rd-degree polynomial from R762FI moving-frame spectrum (PR #2773).
# We independently certify Q(C)h1=0, which alone suffices for this trajectory.
QPOLY=(-35126124336,-33404255496,494463335220,80927835480,
 -2424772369917,893378361609,5174614267803,-3602916482643,
 -5480907808095,5538001341411,2860442623503,-4523567996151,
 -418901654160,2173478400108,-321833010726,-630844592526,
 209061245835,106100806905,-58427601858,-8032977846,
 9305831529,-370276353,-873783045,140091201,44801505,
 -13153833,-800280,600588,-29646,-12726,1617,63,-21,1)
assert len(QPOLY)==34 and QPOLY[-1]==1

def canon(a):
 a=tuple(x%Q for x in a)
 return min(tuple(sorted(a)),tuple(sorted((-x)%Q for x in a)))

REPS=sorted({canon((x,y,z)) for x in range(Q) for y in range(Q) for z in range(Q)})
RID={r:i for i,r in enumerate(REPS)}
assert len(REPS)==85
CENTER=pow(2,-1,Q)
TS=tuple(((x-CENTER)%Q,(CENTER-y)%Q,(z-CENTER)%Q) for x,y,z in STEPS)
NEIGHBORS=tuple(tuple(RID[canon(tuple((k[i]-t[i])%Q for i in range(3)))] for t in TS) for k in REPS)

def next_orbit(v,mod=None):
 if mod is None:
  return [sum(v[j] for j in ns) for ns in NEIGHBORS]
 return [sum(v[j] for j in ns)%mod for ns in NEIGHBORS]

def v3_exact(x):
 if x==0:return None
 t=0
 while x%3==0:t+=1;x//=3
 return t

def verify_coeff_bounds():
 for j in range(1,34):
  assert QPOLY[33-j]%(3**((j+2)//3))==0,(j,QPOLY[33-j])
 return 33

def base_vectors():
 v=[0]*85;v[RID[canon((0,0,0))]]=1
 vs=[v]
 for _ in range(41):vs.append(next_orbit(vs[-1]))
 for n in range(9,42):
  d=3**(n//3-2)
  assert all(x%d==0 for x in vs[n]),(n,'initial_integrality')
 for i in range(85):
  assert sum(QPOLY[j]*vs[j+1][i] for j in range(34))==0,(i,"invalid Q(C)h1")
 return vs

# Arithmetic in Z[T]/(Q(T)) modulo 3^E.
def polymul(a,b,mod):
 d=33
 p=[0]*(2*d-1)
 for i,ai in enumerate(a):
  if ai:
   for j,bj in enumerate(b):
    if bj:p[i+j]+=ai*bj
 for k in range(2*d-2,d-1,-1):
  x=p[k]%mod
  if x:
   for j in range(d):p[k-d+j]-=x*QPOLY[j]
  p[k]=0
 return [x%mod for x in p[:d]]

def poly_x_pow(n,mod):
 v=[0]*33;v[0]=1
 b=[0]*33;b[1]=1
 while n:
  if n&1:v=polymul(v,b,mod)
  n//=2
  if n:b=polymul(b,b,mod)
 return v

def fast_orbit_at(n,mod,vs):
 assert n>=1
 p=poly_x_pow(n-1,mod)
 return [sum(p[j]*vs[j+1][i] for j in range(33))%mod for i in range(85)]

def witness(h,n,L,vs):
 b=L//3
 E=n//3-2+b
 mod=3**(E+h)
 a=fast_orbit_at(n,mod,vs)
 c=fast_orbit_at(n+L,mod,vs)
 div=3**E
 bad=[]
 origin=None
 for i in range(85):
  numer=(c[i]-3**b*a[i])%mod
  assert numer%div==0,(h,n,L,i,'normalization_integrality_failed')
  residue=numer//div
  if i==RID[canon((0,0,0))]:origin=residue
  if residue:
   bad.append((i,REPS[i],residue,v3_exact(residue)))
 if not bad:return {"h":h,"n":n,"L":L,"equal":True,"nonzero_orbits":0,"origin_residue":origin}
 i,r,res,val=min(bad,key=lambda x:(x[3],x[0]))
 return {"h":h,"n":n,"L":L,"equal":False,"nonzero_orbits":len(bad),
    "minimum_v3":val,"witness_orbit":list(r),"witness_residue_mod_3h":res,
    "origin_residue":origin}

def first_onset(h,vs,nstart=9,nend=50):
 # One modular polynomial-power pair covers the whole scan plus a 33-time
 # recurrence certificate at the first matching onset.
 L=18*3**(h-1);b=L//3
 maxexp=(nend+32)//3-2+b+h
 mod=3**maxexp
 a=fast_orbit_at(nstart,mod,vs)
 c=fast_orbit_at(nstart+L,mod,vs)
 hits=[];origin=[];witnesses={}
 i0=RID[canon((0,0,0))]
 factor=3**b
 for n in range(nstart,nend+33):
  f=n//3-2
  scale=3**(f+b)
  target=scale*3**h
  bad=[]
  origin_residue=0
  for i in range(85):
   raw=(c[i]-factor*a[i])%target
   assert raw%scale==0,(n,i,'normalized difference not integral')
   residue=raw//scale
   if i==i0:origin_residue=residue
   if residue:bad.append((i,REPS[i],residue,v3_exact(residue)))
  good=not bad
  hits.append(good)
  if n<=nend:
   origin.append(origin_residue==0)
   if bad:
    i,r,res,val=min(bad,key=lambda x:(x[3],x[0]))
    witnesses[n]={"h":h,"n":n,"L":L,"minimum_v3":val,
       "nonzero_orbits":len(bad),"witness_orbit":list(r),
       "witness_residue_mod_3h":res,"origin_residue":origin_residue}
  a=next_orbit(a,mod)
  c=next_orbit(c,mod)
 onset=None
 for n in range(nstart,nend+1):
  if all(hits[n-nstart:n-nstart+33]):
   onset=n;break
 cert=None
 if onset is not None:
  cert={"n0":onset,"L":L,"window_size":33,"orbit_count":85,
        "checks":2805,"all_pass":True,"per_time_pass":hits[onset-nstart:onset-nstart+33],
        "modulus_exponent":maxexp}
 return {"h":h,"period_candidate":L,"scanned_n":[nstart,nend],
  "earliest_33_consecutive_pass":onset,
  "previous_fails":None if onset is None or onset==nstart else (not hits[onset-1-nstart]),
  "preperiod_witness":witnesses.get(onset-1) if onset is not None else None,
  "hits_nstart_to_nend":hits[:nend-nstart+1],
  "origin_hits_nstart_to_nend":origin,"certificate":cert}

def full_direct_check(vs):
 q=Q
 F=[0]*729;F[0]=1
 def index(t):return t[0]*81+t[1]*9+t[2]
 ed=[[index(((x+dx)%q,(y+dy)%q,(z+dz)%q)) for x in range(q) for y in range(q) for z in range(q)] for dx,dy,dz in STEPS]
 v=vs[0]
 for n in range(56):
  shift=(n*CENTER)%q
  for x in range(q):
   for y in range(q):
    for z in range(q):
     centered=((x-shift)%q,(shift-y)%q,(z-shift)%q)
     assert F[index((x,y,z))]==v[RID[canon(centered)]],(n,(x,y,z))
  if n==55:break
  ff=[0]*729
  for edge in ed:
   for i,x in enumerate(F):ff[edge[i]]+=x
  F=ff
  v=next_orbit(v)
 return 56*729

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--h',type=int,nargs='+',default=[7,8,9])
 ap.add_argument('--scan-end',type=int,default=42)
 ap.add_argument('--output')
 args=ap.parse_args()
 vs=base_vectors()
 divisor_checks=verify_coeff_bounds()
 direct=full_direct_check(vs)
 for n in range(1,42):
  mod=3**40
  v=fast_orbit_at(n,mod,vs)
  assert v==[x%mod for x in vs[n]],('fast_poly_not_equal_direct_orbit',n)
 evidence={"schema":"EM_R762FJ_MOVING_FRAME_PERIOD_CERTIFICATE_V1",
   "arithmetic":"unbounded exact Python integers; reduced modulo exact powers of three",
   "q":9,"branches":list(STEPS),"orbit_count":85,
   "Q_coefficients_ascending":list(QPOLY),"checked_identity":"Q(C) h_1 = 0 over exact integers, 85 entries",
   "direct_terminal_comparisons":direct,"recurrence_coefficient_valuation_bounds":divisor_checks,
   "initial_integrality_window":[9,41],"results":[],
   "scientific_scope":"full 729 positive-BRC terminal counts, not signed X6 Cell/Link/Port"}
 for h in args.h:
  ans=first_onset(h,vs,nend=args.scan_end)
  onset=ans['earliest_33_consecutive_pass']
  if onset is not None:
   assert ans['certificate']['all_pass']
   assert ans['preperiod_witness'] is not None and ans['previous_fails']
  if h==9 and onset is not None:
   ans['proper_divisor_witness']=witness(h,onset+1,ans['period_candidate']//3,vs)
   assert not ans['proper_divisor_witness']['equal']
  evidence['results'].append(ans)
  print("h",h,"L",ans['period_candidate'],"first",onset,
        "previous_fail",ans['previous_fails'],"cert",ans.get('certificate',{}).get('all_pass'),flush=True)
 if args.output:
  with open(args.output,'w',encoding='utf-8') as fh:json.dump(evidence,fh,indent=2,ensure_ascii=False)
 return evidence

if __name__=='__main__':main()
