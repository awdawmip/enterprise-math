# D25/LIFT — exact composite-cutoff falsifier and prime-block provenance for the 216↔2304 comparison

Date: 2026-10-28 Asia/Hong_Kong. Research classification: **AUTHOR-SIDE / EXACT FINITE COUNTEREXAMPLE / TWO INDEPENDENT INTEGER ALGORITHMS EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_EXECUTED**. This is a boundary result, *not* a proof or disproof of the prime-only supercongruence.

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` (OPEN). Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Prior own-lane research label `chatgpt-research-onhour-enterprise-math-20260923`; no maintenance identity, native session or claim is assumed.

## Original full-cutoff objects and inherited OPEN assertion

For any positive integer N with gcd(N,6)=1 define the *same original term formulas* and the full cutoff N-1:
[
t_n=rac{inom{2n}{n}^2inom{3n}{n}}{216^n}
=rac{(2n)!(3n)!}{(n!)^5 216^n},qquad
s_n=rac{inom{2n}{n}^2inom{4n}{2n}}{2304^n}
=rac{(4n)!}{(n!)^4 2304^n},
]
[
A_N=sum_{n=0}^{N-1}(6n+1)t_n,qquad
B_N=sum_{n=0}^{N-1}(8n+1)s_n.
]
The research conjecture **for prime** (N=p>3) is (A_pequiv B_pmod p^3). The earlier author-side 781-prime computation and the published Guo–Zudilin theorem for (B_p) remain input/provenance only. Do **not** extend their quantifier or theorem to composite N. Prior all-prime proof of transport remains OPEN.

## New exact finite counterexample to any unrestricted integer-cutoff lift

For N=85=5·17, both denominators are units modulo N³=614125. Full original 85-term exact integer computations give
[
oxed{A_{85}equiv416500,quad B_{85}equiv144500pmod{614125}.}
]
Thus
[
oxed{A_{85}-B_{85}equiv272000pmod{614125},
qquad A_{85}-B_{85}equiv4675
e0pmod{85^2=7225}.}	ag{C85}
]
In particular even the weaker universal statement (A_N=B_Nmod N^2) for all N≡1(mod6), gcd(N,6)=1 is **false**. This does not challenge the prime conjecture; it precisely falsifies extension of the *cutoff-length* quantifier to all such composite N.

An independent prime-only control using the same original objects at p=17 gives
[
A_{17}equiv B_{17}equiv4896=-17pmod{17^3=4913},
]
whereas the composite N=85 outputs satisfy
[
oxed{A_{85}equiv51,quad B_{85}equiv0pmod{17^2=289}.}	ag{P17}
]
Therefore even local 17-adic equality at the length-17 prime cutoff cannot be transported to length 5·17 by a naive CRT argument. This is **cutoff-sensitive**, not merely a change of ambient modulus.

The distinct weaker precision boundary N=25=5² gives (A_{25}=3150, B_{25}=9400pmod{25^3}), difference (9375=15cdot25^2pmod{25^3}): it passes mod N² but fails mod N³. N=25 and 85 are independent witnesses with different failure precision; do not infer all composites have the same valuation.

## Source-labeled 17-adic block decomposition

Partition the complete N=85 cutoff into five blocks of length p=17. Direct original signed sums in the ring Z/289Z give the following **exact finite certificate**:

| original indices n | A-block | B-block | signed difference |
|---|---:|---:|---:|
| 0–16 | 272 | 272 | 0 |
| 17–33 | 170 | 170 | 0 |
| 34–50 | 255 | 0 | 255 = 15·17 |
| 51–67 | 238 | 204 | 34 = 2·17 |
| 68–84 | 272 | 221 | 51 = 3·17 |
| whole cutoff, mod 289 | 51 | 0 | 51 = 3·17 |

The last three signed differences add to 340≡51 mod289. In particular, equality of the first prime block and second block does **not** guarantee equality after the allowed future operation "append the remaining three blocks."

A concrete carry-changing source index is n=73, inside the final block. By Legendre's factorial valuation formula at p=17:
[
v_{17}(t_{73})=v_{17}(146!)+v_{17}(219!)-5v_{17}(73!)=8+12-5cdot4=0,
]
[
v_{17}(s_{73})=v_{17}(292!)-4v_{17}(73!)=(17+1)-4cdot4=2.
]
The extra (+lfloor292/289floor=+1) is the **second-level p² factorial carry** in the 2304 kernel, absent in the 216 kernel at this index. Consequently the *weighted* n=73 residues mod289 are
[
(6cdot73+1)t_{73}equiv232,qquad
(8cdot73+1)s_{73}equiv0pmod{289}.
]
One signed term is a 17-adic unit while the other vanishes mod17². Other indices still cancel these sources modulo17 to yield the block-level multiple of 17. A scalar-only quotient equating the 17-blocks or indices mod17 would erase the actual reason for the precision change.

## Actual execution, exact verification, mathematical scope

Companion standard-library executable:
`research_notes/portable_direct/d25_composite_cutoff_block_guard_20261028.py`, first immutable source commit `ea4764cee0f5658ff8d3f515afe82b35a75692ea`, Git blob SHA-1 `61a6f7bac52f76f0eed238a9c412d348606e85b4`. The local executable byte identity and remote blob were independently compared.

The program was **actually executed** with assertions. It computes original summands through two independent integer routes: (i) `math.comb` binomial products and (ii) factorial quotients. It checks full lengths N=17,25,85 modulo N³; computes the five original 17-length blocks modulo 17² independently by both routes; verifies valuation and weighted term at n=73. All assertions passed; marker:
`PASS_D25_N85_COMPLETE_CUTOFF_CRT_FALSIFIER`.

This is a rigorous **finite arithmetic falsifier** of a quantified composite extension. It does *not* prove global prime transport, does not prove a universal prime-block transformation, does not execute H0/B0, and does not upgrade any prior AUTHOR-SIDE theorem to an admitted Result.

BRC / residual typing: original carrier ((N,p,n,	ext{kernel A/B},6n+1	ext{ or }8n+1,
u_p,	ext{block},	ext{factorial carry},	ext{signed residue})). Observer is complete weighted truncated sum modulo the stated exact modulus; allowed future operation is append more original index blocks or increase p-adic precision. The prime-cutoff equality is **not** an observer-safe quotient under changing the cutoff to 5p, because source provenance and factorial carries change. This arithmetic observer is an explicitly external model, not a new X6 spatial axis, a 2D plane, or native divided-power evidence. ACTIVE P000 six spatial axes and separately typed time remain fixed.

## Native hard target / exact continuation

The highest-priority **native** missing object is unchanged: [Enterprise Math support issue #1559](https://github.com/awdawmip/enterprise-math/issues/1559), original same-class p=373 H0/B0 divided-power `[X]U mod139129`, genuine module rank, Frobenius/eta direction, signed odd Green/Hesse, original κ and Δp−Rp, with raw source/version and independent validation. At this turn's read, #1559 was OPEN with no assigned executing owner: **PENDING_OWNER / NATIVE_NOT_EXECUTED**. No scalar finite calculation supplies it.

Current Site gateway at 2026-10-28 read: v0.6.11, Research authority false, write relay false, executor binding false, SOURCE code review required; active native control request quota 5/5. No new session, CLAIM, open, dispatch, Source checkpoint, Result or official Research-Activity has been created. Existing historical Research lane request/staging/owner status was not reissued or replaced. The global knowledge journal is only a loss-prevention mirror.

**Next mathematical action:** return to the original *prime-only* source-bound p³ target, proving or refuting the previously derived halfcut identity (T1) with the A high-tail inverse-unit correction, using a finite WZ/CM transformation whose proof specifically exploits prime p and preserves the entire p−1 cutoff. Do not repeat composite trials or replace the genuine native benchmark. D25/LIFT/JT2 remains OPEN; the frozen scientific source pin is unchanged.
