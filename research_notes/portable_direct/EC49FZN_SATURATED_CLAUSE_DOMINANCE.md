# EC49FZN — Exact dominance of saturated residual clauses

2026-11-25. Independent portable continuation of FZM, frozen BRC16943, h=14,m=25. Parent fc3bed947e69dd5684c8cebf1a4562b537bcd24e:research_notes/portable_direct/EC49FZM_SATURATED_FIBER_CERTIFICATE.md (blob a5840383cb1bd81a8532302e4007f4dd0a08abf2). Historical researcher EM-DIRECT-23537B; current private writer binding unconfirmed. Native topic read r4-20261125-1030-ec49as-read-v1 SUCCEEDED, Source 1d8b919f1c9a2c8ef823172f6e3dceafa8882228, NO_CANONICAL_PUBLICATION_DIRECTORY; no native owner projection or formal claim.

## Exact pairwise dominance

Use FZM genuine-history common potential-hole universe and FZI anchored certificate. At saturated target x=(U,H), |H|=h, write B=B_U, O=H minus B. O is mandatory. For each competing V define
R_v=U xor V, L_v=B_V minus H, G_v=B minus B_V, d_v=h-|B_V union O|+1.
Discard d_v<=0 (already excluded). For arbitrary row features T, live features P subset complement H, extra missing features J subset B, the remaining clause is
E_v(T,P,J) := (T intersects R_v) OR (P intersects L_v) OR (|J intersect G_v|>=d_v).
This is exactly FZM's competitor exclusion, by disjointness of O and B. For two remaining clauses v,w, the implication E_v => E_w for all T,P,J holds iff
R_v subset R_w, L_v subset L_w, and [d_v>|G_v| OR d_v-|G_v minus G_w|>=d_w].

Proof: a row in R_v outside R_w yields a counterexample with just that row and P=J=empty; the live-feature inclusion is necessary by the corresponding singleton. If d_v>|G_v|, its capacity alternative never holds. Otherwise select d_v elements of G_v, prioritizing G_v minus G_w: the minimum intersection with G_w is max(0,d_v-|G_v minus G_w|). With d_w>0, this proves necessity and sufficiency of the third condition. In the sufficient direction each of the three alternatives separately implies the corresponding alternative of E_w. Mandatory O is held fixed throughout. In particular this implication is exact on the entire feature selection domain, not just sampled states.

The relation is a preorder. Quotient mutually implying clauses, retain one representative, and keep only maximal constraints under strength (i.e. clauses that imply weaker ones and are not strictly implied by another). Finite transitivity ensures every deleted clause is implied by some retained clause. Thus the conjunction is unchanged for ALL feature choices. By FZI's monotone exact cost formula the minimum certificate cost is unchanged, even with positive row/column pairing. This is a certificate-only BRC residual quotient; adaptive query transitions continue to use the FZJ full fiber representation. It is not a claim of globally minimum equivalent clause set under collective implication.

## Executed finite evidence

Parent local FZM archive frozen fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; fullrow.cpp SHA256 3d1ae2d75991d5b6cd9a131f38068f27d04a1e2fc2abccf6e6673893e00f9d0b; prior fourth_partial.csv SHA256 494f70227d537e0d57b36477ecaea66ad46dcc7f8c6151deeedc3db440ce8e27. All matched actual local bytes.
Sample two saturated targets per each of 2393 frozen roots using seed 16943, 4786 targets; 29434 nontrivial clauses before, 19105 after, 3659 targets reduced. 38288 feature tests, 43804880 explicit labeled-state comparisons, zero assertion failures. Counts refer to sampled target instances, not all possible saturated targets. Compression is 35.09% in aggregate clause count; no runtime gain claimed.

Executed dominance.py (SHA256 14dd9c4e7ea550bb94adfcf963934f8784a9992746458e187f7f0cea5c8dcbb2):
```python
from fourth import fibers
from gen import physical
from collections import Counter
import json,random
H=14; M=25

def constraints(f,u,h):
 b=next(b for v,b,a in f if v==u); o=h&~b
 out=[]
 for v,c,a in f:
  if v==u:continue
  d=H-(c|o).bit_count()+1
  if d<=0:continue
  out.append((u^v,c&~h,b&~c,d))
 return b,o,out

def implies(v,w):
 r,l,g,d=v; R,L,G,D=w
 return not(r&~R or l&~L) and (d>g.bit_count() or d-(g&~G).bit_count()>=D)

def reduce(q):
 q=list(dict.fromkeys(q));return [v for i,v in enumerate(q) if not any(implies(w,v) and (not implies(v,w) or j<i) for j,w in enumerate(q) if i!=j)]

def covered(q,t,p,j):
 return all(t&r or p&l or (j&g).bit_count()>=d for r,l,g,d in q)

def main():
 rng=random.Random(16943); totals=Counter(); roots=json.load(open('fourth.json'))
 for n,key,paths,status in roots:
  r,mask,other=key; f=list(fibers(key)); st=physical([mask,*other],H,r,0);assert len(st)==n
  sat=[(u,h) for u,h in st if h.bit_count()==H]
  for u,h in rng.sample(sat,min(2,len(sat))):
   b,o,q=constraints(f,u,h); z=reduce(q); totals['targets']+=1;totals['before']+=len(q);totals['after']+=len(z);totals['reduced']+=len(z)<len(q)
   for _ in range(8):
    t=rng.getrandbits(10);p=rng.getrandbits(M)&~h;j=rng.getrandbits(M)&b
    assert covered(q,t,p,j)==covered(z,t,p,j)
    actual=sum(not ((u^v)&t or K&p or (o|j)&~K) for v,K in st)
    assert covered(z,t,p,j)==(actual==1)
    totals['feature_checks']+=1;totals['state_comparisons']+=len(st)
 print(dict(totals))
if __name__=='__main__':main()
```

## Further fourth-level branch replay

Reuse unchanged fullrow.cpp from parent. g++ -O3 -std=c++17 fullrow.cpp -o solver; python fourth_input.py 1550 1750 12000 > untouched.txt; timeout 18s ./solver < untouched.txt > fourth_new.csv. Completed rows only: IDs 1550..1738, 189 rows, 50 YES, 139 cap-UNKNOWN, no NO; 2035542 recorded recursive calls; 66123 labeled state replays for YES. Exact YES IDs:
1550,1551,1556,1557,1561,1569,1571,1572,1574,1583,1584,1596,1600,1608,1616,1617,1618,1619,1620,1623,1625,1626,1627,1629,1631,1633,1634,1635,1644,1645,1646,1651,1654,1655,1656,1680,1681,1686,1687,1688,1689,1692,1694,1695,1697,1699,1706,1707,1708,1735.
Every other completed ID in the stated range is UNKNOWN. Raw fourth_new.csv SHA256 8fcecca3636d17e307ca143224db69b9825b8c7489cf8c13d9b25aefcbba64c8. Together with prior FZM: 1547 YES, 192 cap-UNKNOWN, 654 not completed (IDs 1739..2392), 0 NO. Ordered histories 3149 YES, 374 cap-UNKNOWN, 1172 unrun. No full 25-column strategy; M14 remains 25..27. The dominance reducer was evaluated separately, not used for these branch runs.

Next: preserve these 1547 YES, continue untouched roots and capped roots; implement a reduced-clause budget feasibility optimizer and compare actual adaptive pruning cost. P000 unchanged. AUTHOR_PROVED / EXACT_FINITE_FEATURE_CHECK / PARTIAL_EXACT_BRANCH_REPLAY / PARENT_DEPENDENT / NOT_REVIEWED.
