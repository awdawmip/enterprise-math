# R749SMC — Exact future-safe BRC provenance quotient for restricted Walsh-character controllers

2026-11-13 Asia/Shanghai. Status: author-side exact theorem and finite Fraction verification. Predecessor: R749SMB in draft PR #2193. Immutable scientific input pin remains `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Model: R749SF conditional signed-Port kernel plus a **declared** historical-sign controller; native V29/V39 PASS or Cell/Link/Port event permission is not asserted.

R749SMB proves that unrestricted finite historical memory can require arbitrarily many prediction coordinates even though the current signed lift has eight states. This companion gives a constructive **positive compression theorem** when declared future operations access only a restricted algebra of history characters.

## 1. A finite declared character sequence

Let hidden historical signs `Z=(Z_1,...,Z_d)∈{±1}^d`, obtained through the legal six-axis nonforced-prefix and three-step washout construction in R749SMB. For a binary vector `v∈F_2^d` define `χ_v(z)=∏_{i:v_i=1} z_i`; `χ_0=1`. Fix any finite sequence `v_1,...,v_h`, allowing repeats, zero or linear dependencies. At public support-choice stage i the controller selects a forced versus a nonforced legal next support with

`Pr(A_i=a | Z=z)=(2+a χ_(v_i)(z))/4`, `a∈{±1}`.

These choices use independent Bernoulli coins conditional on Z. The underlying exact R749SF conditional sign kernel preserves the uniform current eight-lift law, so no additional dependence on current signed axes is hidden in the public-choice likelihood. The public h-letter law is

`M_v(a,z)=4^{-h} ∏_{i=1}^h (2+a_i χ_(v_i)(z))`.

Fix the declared future-operation sequence as part of the observer contract. Set `H=span_{F_2}{v_1,...,v_h}` and `r=dim H`.

## 2. Exact rank, equivalence, and minimal affine statistics

**Theorem (sharp restricted Walsh lease).**

1. `rank_Q(M_v)=2^r`.
2. Two deterministic historical sources `z,z'` induce identical probabilities for all public observation words iff `χ_v(z)=χ_v(z')` for every `v∈H`. This defines exactly `2^r` equivalence classes, each containing `2^{d-r}` histories.
3. Over arbitrary interior priors on all `2^d` histories, precisely `2^r-1` independent affine source expectation coordinates are necessary and sufficient for every declared word probability. A valid carrier is the collection `m_v=E[χ_v(Z)]`, `v∈H\{0}`.

**Proof.** Taking the Walsh Fourier transform in the *public* word `a∈{±1}^h` gives, for every subset of stage indices `J⊆{1,...,h}`,

`∑_a (∏_{i∈J} a_i) M_v(a,z) = 2^{-|J|} χ_(⊕_{i∈J} v_i)(z).`

The Fourier transform is invertible and its nonzero coefficients are precisely the distinct characters of the subgroup `H`. Characters of `F_2^d` form a linearly independent basis of functions on histories. Hence the row span is exactly `span_Q{χ_v : v∈H}`, of dimension `|H|=2^r`. The same transformed equalities show deterministic observational equivalence iff all H-characters agree, producing `2^r` fibers of size `2^{d-r}`. The constant character gives normalization, so R749SM's affine-span minimality theorem yields exactly `2^r-1` nonconstant moments. ∎

In particular, repeated observations of the *same* historical parity never raise the affine predictive rank beyond 2, whereas observing r independent signed-source parity characters reaches rank `2^r` regardless of the original d.

## 3. Recursion and bounded operation families

For any future controller policy whose (possibly public-history-adaptive) choice of historical character always lies in the **fixed subgroup** H, all action likelihoods factor through the same quotient

`π_H(z)=(χ_(b_1)(z),...,χ_(b_r)(z))`

for any basis `b_1,...,b_r` of H. The quotient has `2^r` states and its exact positive-rational posterior update is

`\hat μ_{t+1}(q)=\hat μ_t(q) L_t(a_t|q,h_t) / \sum_{q'}\hat μ_t(q') L_t(a_t|q',h_t)`.

Thus the quotient stays future-safe for arbitrarily many such operations. This is a **sufficiency** statement for adaptive schedules; the exact minimality formula above concerns the declared complete fixed character sequence. Branch-specific adaptive restrictions may permit smaller quotients, to be checked from their actual reachable word laws.

If a later controller requests a character outside H, the observer lease has expanded; it cannot in general recover that moment from the old H-quotient. The required repair is precisely the newly needed independent Walsh character span, not indiscriminate retention of all provenance.

## 4. Exact verification

`R749SMC_RESTRICTED_WALSH_QUOTIENT_CHECK.py` enumerates every possible ordered sequence of `h≤3` character selectors (including the zero vector and repetitions) on `d=1,2,3` historical signs: respectively 15, 85, 585 sequences. It also checks 11 targeted dependent/independent cases each for `d=4,5`. The checker constructs the complete `2^h×2^d` rational likelihood matrix; verifies its rank equals `2^{rank_{F_2}{v_i}}`, all deterministic history equivalence fibers, every public-Walsh transform identity and column normalization. Python standard-library Fraction arithmetic returned `PASS`; exact output in `R749SMC_RESTRICTED_WALSH_QUOTIENT_RESULTS.json`. The algebraic proof is valid for all finite d and h; these finite checks do not substitute for it.

## 5. Next research

Apply this subgroup-rank compression to the exact reachable *native* branch observation and controller action alphabet after reading actual V29/V39 event guards and closure certificates. In a general adaptive branch-dependent observer, compute the minimal reachable row span rather than assuming the union-of-characters sufficient carrier is always sharp.
