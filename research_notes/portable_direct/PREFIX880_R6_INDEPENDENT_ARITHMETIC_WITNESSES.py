#!/usr/bin/env python3
"""Independent exact modular-residue arithmetic counts and direct XOR witnesses for PREFIX-880."""
import json
from pathlib import Path
P,B,Q=32,19,(1<<19)-1
N=1<<P
ratios=[(5,2),(2,5),(7,2),(2,7),(5,4),(4,5),(7,4),(4,7)]
E=sorted({sgn*z for i in range(1,22) for z in ((1<<i)-1,(1<<i)+1) for sgn in (-1,1)})
assert len(E)==82
result=json.loads(Path(__file__).with_name("PREFIX880_R6_ODD_RATIO_RESULTS.json").read_text())
def ceildiv(a,b): return -((-a)//b)
def classify(d):
 z=abs(d)
 if z==1:return ("one",0)
 for i in range(1,22):
  if z==(1<<i)+1:return ("plus",i)
  if z==(1<<i)-1:return ("minus",i)
 raise AssertionError(z)
def witness(k,l,x,y,d):
 a,b=k*x,l*y
 assert a-b==d
 if d>0:
  kind,i=classify(d)
  if kind=="one": X=(0,1);Y=(a,a)
  elif kind=="plus":
   u=0 if a&1 else 1
   X=(u,u+(1<<i));Y=(u+a,u+a-1)
  else:
   u=a&1
   X=(u,u+(1<<i));Y=(u+a,u+a+1)
 else:
  XX,YY=witness(l,k,y,x,-d)
  X=(XX[1],XX[0]);Y=(YY[1],YY[0])
 for u,v in (X,Y):
  assert 0<=u<N and 0<=v<N
  assert u==v or ((u^v)&((u^v)-1))==0
 assert X!=Y and X[0]%x==Y[0]%x and X[1]%y==Y[1]%y
 return X,Y
counts=[];checks=0;examples=[]
for k,l in ratios:
 total=0
 for d in E:
  lo=max(1,ceildiv(d+l,k))
  hi=min(Q,(d+l*Q)//k)
  if lo>hi:continue
  if k%2:
   mod=2*l;residue=pow(k,-1,mod)*(d+l)%mod
  else:
   mod=2*l;r=pow(k,-1,l)*d%l
   residue=r if r%2 else r+l
  first=lo+(residue-lo)%mod
  if first>hi:continue
  cnt=(hi-first)//mod+1
  diagonal=d//(k-l) if d%(k-l)==0 else None
  diag=int(diagonal is not None and 1<=diagonal<=Q and diagonal%2 and lo<=diagonal<=hi and (diagonal-residue)%mod==0)
  total+=cnt-diag
  if cnt>diag:
   x=first+mod if diagonal==first else first
   assert x<=hi
   y=(k*x-d)//l
   assert 1<=x<=Q and 1<=y<=Q and (x&1) and (y&1) and x!=y
   W=witness(k,l,x,y,d)
   checks+=1
   if len(examples)<16:examples.append({"slope":f"{k}:{l}","q1":x,"q2":y,"gap":d,"transitions":[list(W[0]),list(W[1])]})
 counts.append(total)
assert counts==[v["total"] for v in result["slope_families"]]
output={"schema":"PREFIX880_INDEPENDENT_CHECK_V1","arithmetical_total_counts":counts,"xor_witness_count":checks,"checked_all_accessible_odd_gaps":True,"examples":examples}
Path(__file__).with_name("PREFIX880_R6_INDEPENDENT_RESULTS.json").write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({k:v for k,v in output.items() if k!="examples"}))
