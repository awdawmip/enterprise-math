#!/usr/bin/env python3
"""R556 k15 rational root disks + normalized exact recurrence; reuse R555 exact kernels at pinned upstream source."""
from pathlib import Path
import importlib.util
from fractions import Fraction as F
PARENT=Path(__file__).resolve().parents[1]
UP=PARENT/"r555_signed_brc_fixed_k14_half_density_20261105_emr3"/"R555_VERIFY.py"
spec=importlib.util.spec_from_file_location("r555_rational_kernels",UP)
M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
M.K=15;M.d=29
CENTERS=[
 ("12.69961421677918","-17.38022669197763"),
 ("12.69961421677918","17.38022669197763"),
 ("5.88263349245423","-4.34852356046641"),
 ("5.88263349245423","4.34852356046641"),
 ("6.61975170985052","0"),
 ("3.09152949650173","-1.96003143324213"),
 ("3.09152949650173","1.96003143324213"),
 ("2.02811828082086","-1.17511807397136"),
 ("2.02811828082086","1.17511807397136"),
 ("1.48347309673602","-0.79203316423712"),
 ("1.48347309673602","0.79203316423712"),
 ("1.15690384797682","-0.57782359804974"),
 ("1.15690384797682","0.57782359804974"),
 ("0.94199029608057","-0.44513941631892"),
 ("0.94199029608057","0.44513941631892"),
 ("0.79211066296375","-0.35500241968175"),
 ("0.79211066296375","0.35500241968175"),
 ("0.68356931716917","-0.28894841302604"),
 ("0.68356931716917","0.28894841302604"),
 ("0.60257477362882","-0.23745797915760"),
 ("0.60257477362882","0.23745797915760"),
 ("0.54040533585801","-0.19495437756226"),
 ("0.54040533585801","0.19495437756226"),
 ("0.49115267159994","-0.15769761289764"),
 ("0.49115267159994","0.15769761289764"),
 ("0.45023742485340","-0.12262968128141"),
 ("0.45023742485340","0.12262968128141"),
 ("0.41247789831889","-0.08597724909548"),
 ("0.41247789831889","0.08597724909548"),
]
def polynomials():return M.polynomials()
def verify():
 co,a,p2=polynomials();assert M.C(15)==9694845 and p2==40920
 eps=F(1,10000); cc=[(F(x),F(y)) for x,y in CENTERS]; d=len(co)-1
 assert len(cc)==d==29
 ratio=[]
 for idx,c in enumerate(cc):
  b=M.Taylor_at(c,co)
  left=M.lower(b[1])*eps
  right=M.upper(b[0])+sum((M.upper(b[j])*eps**j for j in range(2,d+1)),F(0))
  assert left>right,("Rouche",idx)
  ratio.append(right/left)
 assert all(M.n2((cc[i][0]-cc[j][0],cc[i][1]-cc[j][1]))>4*eps*eps for i in range(d) for j in range(i+1,d))
 assert cc[0][0]==cc[1][0] and cc[0][1]==-cc[1][1] and cc[0][1]!=0
 assert M.n2(cc[0])>(F(21)+eps)**2
 assert all(M.n2(c)<(F(8)-eps)**2 for c in cc[2:])
 assert abs(cc[0][1])>cc[0][0]+2*eps
 assert 3*(cc[0][0]-eps)**2>(abs(cc[0][1])+eps)**2
 assert max(ratio)<F(3,500)
 print("R556_RATIONAL_ROUCHE_PASS roots=29 disjoint_pairs=406 radius=1/10000 max_ratio=",float(max(ratio)),flush=True)
 t=[F(1)]
 for m in range(1,1025):
  t.append(sum((a[j-1]*t[m-j] for j in range(1,min(m,d)+1)),F(0)))
 counts=(sum(v>0 for v in t),sum(v<0 for v in t),sum(v==0 for v in t),sum(t[i-1]*t[i]<0 for i in range(1,len(t))))
 assert counts==(514,511,0,306),counts
 print("R556_EXACT_RECURRENCE_PASS m=0..1024 plus=514 minus=511 zero=0 changes=306",flush=True)
 return co,a,p2
if __name__=="__main__":verify()
