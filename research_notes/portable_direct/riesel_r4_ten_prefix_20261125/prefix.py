from fractions import Fraction as F
from collections import Counter
H=(0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100)
c={g:max(Counter(h%g for h in H).values()) for g in (1,3,5,7,15,21,35,105)}
r1=sum(h%3==1 for h in H)
# Both missing: discard the now-inactive 43,5419,29; keep every potentially
# active old exceptional prime and bound the five other channels by 1/12.
both=2*F(13,108)+3*F(1,11)+5*F(1,12)
# Exactly one missing: in the opposite u-parity, 29,43 (e7), 15790321 (e14),
# 1429,5419 (e21) and 433 (e18) are inactive. Allow 61681 as an upper bound.
g=max(F(c[q],d) for q,d in [(1,11),(3,8),(5,4),(7,4),(15,2),(21,2),(35,1),(105,1)])
one=sum(sorted([F(r1,3)]*2+[F(c[5],2),F(c[3],6)]+[g]*9,reverse=True)[:9])
print(c,r1,g,both,one,len(H),F(len(H))-one)
assert both<1 and one<len(H)
assert 8*F(3,13)<2
