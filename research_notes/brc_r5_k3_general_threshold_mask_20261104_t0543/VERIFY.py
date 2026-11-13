from fractions import Fraction as F
from itertools import product
S=('C','I','BJ','IJ')
c=(F(1,8),F(1,6),F(1,16),F(3,32))
M=[set(),{'C'},{'C','I'},{'C','BJ'},set(S)]
UPF=[(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0)]
UPL=[(0,0,0),(0,1,1),(1,0,0),(1,1,0)]
count=0

def eq(x,y):
 global count
 assert x==y,(x,y)
 count+=1

def obs(up,st,r,v,p,q):
 x,y,i=map(F,up)
 d=y/16+3*i/32
 w=(F(1,8),(1-x)/6,y/16,3*i/32)
 Mv=[]; Sv=[]; Uv=[]
 for w0,j in zip(w,st):
  m=w0 if j else F(0)
  s=F(2,3)*m if j>=2 else F(0)
  u=s if j==3 else F(0)
  Mv.append(m); Sv.append(s); Uv.append(u)
 return (F(107,128)-21*x/128+d/4-sum(Sv)/2+sum(p[j]*Sv[j]/8 for j in range(4)),
         F(13,64)+3*x/64-d/2+sum(Sv)/8+sum(q[j]*Sv[j]/32 for j in range(4)),
         3+sum(Mv)+F(3,2)*sum(Sv)+sum(r[j]*Uv[j] for j in range(4)),
         3+sum(Mv)/2+F(3,8)*sum(Sv)+sum(v[j]*Uv[j]/4 for j in range(4)))

def run(label,r,v,p,q,t=F(1,3),eps=F(1,4096)):
 r,v,p,q=tuple(tuple(map(F,a)) for a in (r,v,p,q))
 mu=[(9+2*v[j])/(8*(3+r[j])) for j in range(4)]
 g=[(2+F(2,3)*r[j])*t-F(3,4)-v[j]/6 for j in range(4)]
 D={S[j] for j in range(4) if g[j]>0}
 eq(all(0<z<1 for z in r+v+p+q),True)
 eq(all(g[j]!=0 and ((g[j]>0)==(t>mu[j])) for j in range(4)),True)
 eq(0<len(D)<4,True)
 full=[obs(up,st,r,v,p,q) for up in UPF for st in product(range(4),repeat=4)]
 lr=[obs(up,(j,)*4,r,v,p,q) for up in UPL for j in range(4)]
 eq((len(full),len(lr)),(1536,16))
 norm=lambda z,n:sum(a*b for a,b in zip(z,n))
 n0=(F(0),F(0),t,F(-1))
 hf=max(norm(z,n0) for z in full)
 hl=max(norm(z,n0) for z in lr)
 eq(hf,3*t-3+sum(c[j]*max(0,g[j]) for j in range(4)))
 eq(hl,3*t-3+max(sum(c[j]*g[j] for j in range(4) if S[j] in B) for B in M))
 if D not in M:
  eq(hf>hl,True)
  return (label,''.join(sorted(D)),str(hf-hl))
 eq(hf,hl)
 H=[z for z in lr if norm(z,n0)==hl]
 eq(len(H),1)
 W=obs((0,1,1),tuple(3 if s in D else 0 for s in S),r,v,p,q)
 expect={frozenset({'C'}):(F(13,64),-F(1,8)),frozenset({'C','I'}):(F(5,128),-F(5,64)),frozenset({'C','BJ'}):(F(3,16),-F(3,32))}[frozenset(D)]
 eq(tuple(W[j]-H[0][j] for j in range(4)),expect+(F(0),F(0)))
 n=(eps,F(0),t,F(-1))
 hfn=max(norm(z,n) for z in full)
 hln=max(norm(z,n) for z in lr)
 eq(norm(H[0],n),hln)
 eq(hfn>=norm(W,n)>hln,True)
 return (label,''.join(sorted(D)),str(hfn-hln),str((norm(W,n)-hln)/sum(map(abs,n))))

if __name__=='__main__':
 p=(F(1,4),F(1,2),F(3,4),F(1,3))
 q=(F(3,4),F(1,2),F(1,4),F(2,3))
 examples=[('nonproportional_C_BJ',(F(4,5),F(1,5),F(4,5),F(1,5)),(F(2,5),F(1,8),F(1,3),F(1,10))),
           ('inaccessible_BJ',(F(1,5),F(1,5),F(4,5),F(1,5)),(F(1,10),F(1,10),F(3,10),F(1,10))),
           ('nonproportional_C_I',(F(4,5),F(7,10),F(1,5),F(3,10)),(F(2,5),F(1,3),F(1,10),F(1,5)))]
 for name,r,v in examples: print('EXAMPLE',*run(name,r,v,p,q))
 for bits in range(1,15):
  D={S[j] for j in range(4) if bits>>j&1}
  r=tuple(F(4,5) if s in D else F(1,5) for s in S)
  v=tuple(a/2 for a in r)
  run('mask'+str(bits),r,v,p,q)
 print('MASKS_EXHAUSTIVE',14,'EXACT_ASSERTIONS',count)
 print('PASS_EXACT_R5_K3_GENERAL_CLOCK_THRESHOLD_MASK_FIBER')
