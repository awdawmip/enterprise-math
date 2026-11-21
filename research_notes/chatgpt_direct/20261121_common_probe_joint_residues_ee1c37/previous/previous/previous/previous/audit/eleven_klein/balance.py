from functools import cache

def check(p):
 output=[]
 for i in range(7):
  masks=list(map(int,(p/f'ksz{i}').read_text().split())); target=tuple(m.bit_count()for m in masks);D={}
  for r,f in [(1,p/f'fbank{i}'),(4,p/f'qbank{i}')]+[(2,p/f'pbank{i}.{j}')for j in [1,2,3]]:
   for line in f.read_text().splitlines():
    q,c,*rest=map(int,line.split());D[q,r]=min(D.get((q,r),10**6),r*c)
  terms={}
  for (q,r),c in D.items():
   sig=(r,*((q&m).bit_count()for m in masks));terms[sig]=min(c,terms.get(sig,10**6))
  @cache
  def lb(k,x,y,z,t):
   if k==0:return 0 if not(x or y or z)else 10**6
   return min((val+lb(k-r,x-a,y-b,z-c,t-e) for (r,a,b,c),val in terms.items() if r<=k and a<=x and b<=y and c<=z and (e:=r if a+2*b+4*c==13*r else 0)<=t), default=10**6)
  bound=lb(11,*target,2);full=sum(masks);cols=[[]for j in range(full.bit_count())]
  for (q,r),c in D.items():
   a,b,d=tuple((q&m).bit_count()for m in masks);e=r if a+2*b+4*d==13*r else 0
   if e<=2 and c+lb(11-r,target[0]-a,target[1]-b,target[2]-d,2-e)<=11291:
    for j in range(len(cols)):
     if q>>j&1:cols[j].append((q,r,c,e))
  lens=sorted((len(col),j)for j,col in enumerate(cols))
  visited=[0]
  def seek(f,k,cost,t,depth):
   visited[0]+=1
   if not f:return cost if not k else 1000000
   if not k:return 1000000
   a,b,d=tuple((f&m).bit_count()for m in masks)
   if cost+lb(k,a,b,d,t)>11291:return 1000000
   best=None
   for _,j in lens:
    if not (f>>j)&1:continue
    opt=[]
    for q,r,c,e in cols[j]:
     if r>k or e>t or q&~f:continue
     u,v,w=tuple((q&m).bit_count()for m in masks)
     if cost+c+lb(k-r,a-u,b-v,d-w,t-e)<=11291:opt.append((q,r,c,e))
    if not opt:return 1000000
    if best is None or len(opt)<len(best):best=opt
   if not depth:return -1
   return min(seek(f^q,k-r,cost+c,t-e,depth-1)for q,r,c,e in best)
  visited[0]=0
  if bound>=11292:
   result=1000000;visited[0]=1;depth=0
  else:
   depth=3
   result=seek(full,11,0,2,depth)
  assert result>=1000000
  output.append(dict(signatures=len(terms),relaxed_lower=bound if bound<1000000 else None,support_checks=visited[0],search_depth_bound=depth,history_orbits=target))
 return output
