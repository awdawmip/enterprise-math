# D25 / SECOND-DIGIT-LIFT — linear-degree lower bound for exact A216 middle-window scalar telescopers

Date: 2026-10-30 (Asia/Hong_Kong). Research lane: `chatgpt-research-onhour-enterprise-math-20260923`, not CONTROL_PLANE_MAINTENANCE. Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; task publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged.

**Classification: AUTHOR-SIDE / PROVED EXACT FINITE-WINDOW DEGREE BOUND / CONSTRUCTIVE INTERPOLATION / EXECUTED EXACT FRACTION CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.**

## Original carrier, exact and source-faithful

Reuse the previously proved original A216 middle-port double-zero coefficient (the 2026-10-30 signed regular terminating tail note), without changing its original coefficient, signed weight, valuation or index.

Let \(m\ge1\) be an integer. For the original middle zone \(n=3m+1+s\), \(0\le s<m\), the coefficient of \(T^2\) in the original three-parameter polynomial is

\[
d_s=\frac{(-1)^{s+1}(3m)!(2m)!(4m)!\,s!\,(m+s)!}
{6\,2^{3m+1+s}[(3m+1+s)!]^3(m-1-s)!},
\quad
\frac{d_{s+1}}{d_s}=
\frac{(s+1-m)(s+1)(s+m+1)}{2(s+3m+2)^3}.
\tag{1}
\]

The actual signed A216 weight is \(W_m(s)=6(3m+1+s)+1=18m+7+6s\), and the middle-port \(p\)-adic source is \(\sum_{s=0}^{m-1}W_m(s)d_s\) when \(p=6m+1\) is prime.

Set
\[
A_m(s)=(s+1-m)(s+1)(s+m+1),\quad
B_m(s)=2(s+3m+2)^3,\quad
D_m(s)=B_m(s-1)=2(s+3m+1)^3.
\tag{2}
\]

For any nonzero polynomial \(W(s)\in\mathbb Q[s]\) with \(\deg W\le2\), write \(t_s=W(s)d_s\). A characteristic-zero **single-term same-kernel rational** Gosper antidifference \(t_{s+1}q(s+1)-t_sq(s)=t_s\), interpreted as a rational functional identity in the free variable \(s\), implies upon setting \(Y(s)=W(s)q(s)/D_m(s)\):
\[
\boxed{A_m(s)Y(s+1)-D_m(s)Y(s)=W(s).}\tag{3}
\]
This also defines the *finite-window* local polynomial/rational certificate class: require (3) at every integer \(s=0,\dots,m-1\), with all displayed evaluations finite.

## Theorem A — all-m rational identity obstruction

For **every** integer \(m\ge1\) and **every** nonzero \(W\in\mathbb Q[s]\) of degree at most two, equation (3) has **no solution** \(Y\in\mathbb Q(s)\) as a rational identity in \(s\). This is stronger than a degree-bounded computer search and concerns the *genuine m-dependent, naturally terminating middle-port coefficient*, not the older singular universal 4F3 kernel or a different outer-rank observer.

**Proof.** Suppose \(Y\) is rational and has finite poles over \(\mathbb C\). Along any chain of poles connected by integral shifts, choose the leftmost \(\beta\) and rightmost \(\gamma=\beta+h\), \(h\ge0\). At \(s=\beta-1\), the leftmost pole of \(Y(s+1)\) cannot be canceled by \(Y(s)\), so \(A_m(\beta-1)=0\). At \(s=\gamma\), the rightmost pole of \(Y(s)\) cannot be canceled by \(Y(s+1)\), so \(D_m(\gamma)=B_m(\gamma-1)=0\). Consequently \(A_m(z)\) and \(B_m(z+h)\) share the root \(z=\beta-1\). But the three roots of \(A_m\) are \(m-1,-1,-m-1\), all at least \(-m-1\), while the only root of \(B_m(s+h)\) is \(-3m-2-h<-m-1\). Contradiction. Thus \(Y\) has no finite poles and is a polynomial.

For nonzero polynomial \(Y(s)=c s^d+\cdots\), the two cubic leading coefficients in (3) are \(1\) and \(2\), so the left side has degree \(d+3\) with leading coefficient \(-c\ne0\). Its degree is at least three, whereas \(\deg W\le2\). The zero polynomial cannot solve (3) for nonzero \(W\). QED.

## Theorem B — a new finite-window certificate-size lower bound

Let \(m\ge4\), let \(W\) be as in Theorem A, and require (3) **only** at the \(m\) distinct integers \(0,\dots,m-1\).

1. Every polynomial local certificate \(Y(s)\in\mathbb Q[s]\) of degree \(d\) must satisfy
\[
\boxed{d\ge m-3.}\tag{4}
\]
Indeed \(A_mY(s+1)-D_mY(s)-W\) is a **nonzero** polynomial of exact degree \(d+3\), yet has \(m\) roots. The zero \(Y\) cannot satisfy \(m\ge4\) points because \(\deg W\le2\).

2. More generally, for \(Y=P/Q\) in reduced terms with \(\deg P=d\), \(\deg Q=e\), and \(Q(s)Q(s+1)\ne0\) for all sampled indices, necessarily
\[
\boxed{\max(d+e+3,\;2e+2)\ge m.}\tag{5}
\]
Cross-multiply (3) to obtain the nonzero polynomial
\[
A_m(s)P(s+1)Q(s)-D_m(s)P(s)Q(s+1)-W(s)Q(s)Q(s+1).
\]
It vanishes at the \(m\) indices and has degree at most \(\max(d+e+3,2e+2)\). If it vanished identically, Theorem A would be contradicted. QED.

3. This lower bound is **linear in the actual window length** and has a matching constructive upper bound. Since \(A_m(m-1)=0\) and \(D_m(s)\ne0\) for \(0\le s<m\), define
\[
y_{m-1}=-\frac{W(m-1)}{D_m(m-1)},\qquad
y_s=\frac{A_m(s)y_{s+1}-W(s)}{D_m(s)}
\quad(s=m-2,\dots,0).
\tag{6}
\]
There is a unique polynomial \(Y_m(s)\) of degree at most \(m-1\) interpolating \((s,y_s)\), and it satisfies (3) at all \(m\) nodes, including the naturally terminating last node. Therefore, for polynomial scalar local certificates:
\[
\boxed{m-3\ \le\ \deg Y_m^{\min}\ \le\ m-1\qquad(m\ge4).}\tag{7}
\]
The inequalities are exact statements for this certificate class; they **do not** assert a general lower bound on arithmetic algorithms or paired WZ/CM certificates.

## Executed exact evidence

The Python standard-library `Fraction` checker `research_notes/portable_direct/d25_a216_middle_window_degree_guard_20261030.py` was actually executed. It independently checks the original factorial ratio, the rational root separation, the source-signed weight and the terminal backward recursion, and constructs every Newton interpolation polynomial through exact forward differences for all \(1\le m\le16\). All 16 windows passed. In these finite cases the interpolated degrees were \(m-1\), while (4)–(7) are proved algebraically for all specified \(m\), not inferred from the 16 examples.

**Scientific meaning and BRC:** `COMPOSE_APPLIED`. The carrier retains the original \(n=3m+1+s\) label, double-zero \(T^2\) provenance, sign \(6n+1\), factorial denominators and finite cutoff. The permitted observer here is exact rational scalar telescoping across the middle window; its bounded-degree compression fails quantitatively. The original mod-\(p\) signed residual can admit finite-field, parameter-dependent, paired or more sophisticated compressed certificates, which this theorem does not exclude. No native X6/H0/B0 identification follows.

## Exact continuation, originality and authority

This is a **finite-window quantitative theorem**, distinct from earlier author notes excluding an unbounded single-term rational Gosper antiderivative of the *singular* 4F3 kernel (2026-10-30), the *full original* endpoint (2026-10-24), and the outer corrected rank (2026-10-26). Their negative results are reused, not recredited. Theorem B adds a precise required degree that grows with the actual original middle-source window; the note does not claim it resolves the all-prime LIFT.

**Mother target still OPEN:** \(A_p=\sum_{n<p}(6n+1)\binom{2n}{n}^2\binom{3n}{n}/216^n\equiv p\bmod p^3\) for \(p\equiv13,19\bmod24\), equivalent under already established original-port alignment to frozen \(\Delta_p-R_p=0\bmod p\). The accepted D24 first digit, finite Clausen port identity, all-class CM zero and regular middle-tail transformation are used unchanged. Next arithmetic step must pair the original *low two-zone* \(T^2\) jet and this middle source in a **multi-source p-adic/WZ** relation, retaining both signs. A fixed-degree exact one-term rational primitive is formally excluded; repeatedly searching the same class cannot finish the target.

**Non-substitutable native benchmark:** issue `awdawmip/enterprise-math#1559`: exact original H0/B0 divided-power \([X]U\bmod139129\) at \(p=373\), module rank, semilinear Frobenius/eta, signed odd Green/Hesse, \(\kappa\), \(\Delta-R\), and independent reproduction. At 2026-10-30 12:00+08 the Site status returned `research_authority_granted=false`, `write_relay_enabled=false`, checkpoint list `ACCESS_DENIED`; the current native session/claim/run/request and rightful owner were not independently established in this run. Existing `#1559` is a support intake with responsible owner path, **not** a completed native experiment. Do not infer registration, Source checkpoint, CLAIM, freeze, review or admitted Result from this author-side GitHub note.

Scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`, P000 and ACTIVE worldview remain unchanged; the separate maintenance lane was not accessed. Author-side project persistence does not grant session or task authority.

## Additional executed fixed-prime source cross-check (same research unit)

The already-published exact Fraction checker was extended and rerun against the original signed middle source at fixed primes 13, 19, 373. The backward recurrence defines \(y_0\); the exact finite identity follows by summing (3) after multiplication by \(d_s\):

\[
\boxed{\sum_{s=0}^{m-1} W_m(s)d_s=-d_0D_m(0)y_0}\quad\text{in }\mathbb Q.
\]

Every denominator is a \(p\)-unit for \(p=6m+1\) prime; the independently evaluated original middle valuation-two scalar is 10 (mod 13), 9 (mod 19) and **266 (mod 373)**. At \(p=373\), \(m=62\), the exact Newton polynomial was computed from 62 rational nodes and had degree **61**. The proved polynomial lower bound is 59 and the constructive upper bound is 61. These values verify the original n-labelled scalar contribution only, not the native H0/B0 \([X]U\) module experiment.

Executed source script commit 3e75f33489915828ec4193cff9c44a10ef55d754 (same path above; remote blob c05a07392cf00dcac08eec95a6fddf59d8812e15). This added p373 execution is a finite exact check, while the general rational identity and degree bounds rest on the proofs above.
