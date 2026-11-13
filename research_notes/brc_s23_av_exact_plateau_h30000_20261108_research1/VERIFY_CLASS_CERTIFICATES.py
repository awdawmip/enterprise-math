#!/usr/bin/env python3
"""Certify a full triangle stream's class count, exact log bounds, and witnesses."""
from fractions import Fraction
from hashlib import sha256
from math import gcd
import csv,sys
Q=10**26
LO=545569623581288298975349314
HI=LO+1
P,D=2074774,380295
N=2455069

def atanh(z,terms=45):
 s=Fraction(0);term=z
 for i in range(terms):
  s+=2*term/(2*i+1);term*=z*z
 return s,s+2*term/((2*terms+1)*(1-z*z))

def exact_bounds(H):
 l2,u2=atanh(Fraction(1,3));l9,u9=atanh(Fraction(1,9));l15,u15=atanh(Fraction(1,15))
 a,b=3*l2-u15,3*u2-l15
 c,d=l9+l15,u9+u15
 assert Fraction(LO,Q)<a/d and b/c<Fraction(HI,Q)
 assert gcd(P,D)==1 and 1<=H<D
 assert H*max(abs(LO*D-P*Q),abs(HI*D-P*Q))<Q

def valid(K,L,dv,dj,V,J,S):
 return K>=J and L>=V and K+L<=N+S and K*Q>HI*L and (K+dj)*Q<LO*(L+dv)

def check(path):
 with open(path,newline='') as f:data=list(csv.reader(f))
 kind,H,M,C=data[0];H,M,C=map(int,(H,M,C))
 assert kind=="SUMMARY" and M==(H+1)*(H+2)//2 and C==len(data)-1
 exact_bounds(H)
 print("PASS_EXACT_LOG_ENCLOSURE_AND_ORDER_KEY",H,flush=True)
 rows=[];classes=set();total=0;unresolved=[]
 for fields in data[1:]:
  assert fields[0]=="CLASS" and len(fields)==7
  dv,dj,V,J,S,num=map(int,fields[1:]);total+=num
  assert (dv,dj) not in classes;classes.add((dv,dj))
  assert 0<=V<=H and 0<=J<=H and 0<=S<=H and num>=1
  assert abs(dv)<=H and abs(dj)<=H
  assert (LO if dv>0 else HI)*dv>Q*dj
  if (dv,dj)==(79,431):
   K,L=2074774,380295
   assert valid(K,L,dv,dj,V,J,S)
  else:
   for L in range(V,V+100000):
    K=max(LO*L//Q+1,J)
    if valid(K,L,dv,dj,V,J,S):break
   else:
    unresolved.append((dv,dj,V,J,S,num));continue
  rows.append((dv,dj,V,J,S,num,K,L,K+L-S))
  print("CLASS",*rows[-1],flush=True)
 assert total==M-1
 ell=H*Q//LO+1;k=HI*H//Q+1
 assert LO*ell>H*Q and k*Q>HI*H and ell<=N and k<=N
 print("PASS_EXTERIOR",ell,k,flush=True)
 print("UNRESOLVED",unresolved,flush=True)
 if not unresolved:
  assert len(rows)==C and max(row[-1] for row in rows)<=N
  digest=sha256("\n".join(",".join(map(str,row)) for row in rows).encode()).hexdigest()
  print("CLASS_DATA_SHA256",digest,flush=True)
  print("PASS_S23_AV_STREAM_GAP_CLASS_ENDPOINT",H,N,"M",M,"C",C,flush=True)

if __name__=="__main__":check(sys.argv[1])
