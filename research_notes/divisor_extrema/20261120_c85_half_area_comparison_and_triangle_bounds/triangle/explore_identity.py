from math import gcd
from itertools import combinations

def det(v,w): return v[0]*w[1]-v[1]*w[0]
def calc(pts,src):
 s={(x-src[0],y-src[1]) for x,y in pts if gcd(abs(x-src[0]),abs(y-src[1]))==1}
 D=len({min(v,(-v[0],-v[1])) for v in s})
 B=sum(abs(det(v,w))==1 for v,w in combinations(s,2))
 C=sum(det(v,w)==1 and(-v[0],-v[1])in s for v in s for w in s)
 P=sum(abs(det(v,w))==1 and(v[0]+w[0],v[1]+w[1])in s for v,w in combinations(s,2))
 T=sum(det(v,w)==1 and(-v[0]-w[0],-v[1]-w[1])in s for v in s for w in s)//3
 Q=sum(det(v,w)==1 and(-v[0],-v[1])in s and(2*w[0]-v[0],2*w[1]-v[1])in s for v in s for w in s)
 return D,B,C,P,T,Q,1-D+B-C-P-T+Q

def inside(poly,p):
 vals=[det((b[0]-a[0],b[1]-a[1]),(p[0]-a[0],p[1]-a[1]))for a,b in zip(poly,poly[1:]+poly[:1])]
 return min(vals)>=0 or max(vals)<=0

def checktri(N):
 bad=[];cs=0
 for n in range(1,N+1):
  for d in range(1,n+1):
   if n%d:continue
   h=n//d
   for r in range(h):
    pts=[(x,y)for x in range(max(d,r)+1)for y in range(h+1)if 0<=x*h-r*y and x*h-r*y+d*y<=d*h]
    for src in pts:
     cs+=1;c=calc(pts,src)
     if c[-1]!=0:bad.append((d,r,h,src,c))
 return cs,bad

def checkquad(N):
 bad=[];cs=0;polys=[]
 for n in range(2,N+1):
  for k in range(1,n+1):
   if n%k:continue
   for h in range(1,n//k):
    j=n//k-h
    for a in range(h):
     for b in range(-j-2,k*(h+j)+2):
      if not 0<j*a+h*b<k*(h+j):continue
      poly=[(0,0),(a,h),(k,0),(b,-j)]
      points=[(x,y)for x in range(min(p[0]for p in poly),max(p[0]for p in poly)+1)for y in range(-j,h+1)if inside(poly,(x,y))]
      polys.append(poly)
      for src in points:
       cs+=1;c=calc(points,src)
       if c[-1]!=0:bad.append((poly,src,c))
 return len(polys),cs,bad

if __name__=='__main__':
 for N in range(4,8):
  cs,bad=checktri(N)
  print('tri',N,cs,len(bad),bad[:3])
  pc,cs,bad=checkquad(N)
  print('quad',N,pc,cs,len(bad),bad[:5])
