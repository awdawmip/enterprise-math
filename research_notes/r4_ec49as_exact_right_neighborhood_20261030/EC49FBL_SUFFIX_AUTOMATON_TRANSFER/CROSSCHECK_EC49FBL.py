from collections import Counter
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
S=(0,0,4,1,16,32,8,2,0); A='acdefg'
R={h:({1,2,4,8} if h in (4,5,7,8) else {16,32}) for h in range(4,10)}
def candidates(h,K):
 x,y,z=K; n=[z-1,0,0,z,h+1-y-2*z,h+1-x]; r=x+y-h-1
 if min(*n,r)<0:return []
 out=[]
 for c in range(r+1):
  n[1],n[2]=c,r-c
  def go(w,s):
   if len(w)==h:
    if S[s]:out.append((w,S[s]))
    return
   for j,ch in enumerate(A):
    if n[j]:
     n[j]-=1;go(w+ch,T[s][j]);n[j]+=1
  go('',0)
 return out
CHECK=[
 ((4,3,1),(7,4,2),(4920,1440,4320)),
 ((5,2,1),(8,2,1),(194,194,194)),
 ((4,3,1),(8,2,1),(0,0,0)),
 ((4,2,1),(7,3,2),(2304,1440,2016))
]
for L,M,expect in CHECK:
 sums=[0,0,0]
 for h in (4,5,6):
  early=candidates(h,L)
  for H in (7,8,9):
   late=candidates(H,M)
   prefix=Counter((v[:h],s) for v,s in late)
   for w,s in early:
    for t in (1,2,4,8,16,32):
     n=prefix[w,t]
     sums[0]+=n
     sums[1]+=n*(s in R[h] and t in R[H])
     sums[2]+=n*(s==t)
 assert tuple(sums)==expect,(L,M,sums,expect)
 print('PASS',L,M,tuple(sums))
