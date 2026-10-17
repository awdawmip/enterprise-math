# PREFIX-149 — Dense-edge obstruction and conditional lower bound 54

Date: 2026-10-17. **UNREVIEWED / NOT_ADMITTED.** Auxiliary labelled-Boolean BRC observation only; not P000 native six-dimensional Cell dynamics.

## Frozen provenance
GLOBAL_KNOWLEDGE_V1 canonical-main snapshot `3ef0c52278af731df90462d9dcdc635bc6d7040d`; P000 record Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. EM source read `24f3e2953aea62973332a12003a802cbbd4283b2`, portable protocol and ordinary control. Predecessor: local PREFIX-148 handoff with its unreviewed 832-row necessary-profile CSV and M49 positive-support obstruction. This note is not formal Source registration, CLAIM, frozen Result or Driver acceptance.

## Exact theorem A (new, self-contained, finite certificates)
Write `Delta_b^4={x in Z>=0^4: sum_i x_i=b}` and `beta_4(8)=min{|S|:S subset Delta_8^4, S+S=Delta_16^4}`. There are 165 candidate states, 969 target states and exactly 455 targets with all four coordinates positive. Full coverage forces all four vertices 8e_i into S. For any 53-element complete S, let `e_ij` count strict two-coordinate edge states, `h_i` strict three-coordinate states missing i, and `t` strict four-coordinate states. Let `D=42-sum e_ij` count the missing strict edge states (there are exactly 42 possible). Then `53=46-D+sum h_i+t`.

**Proposition A:** Every complete S with |S|<=53 has D>=3, i.e. at most 39 of the 42 possible strict edge-interior states. No inherited edge-profile list or predecessor catalogue is needed.

*Facet deficit lemma.* A 3D triangle slice has 24 vertex/edge states and 21 possible strictly three-positive states, and must cover 153 targets. For an arbitrary r=0,1,2 deleted edge states, literal enumeration of all missing subsets and all possible 0/1/2 three-positive additions gives these minimum-addition histograms (3 means >=3, not exactly 3):
- r=0: 1 configuration needs 0;
- r=1: 21 configurations, counts needing 1:6, 2:9, >=3:6;
- r=2: 210 configurations, counts needing 2:24, >=3:186.
Thus every face needs at least r additional three-positive states. Every missing 4D edge state belongs to two of the four 3D faces, so `sum_i h_i>=2D`, hence `t<=7-D`. Both Python and independent C++17 enumerations replay the literal 153-target coverage tests.

*Exact four-positive pair identity.* For unordered state pairs with repetition, the number with union of supports equal to all four coordinates is exactly
```
P = e01*e23 + e02*e13 + e03*e12
  + SUM_{i<j} e_ij*(h_i+h_j)
  + SUM_i h_i + SUM_{i<j}h_i*h_j
  + t*(53-t) + t*(t+1)/2.
```
This counts complementary edge pairs, edge+face, vertex+opposite-face, different-face, all pairs with a four-positive state. Every such pair produces exactly one four-positive target, so to cover the 455 distinct targets it is necessary that P>=455. Enumerating *all* edge-count deficit profiles with D=0,1,2 and *all* nonnegative allocations of h=7+D-t among four faces (no facet-completeness filtering) yields: at D=0 and t<=5, P<=447; at D=1 and t<=4, P<=438; at D=2 and t<=3, P<=430. Both Python polynomial counting and C++17 independently enumerated support-mask pair OR counts agree in all 27 (D,t) cases.

*Optimistic distinct-output cap.* The only potentially remaining cases are (D,t,h)=(0,6,1),(0,7,0),(1,5,3),(1,6,2),(2,4,5),(2,5,4). Let B be the four vertices and all present strict edge states (size 46-D), let Y be the distinct four-positive outputs of B+B, and for a three-positive state f or four-positive state u define A_f=(f+B)\\Y and A_u=(u+B)\\Y, restricted to four-positive targets. Enumerate *every* B obtained by deleting D<=2 of the 42 possible edge states: 1+42+861=904 deletion patterns; all 84 three-positive f, all 35 four-positive u and all 455 positive target sums. Python integer bitsets and independently written C++17 fixed bitsets agree on the unconditional maxima:
```
D   max|Y|   max|A_f|   max|A_u|  B deletion patterns
0      127       17       40           1
1      122       18       40          42
2      118       19       40         861
```
Allowing every added face or full-support state to obtain independently the *best* possible gain while ignoring overlaps is a deliberate relaxation. It yields
```
| (S+S) intersect positive_targets |
   <= C_D + h F_D + binomial(h,2)
               + t*(U_D+h) + binomial(t+1,2).
```
For the six remaining (D,t,h) cases in the order displayed above, the resulting generous caps are **411,435,409,432,413,435**, respectively. All are <455. Hence D<=2 is impossible. For |S|<53, add arbitrary states to make 53; D cannot increase. This completes Proposition A.

## Theorem B (conditional on prior unreviewed certificate completeness)
The inherited necessary-filter file has 832 labelled edge-count profiles for a hypothetical 53-state complete basis. PREFIX-144–147 previously excluded its M(e)>=50 profiles. PREFIX-148 previously excluded all M(e)=49 cases with t>0; those finite claims were **not fully independently replayed here**. This turn additionally enumerated every one of the 66 M(e)=49 labelled profiles at t=0, for all C(7,3)=35 allocations of four excess face states, using the exact pair identity; maximum P was 421<455 (2310 checks, Python/C++ agreement). Therefore all 66 are excluded provided the earlier M49,t>0 certificate is valid. The remaining 28 profiles (21 at M48, 6 at M47, 1 at M46) have exactly D=2,1,0 and are independently excluded by Proposition A. Accordingly *relative to completeness and correctness of the earlier necessary-profile/exclusion certificates*, the resulting interval is **54<=beta_4(8)<=61**. The inherited 61-state witness was independently replayed and covers all 969 targets. This interval is not asserted as a Driver-admitted theorem.

## Evidence and limits
Full local handoff includes the complete manuscript, executable Python and C++17 scripts, raw logs and SHA-256 file manifest. The unconditional dense-edge lemma needs no predecessor data. The global 54 deduction still requires independent audit of the inherited 832-row necessary-profile generator and M>=50, M49-positive exclusions; no Lean formalization, formal CLAIM, winning-Owner verification, native-Cell lift or Driver acceptance has occurred.

## Next research unit
PREFIX-150: independently regenerate and audit the necessary-profile generator plus all predecessor finite no-go certificates, especially M49 positive-support cases. Seek a minimal counterexample to any unsound gluing claim, or independently establish lower bound 54. Continue the search for an exact complete <=60-state upper witness. Preserve the auxiliary-observer/native-P000 firewall.
