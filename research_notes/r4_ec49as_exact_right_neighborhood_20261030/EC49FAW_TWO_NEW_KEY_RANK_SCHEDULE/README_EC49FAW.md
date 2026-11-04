# EC49FAW: exact two-key rank-feasible schedules after the 16-edge H2/H3 seed

Date: 2026-11-05 Asia/Shanghai. Status: AUTHOR_EXACT_FINITE / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Predecessor: EC49FAV at immutable commit be512db5ebe0d9d6b6d801824600c2a50abb13b4.
P000 and ACTIVE worldview unchanged.

## Theorems and exact domain

Fix H2={fe,ge} and H3={feg,gef}. The earlier source-verified construction has 16 ordered signed-native-X6 distinct prefix edges, and three distinct full positive BRC cache keys: (2,1,1,0,0,0), (3,0,1,0,0,0), (3,1,1,0,0,0). Require every H4,...,H9 horizon to contain a family of valid endpoint words with only the six allowed nine-history signatures D=de, E=ed, C=ce, J=ec, F=feg and G=gef and rational rank nine, characterized exactly by (E or F)&(C or F)&(D or G)&(J or G).

A. The three early keys expire by H2,H2,H3 respectively. No single new full key can be endpoint-feasible at both H4 and H9. Consequently a full completion under a five-key budget must introduce exactly two new keys.

B. Exactly 158 endpoint-feasible full positive BRC keys appear in at least one horizon H4–H9. Exactly 128 unordered distinct key pairs cover H4–H9 by endpoint feasibility; exactly 124 pairs can realize the six allowed observation signatures and rank nine at EACH of H4,H5,H6,H7,H8,H9, when primitive-prefix edge cost is not yet constrained. Four pairs fail at H4:
- (2,3,1) and (6,4,1): only G available, mask 32;
- (4,1,2) and (6,4,1): only G, mask 32;
- (5,0,1) and (6,4,1): only F, mask 16;
- (5,0,2) and (6,4,1): only F, mask 16.
Triples in this paragraph abbreviate full keys (x,y,z,0,0,0). The pair (4,2,1),(6,4,1) of the existing 112-edge nine-horizon witness belongs to the 124 survivors.

C. For every integer z>=1, the raw endpoint-feasible full key (2z,0,z,0,0,0) exists only at horizon 2z-1, but cannot realize any of the six permitted observer signatures. The sole realizing operations are a,e, and every word starts with a primitive -1 or +3; it has no positive-2 primitive step. Therefore the nine-history observer never performs its +1,+2 / +2,+1 state transition, leaving the initial-state vector, not one of six signatures. H2–H9 sees exactly the four missing raw keys (4,0,2)@H3, (6,0,3)@H5, (8,0,4)@H7, (10,0,5)@H9.

## Proof and finite exhaustive calculation

The frozen operations have signed primitive expansions a=(-1,-1), b=(-2,-2), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2). Exact endpoint (+2,0,0,0,0,0) forces #b=0 and #e=#a+1. Set z=#e>=1, r=#c+#d, f=#f, g=#g. Then x=2z+r+f, y=r+g, h=2z-1+r+f+g. Inverting:
r=x+y-h-1, f=h+1-y-2z, g=h+1-x.
Their nonnegativity is equivalent to endpoint key feasibility; consequently max(x-1,y+2z-1)<=h<=x+y-1. From H4 feasibility x<=5,y+2z<=5, so x+y<=8 and upper feasible horizon <=7; a single key cannot span H4 to H9. Every key feasible in H4–H9 lies in 0<=x<=10,0<=y<=10,1<=z<=5; complete integer enumeration yields 158 keys and 128 covering pairs.

The executable JavaScript verifier enumerates all ordered legal endpoint words of H2–H9, using only the proven operator-count balance for pruning. It composes the original nine-history DFA over the ordered signed native X6 primitive steps, retains each permitted signature and the full positive cache key, and OR-combines the six-signature masks for each key at each horizon. The rank-nine four-clause test is exact. This gives 124 schedules and the four stated exclusions. It produces complete 128- and 124-pair lists and exact census in EXACT_REPORT_EC49FAW.json. The independent C++ checker in CROSSCHECK_EC49FAW.cpp scans literal signed six-axis steps and reproduces the same counts and exceptions.

h | endpoint words | allowed-signature words | allowed keys | one-key rank9
2 | 8 | 6 | 3 | 1
3 | 51 | 38 | 6 | 4
4 | 304 | 206 | 13 | 9
5 | 1770 | 1062 | 21 | 17
6 | 10224 | 5352 | 34 | 28
7 | 58947 | 26644 | 49 | 43
8 | 340064 | 131686 | 70 | 62
9 | 1964862 | 647930 | 94 | 86

## Reproduction, scope and next action

Run Node.js >=18: node VERIFY_EC49FAW.js > EXACT_REPORT_EC49FAW.json. Independent crosscheck: g++ -O3 -std=c++17 CROSSCHECK_EC49FAW.cpp -o checker && ./checker > CROSSCHECK_REPORT_EC49FAW.json. Both were executed with matching 158/128/124 and all horizon counts. This finite screen is not a total-prefix-edge optimum and leaves the global author's range 80<=E*_H9<=94 unchanged.

Next EC49FAX: jointly optimize ordered signed primitive-prefix costs over the 124 surviving key pairs, first testing (4,2,1),(6,4,1) against the existing 112-edge witness. Compare with the alternate 31-edge/two-key H2/H3 seed. Seek a legal <=93-edge witness with complete word set or a declared-family exact lower-bound certificate. Keep frozen scientific input, provenance, and Source authorization distinct. No native CLAIM, Result or independent Driver is inferred.
