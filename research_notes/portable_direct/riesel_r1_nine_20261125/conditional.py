"""Independent R1 count by conditioning on its two released f=6 primes."""
import json
from pathlib import Path
from fractions import Fraction
from math import comb,prod
from decimal import Decimal,localcontext
base=Path(__file__).parent
def read(x):return json.loads((base/x).read_text())
def f(o):return Fraction(int(o.get('numerator',o.get('num'))),int(o.get('denominator',o.get('den'))))
def fm(x):
 with localcontext() as c:
  c.prec=65
  return {'numerator':str(x.numerator),'denominator':str(x.denominator),'decimal':format(Decimal(x.numerator)/x.denominator,'.55E')}
none=read('no_binary.json')
one=read('r2_conditional_source.json')
known=read('r2_budget_eight.json')
p,q=433,38737
weights=[Fraction((p-4)*(q-4),p*q), Fraction(2*((p-2)*(q-2)-(p-4)*(q-4)),p*q),Fraction(8,p*q)]
assert sum(weights)==1
high=(2521,1711081,430839361,15169173997557864184867895400813639018421,17369459529909057773233442461)
def occupy(k):return Fraction(sum((-1)**j*comb(k,j)*prod(q-2*j for q in high) for j in range(k+1)),prod(high))
gain1=sum(f(a)*occupy(k) for k,a in enumerate(one['need_high_short_slots']) if k)
first={n:f(n0) for n,n0 in none.items() if isinstance(n0,dict)}
second={'E6':Fraction(0),'E7':f(known['exact_7']),'E8':f(one['E8']),'L':f(one['L']),'gain':gain1}
mix=lambda a,b,c:sum(x*y for x,y in zip((a,b,c),weights))
z={k:mix(first[k],second[k],Fraction(int(k!='gain'))) for k in second}
z.update(exact6=z['E6'],exact7=z['E7']-z['E6'],exact8=z['E8']-z['E7'],
         exact9=z['L']-z['E8']+z['gain'],at_most_9=z['L']+z['gain'],L_minus_E8=z['L']-z['E8'])
assert z['exact6']==Fraction(8,433*38737)
check=read('forward.json') if (base/'forward.json').read_text().strip() else None
if check:
 for k,v in z.items():assert f(check[k])==v,k
out={k:fm(v) for k,v in z.items()}
out.update(parity_status_weights=[fm(v) for v in weights],matching_direct_result=check is not None)
print(json.dumps(out,indent=2))
