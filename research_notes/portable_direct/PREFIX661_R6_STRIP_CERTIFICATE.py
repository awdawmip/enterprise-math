#!/usr/bin/env python3
"""PREFIX-661 exact BRC inward-gradient strip / unique 2D maximum.
Requires sibling PREFIX660_R6_EDGE_CONCAVITY_CERTIFICATE.py.
Original science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from fractions import Fraction as F
from math import comb
import json
import PREFIX660_R6_EDGE_CONCAVITY_CERTIFICATE as prev

N,S,Q,delta=189,2**225,F(19,128),F(1,4096)
eps=F(1,2**30);checks=0

def check(p,msg):
 global checks
 assert p,msg
 checks+=1

def main():
 rows=prev.make_rows()
 check(len(rows)==190 and not rows[-1],'frozen 189-layer extinction')
 A=[];C=[];D=[]
 for m in range(N):
  a=F(1);c=F(0);d=F(0)
  for n in range(25):a-=F(comb(m+n,n),2**(m+n+1))
  for n in range(25,34):
   w=F(comb(m+n,n),2**(m+n+1))
   c-=25*w;d-=F(25*(n+m+1),2)*w
  A.append(a);C.append(c);D.append(d)
 check(all((s*S).denominator==1 for s in A+C+D),'exact dyadic polynomial scaling')
 M=[0]*N;U=[0]*N;H=[0]*N
 M[0]=25*S;U[0]=225*S;H[0]=25*sum(range(26,35))*S
 for m,row in enumerate(rows[:N]):
  a,c,d=int(A[m]*S),int(C[m]*S),int(D[m]*S)
  for j,v in row.items():
   for k in range(j,m+1):
    term=v*(-1)**(k-j)*comb(m-j,k-j)
    M[k]+=a*term;U[k]+=c*term;H[k]+=d*term
 out={}
 for q in (12,24):
  P=[0]*(2*N-1)
  for j in range(N):
   P[j]+=2*q*q*S*H[j]-q*S*U[j]
   for k in range(N):P[j+k]-=2*q*q*M[j]*U[k]
  cc=prev.shift(P,Q)
  center=F(cc[0],S*S)
  tail=sum(abs(cc[k])*delta**k for k in range(1,len(cc)))/S**2
  check(len(cc)==377,'mixed partial polynomial degree <=376')
  check(center+tail<(-76650 if q==12 else -306490),'uniform negative edge p gradient')
  check((-77041<center<-77039) if q==12 else (-308046<center<-308044),
        'center gradient predecessor interval')
  check(tail<(389 if q==12 else 1554),'Taylor tail finite bound')
  out[str(q)]={'center_inward_p_gradient':prev.dec(center,12),
   'inward_gradient_taylor_error_upper':prev.dec(tail,9),
   'uniform_edge_inward_gradient_upper':'-76650' if q==12 else '-306490'}
 # Each survivor s_n has Bernstein coefficients in [0,1]; second
 # differences have absolute value at most 2. Bound all p in [0,1].
 M1=sum(range(N));M2=2*sum(n*(n-1) for n in range(N))
 H2=2*sum(n*(n-1)*(n+1) for n in range(N))
 W2=2*H2+2*M1*M1+2*378*M2
 K=24**2*W2+24*M2
 check((M1,M2,H2,W2,K)==(17766,4429656,631225980,5242533408,3019805554752),
       'universal p second derivative budget')
 check(K*eps<2813,'gradient extension to narrow p strip')
 check(-76650+K*eps<-73000,'strict uniform p-gradient negativity')
 # PREFIX660 certifies for q=12,24 whole-band Vzz<-12800000 and
 # Vzz<-51500000; Vzz/q is affine in q, extending to all q.
 result={'schema':'EM_PREFIX661_R6_EDGE_TO_STRIP_STABILITY_V1',
  'date':'2026-11-10',
  'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'predecessor':'PREFIX660_R6_EDGE_CONCAVITY_CERTIFICATE.py',
  'rectangle':{'p':['0','1/1073741824'],'z':['607/4096','609/4096']},
  'uniform_for_real_q':'12<=q<=24',
  'strict_uniform_p_derivative':'dVq/dp < -73000',
  'unique_2d_maximizer':'(0,z*(q)) with z*(q) as in PREFIX660',
  'quantitative_stability':'M(q)-Vq(p,z) >= 73000*p + 6400000*(z-z*(q))^2; strict off maximizer',
  'q_values':out,'p_second_derivative_budget':str(K),
  'checks_passed':checks,'arithmetic':'integer/Fraction, analytic Bernstein second derivative bound',
  'status':'AUTHOR_DERIVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED',
  'next_question':'extend p-strip with sharper mixed partial bounds; full-domain triangular chamber elimination'}
 print(json.dumps(result,ensure_ascii=False,indent=2))
 print('ALL_CHECKS_PASS',checks)

if __name__=='__main__':main()
