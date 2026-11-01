"""GH-146/147 short independent exact verifier; Python 3 standard library."""
from math import comb

def a(x,y,p):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def m(x,y,p):return ((x[0]*y[0]+2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def s(x,c,p):return (x[0]*c%p,x[1]*c%p)
def bar(x,p):return (x[0],-x[1]%p)
def val(h,x,p):
 z=(0,0)
 for c in h[::-1]:z=a(m(z,x,p),c if isinstance(c,tuple) else (c,0),p)
 return z

def H(p):
 n=(p-1)//2;h=[1]
 for j in range(n//2):h.append(h[-1]*(n-2*j)*(n-2*j-1)*pow(j+1,-2,p)%p)
 return h

def interp_prime(vals,z,p):
 c=vals[:];n=len(c)
 for j in range(1,n):
  u=pow(j,-1,p)
  for i in range(n-1,j-1,-1):c[i]=(c[i]-c[i-1])*u%p
 v,d=c[-1],0
 for i in range(n-2,-1,-1):d=(d*(z-i)+v)%p;v=(v*(z-i)+c[i])%p
 return v,d

def trace_and_S1(p,B,need_s1):
 L=[0]*p
 for z in range(1,p):L[z]=1 if pow(z,(p-1)//2,p)==1 else -1
 ss=0;moment=(0,0)
 for x0 in range(p):
  for x1 in range(p):
   x=(x0,x1);g=a(a(m(x,x,p),x,p),B,p);f=m(x,g,p)
   c=L[(f[0]*f[0]-2*f[1]*f[1])%p];ss+=c
   if need_s1 and c:
    norm=(g[0]*g[0]-2*g[1]*g[1])%p
    moment=a(moment,s(bar(g,p),c*pow(norm,-1,p),p),p)
 return -ss%p,moment

def small(p):
 n=(p-1)//2;h=H(p);d=len(h)-1
 B=(pow(8,-1,p),pow(12,-1,p));powers=[(1,0)]
 for _ in range(d):powers.append(m(powers[-1],B,p))
 ht=[(0,0)]*(d+1)
 for i,hi in enumerate(h):
  for j in range(i+1):ht[j]=a(ht[j],s(powers[i-j],hi*comb(i,j),p),p)
 assert all(bar(z,p)==s(z,(-1)**j,p) for j,z in enumerate(ht))
 P=[(0,0)]*(d*(p+1)+1);G=[(0,0)]*(2*d+1)
 for i,x in enumerate(ht):
  for j,y in enumerate(ht):
   z=s(m(x,y,p),1 if j%2 else -1,p)
   P[i+p*j]=a(P[i+p*j],z,p);G[i+j]=a(G[i+j],z,p)
 D=P[:]
 for i,x in enumerate(G):D[i]=a(D[i],s(x,-1,p),p)
 Q=[(0,0)]*(len(D)-p)
 for i in range(len(D)-1,p-1,-1):
  Q[i-p]=D[i];D[i]=(0,0);D[i-p+1]=a(D[i-p+1],Q[i-p],p)
 assert all(z==(0,0) for z in D[:p])
 assert Q[0]==m(ht[0],ht[1],p)
 assert all(G[j]==(0,0) for j in range(1,len(G),2))
 for t in range(p):assert val(P,(t,0),p)==val(G,(t,0),p)
 base=pow(8,-1,p);v0=pow(12,-1,p)
 traces=[trace_and_S1(p,(base,v),False)[0] for v in range(n)]
 at,deriv=interp_prime(traces,v0,p)
 S1=(0,deriv*pow(2,-1,p)%p)
 actual=trace_and_S1(p,B,True)[1]
 assert S1==actual==s(Q[0],2,p)
 assert at==m(ht[0],ht[0],p)[0]
 print('PASS_SMALL',p,'trace_samples',n,'trace_modp_at_mark',at,'line_derivative',deriv,'S1',S1)

def large():
 p=3347;n=(p-1)//2;h=H(p);base=pow(8,-1,p);v0=pow(12,-1,p)
 B=(base,v0);hh=val(h,B,p);dh=val([j*h[j]%p for j in range(1,len(h))],B,p)
 assert hh==(783,0) and dh==(0,1351)
 q=m(hh,dh,p);assert q==(0,181)
 traces=[]
 for v in range(n):
  z=val(h,(base,v),p);assert z[1]==0
  traces.append(z[0]*z[0]%p)
 x,dx=interp_prime(traces,v0,p)
 assert (x,dx)==(588,724) and (0,dx*pow(2,-1,p)%p)==(0,362)
 print('PASS_P3347_DEPENDENT',n,'H',hh,'Hprime',dh,'Q0',q,'trace_line_derivative',dx)

if __name__=='__main__':
 for p in [11,19,43,59,67,83,107]:small(p)
 large();print('PASS_GH146_GH147_COMPACT_EXACT')
