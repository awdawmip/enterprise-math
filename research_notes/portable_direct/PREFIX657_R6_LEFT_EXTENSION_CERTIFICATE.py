#!/usr/bin/env python3
"""PREFIX-657 exact rational implication certificate. Inherited strict inputs: PREFIX-643/654/655."""
from fractions import Fraction as F
import json
L,R=F(3,20),F(1,6)
z0=F(19,128); h=F(1,2**18); d=F(1,2**22)
a=z0-h; b=z0+h; left=a-d
K=F(6598084500)
pgap={12:F(226),24:F(785)}
zslope={12:F(9476),24:F(31590)}
M=lambda q:F(141976800)*q*q+F(283500)*q
checks=[]
def ck(name,condition):
    assert condition,name
    checks.append(name)
ck("zmin exact",left==F(622575,4194304))
ck("old z interval",a==F(38911,262144) and b==F(38913,262144))
ck("BRC observer range",F(37,256)<left and b<F(39,256))
ck("disjoint symmetric boxes",b<L)
ck("extension positive",d>0 and left<a)
ck("z second-score",left*(1-left)>F(188,1500))
ck("z first-score",1600*left*(1-left)>188)
ck("mu cap",104+3780*(h+d)<105)
ck("p derivative change",75600*d<1)
ck("p derivative cap",322+75600*d<323)
ck("p convex",1930-K*d>356)
ck("p chord constant",F(356,2)==178)
Dw=2*F(119700)+F(1260)*394+F(323,60)*7560
ck("Delta Wz constant",Dw==776538)
Dp=lambda q:q*q*Dw+q*1260
newp={12:F(199),24:F(678)}
newz={12:F(4600),24:F(12090)}
for q in (12,24):
    ck("M positive q%d"%q,M(q)>0)
    ck("p gap q%d"%q,Dp(q)*d<pgap[q]-newp[q])
    ck("z slope q%d"%q,M(q)*d<zslope[q]-newz[q])
    ck("positive gain q%d"%q,zslope[q]*d-M(q)*d*d/2>0)
pr=min(newp[q]/q for q in (12,24))
zr=min(newz[q]/q for q in (12,24))
ck("p slope",pr/(R-L)==995)
ck("z slope",zr==F(1150,3))
ck("p endpoint order",newp[12]/12<newp[24]/24)
ck("z endpoint order",newz[12]/12<newz[24]/24)
for q in map(F,(12,15,18,21,24)):
    lam=(q-12)/12
    ck("affine p "+str(q),(1-lam)*newp[12]/12+lam*newp[24]/24>=pr)
    ck("affine z "+str(q),(1-lam)*newz[12]/12+lam*newz[24]/24>=zr)
g={str(q):zslope[q]*d-M(q)*d*d/2 for q in (12,24)}
ck("q12 beats old upper",F(47425459,1000)+g["12"]>F(47425460,1000))
ck("q24 baseline",F(192190134,1000)+g["24"]>F(192190139,1000))
assert len(checks)==37,len(checks)
out={"schema":"EM_PREFIX657_LEFT_EXTENSION_CERTIFICATE_V1",
"science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
"new_domain":{"I":[str(L),str(R)],"Zprime":[str(left),str(b)],"q":[12,24]},
"maximizers":[[str(L),str(left)],[str(left),str(L)]],
"bounds":{"Fpp_lower":"356","DeltaWz_upper":str(Dw),
"p_gaps":{"12":"199","24":"678"},"z_slopes":{"12":"4600","24":"12090"},
"deficit":"995*q*(p-L)+(1150/3)*q*(z-left)+178*q^2*(p-L)*(R-p)"},
"gain_lower":{k:str(v) for k,v in g.items()},
"new_variance_lower":{"12":"47425.460","24":"192190.139"},
"q_data":{str(q):{"Mzz":str(M(q)),"Mzz_times_delta":str(M(q)*d),
"Dprime_upper":str(Dp(q)),"Dprime_times_delta":str(Dp(q)*d)} for q in (12,24)},
"checks":checks,"checks_passed":len(checks),"result":"ALL_CHECKS_PASS",
"scope":"Exact rational implication from pinned PREFIX-643/654/655; no native rerun"}
print(json.dumps(out,indent=2,sort_keys=True))
print("ALL_CHECKS_PASS",len(checks))
