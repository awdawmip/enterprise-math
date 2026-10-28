# D25/LIFT — the 2304 half-cut reciprocal zero and the original 216 cross-kernel correction

Date: 2026-10-28, Asia/Hong_Kong. Mode: **AUTHOR-SIDE / EXACT DERIVATION / PUBLISHED-THEOREM COROLLARY / EXECUTED INTEGER CHECK / UNREVIEWED / NOT_ADMITTED / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_EXECUTED**.

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`.
Last verified scientific publication reference: `TP2-B6F4FC938FF94941C1B7`.
Frozen scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`, **unchanged**.
Research lane identifier (historical logical routing label only; not a claimed native session): `chatgpt-research-onhour-enterprise-math-20260923`. The CONTROL_PLANE_MAINTENANCE lane is distinct and unused.

## 1. Exact original objects and prior work consumed

For primes `p>3`, with all rational coefficients interpreted in `Z_(p)`, let

```math
t_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
    =\frac{(2n)!(3n)!}{(n!)^5 216^n},\quad
s_n=\frac{\binom{2n}{n}^{2}\binom{4n}{2n}}{2304^n}
    =\frac{(4n)!}{(n!)^4 2304^n}.
```

The original scalar task is

```math
A_p=\sum_{n=0}^{p-1}(6n+1)t_n.
```

Its auxiliary published-model comparator is

```math
B_p=\sum_{n=0}^{p-1}(8n+1)s_n.
```

The prior author-side D25 note `research_notes/portable_direct/20261028_onhour_d25_216_2304_kernel_transport_p4_no_go.md` (EM commit `7f23e5cb67cd455564317004e377feba60ace1bb`) reported `A_p=B_p (mod p^3)` in 781 exact finite prime examples, explicitly **not** an all-prime proof. It also proved an analytic-series no-go and exhibited exact mod-`p^4` counterexamples. These are consumed, not recredited.

The published external result used **as an input theorem** is Guo–Zudilin, *A q-microscope for supercongruences*, *Advances in Mathematics* 346 (2019), 329–358, arXiv:1803.01830, https://arxiv.org/abs/1803.01830. Their two congruences are

```math
\sum_{n=0}^{p-1}(8n+1)s_n
\equiv\sum_{n=0}^{(p-1)/2}(8n+1)s_n
\equiv p\left(\frac{-3}{p}\right)\pmod{p^3},\quad p>3.
```

The already-proved original-`216` middle/high reflection is consumed from `research_notes/portable_direct/20261028_onhour_d25_original216_interior_middle_high_nonlocal_reflection.md` (EM commit `a4a706832aec5351ab7cfd36b76daef4b1ac7e28`).

## 2. New exact 2304 reflection theorem

Put `h=(p-1)/2` and choose an integer

```math
\lceil p/4\rceil\le j\le h,\qquad k=p-j.
```

For such indices, Legendre's factorial valuation formula gives

```math
\nu_p(s_j)=\lfloor4j/p\rfloor=1,\qquad
\nu_p(s_k)=\lfloor4k/p\rfloor=2.
```

Write `v_j=(s_j/p) mod p\in F_p^\times`. **Theorem B1**, for every prime `p>3` and every indexed pair in this range:

```math
\boxed{\left(\frac{s_j}{p}\right)\left(\frac{s_{p-j}}{p^2}\right)
\equiv\frac1{288j^3}\pmod p.}\tag{B1}
```

**Proof.** Put `a=4j-p` and `b=2p-4j=p-a`. Since `p\le 4j<2p` and `2p<4(p-j)<3p`, the factorial block formulas and Wilson's theorem yield

```math
\frac{(4j)!}{p}\equiv-a!,\qquad
\frac{(4(p-j))!}{p^2}\equiv2b!\pmod p.
```

Here `a` is odd, so Wilson reflection implies `a!b!\equiv(-1)^a a=-a\equiv-4j\pmod p`. Also `j!(p-j)!\equiv(-1)^j j\pmod p` and `2304^p\equiv2304\pmod p`. Substitution into the factorial definitions of `s_j,s_{p-j}` gives

```math
\frac{-2a!b!}{[j!(p-j)!]^4 2304^p}
\equiv\frac{8j}{2304j^4}=\frac1{288j^3}\pmod p.
```

All denominators in the displayed quotient are units: `j<p`, `v_j\ne0`, and `p>3`. This proves B1. The formula is an exact p-adic statement, not a fitted pattern. QED.

## 3. New high-tail readout and all-prime character corollary

For `h+1\le n<p`, the valuation `\nu_p(s_n)=\lfloor4n/p\rfloor` equals 2 for `n<3p/4` and at least 3 thereafter. Reflect the valuation-2 band through `n=p-j` and apply B1. Since `8(p-j)+1\equiv1-8j\pmod p`:

```math
\boxed{
H_B:=\sum_{n=h+1}^{p-1}(8n+1)s_n
\equiv\frac{p^2}{288}
\sum_{j=\lceil p/4\rceil}^{h}
\frac{1-8j}{j^3v_j}\pmod{p^3}.}\tag{B2}
```

The cited Guo–Zudilin theorem proves `H_B\equiv0\pmod{p^3}`; therefore **Corollary B3** holds for every prime `p>3`:

```math
\boxed{
\sum_{j=\lceil p/4\rceil}^{(p-1)/2}
\frac{1-8j}{j^3(s_j/p)}\equiv0\pmod p.}\tag{B3}
```

This finite inverse-unit cancellation is a **deduced corollary** of published prior art plus the new elementary reflection, not a newly independent proof of the Guo–Zudilin theorem.

## 4. Original 216 has a different high-tail port

For `p=6m+1>3`, consume the independently established `216` reflection

```math
\left(\frac{t_j}{p}\right)\left(\frac{t_{p-j}}{p^2}\right)
\equiv\frac1{36j^3}\pmod p,\qquad 2m+1\le j\le3m.
```

Let `u_j=(t_j/p) mod p\in F_p^\times`. The original weighted high band satisfies

```math
\boxed{
H_A:=\sum_{n=3m+1}^{p-1}(6n+1)t_n
\equiv\frac{p^2}{36}
\sum_{j=2m+1}^{3m}\frac{1-6j}{j^3u_j}\pmod{p^3}.}\tag{A1}
```

Here the `4m+1..p-1` terms vanish at the declared precision, while `3m+1..4m` need not vanish. Define the two half-cut weighted sums `A_{\le h}=\sum_{n=0}^{h}(6n+1)t_n` and `B_{\le h}=\sum_{n=0}^{h}(8n+1)s_n` with their *original* coefficients, not cross-substituted hypergeometric terms.

As `B_p-B_{\le h}=0 (mod p^3)` by Guo–Zudilin, the still-unproved full-cutoff scalar transport `A_p\stackrel?\equiv B_p\pmod{p^3}` is **equivalent** to the following sharper original-boundary identity:

```math
\boxed{
A_{\le h}-B_{\le h}
+\frac{p^2}{36}\sum_{j=2m+1}^{3m}\frac{1-6j}{j^3u_j}
\stackrel?\equiv0\pmod{p^3}.}\tag{T1}
```

The `B` high band is **provably zero**, whereas the `A` high band can be nonzero. Thus truncating `A` at the halfway point, or assuming the kernels have identical high-tail cancellation, is not a valid path. B1–B3 and the reduction (T1) have proofs; the global evaluation (T1) remains **OPEN**, so LIFT is not closed.

## 5. Exact integer verification and nonzero p=373 witness

Source program: `research_notes/portable_direct/d25_crosskernel_halfcut_reflection_guard_20261028.py` (the actual standard-library script was executed locally and is stored in the same repository). Its computation uses the exact recurrence

```math
\frac{t_{n+1}}{t_n}=\frac{(2n+1)(3n+1)(3n+2)}{36(n+1)^3},
\quad
\frac{s_{n+1}}{s_n}=\frac{(2n+1)(4n+1)(4n+3)}{288(n+1)^3},
```

and independently compares integer-binomial values for selected primes. Checked all 166 primes `5\le p<1000` for B reflection, all 80 primes `p\equiv1\pmod6` in that range for the A predecessor reflection, the B high-vanishing instances, and four full termwise integer-binomial cross-checks. Executed output:

```text
PASS_D25_B2304_HALF_CUT_REFLECTION 166 primes <1000
PASS_D25_A216_PAIR_RECIPROCITY 80 primes <1000
B373_UNIT_SUM_SPLIT 289 84 total 0
P373 {'p': 373, 'Ashort': 14887176, 'Bshort': 373,
'Ahigh_digit': 266, 'Bhigh_digit': 0, 'A_mirror': 266,
'B_mirror': 0, 'full_diff_digit': 0}
```

At `p=373`, `p²=139129`, `p³=51895117`,

```math
A_{\le186}\equiv14887176=373+107\cdot373^2\pmod{373^3},
\quad B_{\le186}\equiv373\pmod{373^3},
```

```math
H_A\equiv266\cdot373^2=37008314\pmod{373^3},
\qquad H_B\equiv0\pmod{373^3}.
```

Consequently `107+266=373\equiv0\pmod{373}`: the observed cross-kernel full-cutoff matching requires **inter-band cancellation**, not equal half-cut sums. The new B reciprocal sum separates into nonzero labeled blocks `289` (j=94..140) and `84` (j=141..186), summing to `0 mod373`. The 373 certificate is a finite example, not a universal proof of T1.

## 6. BRC/precision and actual next unit

BRC resolution: **COMPOSE_APPLIED** (new B reciprocal reflection with established A 216 reflection and published B theorem). Carrier: indexed signed pairs `(p,j,p-j,s_j,s_{p-j})` or `(p,j,p-j,t_j,t_{p-j})`; valuations, weight, exact coefficient denominator, source and terminal cutoff are retained. Observer: the weighted scalar sum mod `p³`; future operation: complement half-cut to full original `p-1` cutoff. The B high-band quotient is safe at `p³` because of an actual theorem; the A high-band quotient is **not** safe without the explicit correction A1. This does **not** claim observer equivalence at `p⁴`, native H0/B0, signed odd Green/Hesse, or any X6/P000 coordinate transfer.

The next **mathematical** obligation is to prove or refute (T1) uniformly in both frozen prime classes `p\equiv13,19\pmod{24}` by a complete-half-cut finite p-adic transformation/WZ or a character/CM identity, retaining the A inverse-middle correction. Compare proposed certificates against `p=7,373` known `p⁴` errors before promoting precision. The cross-kernel `p³` conjecture was previously checked on 781 primes `p<6000`; rechecking finite cases is not a substitute for this proof.

The **native hard target** remains unchanged: Issue https://github.com/awdawmip/enterprise-math/issues/1559 for the original same-class H0/B0 divided-power `[X]U mod 139129` at p=373, module rank, genuine semilinear Frobenius/basis normalization, odd signed Green/Hesse, original `\kappa`, `\Delta_p-R_p`, with an authorized native executor and independent source-bound review. At this turn's read the issue was OPEN, no assignee, `PENDING_OWNER/NATIVE_NOT_EXECUTED`. This author-only scalar calculation **does not execute** the native benchmark.

The authenticated Site configuration was `research_authority_granted=false`, `write_relay_enabled=false`; the exact read-only continuation returned `CONTROL_QUOTA`. No Source session/claim/run was evidenced or created; no dispatch, Result, formal Source checkpoint, review or acceptance was asserted. Historical Issue #6575/#6576 are provenance, not this turn's newly verified request ownership. This file is an **author-side durable evidence artifact** and must not be mistaken for a native Source progress or Research-Activity record. The registered activity/Source checkpoint is pending under the real, separately authorized Research lane. Preserve P000, ACTIVE worldview and frozen pin; do not use a maintenance identity.
