"""Port the prior maximum-class result to a full constructive covering. Standard library only."""
import argparse,json
from itertools import product
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
HERE=Path(__file__).resolve().parent
# The coordinate permutation of leaves is immaterial; rows are ordinary old histories.
data={
6:([4,4,4,0,2,2],[4,0,3,2,1,2],4,(4,0)),
7:([0,4,0,1,4,0,0],[1,1,3,3,4,2,4],4,(2,2)),
8:([0,1,3,0,1,4,1,4],[4,0,2,2,4,0,3,1],4,(1,4))}
def witness(n):
 if n==8:return [tuple(next((i for i in range(3) if t[i]!=p[i]),3+t[3])for p in product(range(2),repeat=3))for t in product(range(2),repeat=4)]
 return EXPLICIT[n]
EXPLICIT={
6 : [(0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 2), (0, 0, 0, 0, 1, 3), (0, 0, 0, 0, 2, 3), (0, 0, 0, 0, 3, 3), (1, 1, 1, 1, 4, 4), (1, 1, 1, 2, 4, 4), (1, 1, 2, 3, 4, 4), (1, 1, 3, 3, 4, 4), (2, 2, 4, 4, 4, 4), (2, 3, 4, 4, 4, 4), (3, 4, 4, 4, 4, 4), (4, 4, 4, 4, 4, 4)] ,
7 : [(0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 2), (0, 0, 0, 0, 1, 1, 3), (0, 0, 0, 0, 1, 2, 3), (0, 0, 0, 0, 2, 3, 3), (0, 0, 0, 0, 3, 3, 3), (1, 1, 1, 1, 4, 4, 4), (1, 1, 1, 2, 4, 4, 4), (1, 1, 2, 3, 4, 4, 4), (1, 1, 3, 3, 4, 4, 4), (2, 2, 4, 4, 4, 4, 4), (2, 3, 4, 4, 4, 4, 4), (3, 4, 4, 4, 4, 4, 4), (4, 4, 4, 4, 4, 4, 4)] ,
}
def syndrome(w,rs):return tuple(sum(x*y for x,y in zip(r,w))%5 for r in rs)
def ok(W):
 b=[{i for i,w in enumerate(W) if w[j]==v}for j in range(len(W[0]))for v in range(5)]
 return all(not u&v or u<=v or v<=u for u in b for v in b)
def cap(n):return [1,5,8,10,12,13,14,15][n] if n<8 else 16
def block(d):
 a,b,c,t=data[d];rs=(a,b);W=witness(d);assert ok(W);idx={syndrome(x,rs):x for x in W};assert len(idx)==cap(d)==len(W)
 h=next(x for x in product(range(5),repeat=d)if syndrome(x,rs)==t)
 W2=[tuple((c*y+x)%5 for x,y in zip(h,w))for w in W];left={syndrome(x,rs):x for x in W2 if syndrome(x,rs) not in idx};assert ok(list(left.values()))
 look=dict(idx,**{});look.update(left);assert len(look)==25 and len(left)==25-len(W)
 # Every full block old input is actually encoded and checked: key=(which type,k in kernel), code representative w.
 groups={};ct=0
 for v in product(range(5),repeat=d):
  s=syndrome(v,rs);rep=look[s];dif=tuple((x-y)%5 for x,y in zip(v,rep));key=(s in idx,dif)
  groups[key]=groups.get(key,0)+1;ct+=1
 assert len(groups)==2*5**(d-2) and all(x==(len(W) if a else len(left)) for (a,k),x in groups.items())
 return dict(width=d,checked_histories=ct,linear_rows=[a,b],large_class_size=len(W),complement_class_size=len(left),classes_per_type=5**(d-2),shift=list(t),multiplier=c,large_witness=W,small_witness=list(left.values()))
def count(nmax,extra):
 U=[1];rows=[]
 for n in range(1,nmax+1):
  h=5**n;t=[5*U[-1],h//5]
  if n>=2:t+=[4*(h//25)]
  if n>=3:t+=[13*(h//125)]
  if n==5:t.append(250)
  for d in data:
   if n==d:t.append(2*5**(n-2))
   if n>=d:t+=[h//25+(25-cap(d))*5**(d-2)*U[n-d]]
  if extra and n>=8:t.append(extra*5**(n-3))
  u=min(t);U.append(u);lo=(h+cap(n)-1)//cap(n)
  if n<=32:rows.append(dict(n=n,upper=u,lower=lo,guaranteed_fixed_saving=(h-1).bit_length()-(u-1).bit_length(),max_possible_fixed_saving=(h-1).bit_length()-(lo-1).bit_length()))
 return U, rows
def logbounds(m,T=180):
 x=Q(m-1,m+1);s=sum((2*x**(2*i+1)/(2*i+1)for i in range(T)),Q())
 return s,s+2*x**(2*T+1)/((2*T+1)*(1-x*x))
def lead():
 # Rational separation, no floating point and no evaluation of enormous 5^n.
 p,q=3257603715218890894709,1402973555637569621645
 nmax=10**20;l,u=logbounds(5);c,d=logbounds(2)
 e=max(abs(Q(p,q)-l/d),abs(Q(p,q)-u/c));assert gcd(p,q)==1 and nmax<q and 2*q*nmax*e<1
 # for all n>=512, the raw upper multiplier-1 is < relative integer power gap.
 assert 15*Q(9,25)**64 < c/(2*q)
 assert 2**33<10**10 and nmax//8-1-3>10**10*63 and nmax>8*10**10
 return dict(matveev_doi='10.1070/IM2000v064n06ABEH000314',matveev_large_n_check={'start':10**20,'relaxed_constant':10**10,'corollary':'2.3 directly in primary original, pp. 1218–1219','conclusion':'applies to the whole tail n>=10^20'},nmax=nmax,nmin=512,p=p,q=q,atanh_positive_term_count=180,details='alpha=log_2 5 within 1/(2 q nmax) of reduced p/q; each n<q has dist(np/q,Z)>=1/q')
def run():
 bs=[block(d) for d in data]
 f=HERE/'quotient125.json';extra=len(json.loads(f.read_text())['classes']) if f.exists() else None
 extra8=verify_family(json.loads(f.read_text()),8,3);assert extra8['quotient_points']==125
 # two templates in a plane give a full 5D partition with at most 250 messages.
 extra5=verify_family(json.loads((HERE/'quotient5d.json').read_text()),5,2);assert extra5['quotient_points']==25
 u,rows=count(511,extra);no4=[n for n in range(1,512) if (5**n-1).bit_length()-(u[n]-1).bit_length()<4]
 return dict(status='PASS',projection_5d=extra5,projection_8d_125=extra8,blocks=bs,optional_125_syndrome_classes=extra,elementary_large_interval=lead(),all_n_four_bits_from=1+max(no4),certified_from=1+max(no4),small_widths_where_construction_does_not_yet_show_four=no4,small_ranges=rows,last_block_classes='(Q-L)/16 very large classes; optionally handle complement by smaller-seed U of remaining n or a second class inside last block',asymptotic='5^n/16 <= M_n <= (5^n/16)[1+15(9/25)^floor(n/8)]; therefore 16 M_n/5^n -> 1')
def verify_family(record,n,rank):
 mat=record['projection_rows'];groups=record['classes'];touched=set();W=record['witness'] if 'witness'in record else witness(n);sp=5**(n-rank);tot=0;counts=[];assert ok(W)
 assert len({syndrome(x,mat)for x in product(range(5),repeat=n)if sum(bool(a) for a in x)<=rank})==5**rank
 for row in groups:
  tr=row['shift'];per=row['permutations'];assert all(sorted(pp)==list(range(5))for pp in per)
  sw=[tuple(per[j][val] for j,val in enumerate(w))for w in W];assert ok(sw);syms=[tuple((s+u)%5 for u,s in zip(syndrome(w,mat),tr))for w in sw];fresh=set(syms)-touched;touched.update(fresh);tot+=sp*len(fresh);counts.append(len(fresh))
 assert len(touched)==5**rank and tot==5**n;return dict(quotient_points=len(touched),assigned_class_sizes=counts,histories=tot)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=HERE/'block_lift_results.json');a=p.parse_args();res=run();a.out.write_text(json.dumps(res,indent=2)+'\n');print('PASS',res['certified_from'],res['small_widths_where_construction_does_not_yet_show_four'])
