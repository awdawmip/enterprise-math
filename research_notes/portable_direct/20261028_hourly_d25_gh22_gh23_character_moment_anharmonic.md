# D25/LIFT GH-22 and GH-23 — two finite-field character moments; four-point cubic symmetry obstruction

Date 2026-10-28. **Author-side portable mathematical evidence:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is not a canonical research checkpoint or a claimed proof of the original W/S supercongruence.

Parent Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; Objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` remains OPEN. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. GH-17–GH-19 source proof/verification remains a separately preserved local portable package (remote synchronization debt); GH-20/GH-21 GitHub evidence at `4e04fe770be5a5f99a0d2e05efb78e648cd71991` and `17010f1d01c52fe5aa905fc8c2a6e826cb253124`.

## GH-22: a joint finite-field character-sum interface

Let **p=8m+3 >= 11 be prime**, m>=1, k=F_p, and
`F_m(z)=sum_{r=0}^m (-m)_r^2 z^r / ((2m+2)_r r!)`,
`G_m(z)=(16z d/dz+5)F_m(z)`,
`D_m=binom(3m+1,m)` (a p-unit).
Define the quadratic character `chi(x)=x^((p-1)/2)` including chi(0)=0.

**Theorem**: Two distinct channel identities hold exactly in k:

```
D_m F_m(9) = - sum_{x in F_p} chi(x) [x(1+x)]^(3m+1) (1+9x)^m
D_m G_m(9) = - sum_{x in F_p} chi(x) [x(1+x)]^(3m+1) (1+9x)^(m-1) (5-9x)
```

**Proof.** The exact GH-19 integer identity gives `D_m F_m(z)=[t^m]P_z(t)`, `P_z(t)=(1+t)^(3m+1)(1+zt)^m`, degree `4m+1`. For any `P(t)=sum_{0<=j<=4m+1} b_j t^j` over F_p, `[t^m]P=-sum_{x in F_p}x^(p-1-m)P(x)`: since p-1=8m+2, among powers `p-1-m+j` the only positive multiple of p-1 occurs at j=m; the complete-field power sum there equals -1, all others 0. Since `p-1-m=7m+2=(p-1)/2+(3m+1)`, the F identity follows, including x=0.

Differentiate the **original integer coefficient model** before reducing. Then
`D_m G_m(9)=[t^m](1+t)^(3m+1)(1+9t)^(m-1)(5+(16m+5)9t)`.
Because `16m+5=2p-1=-1 (mod p)`, the bracket is `5-9t`. Apply the same coefficient/power-sum identity. QED.

There is no division by `1+9x` in either formula; singular fibers and the entire composite/background population remain in the finite sum. These are exact equivalents of the as-yet **unproved** all-prime F-branch vanishing for p=19 mod24 and G-branch vanishing for p=11 mod24. The channels, integer normalization D, observer x, input parameter 9, finite rank, provenance and later p-adic GH-20 moments remain separate.

## GH-23: a rigorous no-go for a naive order-three base symmetry

The four marked base points `S={0,-1,-1/9,infinity}` in P^1(F_p) are distinct for every prime p>3. Their ordered cross-ratio at `(infinity,0,-1/9,-1)` equals 9.

**Theorem.** Over Q the fractional-linear set stabilizer of S has order 4. For p>3 its order is 8 at p in {5,7,17}, 12 at p=73, and 4 otherwise. Thus **for all prime p=8m+3 >=11**, no order-three Möbius transformation can cyclically permute and preserve these four original base points.

**Proof.** The anharmonic orbit of cross ratio lambda is the six values `lambda, 1/lambda, 1-lambda, 1/(1-lambda), lambda/(lambda-1), (lambda-1)/lambda`. For lambda=9 they are `9,1/9,-8,-1/8,9/8,8/9`. A permutation of four distinct points extends to a unique PGL2 map iff it preserves the cross ratio. The six-value orbit generically gives a group of order 24/6=4 (the Klein four). The only collisions in characteristic p>3 are harmonic lambda in {-1,2,1/2} at p=5,7,17 (orbit size 3 and group 8), or equianharmonic `lambda^2-lambda+1=73=0 mod p` at p=73 (orbit size 2 and group 12). None of these exceptions satisfies p=3 mod8, p>=11. A group of order 4 has no element of order 3. QED.

**Exact obstruction scope:** this excludes only degree-one fractional-linear order-three stabilizers of this base four-point set. Higher-degree covers, extension-field characters, Frobenius correspondences, nonlocal WZ and CM routes are not excluded.

## Executed arithmetic and next unit

The independent Python standard-library checker performed exact terminating-hypergeometric, GH-19 integer-coefficient and complete finite-field character sum computations for both channels at **76 primes p<2000 with p=3 mod8**. The channels matched for every prime. It enumerated all 24 cross-ratio permutations, confirming stabilizer order 4 on those primes and exception orders (p,order)=(5,8),(7,8),(17,8),(73,12). Additional integer binomial/derivative checks covered m=1,...,29. Observed F/G vanishing samples split 37 / 39; these finite observations are not universal proofs. Exact examples (p,m,F,G,D,DF,DG):
`(11,1,6,0,4,2,0); (19,2,0,5,2,0,10); (43,5,0,6,25,0,21); (59,7,21,0,34,6,0); (67,8,0,33,61,0,3); (139,17,0,117,128,0,103)`.

**Next exact action:** seek a genuinely prime-dependent finite-field/extension-field character identity, nontrivial higher-cover correspondence, or source-retaining WZ certificate proving or disproving the F-moment zero at every p=19 mod24. No base order-three Möbius route. Then use GH-15/16 Laurent compensation and GH-20/GH-21 p-adic source data before making claims about T_p or native JT2. P000 six native spatial axes plus separately typed time remain unchanged; these scalar variables are only auxiliary source observers, not a full-X6 law.

Native control snapshot dated 2026-10-28 ~07:49 +08: gateway 0.6.11, `research_authority_granted=false`, disabled write relay. No fresh winning own CLAIM/open/run/Source checkpoint established; original control support `enterprise-math#1558`. Research-Activity registration pending. H0/B0, [X]U mod p^2, Frobenius eta/kappa, native p=373 experiment, independent Driver review and original finite endpoints/infinity remain open.
