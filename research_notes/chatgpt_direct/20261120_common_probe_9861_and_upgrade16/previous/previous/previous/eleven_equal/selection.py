from collections import Counter
from functools import cache
from itertools import combinations

def select(p,g):
    eye=0;idx={}
    for i in range(125):
     if i in idx:continue
     o=[];j=i
     while j not in o:o.append(j);j=g[j]
     index=len(set(idx.values()));idx.update(dict.fromkeys(o,index));
     if len(o)==1:eye|=1<<index
    fix=[]
    for line in (p/'trifix0').read_text().splitlines():
     q,c=map(int,line.split());d=(q&eye).bit_count();s=3*q.bit_count()-2*d;fix.append((q,c,s,d))
    caps={9:557,10:744,11:936,12:1104}
    @cache
    def remdp(n,k):
     if k==0:return 0 if n==0 else 10**8
     return min((3*c+remdp(n-3*s,k-1)for s,c in caps.items()if 3*s<=n),default=10**8)
    cnt=Counter(); q2={}
    for (a,ca,sa,da),(b,cb,sb,db)in combinations(fix,2):
     if a&b or da+db!=5 or ca+cb+remdp(125-sa-sb,3)>11292:continue
     u=a|b;cnt[sa+sb]+=1;q2[u]=min(q2.get(u,(10000000,)),(ca+cb,a,b))
    with (p/'tritask').open('w')as f:
     for u,(c,a,b)in q2.items():print(u,c,a,b,file=f)
    return len(q2),sum(cnt.values())

def reduce(P,g,lin,tr):
    lines=[];ix={}
    for i in range(125):
     if i in ix:continue
     w=[];j=i
     while j not in w:w.append(j);j=g[j]
     ix.update(dict.fromkeys(w,len(lines)));lines.append(w)
    qs={u:(c,a,b)for u,c,a,b in(map(int,l.split())for l in (P/'tritask').read_text().splitlines())};red=[]
    ms=set()
    for l in lin:
     for t in tr:
      if len({ix[t[l[i]]]for i in lines[1]})>1:continue
      f=[ix[t[l[z[0]]]]for z in lines];
      if len(set(f))==45 and all(len({ix[t[l[i]]]for i in z})==1 for z in lines):ms.add(bytes(f))
    while qs:
     u=min(qs);c,a,b=qs[u];red.append((u,c,a,b));terms=[i for i in range(45)if u>>i&1]
     for y in {sum(1<<m[i]for i in terms)for m in ms}:assert qs.pop(y)[0]==c
    (P/'trireps').write_text(''.join(' '.join(map(str,j))+'\n'for j in red));return len(ms),len(red)
