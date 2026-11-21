#!/usr/bin/env python3
"""R284DT: exact seven-window affine observer for frozen Port minimum-gap pairs."""
from itertools import product
from collections import Counter
import hashlib, json
from pathlib import Path

P=17179869143
D=(1120832,6,13,1651128)
Z=(0,390139,394465,1497639)
SELECT=(0,1,2,4,5,6)
FROZEN_SHA='b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4'
PAIR_SHA='7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a'
WINDOWS=(
 (32,4615469395,4673631799,-1,12686611854,5263582),
 (56,4676964764,4781786875,1,3334084674,1402348),
 (44,8340968948,8431780928,-1,16684966842,6212980),
 (63,8436287924,8507286428,1,-184807994,2801012),
 (21,14652558810,14761366612,-1,22929044144,1094375),
 (45,14761932474,14818876290,1,-6594783455,37349),
 (55,15722869762,15886415284,1,-7634296129,32564673),
)

def det(L,top):
 u1,a,x,y,u2,w,b,z,u3,g,h,r=L
 t,s=6-a,13-b;u=t*s-x*w
 v=-r*u-z*(t*h+x*g)-y*(w*h+s*g)
 p1,p2=s*u1+x*u2,t*u2+w*u1
 q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
 q2=-r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
 q3=u*u3+p1*g+p2*h
 k=(u*D[3]+v,p1*D[3]+q1,p2*D[3]+q2,q3)
 base=D[0]*k[0]-Z[1]*k[1]-Z[2]*k[2]-Z[3]*k[3]-sum(k)
 return base-sum(k[j] for j in range(4) if top&(1<<j))

def lower(low):return [1+((low>>(11-j))&1) for j in range(12)]
def residue(i):
 upper=i>>12
 top=sum(((upper>>(3-j))&1)<<j for j in range(4))
 return det(lower(i&4095),top)%P

def q3(low):
 u1,a,x,y,u2,w,b,z,u3,g,h,r=lower(low)
 t,s=6-a,13-b
 return (t*s-x*w)*u3+(s*u1+x*u2)*g+(t*u2+w*u1)*h

def arcs():
 ans=[]
 for key in range(64):
  lo=[1]*12;hi=[2]*12
  for j,pos in enumerate(SELECT):lo[pos]=hi[pos]=1+((key>>(5-j))&1)
  h=det(hi,15)
  ans.append((h%P,det(lo,0)-h))
 return ans

def dist(x,arc):
 a,w=arc;d=(x-a)%P
 return 0 if d<=w else min(d-w,P-d)

def event_times(A):
 times={0,P}
 for a,w in A:
  for k in (-1,0):
   b=a+w+k*P;e=a+(k+1)*P;mid=(b+e)//2
   for lo,hi in ((b,mid+1),(mid+1,e+1)):
    lo=max(0,lo);hi=min(P,hi)
    if lo<hi:times.add(lo);times.add(hi)
 return sorted(times)

def fast_observe(x):
 for label,lo,hi,s,c,_ in WINDOWS:
  if lo<=x<=hi:return s*x+c,label
 raise ValueError('outside certified candidate window')

def verify():
 A=arcs();assert len(A)==64 and all(0<w<P for _,w in A)
 times=event_times(A);assert len(times)==194
 vertices=0;all_margins={}
 for label,lo,hi,s,c,claimed_margin in WINDOWS:
  checks={lo,hi}
  for t in times:
   if lo<t<=hi:checks.update((t-1,t))
  margins=[]
  for x in sorted(checks):
   ds=[dist(x,a) for a in A]
   assert s*x+c==ds[label]==max(ds)
   margins.append(ds[label]-max(v for j,v in enumerate(ds) if j!=label))
  assert min(margins)==claimed_margin and claimed_margin>0
  all_margins[str(label)]={'tested_vertices':len(checks),'minimum_margin':min(margins)}
  vertices+=len(checks)
 digest=hashlib.sha256()
 for upper in product((1,2),repeat=4):
  top=sum((v-1)<<j for j,v in enumerate(upper))
  for lo in product((1,2),repeat=12):
   digest.update((det(lo,top)%P).to_bytes(8,'big'))
 assert digest.hexdigest()==FROZEN_SHA
 pairs=set();labels=Counter();patterns=Counter();sites=set()
 skeletons=sorted(1056+(x<<9)+(y<<8)+(z<<4) for x,y,z in product((0,1),repeat=3))
 assert skeletons==[1056,1072,1312,1328,1568,1584,1824,1840]
 for low in skeletons:
  for upper in range(0,16,2):
   root=(upper<<12)|low;gaps=[]
   for shift in (0,1,64,65):
    i=root^shift;j=i^4096
    x=residue(i);delta=q3(i&4095);y=(x-delta)%P
    d0,l0=fast_observe(x);d1,l1=fast_observe(y)
    assert l0==l1 and abs(d0-d1)==delta and delta in (59,60)
    assert (residue(j)-x)%P==(-delta)%P
    assert i not in sites and j not in sites
    sites.update((i,j));pairs.add((min(i,j),max(i,j)))
    labels[l0]+=1;gaps.append(delta)
   assert max(gaps)==60
   patterns[tuple(gaps)]+=1
 assert len(pairs)==256 and len(sites)==512
 assert labels==Counter({21:45,32:21,44:37,45:19,55:64,56:43,63:27})
 assert patterns==Counter({(60,60,60,60):32,(60,60,59,59):32})
 sha=hashlib.sha256(b''.join(i.to_bytes(2,'big')+j.to_bytes(2,'big') for i,j in sorted(pairs))).hexdigest()
 assert sha==PAIR_SHA
 return {'schema':'R284DT_SEVEN_WINDOW_AFFINE_CERTIFICATE_V1',
  'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
  'frozen_source_commit':'acba2d8667903434aaa2a10720f43637fcc2421b',
  'frozen_source_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
  'frozen_codewords_sha256':FROZEN_SHA,'period':P,
  'arcs':len(A),'event_positions':len(times),
  'windows':[{'arc_label':l,'lo':lo,'hi':hi,'slope':s,'intercept':c,'margin':m} for l,lo,hi,s,c,m in WINDOWS],
  'proof_event_vertices_checked':vertices,'window_vertex_checks':all_margins,
  'candidate_states':len(sites),'nearest_pairs':len(pairs),'pair_sha256':sha,
  'winning_arc_label_counts':dict(sorted(labels.items())),
  'construction_arc_distance_calls':0,'construction_envelope_queries':0,
  'proof_arc_distance_calls':vertices*len(A),
  'word_digest_det_evaluations':65536,
  'dependencies':'R284DN global minimum and exhaustive pair count; R284DQ eight skeletons',
  'review':'NOT_REVIEWED'}

if __name__=='__main__':
 cert=verify()
 out=Path(__file__).with_name('R284DT_seven_window_affine_certificate.json')
 out.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 print(json.dumps(cert,indent=2,ensure_ascii=False))
