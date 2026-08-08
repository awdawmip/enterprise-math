# Legendre Pressure Test — Supplement 03

Status: `ACTIVE RESEARCH NOTE`  
Scope: established threshold-complex topology specialized to the integer cutoff, plus the Enterprise Math integer-root dimension bound.  
Discipline: **this note does not prove Legendre's conjecture.**

## 1. Prior-art correction

The cutoff-crossing pairing in Supplement 02 has a mature topological home.

Pakianathan and Winfree developed scalar quota/threshold complexes and proved that every scalar quota complex is homotopy equivalent to a bouquet of spheres indexed by shell faces near the quota. They also study `LogPrime`, assigning weight \(\log p\) to a prime vertex so that additive quota conditions encode multiplicative prime-product thresholds. [SRC-PAKIANATHAN-WINFREE-2013-THRESHOLD]

Therefore Enterprise Math does **not** claim threshold complexes, LogPrime topology, the shell/bouquet theorem, or the topological interpretation of Möbius cancellation as new.

The useful pressure-test question is narrower: what extra restrictions arise because our quota is the exact square-basin cutoff and the minimum prime is constrained by integer-root layers?

## 2. L013 — Multiplicative threshold complex and Euler tail

Status: `ESTABLISHED PRIOR ART + SPECIALIZED EXACT IDENTITY`

Let

\[
G=\prod_{p\in\mathcal P}p
\]

be square-free and let \(T\ge1\) be an integer. Define a simplicial complex

\[
K(G,T)
=
\left\{
F\subseteq\mathcal P:
\prod_{p\in F}p\le T
\right\}.
\]

The empty face has product 1. Downward closure is immediate because every subproduct of a product not exceeding \(T\) also does not exceed \(T\).

The Möbius function of a square-free divisor is

\[
\mu\!\left(\prod_{p\in F}p\right)=(-1)^{|F|}.
\]

If \(G>1\), the full Boolean divisor sum is zero:

\[
\sum_{d\mid G}\mu(d)=0.
\]

Hence

\[
\sum_{\substack{d\mid G\\d>T}}\mu(d)
=
-
\sum_{\substack{d\mid G\\d\le T}}\mu(d).
\]

For the complex above,

\[
\sum_{\substack{d\mid G\\d\le T}}\mu(d)
=
1-\chi(K(G,T)),
\]

so

\[
\boxed{
\sum_{\substack{d\mid G\\d>T}}\mu(d)
=
\widetilde\chi(K(G,T))
}.
\]

Thus the large Möbius tail is exactly a reduced Euler characteristic.

No logarithm is needed in this integer identity. To connect it to the established quota-complex theorem, assign each prime the external weight \(w(p)=\log p\) and quota

\[
q=\log(T+1).
\]

Because face products are integers,

\[
\sum_{p\in F}\log p<\log(T+1)
\iff
\prod_{p\in F}p\le T.
\]

So \(K(G,T)\) is precisely a finite scalar quota complex in the sense of the prior work.

## 3. L014 — Shell faces are exactly cutoff-crossing divisors

Status: `SPECIALIZATION OF ESTABLISHED QUOTA-COMPLEX SHELL THEOREM`

Let \(p\) be the least prime in \(\mathcal P\), and assume \(p\le T\). Pakianathan–Winfree's scalar quota theorem identifies one sphere for each face \(F\) not containing the minimum-weight vertex and lying in the shell

\[
q-w(p)\le w(F)<q.
\]

Under the multiplicative specialization

\[
w(r)=\log r,
\qquad
q=\log(T+1),
\]

write

\[
c=\prod_{r\in F}r.
\]

The shell inequalities become

\[
\frac{T+1}{p}\le c<T+1.
\]

Since \(c\) is an integer, this is exactly

\[
\boxed{c\le T<pc.}
\]

These are precisely the unpaired cutoff edges of L010.

If \(|F|=s+1\), the associated sphere has dimension \(s\). Its contribution to reduced Euler characteristic is

\[
(-1)^s,
\]

which equals

\[
\mu(pc)=(-1)^{s+2}=(-1)^s.
\]

Therefore L010 is not merely analogous to the quota shell theorem: on the finite prime support it is exactly its Euler-characteristic cancellation pattern written without logarithms.

## 4. L015 — Integer-root bound on shell dimension

Status: `PROVED`

The established topology now combines with Enterprise Math's integer-root hierarchy.

Let \(F\) be a shell face of dimension \(s\), so it contains \(s+1\) primes other than the least vertex \(p\). Because \(p\) is least, every prime in \(F\) is at least \(p\). Therefore

\[
c=\prod_{r\in F}r\ge p^{s+1}.
\]

But every shell face satisfies \(c\le T\). Hence

\[
p^{s+1}\le T,
\]

and by the exact integer-root definition,

\[
\boxed{p\le R_{s+1}(T).}
\]

This gives a dimension filtration without real-valued asymptotics.

In the Legendre application \(T=2k\):

\[
\boxed{p\le R_{s+1}(2k).}
\]

Consequently:

- 1-dimensional shell spheres, which contribute negatively to Euler characteristic, require \(p\le R_2(2k)\);
- 3-dimensional negative spheres require \(p\le R_4(2k)\);
- 5-dimensional negative spheres require \(p\le R_6(2k)\);
- in general, an odd-dimensional negative shell sphere of dimension \(2m-1\) requires \(p\le R_{2m}(2k)\).

L011 is exactly the divisor-language form of this odd-dimensional specialization.

## 5. Homological form of the remaining parity problem

Let

\[
\beta_s(G,T)
\]

be the number of shell spheres of dimension \(s\); for scalar quota complexes this is also the reduced Betti rank in that dimension under the bouquet decomposition. Then

\[
\boxed{
\sum_{\substack{d\mid G\\d>T}}\mu(d)
=
\sum_{s\ge0}(-1)^s\beta_s(G,T).
}
\]

The sieve parity obstruction has therefore acquired an exact finite topological form:

> control the balance between even-dimensional and odd-dimensional shell homology.

The integer-root result does not by itself prove the needed balance, but it says the odd-dimensional homology is not distributed freely: higher odd dimensions can only occur in progressively lower least-prime root shells.

This suggests replacing one undifferentiated parity sum by the two-parameter filtration

\[
(\text{least-prime root shell},\ \text{homological dimension}).
\]

## 6. Next attack

The leading unresolved negative layer is now the 1-dimensional shell homology, corresponding to depth-3 negative cutoff divisors

\[
b=pqr,
\qquad
qr\le2k<pqr.
\]

Higher odd dimensions are automatically pushed deeper toward small \(p\) by L015.

The next pressure-test target is therefore:

1. classify or pair the 1-dimensional shell cycles by least prime \(p\);
2. compare their negative Euler mass with the positive 0-dimensional and 2-dimensional shell mass in the same root shell;
3. determine whether the self-consistency `root = cutoff = k` imposes extra relations between these Betti layers that are absent in an arbitrary quota complex;
4. connect any remaining negative shell mass to the small-modulus discrepancy region \(b\le k\).

A topological reformulation alone is not a solution. Progress requires a new inequality, injection, recursion, or cancellation that uses the square-basin/root-cutoff constraint.

## 7. Executable checks

`src/enterprise_math/cutoff_pairing.py` and `tests/test_cutoff_pairing.py` now verify on bounded finite supports that:

- the shell-sphere alternating count equals the Möbius tail;
- shell counts by dimension reproduce the reduced Euler characteristic;
- every shell dimension \(s\) satisfies the integer-root bound \(p\le R_{s+1}(T)\);
- for actual square-basin composite states the topological tail equals the L010 cutoff-pairing tail.

The quota-complex homotopy theorem is cited prior art; the finite tests do not substitute for that theorem or for the elementary proofs of the specialized identities.
