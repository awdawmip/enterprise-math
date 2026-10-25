# R1 / N14 external ternary iid sequential test — Stage122 exact affine interval

**Evidence status:** AUTHOR_EXACT_COMPUTATION_ASSISTED_PROOF; independent Research Driver review and native Result admission are pending. This finite iid auxiliary theorem is NOT a theorem for the P000 native six-dimensional Cell space.

## Precise statement

Take N=14, alphabet {0,1,2}, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Policies may stop and randomize depending on the full ordered history. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf max(tP,tQ) subject to both errors <=alpha.

The Stage121 author-proved starting point is

- alpha121=2573764738946831699425/7411551152237344456704;
- V121=378361775997993165503285/29646204608949377826816.

Put K=27085186670001462/35130967563833, L=25607353643447976/35130967563833, S=K+L=52692540313449438/35130967563833, and eta122=2986132242925805/274501894527309053952.

**Theorem for every real delta in [0,eta122]:**

$$V_{14}(\alpha_{121}+\delta)=V_{121}-S\delta.$$

Its exact endpoint is

$$\alpha_{122}=\frac{80432667641168459255}{231610973507417014272},\qquad
V_{122}=\frac{377878058477915699662445}{29646204608949377826816}.$$

This affine Bellman support line is right-sharp: its equality cannot hold at any alpha>alpha122.

## Universal dual bound: all ordered-history policies

At count state s=(n,a,b), with a counting symbol 0 and b counting symbol 1, the likelihood ratio is Q(prefix)/P(prefix)=2^(a+b)/3^a. Set H(s) to the minimum among:

1. declare P: K*2^(a+b)/3^a;
2. declare Q: L;
3. if n<14, continue: 1+(1/8)H(n+1,a+1,b)+(1/24)H(n+1,a,b+1)+(5/6)H(n+1,a,b).

Complete exact rational backward induction has 680 count states, 1238 strictly positive alternative-action gaps, zero negative gaps and precisely two tie states:

- A=(9,3,0), declare P / continue;
- F=(3,0,2), declare Q / continue.

The minimum positive gap is 968911136726508551639/90634038091307409604608. The root value is

H(0)=513473783136657607345300527155135/962246355897011428127309561856
     =V121+S*alpha121.

For an arbitrary literal ordered prefix, its likelihood ratio and conditional iid suffix transition coincide with those of its count state. Thus Bellman induction applies to **every** randomized ordered-history policy, not merely count-Markov policies:

H(0) <= tP+L*eP+K*eQ <= max(tP,tQ)+S*alpha.

Therefore V14(alpha)>=H(0)-S*alpha.

## Attainment: exact positive-rational BRC carrier and disjoint first-hit cones

At A declare P with probability y (else continue); at F declare Q with probability r (else continue); elsewhere choose the unique Bellman minimizer. Enumerating literal ordered first-hit words gives

| tie | first-hit words | P mass | Q mass |
|---|---:|---:|---:|
| A=(9,3,0) | 84 | 109375/1990656 | 109375/6718464 |
| F=(3,0,2) | 3 | 5/1152 | 5/288 |

F cannot precede A on one word: b_F=2>b_A=0, and cumulative counts never decrease. A cannot precede F because its depth 9 exceeds depth 3. Consequently the four declared observers have NO mixed y*r term; ordered-provenance and separate P/Q positive masses are retained before an iid-justified count quotient.

With M=(eP,eQ,tP,tQ) we obtain M(y,r)=M00+y*dA+r*dF exactly:

M00=(608842905486837911/1752976676930715648,
27860458683925/80244904034304,
2799712766106923261/219122084616339456,
81040087991357/6687075336192).

dA=(-1921609375/7925422620672,
259765625/835884417024,
-20758609375/330225942528,
-1476453125/69657034752).

dF=(947963206745/21641687369515008,
-6702333665/213986410758144,
-21047123534965/2705210921189376,
-443412559855/17832200896512).

The equality eP=eQ determines

$$y(r)=\frac{665696150804933}{2909391744000000}
+\frac{5267621485201}{38791889920000}r.$$

For ALL real r in [0,1] these are legal probabilities: y(0)=665696150804933/2909391744000000 and y(1)=2367785183471/6494178000000<1. The common error is alpha(r)=alpha121+eta122*r. At the two endpoints respectively,

tP-tQ=19225764576247514675621/29646204608949377826816>0,
tP-tQ=19564553826414832986221/29646204608949377826816>0.

The time margin is affine and hence positive on the WHOLE real interval. Every used action is Bellman minimizing, both errors equal alpha, and max(tP,tQ)=tP, so the lower bound is attained throughout that interval.

## Strict right-sharpness of the support line

The finite collection of ordered-history randomization parameters is compact and an optimum exists. Suppose an alpha>alpha122 attains the same positive-multiplier support. Equality in the dual chain requires eP=eQ=alpha and every positively reached action to be Bellman minimizing. The ONLY ties are A and F. Word-dependent mixing on a common count fiber can be weighted-averaged because the iid conditional suffix and likelihood ratio coincide; this preserves the four declared observers. With disjoint cones, all such policies are observer-equivalent to some (y,r) in [0,1]^2 obeying the unique balance equation above. But their balanced alpha increases strictly with r and r<=1 forces alpha<=alpha122. Contradiction. This is sharpness of this affine support, NOT a claim that larger errors are unachievable.

## Independent execution evidence, limits and next problem

Local execution used Python standard-library exact Fraction Bellman arithmetic and a logically separate literal ordered-word integer-weight DFS with P=(3,1,20)/24 and Q=(1,1,10)/12. At the four (y,r) binary corners, DFS visited 840811, 823333, 835771, 818293 nodes respectively; all 16 moment comparisons and four sets of first-hit counts/masses passed. Zero mixed finite difference and strict endpoint time gaps were explicitly checked. Source and numerical certificate are accompanying files. Source-equivalence is checked by GitHub immutable-readback, not by falsely claiming remote execution.

BRC tool outcome: REUSE_APPLIED for the positive-rational, multiplicity- and ordered-provenance-preserving carrier and exact four-observer pushforward; the published exact checker implements and exercises it. This is an external finite iid type, with NO unproved P000/native X6 readout bridge. Independent Driver mathematical review is pending. Native task inventory returned CONTROL_QUOTA; own native session request returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No CLAIM or Result is asserted.

Frozen research inputs: GLOBAL_KNOWLEDGE_V1 main@28719731af88def01da147f49d19fb0a91474b5d; Enterprise Math source main@6974c5530449705a1105bbadf5349c90ee65f574; Stage121 proof at research_notes/n14_aux_iid_affine_121_20261026/PROOF_STAGE121.md; verified P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. ACTIVE worldview and protected P000 are unchanged.

The Stage123 crossing in the next-task packet is an **exact dual candidate only**, not a proved original/primal interval.
