# D25/LIFT — 原始 W216 的逐项镜像与半长度精确同余证书

Date: 2026-11-11 Asia/Hong_Kong.
Status: AUTHOR_SIDE / EXACT_PROOF / 11_EXACT_PRIME_CHECKS / UNREVIEWED / NOT_ADMITTED / NATIVE_H0B0_NOT_RUN.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`.
Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.
Frozen scientific Source: `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3` (not rebased).
Research lane declared label: `chatgpt-research-onhour-enterprise-math-20260923` (distinct from maintenance; host identity not attested).

## Exact problem and new theorem

For every prime `p>3`, let

```text
a_k = (2k)!(3k)! / (216^k (k!)^5),  0<=k<p,  in Z_(p),
W_p = sum_{k=0}^{p-1} (6k+1) a_k.
v_k = floor(2k/p)+floor(3k/p),
u_k = (a_k/p^{v_k}) mod p  (a unit).
```

**THEOREM 1 (signed full-pair unit identity).** For every `1<=k<p`, put
`alpha=floor(2k/p)`, `beta=floor(3k/p)`. Then

```text
v_k+v_{p-k}=3,
u_k u_{p-k} = (-1)^(1+alpha+beta) beta! (2-beta)! / (36 k^3) (mod p).
```

All denominators in these formulas are p-units. In particular, for
`p/3<k<p/2`, `v_k=1`, `v_{p-k}=2`, and

```text
u_k u_{p-k} = 1/(36 k^3) (mod p).
```

**THEOREM 2 (half-length equivalent certificate, modulus p^3).**
Define the original half-range first and middle strata
`I0={0<=k<p/3}`, `I1={p/3<k<p/2}`.
For `k in I1`, let `b_k=(a_k/p) mod p`, a nonzero residue. Then

```text
W_p =
  sum_{0<=k<p/2}(6k+1) a_k
  + p^2 sum_{p/3<k<p/2} (1-6k)/(36 k^3 b_k)
  (mod p^3).
```

This is an exact all-prime reduction from p original coefficients to
`(p+1)/2` original coefficients (including k=0) plus `(p-1)/6`-scale
unit inversions, with no uncomputed tail, for the original signed sum.
For primes `p=6m+1` the counts are `I0=2m+1`, `I1=m`,
`I2=m`, `I3=2m`; the required coefficients are `3m+1=(p+1)/2`.
The reduction is not an asymptotic sublinear algorithm; cost of
coefficient construction, inversions and exact precision remains counted.

## Proof

For `n=qp+r<3p`, `0<=r<p`, `q<=2`, the p-free factorial
obeys `(n!/p^q) mod p = (-1)^q q! r!`. This follows by grouping
complete nonzero p-blocks and Wilson's theorem. Write
`2k=alpha p+r`, `3k=beta p+s`. Applying that lemma to `(2k)!`
and `(3k)!`, and Fermat's theorem to the denominator, proves the
displayed expression for `u_k`.

Under `k->p-k`, the corresponding quotients become
`alpha'=1-alpha`, `beta'=2-beta`, and the remainders become
`p-r`, `p-s` respectively. Wilson's complement identity is
`j!(p-j)!=(-1)^j j mod p`. Hence
`r!(p-r)! s!(p-s)! = (-1)^{r+s} r s
= (-1)^{k+alpha+beta} 6 k^2 mod p`;
also `[k!(p-k)!]^5=(-1)^k k^5` and `216^p=216 mod p`.
Multiplying the two unit expressions gives precisely
`(-1)^(1+alpha+beta) alpha!(1-alpha)! beta!(2-beta)!/(36k^3)`.
The first factorial pair equals 1 for `alpha=0,1`, proving
Theorem 1, including `v_k+v_{p-k}=3`.

The complete disjoint p-adic strata are:
`I0:0<=k<p/3 (v=0)`;
`I1:p/3<k<p/2 (v=1)`;
`I2:p/2<k<2p/3 (v=2)`;
`I3:2p/3<k<p (v=3)`.
No endpoint is integral since `p>3`. All `I3` terms vanish modulo
`p^3`. Reflection `k->p-k` bijects `I1` with `I2`. For
`k in I1`, the contribution of the reflected term equals

```text
(6(p-k)+1) a_{p-k}
= p^2 (1-6k) u_{p-k}
= p^2 (1-6k)/(36k^3 b_k) (mod p^3).
```

Adding the `I0+I1` direct terms proves Theorem 2. QED.

## Exact executed integer certificates

`d25_w216_mirror_half_length_20261111.py` constructs the original
series through the modular unit-denominator recurrence and *independently*
constructs the normalized units from factorial blocks. It exhaustively
checks each mirror pair, all strata and the half-length sum for
`p=5,7,11,13,19,37,43,109,139,157,373`; all assertions passed.
No floating-point arithmetic is involved.

```text
p    I0/I1/I2/I3       reflected I2/p²  W_p mod p³  raw I0+I1 mod p³
5    2/1/1/1            1                120         95
7    3/1/1/2            5                7           105
11   4/2/2/3            1                1320        1199
13   5/2/2/4            10               13          520
19   7/3/3/6            9                19          3629
37   13/6/6/12          20               37          23310
43   15/7/7/14          35               43          14835
109  37/18/18/36        16               109         1105042
139  47/23/23/46        13               139         2434585
157  53/26/26/52        98               157         1454448
373  125/62/62/124      266              373         14887176
```

For the native priority prime `p=373`,
`p²=139129`, `p³=51895117`; explicitly

```text
14887176 + 139129*266
= 51895490 = 373 (mod 51895117).
```

The signed middle `I1` second digit is 107, the reflected `I2`
second digit is 266, giving `107+266=0 mod 373`.
The reflection formula recovers the second contribution *from the
same original lower-index unit data*. Thus the exact LIFT condition is
equivalent to the half-length congruence
`short_sum + p²*reflected_tail = p (mod p³)`, under the
already established original scalar port identity. This strict
length/scope reduction is an author-side mathematical certificate,
not an independent native H0/B0 evaluation.

## BRC observation and current frontier

Applied BRC/coordinate reuse: `(k,v_k,u_k,6k+1)` is the typed
signed valuation/provenance carrier. Pairing `k<->p-k` is an exact
lossless involution **for the observer `W_p mod p³`**; reducing
`I1` to its total mass would destroy the inverse weights required
to reconstruct the signed `I2` correction. The proof specifies the
minimal retained per-term unit and signed index, while preserving the
original source class and frozen deformation parameter.

No original-class H0/B0 divided-power representative, actual
`[X]U mod 139129`, rank, semilinear Frobenius orientation, eta,
odd kappa or independently reproduced native observable has been
obtained. These remain NOT_RUN / PENDING_OWNER under existing Issue
#1559. The all-target identity `Delta_p=R_p mod p` remains OPEN;
the next mathematical unit is to prove its half-length folded
congruence uniformly, or produce an exact falsifier. Do not
repeat the already completed original W216 large scans, E3
geometry, p² parameter-torsor proof, accepted UR/JT0 or related
auxiliary results.

Native service status in this run: `onhour11-20261111-1457-cont`
reconciled to `SUCCEEDED` (read snapshot
`58cf47c7c048494e3e17318a0b47e9744b737847`).
The separate own recovery call returned
`SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`. No own winning CLAIM,
open run, Source-native checkpoint or Result is asserted.
