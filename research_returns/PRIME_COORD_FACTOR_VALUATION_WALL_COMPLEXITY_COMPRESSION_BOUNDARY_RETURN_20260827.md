# Prime Coordinate Factor Valuation-Wall Complexity Compression Boundary — Research Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Date: `2026-08-27`

Task-ID: `RS-PRIME-COORD-FACTOR-VALUATION-WALL-COMPLEXITY-COMPRESSION-BOUNDARY`

Publication-ID: `TP2-25876E1168D68965C9E4`

Researcher-ID: `EM-PCF5-8A41D7`

Claim-ID: `chatgpt-pcf5-20260827-2316-8a41d7`

Execution record: `ER-6C8B3D4F9A21E705D1C2`

## 1. Frozen primary verdict

The strongest primary verdict is

\[
\boxed{\texttt{CLASSICAL_FACTORIAL_METHOD_EQUIVALENCE_FROZEN}}.
\]

The task hard target

`VALUATION_WALL_COMPLEXITY_COMPRESSED_OR_CLASSICAL_EQUIVALENCE_OR_SCOPED_BARRIER_PROVED`

is closed.

There is a genuine asymptotic compression of the accepted parent splitter relative to its `Theta(p)` streaming recurrence: the required public residues can be evaluated with a Strassen-style block-factorial construction in

\[
\widetilde O(\sqrt p)
\]

ring operations, hence

\[
O\!\left(p^{1/2}\operatorname{poly}(n)\right),
\qquad n=\lceil\log_2N\rceil,
\]

bit work up to the explicitly stated fast-integer-arithmetic factors below.

However, the compression mechanism is not new. It is exactly the classical block-product / fast polynomial multipoint mechanism underlying Strassen and Pollard–Strassen factorial factorization, with `A_s` obtained from a constant number of factorial residues. On balanced semiprimes `p=Theta(sqrt(N))`, the resulting scale is the classical

\[
N^{1/4+o(1)}
\]

layer, not a new deterministic factoring exponent and not polynomial time in `n`.

Therefore the coordinate result is valuable as an exact complexity classification, but no asymptotic novelty claim is made.

## 2. Accepted parent input and exact wall

Treat the accepted result `RR-F24971D684C868A325E2` at its exact scope.

For distinct odd primes

\[
N=pq,\qquad 3<p<q,
\]

define

\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}
=\binom{2s}{s}^2\binom{3s}{s}.
\]

For every prime `r>3` and `0<=s<r`, the parent proves

\[
v_r(A_s)=\left\lfloor\frac{2s}{r}\right\rfloor+
\left\lfloor\frac{3s}{r}\right\rfloor,
\]

hence

\[
r\mid A_s\iff 3s>r.
\]

The first local factor-bearing index for the smaller factor is therefore

\[
h_p=\left\lceil\frac p3\right\rceil=\Theta(p).
\]

The accepted public splitter probes dyadic `s=1,2,4,...`; its first nonunit dyadic seed satisfies `s_*<2p/3<p`. If that gcd is `N`, the synchronized branch proves `q<2p` and the public fallback

\[
t=\left\lfloor\frac{\sqrt N}{3}\right\rfloor,
\qquad t+1<p
\]

returns `p` at `t` or `t+1`.

Those inequalities are the exact reason the denominator `(s!)^5` remains invertible at every `A_s` evaluation actually needed by the parent algorithm.

## 3. Three cost classes

Let

\[
R_N=\mathbb Z/N\mathbb Z,
\qquad n=\lceil\log_2N\rceil.
\]

Let `M_R(d)` denote the number of base-ring operations needed to multiply degree-`d` polynomials over `R_N`, and let `M_int(n)` denote the bit cost of multiplying `n`-bit integers.

We separate the taskbook's three access classes.

### Class S — sequential recurrence access

The parent recurrence is

\[
A_s=A_{s-1}\,
\frac{6(2s-1)(3s-2)(3s-1)}{s^3}.
\]

In the explicitly restricted sequential model, one transition advances the largest known recurrence index by at most one. Therefore producing every state through index `s` requires at least `s` transitions and at most `O(s)` transitions:

\[
\boxed{T_S(s)=\Theta(s)}
\]

base recurrence updates.

Since the first smaller-factor wall is `ceil(p/3)`, any algorithm restricted to this sequential access primitive has

\[
\boxed{T_S(\text{first wall})=\Omega(p)}.
\]

This is a scoped lower bound only. It is not a lower bound for random-index evaluation or for factoring in general.

### Class F — exact random-index factorial / `A_s` evaluation

The construction below computes `k! mod N` without traversing all `1,...,k` as recurrence states and then evaluates `A_s` from three factorial residues.

### Class P — full public splitter

The full algorithm includes the public dyadic schedule, gcds, any denominator safety check, and the synchronized `isqrt(N)//3` fallback. The total cost is derived in Section 7.

## 4. Exact Strassen block-factorial lemma over the composite modulus

Fix public `k>=1`. Put

\[
m=\lceil\sqrt k\rceil,
\qquad L=\left\lfloor\frac{k}{m}\right\rfloor,
\]

and define the monic block polynomial

\[
Q(X)=\prod_{j=1}^{m}(X+j)\in R_N[X].
\]

Then

\[
Q(im)=\prod_{j=1}^{m}(im+j),
\qquad 0\le i<L,
\]

so the blocks are disjoint and cover `1,...,Lm`. Consequently

\[
\boxed{
k!
=
\left(\prod_{i=0}^{L-1}Q(im)\right)
\left(\prod_{r=Lm+1}^{k}r\right)
\pmod N.
}
\]

There are fewer than `m` leftover scalar factors.

### 4.1 Complexity

Build `Q` by a product tree. Evaluate it at the `L<=m` public points

\[
0,m,2m,\ldots,(L-1)m
\]

using a subproduct/remainder-tree multipoint evaluator.

For a commutative ring, standard fast multipoint evaluation has cost

\[
O(M_R(m)\log m)
\]

base-ring operations; the product tree has the same soft-order cost. Hence

\[
\boxed{
T_{\mathrm{fact}}(k)
=O(M_R(\sqrt{k})\log k).
}
\]

With quasi-linear polynomial multiplication over the base ring,

\[
M_R(d)=d^{1+o(1)},
\]

this is

\[
\boxed{T_{\mathrm{fact}}(k)=\widetilde O(\sqrt k)}
\]

ring operations.

Reducing each coefficient operation modulo the `n`-bit integer `N` gives the conservative bit form

\[
\boxed{
T_{\mathrm{fact,bit}}(k)
=\widetilde O(\sqrt{k}\,M_{\mathrm{int}}(n)).
}
\]

The standard product/remainder trees use `O(\sqrt{k}\,\operatorname{polylog} k)` ring elements of workspace, hence `O(\sqrt{k}\,n\,\operatorname{polylog}k)` bits under the present non-optimized accounting.

### 4.2 Composite-modulus legality

The construction does not interpolate from values and does not divide by point differences.

- `Q` is built only by multiplication of monic linear factors.
- The multipoint subproduct tree uses monic factors `(X-a_i)`.
- Remainder reduction by a monic polynomial never requires inversion of an arbitrary coefficient; the leading coefficient is `1`.
- Fast monic remainder algorithms may be expressed through reversal and power-series inversion of a series with constant term `1`; only the known unit `1` is inverted.
- The scalar block product itself uses multiplication only.

Thus the factorial residue computation is valid over `R_N` even when `k!` is a zero divisor or zero modulo one hidden prime. A hidden factor is not needed to select `m`, `L`, the polynomial, or the evaluation points.

This is stronger for the present task than invoking interpolation-based recurrence shifting, which can introduce unit hypotheses on evaluation-point differences.

## 5. Exact fast evaluator for `A_s`

For a public `s` define

\[
F_j=j!\pmod N.
\]

Compute independently by the block-factorial lemma

\[
F_s,\qquad F_{2s},\qquad F_{3s}.
\]

Before division, compute

\[
d=\gcd(F_s,N).
\]

There are three possibilities.

1. `d=1`. Then `F_s` is a unit, so compute
   \[
   A_s\equiv F_{2s}F_{3s}F_s^{-5}\pmod N.
   \]
2. `1<d<N`. Return `d` immediately as an exact factor; no illegal inverse occurs.
3. `d=N`. Stop the generic evaluator with explicit denominator-nonunit status rather than inventing an inverse.

On every seed reached by the accepted parent splitter before termination, `s<p<q`; hence every integer `1,...,s` is coprime to `N` and case 1 is guaranteed. The extra gcd is nevertheless retained so the implementation is safe independently of that proof-side promise.

The cost is a constant number of factorial calls plus one gcd/inverse:

\[
\boxed{
T_A(s)=O(M_R(\sqrt s)\log s)+\operatorname{poly}(n)
=\widetilde O(\sqrt s)+\operatorname{poly}(n)
}
\]

ring operations, or

\[
\boxed{
T_{A,\mathrm{bit}}(s)
=\widetilde O(\sqrt s\,M_{\mathrm{int}}(n)).
}
\]

No constructor parameter depends on `p` or `q`.

## 6. Why this is a real compression of the parent recurrence

The sequential parent route pays `Theta(s)` updates to reach `A_s`.

The block evaluator computes the same residue at an isolated public index in

\[
\widetilde O(\sqrt s)
\]

ring operations. Therefore it is a genuine asymptotic random-index compression with

\[
\delta=\frac12
\]

in the taskbook's threshold language:

\[
T_A(s)=O(s^{1-\delta}\operatorname{poly}(n)).
\]

This statement is about exact arithmetic complexity. The regression implementation intentionally uses elementary polynomial operations and is not itself a timing demonstration of the asymptotic algorithm.

## 7. Composition with the public dyadic/fallback splitter

Let the dyadic probes before the first nonunit be

\[
s_j=2^j,
\qquad s_J=s_*<\frac{2p}{3}.
\]

Because square roots of a geometric progression sum geometrically,

\[
\sum_{j=0}^{J}\sqrt{s_j}=O(\sqrt{s_*})=O(\sqrt p).
\]

Hence evaluating `A_s` independently at every dyadic seed costs

\[
\widetilde O(\sqrt p)
\]

ring operations in total, not `O(\sqrt p\log p)` separate leading scales.

There are only `O(log p)` gcd probes.

If the first dyadic gcd is `N`, the accepted synchronization theorem gives `q<2p` and

\[
t=\left\lfloor\frac{\sqrt N}{3}\right\rfloor,
\qquad t+1<p.
\]

Thus both fallback evaluations also cost `\widetilde O(\sqrt p)` in total and have unit denominators.

The complete public splitter therefore satisfies

\[
\boxed{
T_P(N;p)
=\widetilde O(\sqrt p)
\text{ ring operations}
}
\]

and, with explicit `n`-bit arithmetic,

\[
\boxed{
T_{P,\mathrm{bit}}(N;p)
=\widetilde O(\sqrt p\,M_{\mathrm{int}}(n))
+O(\log p\,M_{\mathrm{int}}(n)\log n).
}
\]

In the taskbook's simpler threshold notation this is

\[
\boxed{O(p^{1/2}\operatorname{poly}(n))}.
\]

For balanced semiprimes,

\[
p=\Theta(\sqrt N),
\]

so

\[
\boxed{
T_P=N^{1/4+o(1)}
}
\]

up to the standard bit-multiplication factors.

This remains exponential in `n=Theta(log N)` and is not polynomial-time factoring.

## 8. Prior-art audit and equivalence classification

The internal Enterprise method/tool audit found no registered fast-factorial/product-tree random-index evaluator. The relevant current internal surfaces are general valuation arithmetic (`T1_SCALE_ENUMERATION_VALUATION`) and the prime-method facade, neither of which supplies the present asymptotic mechanism. Therefore the internal coverage outcome is

`CAPABILITY_GAP_CONFIRMED_FOR_FAST_FACTORIAL_RANDOM_INDEX_EVALUATION`.

The external prior-art audit closes that gap immediately:

1. Alin Bostan, Pierrick Gaudry, Eric Schost, **Linear recurrences with polynomial coefficients and computation of the Cartier-Manin operator on hyperelliptic curves**. The paper explicitly places the Chudnovsky square-root recurrence method as a generalization of Pollard/Strassen integer-factorization methods and gives fast multipoint evaluation over a commutative ring in `O(M(d) log d)` base-ring operations. Source: https://mathexp.eu/bostan/publications/BoGaSc04.pdf
2. Edgar Costa, David Harvey, **Faster deterministic integer factorization**, arXiv:1201.2116. Its abstract states the then-best unconditional deterministic bound `O(M_int(N^(1/4) log N))` due to Bostan–Gaudry–Schost following the Pollard–Strassen approach. Source: https://arxiv.org/abs/1201.2116
3. David Harvey, **An exponent one-fifth algorithm for deterministic integer factorisation**, Math. Comp. 90 (2021), 2937–2950, proves `N^(1/5+o(1))`, explicitly noting that the previous `N^(1/4+o(1))` layer goes back to the 1970s. Source: https://www.ams.org/mcom/2021-90-332/S0025-5718-2021-03658-3/
4. David Harvey, Markus Hittmeir, **A log-log speedup for exponent one-fifth deterministic integer factorisation**, arXiv:2105.11105, sharpens secondary factors while retaining exponent `1/5`. Source: https://arxiv.org/abs/2105.11105

The equivalence here is structural, not merely numerical:

- the PCF5 evaluator forms the same block polynomial `Q(X)=prod(X+j)`;
- it evaluates `Q` at an arithmetic progression of block starts by fast multipoint evaluation;
- it reconstructs factorial residues from those block values;
- `A_s` then requires only three such factorial residues and a certified unit inverse;
- the dyadic wrapper changes how the factor-bearing target scale is discovered publicly, but a geometric sequence of square-root-cost evaluations preserves the same `sqrt(p)` exponent.

Thus the new valuation-wall theorem supplies an exact factor-blind *reason* for which residues separate the hidden primes, but its first valid asymptotic acceleration is classical factorial arithmetic already known from Pollard–Strassen/Strassen-style deterministic factorization.

Freeze:

`VALUATION_WALL_RELATIVE_TO_PARENT_IS_COMPRESSED = TRUE`.

`COMPRESSION_MECHANISM_ASYMPTOTICALLY_NEW = FALSE`.

`BALANCED_SEMIPRIME_EXPONENT = 1/4 + o(1)`.

`GENERAL_DETERMINISTIC_FACTORING_STATE_OF_ART_BEATEN = FALSE`.

## 9. Exact bounded checker

Durable checker:

`scripts/check_prime_coord_factor_valuation_wall_complexity_compression_boundary.py`

The checker deliberately implements the block polynomial with elementary coefficient arithmetic and Horner evaluation. It therefore checks the exact decomposition independently of any fast-polynomial package but is **not** used as evidence for the asymptotic complexity theorem.

Exact local run of the same checker logic:

`PASS factorial_checks=1452 A_checks=582 wall_checks=4222 splitter_checks=946 evaluator_calls=5236 denominator_nonunit_events=0 modes={'DYADIC': 714, 'FALLBACK_T1': 24, 'FALLBACK_T': 208}`

Coverage:

- `1,452` block-factorial residues checked against direct factorial recurrence;
- `582` sampled `A_s` block residues checked against exact binomial integers;
- `4,222` local valuation-wall checks;
- all `946` distinct semiprimes from prime pairs `5<=p<q<=199` passed the complete public dyadic/fallback splitter;
- `5,236` fast-index evaluator calls on those splitter runs;
- zero denominator-nonunit events before promised termination;
- every returned divisor was verified by exact division.

Bounded computation is regression only. Universal correctness is supplied by the block identity, the general-ring polynomial evaluation argument, and the accepted parent dyadic/fallback theorem.

## 10. Required-output accounting

1. **Precise cost model** — Sections 3–4.
2. **Sequential baseline and scoped barrier** — Section 3, `Theta(s)` and `Omega(p)` inside Class S.
3. **Public fast-index evaluator** — Sections 4–5.
4. **gcd/inversion/product-tree/multipoint accounting** — Sections 4–5; no arbitrary composite-ring inverse is used, and `s!` is checked before inversion.
5. **Composition with parent splitter** — Section 7.
6. **Explicit positive threshold** — `delta=1/2` in `p`, Section 6.
7. **Current prior-art comparison** — Section 8.
8. **Independent exact checker** — Section 9.
9. **Durable return** — this file.

## 11. Tool/method disposition

The task did not require creation of a new reusable Enterprise tool family.

Internal lookup outcome:

`CAPABILITY_GAP_CONFIRMED_FOR_FAST_FACTORIAL_RANDOM_INDEX_EVALUATION`.

Research outcome after prior-art audit:

`REUSE_CLASSICAL_PRIOR_ART / NO_NEW_TOOL_FAMILY`.

The proper durable value is a result-level complexity classification attached to the prime-coordinate factorization program, not a renamed Strassen tool.

`METHOD_HARVEST = NO_TOOL_PAYLOAD / RESULT_ONLY`.

## 12. Residue and Driver recommendation

Within the task hard target:

\[
\boxed{\texttt{UNRESOLVED_RESIDUE = NONE}}.
\]

The `Theta(p)` streaming frontier has been classified sharply enough for this task:

- sequential recurrence access has the scoped `Omega(p)` barrier;
- exact random-index access is available in `O(p^{1/2} poly(n))` by classical block-factorial evaluation;
- the full public valuation-wall splitter inherits that compression;
- on balanced semiprimes this is the classical `N^(1/4+o(1))` deterministic factorial-factorization layer and therefore is not a new asymptotic factoring breakthrough.

A separate future task would be needed to ask whether the *valuation-wall structure itself* can be combined with modern post-Strassen deterministic factoring machinery to beat its classical `N^(1/4)` realization. That question is not needed to close the present hard target and is not auto-published here.

Recommended Driver disposition:

`ACCEPTED / CLASSICAL_FACTORIAL_METHOD_EQUIVALENCE_FROZEN / RELATIVE_COMPLEXITY_COMPRESSION_PROVED / NO_NOVEL_FACTORING_EXPONENT / RESULT_ONLY`.
