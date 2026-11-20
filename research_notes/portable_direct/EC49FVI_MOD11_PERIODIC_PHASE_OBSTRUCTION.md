# EC49FVI — periodic mod-11 obstruction for an infinite lattice of rational likelihood phases

Date: 2026-11-21 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_FIELD_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.

## Scientific provenance and domain

Continues EC49FVH (Draft PR #2882, science commit 8fa086c597ead7bad7efaa0f03d2fcc13dae386e) under the frozen derived Bernoulli observer BRC16943 (fc0f038e7bfd12c886b4d37f900bfb770c0f61ab). This theorem concerns the derived two-Bernoulli rational observation model. P000, ACTIVE Heartbeat World and the original task science pin are not modified. Transferring it to the full compound minimax risk depends on the separate upstream FUQ/FUR endpoint-reduction claim.

For real \(0<x<1\), define

\[
u=\frac{4822040484}{8132285009},\quad
\gamma=\frac{141024}{1653649},\quad
L_a(x)=\frac{637-3x}{637},\quad L_b(x)=u(1+\gamma x),
\]
\[
a(x)=1-(1-x)L_a(x),\quad b(x)=1-(1-x)L_b(x),\quad
R=\frac{1-a}{1-b},\quad S=\frac{b(1-a)}{a(1-b)},\quad
t(x)=\frac{\log R}{\log S}\in(0,1).
\]

Let \(h,n\) be **positive integers**, and write \(k=h+n\). Define ten sets of exponent residues:

| \(h\bmod10\) | \(n\bmod10\) allowed |
|:--:|:--|
| 0 | 1, 3, 7, 9 |
| 1 | 2, 3, 4, 7, 8 |
| 2 | 1, 3, 5, 6 |
| 3 | 1, 2, 4, 6, 9 |
| 4 | 1, 2, 5, 7 |
| 5 | 2, 4, 6, 8 |
| 6 | 3, 5, 8, 9 |
| 7 | 1, 4, 6, 8, 9 |
| 8 | 4, 5, 7, 9 |
| 9 | 2, 3, 6, 7, 8 |

## Theorem — periodic exclusion of rational phases

If the residue pair \((h\bmod10,n\bmod10)\) belongs to the table and \(n+2h\not\equiv0\pmod{11}\), then, for **every** rational \(x\in(0,1)\),

\[
\boxed{t(x)\ne \frac{h}{h+n}.}
\]

These conditions select **4840 of 12100** exponent-pair residue classes modulo 110. This is a statement about exponent pairs, not the fraction of distinct rational phases or widths. An explicit infinite family of *distinct reduced* excluded phases is

\[
\boxed{t(x)\ne\frac{1}{3+110j}
\quad\text{for all rational }0<x<1,\ j\in\mathbb Z_{\ge0}.}
\]

## Proof

If \(t=h/(h+n)\), the identity \(R^{h+n}=S^h\) gives

\[
a^h(1-a)^n=b^h(1-b)^n.
\]

Because \(1-a=(1-x)L_a\) and \(1-b=(1-x)L_b\), and \(x\in(0,1)\), it follows that \(a^hL_a^n=b^hL_b^n\). Define

\[
G_{h,n}(X)=
\frac{a(X)^hL_a(X)^n-b(X)^hL_b(X)^n}
{L_a(X)-L_b(X)}\in\mathbb Q[X].
\]

This is an exact polynomial divided difference: replacing \(L_a\) and \(L_b\) by the same \(L\) also makes \(a=b=1-(1-X)L\). Its formal maximum degree is \(D=2h+n-1\).

Every coefficient denominator of \(u,\gamma,637\) is coprime to 11. Furthermore, \(L_a-L_b\equiv X-3\pmod{11}\) is monic, so \(G_{h,n}\) has coefficients in \(\mathbb Z_{(11)}[X]\). A rational zero \(x=m/d\) in lowest terms would give a zero of its degree-\(D\) homogenization on \(\mathbb P^1(\mathbb F_{11})\), including when \(11\mid d\).

Mod 11, the exact model becomes

\[
u=4,\quad\gamma=6,\quad
L_a=1+3X,\quad L_b=4+2X,\quad L_a-L_b=X-3,
\]
\[
a=1-(1-X)L_a,\qquad b=1-(1-X)L_b.
\]

For any finite field element \(z\ne3\), evaluate

\[
G_{h,n}(z)=
\frac{a(z)^hL_a(z)^n-b(z)^hL_b(z)^n}{z-3}\pmod{11}.
\]

At \(z=3\), the four values \(a,b,L_a,L_b\) all equal 10. Differentiating \(F(L)=[1-(1-z)L]^h L^n\) with respect to \(L\) computes the exact divided difference:

\[
\boxed{G_{h,n}(3)=10^{h+n-1}(n+2h)\pmod{11}.}
\]

At projective infinity, the coefficient at degree \(D\) is

\[
\boxed{G_{h,n}^*(1,0)=
\frac{3^{h+n}-2^{h+n}}{3-2}
=3^{h+n}-2^{h+n}\pmod{11}.}
\]

For all ten other finite field points and infinity, nonzero field powers depend only on the exponent modulo 10. Zero-base powers are uniformly zero because \(h,n\ge1\). Evaluating the 100 ordered pairs of exponent residues modulo 10 at these eleven points yields exactly the **44** pairs in the table. At the one remaining point \(z=3\), nonvanishing is equivalent to \(n+2h\not\equiv0\pmod{11}\). Each of the 44 patterns has \(11^2-11=110\) valid lifts to residues modulo 110; hence \(44\cdot110=4840\). Every such pair makes the projective homogenization zero-free over \(\mathbb F_{11}\), which excludes all rational roots. QED.

For a directly inspectable seed, at \((h,n)=(1,2)\),

\[
G_{1,2}(X)=-3X^3-5X^2+X-5\pmod{11}.
\]

At \(X=0,1,\ldots,10\), its values are
\(6,10,8,4,2,6,9,4,6,8,3\), and the leading coefficient at infinity is \(8\). All twelve values are nonzero. In the infinite lifted family \(h=1,n=2+110j\), the entire projective evaluation remains unchanged because 110 is divisible by both 10 (the exponent period) and 11 (the derivative coefficient period).

## Verification and scope

The accompanying executable Python 3 standard-library checker reconstructs the finite-field parameters from the exact rational constants; verifies the one singular point, the cubic seed, all 100 exponent patterns, and all 12100 exponent pairs modulo 110; then compares three exact rational widths with lifted exponent instances. It reports **ALL PASS**, and produces a 4840-row CSV of certified classes. This finite computation plus the above periodicity establishes an infinite-denominator theorem, not just a bounded experiment.

The complement of these residue classes remains open. The theorem has not received independent mathematical review or native Result admission. The compound minimax-risk application requires separate review of the predecessor FUQ/FUR reduction.

## Next scientific unit

Combine analogous good-prime local-period certificates at 17, 19, 31 and larger primes with the mod-11 lattice. Determine the union's coverage of coprime exponent pairs and search the surviving arithmetic progressions for exact rational-width rational-phase counterexamples. Keep scientific publication, Activity metadata, and formal CLAIM/Result/Review as distinct states.
