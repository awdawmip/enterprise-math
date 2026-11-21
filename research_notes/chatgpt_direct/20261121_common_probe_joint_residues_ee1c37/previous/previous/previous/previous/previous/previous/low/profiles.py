from collections import Counter
from functools import cache
mn = dict(enumerate((0,0,12,36,72,120,201,292,419,557,744,936,1104,1296)))
def get(k,v):
 caps={}
 def walk(left,free,high,prof):
  if not left:
   if free:return
   s=prof.count(13)
   if k==11 and (s>=3 or s>=2 and v<10986):return
   if s>6:return
   fixed=sum(mn[i]for i in prof)
   for j in set(prof):
    use=sum(z>=12 for z in prof)-(j==12)
    rest=fixed-mn[j]+12*max(0,use-6)
    if v-rest>=mn[j]:caps[j]=max(v-rest,caps.get(j,0))
   return
  for s in range((free+left-1)//left,min(free-left+1,high)+1):
   walk(left-1,free-s,s,prof+(s,))
 walk(k,125,13,())
 return caps
def make_profiles(k, budget, below, minimum, keys):
 @cache
 def size_tails(n,l,maxs):
  if not l:return [()] if not n else []
  return [(s,)+z for s in range((n+l-1)//l,min(n-l+1,maxs)+1) for z in size_tails(n-s,l-1,s)]
 out=[]
 for prof in size_tails(125,k,13):
  s=prof.count(13)
  if s>6 or k==11 and (s>=3 or s==2 and budget<10986):continue
  types=list(Counter(prof).items())
  def recurse(i,cnts,cost):
   if cost>budget:return
   if i==len(types):
    if cost<below:return
    num=Counter(cnts);big=s;large=sum(v for (l,c),v in num.items() if l>=12 and (l==13 or c in (1104,1116)))
    punct=num[(12,1116)];cheap=num[(12,1104)]+big
    if cheap>6 or large>=8 or large==7 and (big>1 or punct<5+big):return
    out.append((cost,[num[key]for key in keys]))
    return
   size,q=types[i];opts=[c for x,c in keys if x==size]
   extra=budget-cost
   def choose(n,j,remain,prices):
    if n==0:
     recurse(i+1,cnts+[(size,c) for c in prices],cost+extra-remain)
     return
    for h in range(j,len(opts)):
     d=opts[h]-minimum[size]
     if n*d>remain:break
     choose(n-1,h,remain-d,prices+[opts[h]])
   choose(q,0,extra,[])
  recurse(0,[],sum(minimum[s] for s in prof))
 return sorted(out)

