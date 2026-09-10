#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import itertools,json,time
ROOT=Path(__file__).resolve().parent
R2=36;K0=17;CNEAR=F(18,5);CSELF=F(91,20)
pts=[(p,sum(x*x for x in p)) for p in itertools.product(range(-5,6),repeat=3) if 0<sum(x*x for x in p)<R2]
classes=[(a,b,c,a*a+b*b+c*c) for a in range(K0) for b in range(a,K0) for c in range(b,K0) if 0<a*a+b*b+c*c<K0*K0]
def sqrt_lower(n,d=12):
 s=10**d;v=F(isqrt(n*s*s),s);assert v*v<=n and (v+F(1,s))**2>n;return v
start=time.time();min_diag=None;min_det=None;max_diag_read=(0,None)
for k0,k1,k2,nk in classes:
 t1=(k1,-k0,0) if (k0 or k1) else (1,0,0)
 t2=(k1*t1[2]-k2*t1[1],k2*t1[0]-k0*t1[2],k0*t1[1]-k1*t1[0])
 h1=sum(x*x for x in t1);h2=sum(x*x for x in t2);assert h2==nk*h1
 r11=r22=r12=F()
 for p,npv in pts:
  q=(k0-p[0],k1-p[1],k2-p[2]);nq=sum(x*x for x in q)
  if nq==0:continue
  kp=p[0]*k0+p[1]*k1+p[2]*k2;kq=nk-kp
  U=(nk*npv-kp*kp)*nq+(nk*nq-kq*kq)*npv
  V=nk*(npv+nq)-(kp-kq)*(kp-kq);den=4*(npv*nq)**2
  p1=p[0]*t1[0]+p[1]*t1[1]+p[2]*t1[2];p2=p[0]*t2[0]+p[1]*t2[1]+p[2]*t2[2]
  r11+=F(U*h1-V*p1*p1,den);r22+=F(U*h2-V*p2*p2,den);r12+=F(-V*p1*p2,den)
  if nq>=R2:
   ps=q;nps=nq;kps=kq;kqs=kp
   U2=(nk*nps-kps*kps)*npv+(nk*npv-kqs*kqs)*nps
   V2=nk*(nps+npv)-(kps-kqs)*(kps-kqs);den2=4*(nps*npv)**2
   s1=ps[0]*t1[0]+ps[1]*t1[1]+ps[2]*t1[2];s2=ps[0]*t2[0]+ps[1]*t2[1]+ps[2]*t2[2]
   r11+=F(U2*h1-V2*s1*s1,den2);r22+=F(U2*h2-V2*s2*s2,den2);r12+=F(-V2*s1*s2,den2)
 root=sqrt_lower(nk);th=CNEAR*root
 aa=th*h1-r11;dd=th*h2-r22;det=aa*dd-r12*r12
 assert aa>0 and dd>0 and det>0,(k0,k1,k2)
 rd=min(aa/F(h1),dd/F(h2))/th;rt=det/(th*th*h1*h2)
 min_diag=rd if min_diag is None else min(min_diag,rd);min_det=rt if min_det is None else min(min_det,rt)
 diag=max(float(r11/F(h1)/root),float(r22/F(h2)/root))
 if diag>max_diag_read[0]:max_diag_read=(diag,(k0,k1,k2))
FAR=F(62003356548290251911587120911572831191,3626860363525628692824853787443200000)
whole=CNEAR+FAR;assert whole<CSELF*CSELF
res={'status':'PASS','record_id':'FINDING-EM-PDE-SELF-NEAR-KERNEL-20260910','near_points':len(pts),'output_classes':len(classes),'near_squared_upper':str(CNEAR),'min_relative_diagonal_margin':str(min_diag),'min_relative_determinant_margin':str(min_det),'max_diagonal_readout_only':max_diag_read,'far_squared_upper':str(FAR),'total_squared_upper':str(whole),'total_squared_readout':float(whole),'self_constant':str(CSELF),'self_constant_readout':float(CSELF),'acceptance':'exact Fraction matrices with rational lower bounds for sqrt(|k|^2)','PDE_sampling':False,'limits':['Near eigenvalue readout is diagnostic only; acceptance is exact positive-definiteness.','Far tail is inherited analytic result.','Constant not claimed optimal.']}
(ROOT/'selfnear_verification.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(res,indent=2,ensure_ascii=False));print('elapsed',time.time()-start)
