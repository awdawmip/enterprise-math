# R122-FIBER — Exact one-integer oracle on bounded progression floor bands

Author-side S23 auxiliary research, 2026-11-13. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessors: R121-AP/R121-LIT, immutable commit `0cf1633a6b01e5aba2179559c58195a2eebbcc53`. This does **not** assert native Cell/Link/Port permission or independent mathematical acceptance.

## Theorem

Let `m>=2`, `t_i=N+i*d` (`d!=0`), and take rational input `x,J=(l,h)`, integer `N,d,j,a,c`. Fix an old historical open rational atom on which old eligibility and the R120 S23 directed-arc segmentation are constant. For each prescribed bit `b_i`, its eligible real fractional-phase region decomposes into at most two affine-endpoint half-open segments `[L_i(theta),U_i(theta))` in `[0,1)`.

Set `K={floor(d*theta):theta in J}`, `B=|K|`, and let `P_m={(floor(alpha+i*beta))_{i=0}^{m-1}:0<=alpha,beta<1}`.

**R122.1:** A prescribed m-bit S23 qualification vector on J is attainable exactly when one of at most `B*|P_m|*2^m` **one-integer** rational linear systems is feasible. Each system has O(m^2) rational inequalities, is solved with finitely many exact floor/ceil operations, and yields a rational theta witnessing the original directed-arc conditions. In particular, no general two-variable ILP implementation is necessary for this subclass.

Writing `v_-=min(dl,dh)`, `v_+=max(dl,dh)`, we have the exact set

`K={floor(v_-),...,ceil(v_+)-1}`, so `B=ceil(v_+)-floor(v_-)`.

When `|d|(h-l)<=1`, at most **two** k-bands occur, even if the interval crosses an integer in d*theta. Thus for fixed m the method is polynomial in the binary input length, including `log(|N|+2)` and `log(|d|+2)`; the actual bound for arbitrary J carries the B factor. Using the previously published finite Sturmian-word count `|P_m|=1+sum_{r=1}^{m-1}(m-r)*phi(r)=Theta(m^3)`, the number of systems is `O(B*2^m*m^3)`. All-source-signature enumeration carries an additional `2^m` factor. The cost of old atomization is separate; no polynomial-time assertion in unrestricted m or wide J is made.

## Complete mathematical argument

1. **Floor-band partition.** The image of the open interval J under theta↦d*theta is precisely `(v_-,v_+)`, whether d is positive or negative. It meets `[k,k+1)` iff `k+1>v_-` and `k<v_+`, giving exactly the stated finite list of k values. A width at most one cannot meet more than two such intervals.

2. **Exhaustive lifts.** At any actual theta write `Y_0=x+(N-j)*theta=n+alpha` and `d*theta=k+beta`, with `n,k` integers and `alpha,beta in [0,1)`. Then `floor(Y_i)=n+i*k+q_i`, `q_i=floor(alpha+i*beta)`, necessarily `q in P_m`. Every true theta therefore belongs to an enumerated k,q pair. We never assume that independently achievable bits can be combined: the following inequalities share one theta and n.

3. **Exact rational inequalities.** Choose one of up to two segments for each requested bit. For fixed k,q, the necessary and sufficient system in real theta and integer n is

`l<theta<h;quad k<=d*theta<k+1;`

`x+(N+i*d-j)*theta-U_i(theta) < n+i*k+q_i <= x+(N+i*d-j)*theta-L_i(theta)`, for all i.

It consists of affine rational inequalities `A*theta+B*n <(=) C`. The left strict boundary encodes the original upper-open segment endpoint. Conversely any solution puts `Y_i-(n+ik+q_i)` in its declared subsegment of `[0,1)`, forcing the selected integer to be the actual floor of `Y_i`. Thus all original S23 bits hold; there are no false positives from the abstract q vocabulary.

4. **Project out theta without epsilons.** Each inequality with A<0 gives an affine lower theta-bound `theta >= L_r(n)`, with a strict flag where applicable. Each A>0 gives an affine upper bound `theta <= U_s(n)`; A=0 constrains n directly. The old atom endpoints supply both kinds. Real theta exists for a fixed n **iff** every lower bound is <= every upper bound, with strict < whenever either participating bound is strict, and every A=0 constraint holds. This is sufficient because intervals in one ordered real dimension have a common point exactly under these pairwise conditions. Thus we obtain at most O(m²) inequalities `p*n <(=) r`, all rational.

5. **Exact one-integer decision and witness.** For p>0 the constraint imposes `n<=floor(r/p)` if weak or `n<=ceil(r/p)-1` if strict. For p<0 it imposes `n>=ceil(r/p)` if weak or `n>=floor(r/p)+1` if strict. For p=0 test the constant condition directly. Their intersection is an integer interval; n is bounded due to `theta in J` and the i=0 phase inequality. If nonempty, select its least integer. Then recover the maximum lower theta-bound and minimum upper bound, choosing their rational midpoint when distinct, or the common value if both are weak. This is an exact rational witness, with all strict endpoints preserved. Empty intervals certify impossibility on that k,q,segment case. Repeating the exhaustive finite cases proves both directions.

All per-case rational operations, coefficient bit lengths and resulting n lengths are polynomial in the input bit length and m. Existing finite Sturmian enumeration (Mignosi 1991, Berstel–Pocchiola 1993, OEIS A005598) supplies the word count, not a novel claim here.

## Reproducibility and limits

The complete standalone Python standard-library `Fraction` checker is `check_r122.py.gz.b64` (decode: `base64 -d | gzip -d`). It implements the explicit one-segment special case `a=j=0,c=1,0<theta<1`: M_t(theta)=1 iff frac(x+t theta) is in [0,theta). The **general theorem** relies on R120's correctly derived old-atom affine segment decomposition; that general segment generator has not been implemented in this checker.

Deterministic seed 1222026: 48 signed random instances, m=2..5, 1,956 independently enumerated exact full phase-cut singleton/open atom representatives, and 720 exhaustive bit-signature decisions. Results: 501 confirmed attainable with exact original-predicate rational witnesses, 219 exact unattainable; every signature set agrees with the separate full-cut method. P_m counts for m=2..5 are 2,4,8,14. Two additional signed cases have N of 161 decimal digits and d of 101 digits, `|d|(h-l)=1/100`, and one k-band; the solver recovers exact witnesses and 160-digit n values without scanning n. Those huge cases verify *positive* witnesses only, not all negative possibilities. Executed status: `R122_FIBER_EXACT_PASS`.

This proves and implements a useful **bounded-floor-fiber** class, **not** a generic large-width two-integer ILP solver or a native six-dimensional dynamics claim. No formal CLAIM, independent Review or theorem promotion is implied.

## Next question

Implement general exact two-dimensional integer-point feasibility for wide k-band ranges; compare against this complete fiber solver on shared cases. Separately, intersect the reachable beta interval in each band with the Sturmian arrangement to reduce q enumeration without sacrificing joint phase information.
