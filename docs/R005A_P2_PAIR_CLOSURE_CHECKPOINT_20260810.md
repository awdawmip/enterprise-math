# R005-A — p=2 Pair-Closure Structural Checkpoint

Status: `PROVED R005 STRUCTURE + EXACT EXECUTABLE CHECKPOINT / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-10`

## 1. Research compression

The square-basin no-least problem has now been reduced from

`all composites in the basin`

to

`local non-forced witnesses -> witness pairs -> deterministic closure`.

For

\[
A=k^2,\qquad U=k^2+2k,
\]

let candidate divisor witnesses be primes \(q\le k\), and let

\[
C_4=\lfloor U^{1/4}\rfloor.
\]

On the theorem slice where the fourth-root core is forced, the following
statements are exact.

## 2. T-A24 — local forcedness above the fourth-root core

For a prime

\[
C_4<q\le k,
\]

we have

\[
q^2\le A,\qquad q^4>U.
\]

The only possible exclusive collisions for q are therefore:

1. the pure cube \(q^3\), if it lies in the basin;
2. a product \(qr\), with r prime above the candidate horizon.

All \(q^e r\) with \(e\ge2\) are impossible in this range.

Define

\[
P^+(x)=\min\{r\text{ prime}:r>x\}
\]

and

\[
\Delta_k(q)
=
qP^+(k^2/q)-k^2.
\]

Then

\[
\boxed{
q\text{ forced}
\iff
k^2<q^3\le k^2+2k
\quad\lor\quad
\Delta_k(q)\le2k.
}
\]

Thus

\[
\boxed{
q\text{ non-forced}
\iff
q^3\notin(A,U]
\quad\land\quad
\Delta_k(q)>2k.
}
\]

This quantity is intentionally kept distinct from the existing P018
`factor_proof_slack` / fixed-even-prime-gap invariant in
`src/enterprise_math/prime_gap_slack.py`.

## 3. Reciprocal prime-gap shadow

Put

\[
x=k^2/q.
\]

Then the e=1 failure condition is exactly

\[
P^+(x)>x\left(1+\frac2k\right).
\]

So non-forced witnesses above \(C_4\), after excluding pure-cube forcing, are
the reciprocal pullback of forward relative prime gaps larger than \(2/k\).

This gives the sparse generation route

\[
\text{large cofactor gaps}
\to
\text{non-forced witnesses}.
\]

## 4. T-A25 — residual factors all become candidate coordinates

Assume a residual exists and the fourth-root core is forced.

Previous R005 results give \(\Omega(n)=3\). Write

\[
n=abc,\qquad a\le b\le c.
\]

Because a is non-forced, its pure cube cannot lie in the basin, so

\[
\boxed{
C_4<a\le\lfloor A^{1/3}\rfloor.
}
\]

Also \(a>C_4\) gives

\[
a^2>\sqrt U>k.
\]

Hence

\[
ab>k
\]

and therefore

\[
c\le U/(ab)<\sqrt U<k+1.
\]

Thus

\[
\boxed{a,b,c\le k.}
\]

All distinct prime factors of the residual are candidate non-forced
witnesses.

## 5. T-A26 — deterministic pair closure

Fix the two smallest residual factors a,b and put

\[
d=ab.
\]

The third factor must satisfy

\[
\frac{k^2}{d}<c\le\frac{k^2+2k}{d}.
\]

Since \(d>k\), this interval has width

\[
\frac{2k}{d}<2.
\]

For \(k\ge4\), every residual factor is odd, so there is at most one possible
prime c.

Define \(C_k(a,b)\) as the largest odd integer not exceeding

\[
\left\lfloor\frac U{ab}\right\rfloor.
\]

Then the square-basin witness language has no least safe basis iff there exist
non-forced primes a,b satisfying

\[
C_4<a\le\lfloor A^{1/3}\rfloor,\qquad
a\le b,\qquad
ab^2\le U,
\]

such that

\[
c=C_k(a,b)
\]

is another non-forced prime and

\[
A<abc\le U.
\]

So the third prime is reconstructed, not searched.

## 6. Exact executable cross-check

A consolidated verifier uses the existing independent
49-basin / 50-residual certificate family.

It checks:

- 19,794 candidate witness states above the fourth-root core;
- direct exclusive-collision forcedness equals the T-A24 formula every time;
- pair closure exactly reproduces direct exhaustive basin residual enumeration;
- all 50 residuals are reconstructed;
- pattern counts:
  - \(a=b<c\): 43;
  - \(a<b=c\): 2;
  - \(a<b<c\): 5.

Therefore the pair-closure description agrees with an independent direct
residual calculation on the entire declared certificate family.

## 7. T-A28/T-A29 — repeated sector becomes quotient/remainder closure

The repeated-prime sector contains 45/50 exact residual certificates.

For a possible repeated factor q, perform Euclidean division

\[
U=q^2t+s,\qquad0\le s<q^2.
\]

Define the odd quotient closure

\[
R_k(q)=
\begin{cases}
t,&t\text{ odd},\\
t-1,&t\text{ even},
\end{cases}
\]

and corrected remainder

\[
\rho_k(q)=U-q^2R_k(q).
\]

Then the only possible singleton prime factor is

\[
r=R_k(q),
\]

and basin membership is exactly

\[
\boxed{\rho_k(q)<2k}.
\]

Thus a repeated residual is determined by one free witness q:

\[
q
\to
R_k(q)
\to
\rho_k(q)
\to
\text{non-forced test for }q,R_k(q).
\]

No new arithmetic primitive is needed: quotient, remainder, parity, next-prime
observation and inequalities suffice.

In the current 45 repeated certificates all raw quotients happen to be odd.
That parity pattern is recorded as finite evidence only and is not promoted as
a theorem.

## 8. T-A27 — factor-pair parametrization

The same repeated residual can be viewed from factor space.

For distinct primes q,r with

\[
r\le q^2,
\]

define

\[
k=\lfloor\sqrt{q^2r}\rfloor.
\]

Then q and r are both candidate witnesses in basin k, and

\[
\boxed{
q^2r\text{ is residual}
\iff
q,r\text{ are both non-forced in basin }k.
}
\]

So k is not an independent search variable in the repeated sector.

## 9. Correction / negative result

An earlier research note observed that for repeated residual \(q^2r\),

\[
m=\lfloor k/q\rfloor
\]

satisfies

\[
m^2<r<(m+1)^2,
\]

and tentatively interpreted this as a cross-scale prime anchor.

The inequality is correct, but the interpretation is not substantive.

Indeed

\[
k=\lfloor q\sqrt r\rfloor
\]

implies identically

\[
\boxed{
\lfloor k/q\rfloor
=
\lfloor\sqrt r\rfloor.
}
\]

So “r lies between those consecutive squares” is just r's ordinary square
location written in different coordinates.

This observation is explicitly demoted:

- retain as algebraic identity/provenance;
- do not promote as a new prime-existence or collapse-recursion theorem;
- do not use it as Foundation evidence.

## 10. Squarefree-only negative boundary

The repeated sector is dominant in the current finite family, but it is not
complete.

There are no-least basins whose certified residuals are squarefree only,
including

\[
k=888,\qquad 790079=73\cdot79\cdot137.
\]

Therefore a repeated-only search is not a complete decision procedure for
no-least.

The full pair-closure theorem is required.

## 11. Prime Toolkit interpretation

The p=2 path is now:

\[
\text{next-prime field}
\to
\text{local gap defect}
\to
NF_k
\to
\text{pair closure}
\to
\text{residual hypergraph}
\to
\text{repair language}.
\]

Under the fourth-root-core condition, residual support has rank at most 3:

- repeated residual \(q^2r\): support edge \(\{q,r\}\);
- squarefree residual \(qrs\): support edge \(\{q,r,s\}\).

Hence the repair problem after the forced core is a rank-3 hitting-set
problem. If the squarefree sector is absent, it reduces to graph vertex cover.

## 12. Prior-art boundary

Campbell 2026 proves that every consecutive-square interval contains an
integer with at most three prime factors and explicitly uses maximal prime-gap
computations in the finite range.

Therefore R005 does not claim novelty for:

- three-factor almost primes between squares;
- using prime gaps after interval rescaling;
- quotient/remainder arithmetic;
- set-cover/hitting-set language.

The candidate R005 content is specifically the composition:

- forced/non-forced witness semantics;
- exact local forcedness classifier;
- residual-fiber restriction;
- deterministic pair closure;
- observation-language repair interpretation.

Novelty remains unverified.

## 13. Next frontier

The correct next target is the full non-forced pair geometry, not another
composite cutoff.

For fixed k:

1. generate \(NF_k\) from reciprocal cofactor prime gaps;
2. restrict the first coordinate to
   \[
   C_4<a\le A^{1/3};
   \]
3. close each admissible pair deterministically;
4. study the sparse 2-edge / 3-edge residual hypergraph.

The most interesting mathematical question is whether the squarefree
3-edge sector admits an additional structural reduction analogous to the
one-variable quotient closure of the repeated sector.
