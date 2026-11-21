# X6 R99 — Complete ten-direction tie core for the two-parameter positive-count BRC observer

Date: 2026-11-22 (Asia/Shanghai).  
Evidence status: SYMBOLIC_AUTHOR_PROOF / EXACT_RATIONAL_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.  
Parent: R98, research_notes/portable_direct/2026-11-22_x6_r98_all_ports_two_parameter_exact_envelope.md.  
Frozen scientific P000 pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.

Scope: conditional, positive-count four-channel BRC star-moment histogram observer under an unknown common additive offset. The integer triple below is an auxiliary difference index; this model is not identified with a complete native X6 Cell/Link/force/time state.

## Exact model and theorem

For a nonzero unoriented integer difference a=(x,y,z), let

- q(a)=max(sum max(x_i,0), sum max(-x_i,0));
- u=x+3y+6z, v=3x+12y+30z, h=7x+39y+126z;
- F(a;S,T)=max(|u|/2, |v|/(S+1), |h|/(T+1), |v-u|/(S+1), |h-u|/(T+1), |h-v|/(S+T)).

S,T are *arbitrary real numbers at least 1* and p is any integer at least 11. Define eta_p(S,T)=min_{a != 0, q(a)<=p} F(a;S,T). The R98 exact-value envelope is

E_p(S,T)=min{1/2, 12/(T+1), max(3/(S+1),6/(T+1)), [6/(S+1) if p>=27]}.

**R99 theorem.** The entire set of optimal *unoriented* integer differences for every S,T>=1 and every p>=11 is exactly

M_p(S,T)={a in C10 : q(a)<=p and F(a;S,T)=E_p(S,T)},

where C10 is the following set. Put U=|u|, V=max(|v|,|v-u|), H=max(|h|,|h-u|), K=|h-v|. The score for each row is simply max(U/2,V/(S+1),H/(T+1),K/(S+T)).

| a | q | U | V | H | K |
|---|---:|---:|---:|---:|---:|
| (1,0,0) | 1 | 1 | 3 | 7 | 4 |
| (4,-1,0) | 4 | 1 | 1 | 12 | 11 |
| (5,-4,1) | 6 | 1 | 3 | 6 | 8 |
| (6,-4,1) | 7 | 0 | 0 | 12 | 12 |
| (9,-5,1) | 10 | 0 | 3 | 6 | 3 |
| (10,-5,1) | 11 | 1 | 1 | 1 | 1 |
| (14,-9,2) | 16 | 1 | 6 | 1 | 5 |
| (15,-9,2) | 17 | 0 | 3 | 6 | 9 |
| (19,-10,2) | 21 | 1 | 4 | 6 | 2 |
| (24,-14,3) | 27 | 0 | 6 | 0 | 6 |

Every one of these ten directions attains the global minimum for some feasible S,T,p, so ten is the **minimal cardinality of a universal *complete-tie* carrier**. This differs from R98's four-witness carrier for the optimal *value*.

**Port stabilization:** for fixed S,T>=1, the entire minimizing-direction set is constant at every p>=27. This bound is sharp: at S=11,T=1, direction (24,-14,3) joins the existing minimizers at p=27, but is infeasible at p=26. This settles the R98 Port-sensitive multiplicity question for the declared two-parameter section.

## Proof: a universal 17-direction box

The feasible s=(10,-5,1), q=11, has F(s)=1/2 for all S,T>=1. The feasible d=(6,-4,1), q=7, has F(d)=12/(T+1). Hence every minimizing difference satisfies |u|<=1, |h|<=12.

For p>=27, the feasible c=(24,-14,3) has F(c)=6/(S+1); thus |v|<=6. For 11<=p<=26, use q(a)<=26, hence |x|<=26, together with the exact inverse
x=(h+19u)/2-4v,
y=(-h-14u+7v)/3,
z=(h+11u)/12-v/2.
It follows that 4|v|<=26+(12+19)/2=83/2. Since v is a multiple of 3, |v|<=9. Thus all minimizing differences lie in |u|<=1, |h|<=12, |v|<=9, and if p>=27 also |v|<=6.

The exact integrality conditions, necessary and sufficient for the above inverse, are
v in 3Z, h-u in 6Z, h-u-6v in 12Z.
Write v=3k, h=u+6j, so j≡k modulo 2, and the inverse simplifies to

a=(10u+3j-12k, -5u-2j+7k, u+(j-3k)/2).

With u=-1,0,1; k=-3,...,3; |u+6j|<=12; j≡k (mod 2), retain a nonzero vector only if q(a)<=26 (low-Port possibility) **or** |3k|<=6 (high-Port possibility). This finite integer enumeration yields exactly 34 signed vectors, i.e. 17 unoriented directions: the ten in C10 and exactly these seven extras.

| Excluded vector a | q | (U,V,H,K) |
|---|---:|---|
| (18,-10,2) | 20 | (0,6,12,6) |
| (20,-13,3) | 23 | (1,6,12,17) |
| (23,-14,3) | 26 | (1,9,7,2) |
| (25,-14,3) | 28 | (1,4,7,10) |
| (28,-15,3) | 31 | (1,7,12,5) |
| (30,-18,4) | 34 | (0,6,12,18) |
| (34,-19,4) | 38 | (1,7,1,7) |

This is a complete, explicitly bounded enumeration based on the inverse lattice congruences, not an inference from numeric sampling.

## Proof: the seven extras are *strictly* nonoptimal

The vector (18,-10,2) is twice b=(9,-5,1); by positive homogeneity, F(2b)=2F(b)>F(b), with b feasible earlier.

Five extras have U=1, hence F>=1/2. If any is optimal, it must have F=1/2 (as eta<=1/2). The inequalities V/(S+1)<=1/2 and H/(T+1)<=1/2 force the following necessary lower bounds:

| q | S at least | T at least |
|---:|---:|---:|
| 23 | 11 | 23 |
| 26 | 17 | 13 |
| 28 | 7 | 13 |
| 31 | 13 | 23 |
| 38 | 13 | 1 |

For q=23,26,28,31, the always-feasible b=(9,-5,1) then has F(b)=max(3/(S+1),6/(T+1))<1/2, ruling out the extra strictly. For q=38, p>=38 admits c=(24,-14,3) with F(c)=6/(S+1)<=6/14<1/2. Hence none of these five can minimize.

For the remaining vector a=(30,-18,4), q=34, define C=6/(S+1), D=12/(T+1). It has F(a)=max(C,D,18/(S+T)). At p>=34 both c and d are feasible, yielding eta<=min(C,D). If C!=D, then F(a)>=max(C,D)>min(C,D). If C=D, then T=2S+1, whence 18/(S+T)=18/(3S+1)>6/(S+1)=C=D. Thus this vector cannot minimize either.

All global minimizers belong to C10. Conversely, by R98 the exact value E_p is attained in C10, and a feasible C10 member minimizes if and only if its computed F equals E_p. This proves the theorem over the full infinite integer lattice. QED.

## Exact necessity witnesses for all ten directions

The following triples (S,T,p) are all legal; for each listed direction, direct exact substitution gives F=E_p=1/2.

| Direction | (S,T,p) |
|---|---|
| (1,0,0) | (5,13,11) |
| (4,-1,0) | (1,23,11) |
| (5,-4,1) | (5,11,11) |
| (6,-4,1) | (1,23,11) |
| (9,-5,1) | (5,11,11) |
| (10,-5,1) | (1,1,11) |
| (14,-9,2) | (11,1,16) |
| (15,-9,2) | (5,13,17) |
| (19,-10,2) | (7,11,21) |
| (24,-14,3) | (11,1,27) |

Any universal fixed family that lists *all* minimizers in this parameter domain must contain each row, proving minimal cardinality ten.

## Verification, evidence boundary, continuation

The companion exact-integer/rational verifier independently reconstructs the 17-direction box and enumerates all 110,740 unoriented nonzero differences with q<=40. For 16 rational/integer (S,T) pairs it checks every p=11,...,40, yielding 480 complete exact optimal-value and tie-set comparisons, plus the ten witness checks. All author-side assertions passed. The universal proof is the algebra above; finite tests are independent finite-domain corroboration, not an infinite-domain proof.

This auxiliary positive-count BRC statistic does not certify native X6 signed phase, named Cell identities, Link/path/provenance, three-force closure or chronological heartbeat trace. The next scientific step is an explicit classification of the ten equality chambers and the maximal simultaneous tie multiplicity; native P000 observer-fiber preservation remains a separate typed bridge question. Researcher/Activity registration, formal CLAIM, and canonical Result/Review are operationally separate from this independent GitHub paper.
