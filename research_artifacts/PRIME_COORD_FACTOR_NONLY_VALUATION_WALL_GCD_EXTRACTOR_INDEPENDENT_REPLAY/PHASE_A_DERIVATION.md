# PCF4R Phase A — N-only valuation-wall GCD extractor independent derivation

Status: `PHASE_A_FROZEN / DERIVATION_INDEPENDENT / CHECKER_PENDING_SAME_CHECKPOINT`

Task: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`

Publication: `TP2-DF186CDB4959BEA10875`

Researcher-ID: `EM-PCF4R-D74517`

Claim: `chatgpt-pcf4r-20260827-1927`

## Source-exposure boundary

Phase A uses only the published taskbook, the accepted parent result record
`RR-A33E88150B0DAD0B13B8`, standard elementary number theory, and an independently
authored exact-integer implementation.

During control-plane dispatch intake, the Issue #240 scheduler stream exposed a
high-level summary that a non-authoritative duplicate execution had claimed a
positive N-only splitter. No duplicate return, derivation, script, artifact, or
proof discussion has been opened. Therefore this phase is
`DERIVATION_SOURCE_BLIND / OUTCOME_ANCHOR_EXPOSED`; the mathematics below was
reconstructed independently and is not a blind-verdict experiment.

## 1. Observable and local valuation wall

Define

\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}
   =\binom{2s}{s}^2\binom{3s}{s}\in\mathbb Z_{\ge 0}.
\]

Let \(r>3\) be prime and \(0\le s<r\). Since \(2s<2r\), \(3s<3r\), and
\(s<r\), Legendre's formula has only the first \(r\)-adic digit:

\[
v_r((2s)!)=\left\lfloor\frac{2s}{r}\right\rfloor,\quad
v_r((3s)!)=\left\lfloor\frac{3s}{r}\right\rfloor,\quad
v_r(s!)=0.
\]

Hence

\[
\boxed{v_r(A_s)=
\left\lfloor\frac{2s}{r}\right\rfloor+
\left\lfloor\frac{3s}{r}\right\rfloor.}
\]

In particular, for \(s<r\),

\[
\boxed{r\mid A_s\iff 3s\ge r.}
\]

The first divisibility wall is therefore the public-index inequality
\(s\ge \lceil r/3\rceil\). No hidden factor is needed by the constructor to
evaluate \(A_s\); hidden primes appear only in this proof-side interpretation.

## 2. First dyadic nonunit alternative

Let \(N=pq\) with distinct primes \(3<p<q\). Let

\[
s=2^j,\qquad
j=\min\{i\ge 0:3\cdot 2^i\ge p\}.
\]

Because \(p>3\), \(j\ge1\). Minimality gives

\[
\frac{3s}{2}<p\le 3s,
\qquad\text{hence}\qquad
s<\frac{2p}{3}<p<q.
\]

For every earlier dyadic seed \(u\le s/2\), \(3u<p<q\), so the local wall
formula gives

\[
\gcd(A_u,N)=1.
\]

At \(s\), \(p\mid A_s\). Since also \(s<q\), the same local formula gives

\[
q\mid A_s\iff 3s\ge q.
\]

Therefore the first dyadic nonunit is exactly

\[
\boxed{
\gcd(A_s,N)=
\begin{cases}
p,&3s<q,\\
N,&3s\ge q.
\end{cases}}
\]

Thus the public loop "double the seed until the gcd is not 1" has only two
possible first outcomes: it either returns the smaller factor immediately, or
it synchronizes both hidden walls.

If synchronization occurs, then

\[
q\le 3s<2p,
\]

so

\[
\boxed{q<2p.}
\]

This implication is exact and is the only information needed by the fallback.

## 3. Two-seed square-root fallback after synchronization

Assume the synchronized case \(q<2p\). Put

\[
M=\lfloor\sqrt N\rfloor,\qquad
t=\left\lfloor\frac{M}{3}\right\rfloor
 =\left\lfloor\frac{\sqrt N}{3}\right\rfloor.
\]

Because \(p<\sqrt{pq}<q\),

\[
\frac p3<\frac{\sqrt N}{3}<\frac q3.
\]

Also \(q<2p\) implies \(N<2p^2\). Since \(\sqrt2<3/2\),

\[
\frac{\sqrt N}{3}<\frac p2.
\]

Hence, for \(p\ge5\),

\[
t+1<\frac p2+1<p.
\]

So both \(t\) and \(t+1\) lie below \(p\), and therefore below \(q\); the local
valuation-wall formula applies to both.

Write

\[
a_r=\left\lceil\frac r3\right\rceil.
\]

The inequality \(t<q/3\) gives \(t<a_q\), while
\(t+1>\sqrt N/3>p/3\) gives \(t+1\ge a_p\).

For distinct primes \(3<p<q\),

\[
\boxed{a_p<a_q.}
\]

Indeed every prime \(>3\) is \(6k\pm1\). If \(p,q\) lie in the same \(6k\)
block, they are the twin pair \(6k-1,6k+1\), whose ceilings are
\(2k,2k+1\); if their blocks differ, strict increase is immediate.

Now either:

1. \(t\ge a_p\). Then \(a_p\le t<a_q\), so
   \(p\mid A_t\) and \(q\nmid A_t\), hence \(\gcd(A_t,N)=p\); or
2. \(t<a_p\). Since \(t+1\ge a_p\), integrality forces \(t+1=a_p<a_q\).
   Hence \(p\mid A_{t+1}\), \(q\nmid A_{t+1}\), and
   \(\gcd(A_{t+1},N)=p\).

Therefore

\[
\boxed{
\text{after synchronization, at least one of }
\gcd(A_t,N),\gcd(A_{t+1},N)
\text{ equals }p.}
\]

The fallback is universal on the synchronized branch; no density or finite
census assumption is used.

## 4. Public N-only stopping rule

The constructor receives only \(N\).

1. Compute \(M=\lfloor\sqrt N\rfloor\) and \(t=\lfloor M/3\rfloor\).
2. Generate the public integer sequence \(A_n\) exactly.
3. Test dyadic indices \(1,2,4,\ldots\).
4. Stop at the first dyadic \(s\) with \(g=\gcd(A_s,N)>1\).
5. If \(1<g<N\), return \(g\).
6. If \(g=N\), test the already generated or subsequently generated public
   fallback indices \(t,t+1\), returning the first gcd strictly between 1 and
   \(N\).
7. A public safety cap \(n\le M\) is sufficient under the domain promise,
   because the first dyadic wall satisfies \(s<p\le M\), and in the
   synchronized branch \(t+1<p\le M\).

No step queries \(p\), \(q\), a residue class of a hidden factor, a
factor-dependent root, or a prime list. Prime generation is permitted only in
the regression oracle, not in the constructor.

## 5. Exact recurrence

From the factorial ratio,

\[
\frac{A_{n+1}}{A_n}
=
\frac{6(2n+1)(3n+1)(3n+2)}{(n+1)^3}.
\]

Thus

\[
\boxed{
(n+1)^3A_{n+1}
=
6(2n+1)(3n+1)(3n+2)A_n,\qquad A_0=1.}
\]

The division in the implementation is ordinary exact integer division, not a
modular inverse. Exactness follows inductively from the binomial-product
definition of \(A_n\). This is valid over composite \(N\), including exactly
at the nonunit indices where modular division would be illegal.

## 6. Complexity boundary

Let \(L=\lceil\log_2 N\rceil\), and let \(S\) be the largest sequence index
generated before return. The proof gives \(S< p\le\sqrt N\), so

\[
S=O(\sqrt N)=2^{L/2+O(1)}.
\]

Using
\(\binom{2n}{n}<4^n\) and \(\binom{3n}{n}<8^n\),

\[
A_n<128^n,
\]

so \(A_n\) has \(O(n)\) bits. A straightforward exact recurrence therefore
uses \(O(S+L)\) bits of live memory and, with a multiplication-cost function
\(M_{\rm bit}(k)\), a conservative bit-operation bound

\[
O\!\left(S\,M_{\rm bit}(S)\,\operatorname{polylog}S\right).
\]

The number of gcd observations is only \(O(\log N)\) on the dyadic branch plus
two fallback observations, but producing the exact factorial sequence by this
constructor remains square-root scale. Therefore

\[
\boxed{\text{N-only deterministic extractor} \ne
\text{factoring-speedup theorem}.}
\]

## 7. Phase-A verdict before source comparison

All four mathematical target components close positively:

- local valuation wall: proved;
- first dyadic nonunit alternative: proved;
- synchronization implication \(q<2p\): proved;
- \(t,t+1\) fallback: proved.

Provisional Phase-A verdict:

`N_ONLY_GCD_EXTRACTOR_VERIFIED`, subject to the independently authored exact
checker freezing and Phase-B comparison/dedup required by the taskbook.
