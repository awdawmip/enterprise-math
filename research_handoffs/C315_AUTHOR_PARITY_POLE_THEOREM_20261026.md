# C315 — Ordered-label pole-parity theorem and full 125-path denominator audit

Date: 2026-10-26. Status: **AUTHOR_EXACT, NOT_SOURCE_CLAIMED, NOT_DRIVER_ADMITTED**.

## Frozen model and authority
Global knowledge main `0229bbb8cdc9e56d94d475c238281e4ae3c7fc32`, Enterprise Math main `b4a669c89814919fe15471fc9562699b6b87dad5`. Frozen mathematical input: C275 exact executable 79-node positive-rational auxiliary with C284/C293's 125 rational-affine paths, preserved in the earlier C314 portable package. C314 author-verified the identity with C298; the present pole argument **does not call C300/C305 residue or polynomial computation**. The older C195/H168 textual-source identity remains pending.

Let `u_0<...<u_78` be the baseline rational nodes and `I=(5,50,55,56)` the four moving labels. On each certified strip, the ordered nodes `y_r(t)` are either fixed `u_r` or affine moving `x_k(t)=w_k+d_k t`, and satisfy `y_0<...<y_78`. Let

```text
g(z) = (A/H) / ((2-z^2)*(3-z^2))^3
Q = 2^128, H = 2^166, A = 6912*50000^2/17^2
Z = 141421356237309504880/10^20
B_j = Q*g(u_j)* product_{r != j} (Z-u_r)/abs(u_j-u_r)
W_j = floor(B_j), for j not in I
a_j = W_j/B_j for fixed labels, a_j = 1 for moving labels.
```

The frozen exact Fraction computation proves `0 < W_j < B_j` for **all 75 fixed labels**; none of the 75 continuous masses is integral.

## Theorem A: common labelled carrier

The 79 original C275 rational branches admit the following **branch-preserving** form on an order-stable strip:

```text
T_r(t) = a_r*g(y_r(t)) * product_{s != r} (Z-y_s(t))/abs(y_r(t)-y_s(t)).
```

For fixed `j`, substituting the baseline `B_j` collapses the unchanged factors and gives `W_j/Q * fixed_multiplier(j,v)`. For moving `I_k`, this is `moving_mass(I_k,v)/Q`. Direct Fraction equality against raw C275 source was checked for 79 labels at each of frozen paths 0, 28, 63, 124: **316/316 pass**.

## Theorem B: collision parity (general n-node lemma)

Assume an ordered n-node family on a strip, with two nodes `y_r,y_s` (r<s) meeting at a simple isolated affine collision parameter `t0`, with other node gaps and all regular factors nonzero. Freeze the original signs of every absolute value when extending the rational branches off the strip. For any nonzero affine factor `q(t)` vanishing at the collision, put `rho_j=lim_(t->t0) q(t) T_j(t)`. Then both residues are nonzero and

```text
rho_s = (-1)^(s-r-1) * (a_s/a_r) * rho_r.            (B)
```

**Proof.** On the ordered strip, `abs(y_j-y_v)=sgn(j-v)*(y_j-y_v)`. Therefore its rational continuation is
`T_j=(-1)^(n-1-j) a_j g(y_j) product_(v != j) (Z-y_v)/(y_j-y_v)`.
When `y_r=y_s`, after removing one simple pole from each term the remaining products agree exactly. The two singular denominators are opposites; multiplying their minus sign by the global sign ratio produces `(-1)^(s-r-1)`. The shared regular factor is nonzero under the hypotheses. QED.

## Theorem C: 125 paths have exactly 37,925 surviving linear factors

For any fixed label j and moving label I_k, (B) implies that the pole coefficient is a nonzero common factor times `W_j + (-1)^(abs(I_k-j)-1) B_j`. Because `0<W_j<B_j`, **neither sign can produce zero**. All fixed/moving isolated active collision factors survive.

For a moving pair `I_k<I_m`, both weights a are exactly one. Hence its simple pole cancels iff `I_m-I_k-1` is odd. The canceled pairs are precisely `(5,55)` and `(50,56)`; the four other pairs survive. Cancellation refers to analytic scalar continuation, not cancellation of two positive masses or native BRC branches.

The exact audit of C284/C293 paths individually normalizes every rational-affine collision gap to a primitive integer linear polynomial. All 38,175 active collisions have **pairwise distinct rational roots** and no other denominator zero at that root. Every moving numerator factor `Z-x_l(t0)` is nonzero. Path 28 has one stationary moving coordinate, giving 75 constant fixed/moving gaps. Counts:

| Quantity | Exact |
|---|---:|
| Paths | 125 |
| Active fixed/moving poles | 37,425 |
| Fixed/moving positive parity | 18,713 |
| Fixed/moving negative parity | 18,712 |
| Moving/moving poles | 750 |
| Moving/moving cancellation | 250 |
| Moving/moving survivors | 500 |
| **Surviving linear factors** | **37,925** |

These are exact structural tests plus Theorem B, not merely 37,925 sampled function values.

## Theorem D: all quadratic pole factors survive to exponent three

For each nonstationary moving affine `x_k(t)` and `c=2,3`, `c-x_k(t)^2` is irreducible over Q, since its roots satisfy `x_k=±sqrt(c)`. A distinct moving node is a rational-affine expression in `x_k`; it cannot equal `±sqrt(c)` at that root unless its affine map is identically equal/opposite, excluded by the certified strict positive node ordering. It cannot equal a root for the other quadratic `3-c` since Q(sqrt2) and Q(sqrt3) are different quadratic fields. Other rational-affine linear gaps cannot vanish at irrational parameters; fixed coordinates are rational. All numerator factors `Z-y_l` remain nonzero, because Z is rational, an active different affine node has irrational value, and a constant node is not Z. Thus **only one moving branch** carries this quadratic pole and its singularity has exact order 3. No cancellation of any quadratic factor is possible.

Across the 125 frozen paths exactly 499 moving maps have nonzero slope (path 28 has three instead of four). This gives 998 distinct, irreducible quadratic factors (two per moving map), each with exponent three and 5,988 aggregate denominator degree. Therefore the reduced rational denominator, up to a nonzero rational scalar, has:
- degree 352 in each of 124 paths (`300+4+4*12`);
- degree 265 in path 28 (`225+4+3*12`);
- **aggregate degree 43,913** across all 125 paths.

No irreducible factor other than the 250 vanishing moving/moving linears can be canceled. This gives an independent, conceptual proof of the full C300 denominator-factor survival claim *within C275's frozen model*.

## Reproduction and limits

The complete local portable C315 evidence includes the frozen C275/C284/C288/C293 sources, an executable Fraction pole-parity verifier, 125-path pathwise certificate, and independent raw-rational residue spot checker. Observed local checks:
- pole-parity and nondegeneracy: 125/125 paths, 38,175 distinct linear collision factors;
- all 75 fixed masses strictly nonintegral;
- quadratic distinctness/nonzero affine checks: 499 dynamic maps;
- independent raw rational exact residue ratios: **40/40** (16 fixed/moving, 24 moving/moving) across paths 0/28/63/124;
- unified 79-branch identity: **316/316**.

The formal theorems depend on order preservation and exact nondegeneracy; finite checks establish these hypotheses only for the frozen 125 paths. No statement independently audits the oldest C195/H168 textual parameter selection. No assertion of integer content, physical equivalence, or native GF(2)-BRC/X6 quotient follows merely from scalar pole cancellation. The full 79 labelled branches, ports/provenance and future-operation residual remain typed and retained (BRC: `REUSE_APPLIED`, scalar auxiliary boundary). P000 and the protected worldview are unchanged.

**Next exact unit:** verify the oldest C195/H168 written specification (indices, integer floor, Q, A/H, rational Z) against C275 without using C275 as the source of truth; then explore a provenance-preserving native BRC lift of this ordinal pole-parity invariant. Current Source native `em_control_tasks` returned `CONTROL_QUOTA`, and own `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`; active Owner/CLAIM/Driver admission unverified. A GitHub branch is author research persistence, not Source admission.
