# R284CK — Exact 64-level k-fold Port-fiber covering spectrum

Date: 2026-11-21, Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED. Independent portable Port-observer continuation of R284CJ; no canonical Task CLAIM or Result admission.

## Exact frozen inputs and observables

Retain precisely the 34-bit Port model: p=17179869143, D=(1120832,6,13,1651128), Z=(0,390139,394465,1497639), all C in {1,2}^{4×4}; original codeword stream SHA-256 b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4. Preserve the 64 coarse fibers determined by (C_10,C_11,C_12,C_20,C_21,C_22), with their closed minimal covering circular arcs A_i=[a_i,a_i+w_i], 0<w_i<p/2.

Frozen scientific origin: [R284CJ](https://github.com/awdawmip/enterprise-math/blob/e6d09af71b07e17ff7743a66ea20e9a5affe840d/research_notes/portable_direct/R284CJ_FULL_RADIUS_KINETIC_FIBER_ATLAS_20261121.md), derived from [R284CI](https://github.com/awdawmip/enterprise-math/blob/7e030dac04d573dbd8cb1b872141da074cb946f8/research_notes/portable_direct/R284CI_100BYTE_SHARP_PARAMETRIC_EVENT_20261121.md). This work changes only the observation radius and the cardinality statistic, not any codeword, P000 assumption, mathematical pin, or original unique-matrix error radius.

Define N_rho(y)=# {i in {0,...,63}: dist_circle(y,A_i) <= rho}, with real y on R/pZ, real rho>=0. Let T_k = inf {t>=0: for every y, N_(t/2)(y)>=k}, k=1,...,64. The infimum is attained.

## Theorem A — complete k-fold covering-radius spectrum

The exact values of T_k (in doubled-radius units t=2rho) are as follows; all are integers and all 64 are distinct.

| k | T_k=2rho_k |
|---:|---:|
| 1 | 440613304 |
| 2 | 1081059415 |
| 3 | 1487733301 |
| 4 | 1531656496 |
| 5 | 1805603549 |
| 6 | 2140338276 |
| 7 | 2340124953 |
| 8 | 2508437496 |
| 9 | 3055772081 |
| 10 | 3476011011 |
| 11 | 3882684897 |
| 12 | 3988319407 |
| 13 | 4194926292 |
| 14 | 4425970509 |
| 15 | 4654955271 |
| 16 | 4957452505 |
| 17 | 5338453418 |
| 18 | 5446674704 |
| 19 | 5680466152 |
| 20 | 6026239156 |
| 21 | 6356755654 |
| 22 | 6776994584 |
| 23 | 7049906867 |
| 24 | 7352404101 |
| 25 | 7702644825 |
| 26 | 7808279335 |
| 27 | 8014886220 |
| 28 | 8421190752 |
| 29 | 8526825262 |
| 30 | 8808172622 |
| 31 | 9158413346 |
| 32 | 9266634632 |
| 33 | 9507982742 |
| 34 | 9876959273 |
| 35 | 10183687503 |
| 36 | 10296300448 |
| 37 | 10576769393 |
| 38 | 10726973115 |
| 39 | 10963751263 |
| 40 | 11433885077 |
| 41 | 11639456024 |
| 42 | 11860930857 |
| 43 | 12086490052 |
| 44 | 12286276729 |
| 45 | 12557641241 |
| 46 | 12977880171 |
| 47 | 13408597743 |
| 48 | 13828836673 |
| 49 | 14011204093 |
| 50 | 14255882453 |
| 51 | 14372122285 |
| 52 | 14568123848 |
| 53 | 14814234656 |
| 54 | 15284605194 |
| 55 | 15466972614 |
| 56 | 15711650974 |
| 57 | 15819872260 |
| 58 | 15904300658 |
| 59 | 16184011290 |
| 60 | 16443081827 |
| 61 | 16626971629 |
| 62 | 16756468559 |
| 63 | 16792259144 |
| 64 | 16872276929 |

In particular: T_1=440613304, T_4=1531656496, T_8=2508437496, T_16=4957452505, T_32=9266634632, T_48=13828836673, T_64=16872276929. For each k and every real observation y, radius rho>=T_k/2 guarantees at least k coarse-fiber labels, whereas for any rho<T_k/2 there exists a y with fewer than k. This quantifier order concerns uniform all-circle *candidate support*, not identification of the underlying complete matrix or any native BRC state.

At rho=0, exact minimum N=0 and maximum N=4. At rho=T_1/2, the minimum is one and maximum six. At rho=T_64/2, every arc is saturated and N=64 at every y.

## Theorem B — mean candidate count independent of kinetic swaps

For uniform circular observation y (normalized Haar/length measure, as a mathematical observer model, not a claim about the frozen codeword distribution),

E_y[N_rho(y)] = (1/p) sum_(i=0)^63 min(p,w_i+2rho).

Consequently, away from the 64 saturation radii its derivative equals (2/p) times the number of unsaturated fibers. There are precisely 64 piecewise-linear slope changes, even though the circular endpoint order has 3955 distinct pairwise swaps (R284CJ). At zero radius, the exact mean is 24072341088/17179869143. The mean is not interchangeable with the maximum or minimum candidate count: at rho=0 the minimum is zero and maximum four.

*Proof.* A_i enlarged by circular radius rho has length min(p,w_i+2rho). Integrate its indicator over the circle and sum the 64 indicators. Finite additivity gives the formula and its derivative. Crossing another fiber's boundaries changes intersection patterns but not an individual enlarged arc's length.

## Finite exhaustive proof of Theorem A

1. For a nonsaturated arc i, its endpoints in doubled observation coordinates (the circle of circumference 2p) are E_i(t)=2a_i-t and X_i(t)=2(a_i+w_i)+t (mod 2p). The only changes in *cyclic* order can occur at an EXIT/ENTRY collision. A pair (i,j) has the exact candidate t_ij=(a_j-a_i-w_i) mod p and is active precisely when 0<t_ij<min(p-w_i,p-w_j). Additionally arc i saturates exactly at t=p-w_i.
2. Exhausting all 4096 ordered pairs and 64 saturation conditions yields 3955 active, pairwise-distinct crossings, 64 distinct saturations, no shared t values and exactly 4019 breakpoint parameters. On each interval of t excluding those breakpoints, the cyclic order of endpoints and the set of full arcs are constant. Thus the minimum and maximum of N_(t/2)(y) over y are constant there.
3. At every fixed breakpoint parameter, a sweep over all distinct circular endpoints gives exact membership on each *open* cell. At a boundary the closed-arc membership set contains the union of both neighboring limiting sets, so its cardinality cannot be smaller than either adjacent cell; the minimum is attained in an open cell (or everywhere if all arcs saturate). For rho increasing, every enlarged arc grows monotonically, so the pointwise count and its circle minimum are nondecreasing.
4. Therefore scanning t=0 and each of the 4019 breakpoints, recording the first t for which the circle minimum reaches k, proves T_k exactly for *all real t*, not just sampled radii. The companion checker obtains the 64 values above, with a strictly increasing sequence of coverage minima. For each k, it verifies a deficient open-cell rational midpoint at t=T_k-1 and all open cells at t=T_k. As every breakpoint is integral and no other breakpoint intervenes on (T_k-1,T_k), this also certifies sharpness at the real boundary.
5. All arithmetic is exact integers. The independent membership check evaluates each open-cell midpoint in fourfold circular coordinates; it compares each sweep cardinality against 64 direct enlarged-arc predicates, instead of trusting sweep state alone. The complete run checked 510300 open cells across all 4020 critical parameters, plus 8062 threshold witness/at-threshold direct checks. The original 65536-codeword SHA-256 was independently reproduced.

This is a finite proof with an explicit exhaustive domain and a general real-parameter reduction. The theorem is scoped to these 64 *covering arcs*. It does not treat nonmember codewords, actual codeword multiplicities, a genuine native spatial quotient or BRC signed/positive carrier as though they were established by arc counting.

## Reproducibility and independent evidence boundaries

Companion script: R284CK_kfold_coverage_checker.py. Certificate: R284CK_kfold_coverage_certificate.json. The checker builds the exact arcs from the frozen determinant and runs every eligible crossing/saturation parameter, direct open-cell midpoint checks, threshold witnesses, and original frozen SHA consistency. Explicit frozen inputs are executable constants; no floating-point evaluations, numeric tolerances, external package, or random sampling are used.

Validation conducted locally on 2026-11-21: 65536 exact codewords, 4096 ordered potential collisions, 4019 critical radii, 510300 direct cell checks, 8062 boundary-threshold checks. GitHub publication/readback and independent mathematical review are tracked separately; later users should not infer an independent acceptance from a successful script.

The exact observer is a finite Port-fiber support statistic; application to a specific X6 native BRC calculation or heart-beat motion would require its own typed correspondence, state/provenance and quotient preservation proof.

## Follow-up scientific questions

Find a direct combinatorial description or fast rank-select index for the spectrum T_1,...,T_64 without sweeping 4019 critical parameters. Compare worst-case candidate multiplicity with expected multiplicity under the *finite frozen codeword population* rather than uniform circle y. A dynamic event-swap index may update adjacent circular boundaries and saturation in place; benchmark its full initialization, memory and query costs against the 100-byte coefficient compiler and 760/976-byte indexes.

Provenance: R284CJ->R284CK independent portable continuation. Historical attribution EM-DIRECT-20B766 / RA-617F40704F37299B15489DCA is preserved as origin only; current possession of a service-issued session capability is not asserted here. Current owner snapshot is observation-only and this file does not create a Task CLAIM.
