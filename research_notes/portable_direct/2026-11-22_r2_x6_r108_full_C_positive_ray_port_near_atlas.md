# X6 R108 — Exact Port and strict-near atlas for the entire positive C-ray

2026-11-22 · AUTHOR_PROOF / EXACT_INTEGER_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED

Mode: independent auxiliary TASK_RESEARCH, without native X6 CLAIM.
Frozen foundation: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (P000 V5).
Scientific predecessor evidence: R105 (C=59 whole-lattice twelve-direction carrier); R106 (robust chamber); R107 (high-C complete atlas). This is a conditional four-positive-weight six-pair BRC observer, not a native X6 Cell/Link/heartbeat theorem.

## Definitions

For nonzero a=(x,y,z) in Z^3 identify ±a and define the exact Port count

    q(a)=max(sum_i max(a_i,0), sum_i max(-a_i,0)).

Define integer moments

    u=x+3y+6z, v=3x+12y+30z, h=7x+39y+126z.

For real C>=1, put w=(9,1,C,41) and

    F_C(a)=max(|u|/10, |v|/(C+9), |h|/50,
               |v-u|/(C+1), |h-u|/42, |h-v|/(C+41)).

For all integers p>=11, let eta_p(C) be the minimum F_C(a) over nonzero integer triples q(a)<=p, and let N_p(C) be the entire set of unoriented feasible directions satisfying F_C(a)<(3/2)eta_p(C). All membership boundaries below are strict unless an endpoint is explicitly included.

## Theorem 1 — All C>=1 and all Port budgets p>=11

    eta_p(C) =
       2/7       for 1<=C<=5/2;
       1/(C+1)   for 5/2<=C<=9;
       1/10      for 9<=C<=59;
       1/10      for C>=59 and 11<=p<=26;
       6/(C+1)   for C>=59 and p>=27.

Overlaps agree. The true optimal-value transition parameters are C=5/2, 9, 59, with an additional Port 26->27 transition when C>59.

**Proof.** The directions r=(6,-4,1), s=(10,-5,1), t=(24,-14,3) have exact moments (0,0,12), (1,0,1), (0,-6,0) and Port values 7, 11, 27 respectively. Consequently F_C(r)=2/7 for every C>=1 and F_C(s)=max(1/10,1/(C+1)).

For 1<=C<=9, partition all nonzero integer triples by their moments. If v-u is nonzero, its integrality gives F_C>=1/(C+1). If v=u is nonzero, v is a nonzero multiple of three, giving F_C>=|u|/10>=3/10>2/7. If u=v=0, integrality of the inverse moments forces nonzero h to be a multiple of 12, whence F_C>=|h-u|/42>=2/7. Hence eta_p(C)>=min(2/7,1/(C+1)), with equality attained by r or s. Equality of the branches occurs exactly at C=5/2.

For 9<=C<=59, the three C-dependent denominators do not exceed their values at C=59, so F_C(a)>=F_59(a) for every a. The whole-lattice baseline R105 has F_59(a)>=1/10; s attains 1/10 for C>=9. Hence eta_p=1/10.

For C>=59 put k=60/(C+1). All six ratios (denominator at 59)/(denominator at C) are at least k. The two nontrivial inequalities are 8C>=472 and 40C>=2360, true for C>=59. Thus F_C(a)>=k F_59(a)>=6/(C+1). Direction t attains the bound at q=27. When p<=26, u!=0 implies F_C>=1/10; u=0,h!=0 implies F_C>=6/42>1/10; u=h=0 implies a nonzero multiple of t and therefore q>=27. Hence the low-Port minimum is 1/10, attained by s. QED.

## Theorem 2 — Complete strict-near atlas at 1<=C<=9

A direction appears in N_p(C) **if and only if** it is among the ten rows below, p>=q, and C belongs to the stated interval. q is the exact minimum Port budget.

| Unoriented direction a | q | Exact C interval |
|---|---:|---|
| (4,-1,0) | 4 | (4/3,17/4) |
| (5,-1,0) | 5 | (4/3,13/2) |
| (6,-4,1) | 7 | [1,17/4) |
| (10,-5,1) | 11 | (4/3,9] |
| (11,-5,1) | 12 | (4/3,13/2) |
| (15,-6,1) | 16 | [1,4) |
| (16,-9,2) | 18 | (4/3,97/23) |
| (21,-10,2) | 23 | [1,4) |
| (25,-11,2) | 27 | (4/3,11/4) |
| (31,-15,3) | 34 | (4/3,11/4) |

For p>=34 exactly ten strict-near directions occur throughout 4/3<C<11/4; at C=9 only (10,-5,1) remains.

**Whole-lattice proof.** On 1<=C<=9, eta_p(C)<=2/7. A direction with F_C<(3/2)eta_p(C) necessarily satisfies |u|<=4, |h|<=21, |h-u|<=17. The exact maximum of (3/2)eta_p(C)(C+9) is less than 5, giving |v|<=4; the maximum with C+41 is less than 19, giving |h-v|<=18; and (3/2)eta_p(C)(C+1)<=3/2, giving |v-u|<=1.

The exact inverse integer moment map is

    x=(h+19u-8v)/2,
    y=(-h-14u+7v)/3,
    z=(h+11u-6v)/12,

with necessary and sufficient congruences

    v ≡ 0 (mod 3),
    h-u ≡ 0 (mod 6),
    h-u-6v ≡ 0 (mod 12).

The finite integer box u=-4..4, v=-4..4, h=-21..21, together with the three difference bounds and congruences, has exactly 20 nonzero oriented solutions, namely the ten unoriented directions in the table. The companion verifier checks this entire finite certificate. All integer directions outside the box are excluded by a rigorous observer inequality.

For 1<=C<=5/2 the strict cutoff is constant 3/7. The three variable denominators imply the lower walls

    C > max(7|v|/3-9, 7|v-u|/3-1, 7|h-v|/3-41).

For 5/2<=C<=9 the strict cutoff is 3/[2(C+1)]. Fixed observer terms impose

    C < 3/(2 f_fixed)-1,
    f_fixed=max(|u|/10,|h|/50,|h-u|/42).

The v and h-v terms, where their coefficients are positive, impose respectively

    C < (27-2|v|)/(2|v|-3),
    C < (123-2|h-v|)/(2|h-v|-3).

Because |v-u|<=1, its comparison with the moving strict cutoff is automatic. Exact substitution of the ten moment triples yields all endpoint intervals, including strict/excluded equality walls. QED.

## Theorem 3 — Complete strict-near atlas at 9<=C<=59

Select exactly the rows with p>=q and C>L.

| Unoriented direction a | q | Strict lower wall L |
|---|---:|---:|
| (1,0,0) | 1 | 37/3 |
| (5,-4,1) | 6 | 37/3 |
| (9,-5,1) | 10 | 19 |
| (10,-5,1) | 11 | 17/3 |
| (14,-9,2) | 16 | 97/3 |
| (15,-9,2) | 17 | 19 |
| (19,-10,2) | 21 | 77/3 |
| (23,-14,3) | 26 | 157/3 |
| (24,-14,3) | 27 | 39 |
| (25,-14,3) | 28 | 77/3 |
| (29,-18,4) | 33 | 157/3 |
| (34,-19,4) | 38 | 137/3 |

**Proof.** F_C>=F_59 and eta_p(C)=eta_p(59)=1/10 on this interval. Thus no direction outside the complete R105 twelve-direction carrier can become strict-near as C decreases. Comparing all six exact observer terms with 3/20 for those twelve rows yields the lower walls. The displayed rule agrees with Theorem 2 at C=9 and includes all twelve at C=59. QED.

## Theorem 4 — Complete strict-near atlas at C>=59

Let E8 be directions (1,0,0), (5,-4,1), (9,-5,1), (15,-9,2), (19,-10,2), (23,-14,3), (25,-14,3), (29,-18,4).
Let E3 be (10,-5,1), (14,-9,2), (34,-19,4).
Let E1 be (24,-14,3).
Their q-values are those from Theorem 3.

- When 11<=p<=26, N_p(C) consists of the eight Theorem-3 directions with q<=26, further filtered by q<=p, for every C>=59.
- When p>=27 and 59<=C<62, N_p(C)=(E8 union E3 union E1) filtered by q<=p.
- When p>=27 and 62<=C<89, N_p(C)=(E3 union E1) filtered by q<=p.
- When p>=27 and C>=89, N_p(C)=E1.

**Proof.** For p>=27, F_C>=k F_59 with eta_p(C)=k eta_p(59). Thus every C-near direction must lie in the R105 twelve-direction carrier. Its exact fixed-observer upper walls are C<62 for all E8 and C<89 for all E3, with no finite upper wall for E1. Direct substitution verifies the remaining observer inequalities.

For p<=26, F_C<3/20 forces |u|<=1, |h|<=7, |h-u|<=6 independently of C. Port q<=26 implies |z|<=26; by the exact inverse, |v|<=55. The three congruences in this finite range and the Port bound leave exactly 16 nonzero oriented (=8 unoriented) candidates, the q<=26 subset of Theorem 3. Each was already strict-near at C=59, and F_C is nonincreasing for C>=59. QED.

## Exact verification

Companion script: research_notes/portable_direct/x6_r108_full_C_ray_verify.py.
Companion result: research_notes/portable_direct/x6_r108_full_C_ray_results.json.

- Low-C mathematically complete moment box: 20 nonzero oriented / 10 unoriented.
- High-C low-Port mathematically complete box: 16 nonzero oriented / 8 unoriented.
- Exact linear inequality wall calculations: ten low-C rows plus twelve mid-C rows.
- Independent finite brute force: all 110,740 unoriented integer triples q<=40; 66 exact rational C values (including critical thresholds and nearby rational points); 14 Port budgets; 924 full optimal-value and strict-near-set assertions, all PASS.

The infinite-lattice assertions are established by the written analytic integer-box reductions and inherited R105 author proof. The brute-force verification is separately limited to the stated q/C/p inputs. No independent mathematical review or formal Result acceptance has occurred.

## Scientific increment and next question

The entire positive ray w=(9,1,C,41), all real C>=1, is now classified for both exact optimum and all strict 3/2-near integer directions, at every integer Port p>=11. Near multiplicity is nonmonotone along C: ten directions for 4/3<C<11/4 at p>=34, one at C=9, twelve for 157/3<C<62 at p>=38, and one for C>=89 at p>=27.

Next: determine whether any positive quadruple (A,B,C,D) admits 13 strict-near directions, or strengthen R104's universal 13 upper bound to 12. A discriminating approach is exact projective mod-3 saturation combined with six-pair denominator constraints. Separately, a native P000/R063 signed Cell/Link/Port/triadic-event/heartbeat-time readout bridge remains open and must preserve branch/path provenance.

Provenance: preserve the original R105–R107 authors, science pins and unreviewed status. This independent auxiliary BRC result is not a native X6 CLAIM, PROGRESS, Result or Review.