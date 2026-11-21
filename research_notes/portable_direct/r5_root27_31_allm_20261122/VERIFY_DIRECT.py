"""Independent finite original-event threshold enumerator for R5 d=27,31.
Does not use the closed-form A_I generating-function kernels.
"""
import hashlib,json
from VERIFY_ALLM import (S,S4,zero,unit,add,scale,shift,mul,factor,
                         series_one,multi_div,norm,first_jet_series)
S3=set(range(223,291))
def direct_first_jet(d,m):
 p0=216 if d==27 else 217
 p4=297 if d==27 else 310
 U=multi_div(series_one(d,m),(216,217,218))
 J=multi_div(series_one(d,m),(219,220,221))
 prefix_U=[];z=zero(d)
 for row in U:z=add(z,row);prefix_U.append(z)
 J_U=[[mul(J[j],prefix_U[b]) for b in range(m)] for j in range(m)]
 derivative=zero(d)
 for mask in range(1,8):
  sup=set().union(*(S[k] for k in range(3) if mask&(1<<k)))
  P=zero(d)
  for x in (range(m) if mask&3 else (0,)):
   for y in (range(m) if mask&5 else (0,)):
    for j in (range(m) if mask&6 else (0,)):
     loads=[]
     if mask&1:loads.append(x+y)
     if mask&2:loads.append(x+j)
     if mask&4:loads.append(y+j)
     bound=m-1-max(loads)
     if bound>=0:P=add(P,shift(J_U[j][bound],214*x+215*y))
  Q=unit(d)
  for p in sorted(sup-{p0}):Q=mul(Q,factor(d,p))
  sign=1 if mask.bit_count()%2 else -1
  derivative=add(derivative,scale(mul(Q,P),-p0*sign))
 Q=unit(d)
 for p in sorted(S4-{p4}):Q=mul(Q,factor(d,p))
 H=multi_div(series_one(d,m),sorted(S4))
 prefixH=zero(d)
 for row in H:prefixH=add(prefixH,row)
 derivative=add(derivative,scale(mul(Q,prefixH),-p4))
 return norm(derivative,d)
def direct_all_31_at_m1(d):
 support=(*S,S3,S4);der=zero(d)
 for mask in range(1,32):
  sup=set().union(*(support[i] for i in range(5) if mask&(1<<i)))
  roots=[p for p in sup if p%d==0]
  if len(roots)!=1:continue
  p0=roots[0];q=unit(d)
  for p in sorted(sup-{p0}):q=mul(q,factor(d,p))
  sign=1 if mask.bit_count()%2 else -1
  der=add(der,scale(q,-p0*sign))
 return norm(der,d)
def verify():
 result={'schema':'R5_ROOT27_31_DIRECT_FINITE_MASK_CROSSCHECK_V1','independent_from':'GENERATING_FUNCTION_CLOSED_FORMS','arithmetic':'exact_integer','rows':[]}
 for d,ms in [(27,[1,2,3,5,8,9,27]),(31,[1,2,3,5,27,30,31])]:
  baseline=first_jet_series(d,max(ms))
  for m in ms:
   direct=direct_first_jet(d,m)
   assert direct==baseline[m-1],('mismatch',d,m)
   if m==1:assert direct==direct_all_31_at_m1(d)
   h=hashlib.sha256(json.dumps(direct,separators=(',',':')).encode()).hexdigest()
   result['rows'].append({'d':d,'m':m,'full_vector_sha256':h,'nonzero':any(direct),'first_coordinate':direct[0],'direct_31_masks_for_m1':m==1})
   print('PASS direct',d,m,'coefficient0',direct[0])
 return result
if __name__=='__main__':
 print(json.dumps(verify(),indent=2))
