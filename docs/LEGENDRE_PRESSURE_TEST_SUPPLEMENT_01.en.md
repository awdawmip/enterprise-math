# Legendre Pressure Test — Supplement 01

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact refinements of `LEGENDRE_PRESSURE_TEST.en.md`.  
Discipline: **no proof of Legendre's conjecture is claimed here.**

## 1. Purpose

The first pressure-test note reduced the consecutive-square prime count to signed square carries and then to binary carry events. This supplement removes two remaining black boxes:

1. it gives a direct centered-residue criterion for the ternary carry \(\kappa_d(k)\);
2. it rewrites the anchor transfer \(\Lambda_b(k)\) as an ordinary centered discrepancy and proves that every negative transfer is confined to \(b\le k\).

These are exact integer statements, not density heuristics.

## 2. L007 — Centered square-carry criterion

Status: `PROVED`

Write

\[
k=qd+t,\qquad 0\le t<d,
\]

and define the centered anchor residue

\[
a_d(t)=t(t+1)\bmod d.
\]

The local square basin can be centered at \(t(t+1)\):

\[
(t^2,(t+1)^2)
=
 t(t+1)+\{1-t,\ldots,t\}.
\]

Therefore \(\kappa_d(k)=H_d(t)\) is exactly the number of representatives of

\[
s\equiv-a_d(t)\pmod d
\]

inside

\[
\{1-t,\ldots,t\}.
\]

Because this local interval has length \(2t<2d\), there are at most two representatives. For \(t>0\), they are the negative representative \(-a_d(t)\) and the positive representative \(d-a_d(t)\). Hence

\[
\boxed{
\kappa_d(k)
=
\mathbf 1_{a_d(t)<t}
+
\mathbf 1_{a_d(t)\ge d-t}
}
\]

with \(\kappa_d(k)=0\) when \(t=0\).

This recovers \(\kappa_d(k)\in\{0,1,2\}\), but more importantly identifies the values as **left-boundary and right-boundary crossings of one centered residue class**.

## 3. L008 — Explicit binary carry event

Status: `PROVED`

Let \(d\) be odd and write

\[
k=qd+t,
\qquad
0\le t<d.
\]

Set

\[
a=t(t+1)\bmod d,
\qquad
h=\left\lfloor\frac{t(t+1)}{d}\right\rfloor.
\]

The first note proved

\[
\kappa_d(k)-\kappa_{2d}(k)
=(-1)^q\varepsilon_d(k),
\qquad
\varepsilon_d(k)\in\{0,1\}.
\]

The event \(\varepsilon_d(k)\) is now explicit:

\[
\boxed{
\varepsilon_d(k)=
\begin{cases}
\mathbf 1_{a\ge d-t}, & q\equiv0\pmod2,\ h\equiv0\pmod2,\\
\mathbf 1_{a<t},       & q\equiv0\pmod2,\ h\equiv1\pmod2,\\
\mathbf 1_{a\ge t},    & q\equiv1\pmod2,\ h\equiv0\pmod2,\\
\mathbf 1_{a<d-t},      & q\equiv1\pmod2,\ h\equiv1\pmod2.
\end{cases}
}
\]

Proof sketch. The lift from modulus \(d\) to \(2d\) is determined by the parity of \(h\), because

\[
t(t+1)=hd+a.
\]

If \(h\) is even, the lifted residue is \(a\); if \(h\) is odd, it is \(a+d\). The parity of \(q\) decides whether \(k\bmod 2d=t\) or \(d+t\). Applying L007 in those four cases gives the displayed criterion.

For odd \(d\), the local quotient parity also has the global-centered interpretation

\[
\left\lfloor\frac{k(k+1)}{d}\right\rfloor
\equiv h\pmod2.
\]

Indeed, substituting \(k=qd+t\) gives

\[
\left\lfloor\frac{k(k+1)}d\right\rfloor
=q^2d+q(2t+1)+h,
\]

and the first two terms have equal parity and cancel modulo two because \(d\) is odd.

Thus the binary carry is completely determined by:

- the Euclidean quotient layer \(q=\lfloor k/d\rfloor\);
- the local centered quotient parity \(h\bmod2\);
- one boundary comparison involving \(a=t(t+1)\bmod d\).

The open problem is no longer to understand an unspecified \(0/1\) variable, but to control the signed distribution of these explicit boundary crossings over square-free divisor layers.

## 4. L009 — Transverse anchor discrepancy identity

Status: `PROVED`

Let

\[
M=k(k+1)
\]

and let \(A_k\) be the square-free product of all primes \(p\le k\) dividing \(M\). Let \(b\) be any positive integer with

\[
\gcd(b,A_k)=1.
\]

Recall the anchor Möbius transfer

\[
\Lambda_b(k)
=
\sum_{a\mid A_k}\mu(a)\kappa_{ab}(k).
\]

Define

\[
R_A(x)=\#\{1\le m\le x:\gcd(m,A)=1\}
\]

and the centered survivor count

\[
S_b(k)=
\#\left\{
1-k\le s\le k:
 b\mid M+s,
 \gcd(s,A_k)=1
\right\}.
\]

Then

\[
\boxed{
\Lambda_b(k)
=
S_b(k)-2R_{A_k}\!\left(\left\lfloor\frac{k}{b}\right\rfloor\right)
}.
\]

Proof. From the square-carry decomposition,

\[
\kappa_{ab}(k)=H_{ab}(k)-2\left\lfloor\frac{k}{ab}\right\rfloor.
\]

Möbius inversion over \(a\mid A_k\) turns the first sum into the number of multiples \(n\in I_k\) of \(b\) for which \(n/b\) is coprime to \(A_k\). Since \(\gcd(b,A_k)=1\), this is equivalent to \(\gcd(n,A_k)=1\). Writing \(n=M+s\) and using \(A_k\mid M\) turns it into \(\gcd(s,A_k)=1\), giving \(S_b(k)\).

For the coarse term,

\[
\sum_{a\mid A_k}\mu(a)
\left\lfloor\frac{k}{ab}\right\rfloor
=
R_{A_k}\!\left(\left\lfloor\frac{k}{b}\right\rfloor\right).
\]

Subtracting twice this quantity proves the identity.

## 5. Immediate localization corollaries

### 5.1 Negative transfer is a small-modulus phenomenon

If

\[
b>k,
\]

then \(\lfloor k/b\rfloor=0\), so

\[
\boxed{\Lambda_b(k)=S_b(k)\ge0.}
\]

Therefore every negative anchor transfer must satisfy

\[
\boxed{b\le k.}
\]

The previously found counterexample

\[
\Lambda_5(456)=-4
\]

is therefore forced to live in the genuinely small transverse layer; negative anomalies cannot migrate to arbitrary large divisor products.

### 5.2 Beyond twice the root, the transfer is binary

If

\[
b>2k,
\]

then the centered interval contains fewer than \(b\) consecutive integers, so it contains at most one multiple of \(b\). Together with the zero baseline,

\[
\boxed{\Lambda_b(k)\in\{0,1\}.}
\]

Thus the anchor transform has a second binary regime, now on the **large transverse-divisor side**.

### 5.3 Finite support

If

\[
b>(k+1)^2-1,
\]

there is no positive multiple of \(b\) in the square-basin interior and the baseline is zero, hence

\[
\boxed{\Lambda_b(k)=0.}
\]

So only

\[
1<b\le(k+1)^2-1
\]

can contribute after the anchor transform.

## 6. Revised structure of P017

The signed problem now separates naturally into three regions.

1. **Small transverse moduli \(b\le k\):** the only region where \(\Lambda_b(k)\) can be negative; this is where the strong interaction with the root/cutoff lives.
2. **Intermediate moduli \(k<b\le2k\):** nonnegative transfers, with at most two centered hits.
3. **Large moduli \(2k<b\le(k+1)^2-1\):** binary transfers \(0/1\), hence a Boolean boundary problem on the truncated divisor lattice.

This suggests a more focused sign-reversing strategy: do not seek one universal involution across all divisor products. First isolate the small-modulus discrepancy, then attempt to pair the nonnegative binary large-modulus terms through cutoff-crossing edges in the divisor lattice.

Whether that strategy can overcome the classical parity barrier remains open.

## 7. Verification status

Executable checks in `tests/test_legendre_pressure.py` verify, over bounded ranges:

- the centered carry criterion agrees exactly with the original hit-count definition;
- the explicit binary event reproduces \(\kappa_d-\kappa_{2d}\);
- the anchor discrepancy identity agrees exactly with the original Möbius transfer;
- \(b>k\Rightarrow\Lambda_b\ge0\);
- \(b>2k\Rightarrow\Lambda_b\in\{0,1\}\);
- the finite-support cutoff.

The proofs above, not the finite checks, are the mathematical basis for the claims.
