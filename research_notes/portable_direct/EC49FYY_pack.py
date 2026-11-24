import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
S=list(range(1,1024)); A=np.array([[int(bool(u&s)) for s in S] for u in F]); L=np.array([s.bit_count() for s in S]); O=np.ones(len(S)); B=np.vstack([A,L]);
for k in range(1,12):
 q=(26*k+10)//11
 r=milp(O,integrality=O,bounds=Bounds(0,np.inf),constraints=LinearConstraint(B,[k]*50+[q],[np.inf]*50+[q]),options={'time_limit':2.0})
 if r.x is None: print(k,r.message,flush=True);continue
 x=np.rint(r.x).astype(int);assert min(A@x)>=k and L@x==q
 print(k,q,sum(x),[(s,int(v)) for s,v in zip(S,x) if v],r.status,r.mip_dual_bound,flush=True)
