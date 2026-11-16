# PREFIX-838 — Parity-refined three-source even-time weight bound and exact optima T=42..80

Date: 2026-11-16. Status: AUTHOR_PROVED / EXACT_FINITE_EXHAUSTION / EXACT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

**Immutable scientific input:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Science continuity:** PREFIX-832 complete named-source future histogram, PREFIX-834 even-time recollision criterion and three-source construction, PREFIX-835 exact maxima for even T=4..40, PREFIX-836 Pell subsequence, PREFIX-837 distinct two-source odd-time sharp resource law. Current behavioral rules are read from canonical global knowledge separately from the science pin. This is the **positive weighted named-source BRC Q-only auxiliary model**, not an assertion about native X6 physical time or signed amplitude.

## Model and statement

Let p=q=3, with three individually named initially present unmarked sources and no marked source. Positive integer removal weights are an unordered triple. At each step the nonnormalized weighted branching operator Q=R+A sums all legal removal alternatives, and adds the marked source with weight a=1 when absent and capacity permits; marked removal weight b=2. Output Y(t) is the complete integer occupancy-count histogram (bins 0..3). For each even integer T>=4 let M(T) be the least possible largest weight of two **distinct** source-weight multisets with Y_A(1)=Y_B(1), some positive-time difference, and Y_A(T)=Y_B(T).

**Theorem 838.1 (universal parity-refined lower bound).** For every even integer T>=4,

```
T ≡ 0 (mod 4): M(T) >= 1 + ceil(sqrt(9*(T-2)/2)).
T ≡ 2 (mod 4): M(T) >= 1 + ceil(sqrt(9*(T-2)/4)).
```

The square-root is an exact integer-ceiling expression, not a floating approximation. This strengthens the general PREFIX-835 lower estimate M(T)>=ceil(sqrt((T+2)/4)), with different constants in the two residue classes.

**Proof.** Write e_j for the elementary symmetric coefficients of a three-source weight multiset, and Δe_j=e_j(A)-e_j(B). At t=1, the only nonzero occupancy bin is bin 2, equal to e_1; hence equality at t=1 gives Δe_1=0. The exact named-source trace difference from PREFIX-832 gives, at each even T>=4, bin 3 difference zero and bin 1 difference equal to
```
(T-1)*2^((T-4)/2)*[ 4*Delta_e2 + 3*(T-2)*Delta_e3 ].
```
The other bins have zero support by occupancy parity. Thus full re-aliasing occurs exactly when
```
4*Delta_e2 + 3*(T-2)*Delta_e3 = 0.          (838.1)
```
If both differences vanish, then equal e_1,e_2,e_3 give identical monic cubic root multisets, contrary to distinct A,B. Thus Δe_2 and Δe_3 are nonzero integers.

Put m=(T-2)/2. Then (838.1) is 2 Δe_2 = -3m Δe_3. If T divisible by 4, m is odd, which forces Δe_3 even; therefore |Δe_2|>=3m=3(T-2)/2. If T≡2 mod4, m even, and |Δe_3|>=1 gives |Δe_2|>=3m/2=3(T-2)/4.

It remains to prove a **sharp uniform range lemma:** any two three-element real lists in [1,W] with equal sums obey
```
|Delta_e2| <= (W-1)^2 / 3.                  (838.2)
```
For W=1 all triples coincide, so assume W>1. Normalize each entry as 1+(W-1)u_i with 0<=u_i<=1. Since the sums agree, the linear parts of e_2 cancel and Δe_2=(W-1)^2 Δe_2(u). Fix s=u_1+u_2+u_3 in [0,3]. The maximum e_2(u) is s²/3 (equal coordinates). The minimum occurs at a vertex of the fixed-s capped cube, i.e. at (s,0,0) for 0<=s<=1, (1,s-1,0) for 1<=s<=2, or (1,1,s-2) for 2<=s<=3, up to permutation. The corresponding ranges are s²/3, (s²-3s+3)/3, and (s-3)²/3; all <=1/3. (The minimum is attained at a boundary because transferring mass from a smaller positive coordinate to a larger one decreases e_2 at fixed sum until a boundary is hit.) This establishes (838.2). Combining the two parity-dependent lower bounds on |Δe_2| with (838.2) gives (W-1)²>=9(T-2)/2 and >=9(T-2)/4, respectively. Integer ceiling proves the theorem. QED.

**Theorem 838.2 (20 exact finite optima).** For each even T from 42 through 80 inclusive, the values M(T) in the table below are exact global optima for the stated three-source positive-integer model. Together with PREFIX-835 they extend the computed certified window to every even 4<=T<=80. The theorem is a finite exhaustive result, with no extrapolation to all T.

## Complete new finite-optimum certificates

| T | Exact M(T) | Bound 838.1 | A weights | B weights | Δe2 | Δe3 |
|---:|---:|---:|---|---|---:|---:|
| 42 | 96 | 11 | (10,29,90) | (16,17,96) | 360 | -12 |
| 44 | 66 | 15 | (14,46,54) | (17,31,66) | 189 | -6 |
| 46 | 35 | 11 | (1,18,23) | (3,4,35) | 198 | -6 |
| 48 | 71 | 16 | (13,58,58) | (14,44,71) | 138 | -4 |
| 50 | 61 | 12 | (9,48,48) | (10,34,61) | 144 | -4 |
| 52 | 78 | 16 | (2,34,57) | (5,10,78) | 900 | -24 |
| 54 | 53 | 12 | (6,31,41) | (9,16,53) | 234 | -6 |
| 56 | 68 | 17 | (10,49,58) | (11,38,68) | 162 | -4 |
| 58 | 82 | 13 | (4,29,72) | (6,17,82) | 504 | -12 |
| 60 | 57 | 18 | (16,46,46) | (18,33,57) | 87 | -2 |
| 62 | 65 | 13 | (2,27,54) | (3,15,65) | 405 | -9 |
| 64 | 77 | 18 | (1,38,48) | (4,6,77) | 1116 | -24 |
| 66 | 74 | 13 | (6,36,63) | (8,23,74) | 384 | -8 |
| 68 | 42 | 19 | (2,26,29) | (3,12,42) | 198 | -4 |
| 70 | 53 | 14 | (1,14,45) | (3,4,53) | 306 | -6 |
| 72 | 106 | 19 | (14,73,73) | (22,32,106) | 945 | -18 |
| 74 | 81 | 14 | (11,56,71) | (12,45,81) | 216 | -4 |
| 76 | 81 | 20 | (13,58,58) | (18,30,81) | 444 | -8 |
| 78 | 48 | 15 | (2,27,31) | (5,7,48) | 342 | -6 |
| 80 | 94 | 20 | (6,49,69) | (12,18,94) | 1053 | -18 |

Example T=68 achieves M(68)=42 with A=(2,26,29), B=(3,12,42). Here Δe1=0, Δe2=198, Δe3=-4, so 4*198+3*66*(-4)=0. Independent full named-source branching confirms equality at t=0,1,68 only through step 70.

## Finite-optimality algorithm and verification

The standalone program `PREFIX838_R6_EVEN_PARITY_RESOURCE_CHECK.js` uses JavaScript exact safe integer arithmetic for e_1,e_2,e_3 and hash key (e_1,4e_2+3(T-2)e_3), and BigInt for every branching count. For each target T, it iterates maximum weight W=1,2,... in ascending order and enumerates **every** sorted integer triple 1<=x<=y<=z=W. The first two different triples sharing a key have equal e_1 and satisfy (838.1), so give a legal complete-observer re-alias at T. No pair with a smaller maximum weight is omitted: all triples having maxima below W have already been inserted in the map. Hash collisions are checked by the algebraic invariants rather than relying on a non-exact numerical observer. Distinct triples with the same e_1 and key have necessarily different e_2 and e_3 because equality of all three coefficients would force identical roots.

The checker then independently evolves all 16 possible (named-subset mask, marked-presence bit) states with the actual legal Q weighted transitions from initial named mask 111 and marked bit 0. For every optimal pair, it compares all four histogram bins from t=0 through T+2 and asserts the **exact equality-time set is {0,1,T}**. None of the observation values uses float arithmetic. The hash key remains below IEEE-754 exact integer maximum in the scanned finite range; BigInt independently validates full source dynamics.

Run `node PREFIX838_R6_EVEN_PARITY_RESOURCE_CHECK.js > PREFIX838_R6_EVEN_PARITY_RESOURCE_RESULTS.json` to regenerate the stored results byte-for-byte. The completed run reports **20 exact finite optima**, **1,350,734 enumerated triples (summed across independent searches)** and **5,120 exact histogram scalar comparisons**; `ALL_EXACT_ASSERTIONS_PASSED`.

## Research interpretation, limitations, next actions

The new parity factor tightens the resource obstruction for fixed capacity three-source Q recollision; this is an observer-specific positive-count theorem. The Pell construction of PREFIX-836 remains a square-root resource **upper bound on a subsequence**, and the new bound gives stronger constant floors there. The finite T=42..80 global optima show considerable irregularity (for example M(68)=42 versus M(72)=106), motivating a structural study of the arithmetic gaps in the Diophantine collision lattice.

Next: investigate whether all even T admit a uniform O(sqrt T) upper bound, or exhibit a rigorous infinite sequence with larger minimal M(T); compute exact optimum certificates at selected larger T using an optimized modular/source-residual sieve. Separately retain the q>=5,b>0 minimal positive nonnegative Q-carrier problem and the typed X6 native-event coupling gap. There is no change to P000, foundation admission, shared ownership, or the scientific source pin.
