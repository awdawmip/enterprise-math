# Legendre Pressure Test — Supplement 02

Status: `ACTIVE RESEARCH NOTE`  
Scope: sign-reversing cutoff pairings and integer-root localization of the large transverse Möbius tail.  
Discipline: **this note does not prove Legendre's conjecture.**

## 1. Starting point

Supplement 01 proved that after the anchor transform,

\[
\Pi(k)=2+
\sum_{\substack{b\mid B_k\\b>1}}
\mu(b)\Lambda_b(k),
\]

and that

\[
b>2k\quad\Longrightarrow\quad\Lambda_b(k)\in\{0,1\}.
\]

Thus the large transverse region is already Boolean. The remaining question is whether its many signed divisor terms can be cancelled structurally rather than estimated independently.

This supplement gives such a cancellation. The underlying toggle argument is elementary Möbius cancellation on a Boolean divisor lattice and is therefore not claimed as new mathematics; the project-specific point is how the `2k` square-basin cutoff and integer-root hierarchy emerge when it is applied to the Legendre pressure test. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 2. L010 — Cutoff-crossing Möbius pairing

Status: `PROVED`

Let

\[
G=\prod_{r\in\mathcal P}r
\]

be square-free, choose a distinguished prime \(p\mid G\), and let \(T\ge0\) be an integer cutoff. Then

\[
\boxed{
\sum_{\substack{d\mid G\\d>T}}\mu(d)
=
-
\sum_{\substack{c\mid G/p\\c\le T<pc}}
\mu(c)
}.
\]

### Proof

Every divisor of \(G\) is uniquely one of

\[
c,\qquad pc,
\]

with \(c\mid G/p\). Since

\[
\mu(pc)=-\mu(c),
\]

we may pair the two terms by toggling the factor \(p\).

If \(c>T\), then also \(pc>T\), so both terms occur in the tail and cancel exactly.

If \(pc\le T\), neither term occurs.

The only unpaired case is

\[
c\le T<pc,
\]

where only \(pc\) remains and contributes \(-\mu(c)\). Summing those cutoff-crossing edges proves the identity.

This is an explicit sign-reversing involution on every divisor pair that does not cross the cutoff.

## 3. Applying L010 state by state in a square basin

Let

\[
M=k(k+1)
\]

and let \(A_k\) be the square-free product of anchor primes \(p\le k\) dividing \(M\). Consider a state

\[
n\in I_k=(k^2,(k+1)^2)
\]

that survives the anchor sieve:

\[
\gcd(n,A_k)=1.
\]

Define its transverse small-prime support

\[
G_k(n)
=
\prod_{\substack{p\le k\\p\mid n\\p\nmid A_k}}p.
\]

For \(b>2k\), Supplement 01 gives \(\Lambda_b(k)=S_b(k)\in\{0,1\}\). Interchanging the finite sums therefore gives the exact large-region contribution

\[
\boxed{
\sum_{\substack{b\mid B_k\\b>2k}}
\mu(b)\Lambda_b(k)
=
\sum_{\substack{n\in I_k\\\gcd(n,A_k)=1}}
\;
\sum_{\substack{b\mid G_k(n)\\b>2k}}
\mu(b)
}.
\]

If \(n\) is prime, then \(G_k(n)=1\) and its inner tail is zero.

If \(n\) is composite, L001 guarantees a prime factor \(p\le k\). Because the state survived all anchor primes, its least prime factor is transverse and belongs to \(G_k(n)\). Choose this least factor as the distinguished \(p\), and set

\[
T=2k.
\]

L010 then cancels every large-divisor term except the edges

\[
\boxed{
c\le2k<pc.}
\]

So the apparently exponential large-divisor tail is supported only on a cutoff boundary.

## 4. L011 — Odd-depth root hierarchy for negative boundary terms

Status: `PROVED`

Let \(p\) be the least prime factor chosen above. Consider an unpaired cutoff divisor

\[
b=pc,
\qquad
c\le2k<b,
\]

with negative Möbius sign

\[
\mu(b)=-1.
\]

Because \(b\) is square-free, it has an odd number of distinct prime factors. Write

\[
\omega(b)=2m+1.
\]

The case \(m=0\) is impossible: it would give \(c=1\) and hence \(p>2k\), whereas the least factor satisfies \(p\le k\). Thus \(m\ge1\).

After removing the least factor \(p\), the divisor \(c\) contains exactly \(2m\) distinct prime factors. Every one is at least \(p\). Therefore

\[
c\ge p^{2m}.
\]

But the cutoff condition gives \(c\le2k\). Hence

\[
p^{2m}\le2k,
\]

which is exactly

\[
\boxed{
p\le R_{2m}(2k).}
\]

This produces an integer-only hierarchy:

- every negative cutoff term has \(p\le R_2(2k)\);
- every negative term of depth at least 5 has \(p\le R_4(2k)\);
- every negative term of depth at least 7 has \(p\le R_6(2k)\);
- in general, negative depth \(2m+1\) is forced below the \(2m\)-th integer-root layer of \(2k\).

No real exponent or asymptotic approximation is needed.

## 5. L012 — Nonnegative outer root shell

Status: `PROVED`

Let \(n\) be an anchor-surviving composite state in \(I_k\), and let \(p\) be its least prime factor. If

\[
p>R_2(2k),
\]

then its large-region Möbius tail satisfies

\[
\boxed{
\sum_{\substack{b\mid G_k(n)\\b>2k}}\mu(b)\ge0.
}
\]

### Proof

By L010, only cutoff-crossing terms remain. Any negative one would have odd depth at least three, so L011 with \(m\ge1\) would force

\[
p\le R_2(2k),
\]

contrary to the hypothesis. Therefore every surviving boundary term has nonnegative sign, and their sum is nonnegative.

This is the first pressure-test result that assigns a definite sign to an entire root shell rather than merely rewriting the prime count.

## 6. Root-shell stratification

L011 gives a finer statement. If

\[
R_{2m+2}(2k)<p\le R_{2m}(2k),
\]

then no negative boundary term driven by \(p\) can have depth greater than

\[
2m+1.
\]

Thus increasing Möbius overlap depth is progressively confined toward smaller least prime factors:

\[
\text{deep negative overlap}
\Longrightarrow
\text{lower integer-root shell}.
\]

This is a direct interaction between the integer-root hierarchy and signed sieve cancellation. It is the most theory-native structural output of the Legendre pressure test so far.

## 7. What remains after the pairing

The pressure test is now more localized, but not solved.

There are two unresolved sources of possible negative mass:

1. **the small transverse discrepancy region \(b\le k\)** from L009, where \(\Lambda_b(k)\) itself may be negative;
2. **cutoff-crossing edges in the large region**, now constrained by L011 to low integer-root shells.

The next useful theorem would have to connect these two pieces, or control the aggregate cutoff-boundary sum inside each root shell. A purely termwise absolute bound is unlikely to be enough because the classical parity obstruction is fundamentally about signed cancellation.

Concrete next targets:

- sum the cutoff-crossing boundary by least prime \(p\) and root shell;
- determine whether the depth-3 negative layer admits a second involution after fixing \(p\);
- compare small-region negative discrepancies with positive boundary mass generated by the same least-prime shell;
- seek a recursion in \(R_2(2k),R_4(2k),\ldots\) rather than in real-valued density estimates.

## 8. Verification

`src/enterprise_math/cutoff_pairing.py` implements the finite identities. `tests/test_cutoff_pairing.py` checks:

- the Boolean-lattice tail identity over many cutoffs;
- the state-by-state application to actual square-basin composites;
- the odd-depth root hierarchy for every generated negative boundary edge;
- occurrence of both depth-3 and depth-5 negative boundary examples in the bounded test domain.

Finite verification supports the implementation only; L010–L012 are justified by the proofs above.
