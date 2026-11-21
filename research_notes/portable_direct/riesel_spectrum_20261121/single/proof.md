# The exact one-channel branch of the old residual class

Status: author derivation and exact arithmetic evidence, under researcher
`EM-DIRECT-970E1C` and activity `RA-D2EC212845B63844081F9A14`.
This is not an independent project Review or a Foundation promotion.

Let

\[
F_n(a)=a^2 2^n-1,\quad
a_*=690786768637635218740714348513373826260012289,
\]

and let the fixed twenty-prime dictionary \(P\), product \(M\), complete old
phases, and hole set \(H\subset\mathbb Z/105\mathbb Z\) be those in the v6
cost result at source commit `2feef401388e6e81a35dd8b0e66383f43561ad12`,
`research_notes/portable_direct/riesel_budget_20261120/cost/proof.md`.
All roots below are positive odd integers with \(a\equiv a_*\pmod{2M}\).
Every such square is a Riesel number: the old channels cover all odd indices,
and \(F_{2u}(a)=(a2^u-1)(a2^u+1)\) for each \(u\ge1\).

As before, \(\delta_P(a)\) is the minimum number of primes outside \(P\) in
a finite proper prime cover, or infinity if there is no such cover. The
minimum total size is separately denoted \(\tau(a^2)\).

## 1. A complete classification at budget one

**Theorem.** Throughout this old root class,

\[
\delta_P(a)\ne0,\qquad
\boxed{\delta_P(a)=1\iff 3\nmid a.}
\]

If a one-prime supplement exists, that prime is necessarily 3.

**Proof.** The old hole set contains both \(u\equiv0\) and \(u\equiv1\)
modulo 105. In particular \(F_{210}(a)\) and \(F_{212}(a)\) have no prime
divisor in \(P\). Thus zero supplemental primes cannot suffice. If one prime
\(q\notin P\) suffices, it must divide both these terms. Since \(q\nmid2a\),
subtracting the first congruence multiplied by 4 from the second gives

\[
q\mid (2^2-1)=3.
\]

Hence \(q=3\), and necessarily \(3\nmid a\). Conversely, if \(3\nmid a\),
then \(a^2\equiv1\pmod3\), so

\[
F_{2u}(a)\equiv4^u-1\equiv0\pmod3
\]

for every positive \(u\). Prime 3 supplements the old odd-index cover.
All terms exceed the prescribed cover primes, so every divisor is proper. ∎

The original fixed root satisfies \(3\mid a_*\), so this easy branch does not
alter the fixed-root obstruction studied elsewhere in this continuation.

## 2. Exact relative density

Write \(a=a_*+2Mt\) for \(t\ge0\). Since \(3\nmid2M\), these roots run
uniformly through the three residue classes modulo 3 as \(t\) runs through
any three consecutive integers. Exactly two classes satisfy \(3\nmid a\).
Therefore the set with \(\delta_P(a)=1\) has natural relative density

\[
\lim_{T\to\infty}\frac{\#\{0\le t<T:\delta_P(a_*+2Mt)=1\}}{T}
=\frac23.
\]

This is a deterministic density in the specified arithmetic progression,
not an empirical or probabilistic statement about all Riesel numbers.

## 3. An infinite family with exact total cost 21

The old dictionary has a private odd index for each of its twenty channels.
For the current construction one may choose, in increasing-prime order,

\[
(37,3,89,5,293,117,413,113,41,33,87,233,353,207,237,257,53,173,63,47).
\]

No odd index is hit by the new prime 3. Its own private old-hole index can
be \(n=2\). Thus \(S=P\cup\{3\}\) has 21 private indices.
Use the v6 coprimalization lemma, explicitly reproduced here: put

\[
D=\operatorname{lcm}_{i<j}(2^{|n_i-n_j|}-1),\qquad
E=D\Big/\prod_{p\in S}p^{v_p(D)}.
\]

Impose the compatible congruences

\[
a\equiv a_*\pmod{2M},\qquad a\equiv1\pmod3,
\qquad a\equiv0\pmod E.
\]

Any common prime divisor of two private terms divides \(D\). If it belongs
to \(S\), privacy excludes it; otherwise it divides \(E\mid a\), which
would make every \(F_n(a)\) equal to \(-1\) modulo that prime. Consequently
the 21 private terms are pairwise coprime. Every finite prime cover requires
at least 21 primes, while \(S\) supplies 21. Every sufficiently large root
in this CRT progression therefore satisfies

\[
\boxed{\delta_P(a)=1,\qquad\tau(a^2)=21.}
\]

For arbitrary roots with \(3\nmid a\), the assertion is
\(\delta_P(a)=1\) and \(\tau(a^2)\le21\); equality for the total cost is
established for the coprimalized subfamily just constructed.

## 4. Reproducible evidence and native interpretation

`verify_single_channel.py` checks the entire old period 6720, the complete
36-class hole predicate, both necessity indices, all private witnesses,
and the full 21-prime covering period. It constructs a complete 3612-digit
root and its progression modulus, recorded losslessly in hexadecimal in
`single_channel_certificate.json`. The 210 pairwise gcds of the 21 witness
terms are all 1.

Actual term generation uses the four pinned project modules from source
commit `b1efc6c805661ed7b476e6e730107da6043176ee`. The native singleton
positive packet is \(x\mapsto2x+1\), initialized at \(x_0=a^2-1\).
It is executed through index 413, with weight and multiplicity both 1.
The fixed X6 anchor and the typed integer register are retained. Arithmetic
index and prime-observer count are not physical time or spatial dimension.

For the declared observation “does one extra prime suffice?”, the old
observer \(O_P\) omits a necessary distinction, while adding the residue
modulo 3 is sufficient. Within the fixed old fiber, its further binary
readout \(1_{3\mid a}\) is exactly sufficient for that budget-one question.
The integer dynamics and joint cofactor information remain available; this
scoped decision quotient does not erase them from the underlying state.

Run from the project root with pinned native modules available:

```bash
python research_notes/portable_direct/riesel_spectrum_20261121/single/verify_single_channel.py
```
