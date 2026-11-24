"""Two formerly unresolved subcarriers from the R2 order inventory."""
from decide import *
from math import isqrt
R540=27437042128462313499387435995461
R1260=263480353852730122330752072139697321699158754520077217531258822574081
proofs={
  166242935471754241:(17,{2:10,3:3,5:1,11:1,257:1,3433:1,123911:1}),
  165041853060421:(10,{2:2,3:3,5:1,7:1,197:1,4813:1,46049:1}),
}
def smallprime(q):return q>1 and all(q%i for i in range(2,isqrt(q)+1))
for q,(g,F) in proofs.items():
    assert all(smallprime(p) for p in F)
    assert prod(p**e for p,e in F.items())==q-1
    assert pow(g,q-1,q)==1 and all(gcd(pow(g,(q-1)//p,q)-1,q)==1 for p in F)
    assert pow(2,540,q)==1 and all(pow(2,540//p,q)!=1 for p in (2,3,5))
assert prod(proofs)==R540
rows=carriers()[0]
assert rows[540][1]%R540==0 and rows[1260][1]%R1260==0
# Every prime divisor of R1260 has exact order 1260, so is 1 mod1260.
# Excluding all proposed divisors in that residue class is enough.
limit=50_000_000
assert all(R1260%q for q in range(1261,limit+1,1260))
k=0
while (limit+1)**(k+1)<=R1260:k+=1
fermat=next(b for b in range(2,100) if gcd(b,R1260)==1 and pow(b,R1260-1,R1260)!=1)
print(json.dumps({'resolved_540_subcarrier':str(R540),'certified_540_factors':proofs,'unresolved_1260_subcarrier':str(R1260),'fermat_composite_witness':fermat,
'1260_all_prime_factors_strictly_above':limit,'1260_distinct_prime_factor_count_at_most':k},indent=2))
