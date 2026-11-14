#!/usr/bin/env python3
"""R5 delta=1/4 finite rational face-lattice and behavioral adjacency proof.
Usage: python VERIFY.py ../brc_r5_kernel_perturbation_phase_diagram_20261106_t0047/H_FACETS.txt
"""
import sys
from collections import Counter,deque
from itertools import product
from fractions import Fraction as F
S=720000
q2=(F(1,2),F(1,2));r2=(F(3,4),F(5,4))
q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
r3=(F(1,2),F(1),F(3,2));r4=(F(1,10),F(1),F(19,10))
q4={(i,0):(F(509,900),F(382,900),F(9,900)) for i in range(2)}
q4.update({(i,2):(F(9,900),F(382,900),F(509,900)) for i in range(2)})
q4[0,1]=(F(47,180),F(43,90),F(47,180))
q4[1,1]=(F(67,162),F(14,81),F(67,162))
assert all(v>0 for row in (*q3,*q4.values()) for v in row)
assert all(sum(row)==1 for row in (*q3,*q4.values()))
for i in range(2):
 assert sum(q3[i][j]*r3[j] for j in range(3))==r2[i]
 for j in range(3):assert sum(q4[i,j][k]*r4[k] for k in range(3))==r3[j]
assert sum(q2[i]*r2[i] for i in range(2))==1
profiles=[];observations=[]
for a in product(range(3),repeat=6):
 for b in product(range(2),repeat=3):
  w=[F(0)]*4
  def stop(t,r,m,choice):
   if choice==0:w[0]+=m*r
   else:w[1]+=m
   w[2]+=t*m*r;w[3]+=t*m
  if a[0]!=2:stop(1,F(1),F(1),a[0])
  else:
   for i in range(2):
    if a[1+i]!=2:stop(2,r2[i],q2[i],a[1+i])
    else:
     for j in range(3):
      m=q2[i]*q3[i][j]
      if a[3+j]!=2:stop(3,r3[j],m,a[3+j])
      else:
       for k in range(3):stop(4,r4[k],m*q4[i,j][k],b[k])
  assert all((x*S).denominator==1 for x in w)
  observations.append(tuple(int(x*S) for x in w))
  profiles.append(a+b)
assert len(profiles)==5832 and len(set(observations))==806
rows=[tuple(map(int,line.split())) for line in open(sys.argv[1],encoding="utf8") if line.strip()]
assert len(rows)==80 and all(len(row)==5 for row in rows)
facet_masks=[]
for n0,n1,n2,n3,c in rows:
 mask=0
 for k,w in enumerate(observations):
  v=n0*w[0]+n1*w[1]+n2*w[2]+n3*w[3]
  assert v<=c
  if v==c:mask|=1<<k
 assert mask
 facet_masks.append(mask)
full=(1<<len(profiles))-1
masks={full};todo=deque([full])
while todo:
 cur=todo.popleft()
 for f in facet_masks:
  nxt=cur&f
  if nxt and nxt not in masks:masks.add(nxt);todo.append(nxt)
assert len(masks)==619
index={p:k for k,p in enumerate(profiles)}
neighbors=[]
for p in profiles:
 a=[]
 for i in range(9):
  for x in range(3 if i<6 else 2):
   if x!=p[i]:a.append(index[p[:i]+(x,)+p[i+1:]])
 neighbors.append(a)
def indices(mask):
 while mask:
  low=mask&-mask
  yield low.bit_length()-1
  mask-=low
def rank(rows):
 basis={}
 for row in rows:
  x=[F(v) for v in row]
  for j in sorted(basis):
   if x[j]:
    t=x[j];x=[u-t*v for u,v in zip(x,basis[j])]
  for j,v in enumerate(x):
   if v:basis[j]=[z/v for z in x];break
  if len(basis)==4:break
 return len(basis)
def dim(points):
 origin=points[0]
 return rank([tuple(p[j]-origin[j] for j in range(4)) for p in points[1:]])
def independent(u,v):
 return any(u[i]*v[j]!=u[j]*v[i] for i in range(4) for j in range(i+1,4))
def find_box(ids):
 members=set(ids)
 for ix in ids:
  p=profiles[ix];w=observations[ix];adj=[]
  for i in range(9):
   choices=[]
   for act in range(3 if i<6 else 2):
    if act==p[i]:continue
    j=index[p[:i]+(act,)+p[i+1:]]
    if j in members:
     choices.append((i,act,tuple(observations[j][h]-w[h] for h in range(4))))
   for a in range(len(choices)):
    for b in range(a+1,len(choices)):
     if independent(choices[a][2],choices[b][2]):return "triangle"
   adj.extend(choices)
  for a in range(len(adj)):
   i,act,u=adj[a]
   for b in range(a+1,len(adj)):
    j,actj,v=adj[b]
    if i==j or not independent(u,v):continue
    q=list(p);q[i]=act;q[j]=actj
    if index[tuple(q)] in members:return "rectangle"
 return None
counts=Counter();boxes=Counter();disconnected=0;incidences=0
for face in masks:
 ids=list(indices(face));incidences+=len(ids)
 pts=list({observations[i] for i in ids})
 d=dim(pts);counts[d]+=1
 if d==2:
  box=find_box(ids)
  assert box is not None
  boxes[box]+=1
 unseen=set(ids);start=unseen.pop();stack=[start]
 while stack:
  i=stack.pop()
  for j in neighbors[i]:
   if j in unseen:unseen.remove(j);stack.append(j)
 if unseen:disconnected+=1
assert disconnected==0
weak=[]
for i,face in enumerate(facet_masks):
 d=dim(list({observations[j] for j in indices(face)}))
 if d<3:weak.append((i+1,d))
assert weak==[(33,2),(34,2),(38,1),(40,1),(41,2),(43,2),(47,2),(48,2)]
assert [counts[d] for d in range(5)]==[82,237,227,72,1]
assert sum(boxes.values())==227 and counts[0]-counts[1]+counts[2]-counts[3]==0
print("PASS_EXACT_R5_ALL_619_FACES_ONE_KEY_CONNECTED")
print("P_Q_positive_martingale=PASS deterministic_LR_profiles=5832 distinct_observations=806")
print("halfspaces=80 actual_facets=72 nonempty_faces=619 face_vector_dim_0_to_4=82,237,227,72,1")
print("face_optimal_one_key_graph_disconnected=0; all_237_edges_behaviorally_saturated=PROVED")
print("total_optimal_policy_incidence=",incidences)
print("2faces_with_rank2_behavior_patch=",sum(boxes.values()),"patch_types=",sorted(boxes.items()))
print("supporting_inequalities_codimension_gt_1=",weak)
