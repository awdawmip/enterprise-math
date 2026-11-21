# R5 — Exact next coefficient-period precision for the frozen scalar cost observer

Date: 2026-11-22 (Asia/Shanghai). Scientific status: AUTHOR_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED. This result concerns the *frozen independent R5 cost observer* and makes no native-X6 or P000 claim.

## Theorems

Fix the 101 integer prices P={214,...,314} and the five failure supports

S0={214,215,216,217,218},
S1={214,216,217,218,219,220,221},
S2={215,216,217,218,219,220,221},
S3={223,...,290},
S4={296,...,312}.

For a threshold m>=1, count multiplicity vectors a_p>=0 of total price N satisfying at least one of the **original separate inequalities** sum_{p in S_i} a_p < m. Let M_m(O_m(N^a)) be the least coefficient period of the quasipolynomial expansion of that counting function up to error O_m(N^a).

**New universal bound, without any prior mathematical theorem:**

\[
\boxed{\forall m\ge1,\qquad M_m(O_m(N^2))\mid 26\,771\,144\,400.}
\]

**New exact m=1 root certificates, without any prior mathematical theorem:**

\[
\boxed{23\cdot25\mid M_1(O(N^2)).}
\]

Together with the previously established m=1, O(N^3) theorem (the prior author-side result M_1(O(N^3))=232792560), these yield the **conditional-on-inherited-theorem exact new value**

\[
\boxed{M_1(O(N^2))=26\,771\,144\,400
      =115 M_1(O(N^3)).}
\]

The inherited m=1 exact period appears at enterprise-math@ba976ca1d5ea32392e409b5dec08c1607140a610, and its all-threshold extension at @2c995f1106ecd67a5896a9d1aad257fbd485d116. These prior author proofs are NOT_REVIEWED. The new arithmetic and universal upper bound below stand independently.

## Proof of the universal upper bound

Let D(q)=product_{p=214}^{314}(1-q^p). For nonempty I⊆{0,...,4}, define U_I=union_{i in I} S_i. Let P_{I,m}(q) be the finite cost polynomial that sums over multiplicities on U_I under **all individual constraints** sum_{p in S_i} a_p<m for i in I. Then the exact generating-function numerator is

\[
R_m(q)=\sum_{\varnothing\ne I\subseteq\{0,\ldots,4\}}
(-1)^{|I|+1}P_{I,m}(q)\prod_{p\in U_I}(1-q^p),
\qquad F_m(q)=R_m(q)/D(q).
\]

At a primitive d-th root, the denominator zero order is
k(d)=floor(314/d)-floor(213/d). A pole of order at least four is needed to affect coefficients above O_m(N^2). Direct complete integer enumeration gives exactly

\[
D_4=\{d:k(d)\ge4\}=\{1,\ldots,28,31\}.
\]

Every S_i contains a multiple of 27 and a multiple of 31:

| Event | multiple of 27 | multiple of 31 |
|---|---:|---:|
| S0 | 216 | 217 |
| S1 | 216 | 217 |
| S2 | 216 | 217 |
| S3 | 243 | 248 |
| S4 | 297 | 310 |

Thus every nonempty union U_I includes a d-divisible price for d=27 and d=31. Every summand of R_m(q) vanishes at a primitive root of either order, for every m and for every genuinely coupled finite-load polynomial P_{I,m}. Since k(27)=k(31)=4, each corresponding F_m pole has order at most three, making those orders irrelevant modulo O_m(N^2).

Partial fractions at the remaining roots of unity give the **actual universal upper bound**

\[
M_m(O_m(N^2))\mid
\operatorname{lcm}(D_4\setminus\{27,31\})
=26\,771\,144\,400.
\]

The unfiltered lcm(D4)=2,489,716,429,200 is 93 times larger. This cancellation argument applies to all positive m without enumerating their constraints.

## Primitive-root lower certificates at m=1

When m=1, every selected event forces all multiplicities on that event's support to zero. Hence P_{I,1}(q)=1 and

\[
R_1(q)=\sum_{I\ne\varnothing}(-1)^{|I|+1}
\prod_{p\in U_I}(1-q^p).
\]

For d=23 or 25, the supports S3 and S4 both include a multiple of d. Their containing mask terms vanish at primitive d-th roots. Exactly the seven nonempty masks of S0,S1,S2 remain. Evaluate R1 in the integral cyclic ring Z[q]/(q^d-1), writing the unique degree-below-d residue as sum c_j q^j.

For d=23, Phi_23(q)=1+q+...+q^22. Such a residue vanishes at a primitive root iff all 23 cyclic coefficients are equal. The exact cyclic integer computation gives c_0=1 and c_1=6; their difference is -5, so R_1(zeta_23)≠0.

For d=25, Phi_25(q)=1+q^5+q^10+q^15+q^20. A degree-below-25 residue vanishes at a primitive root iff c_r=c_{r+5}=c_{r+10}=c_{r+15}=c_{r+20} for each r∈{0,...,4}. The exact result c_0=4, c_5=-3 has difference 7, so R_1(zeta_25)≠0.

Both denominator orders k(23)=k(25)=4. These exact nonzero numerator values give two fourth-order poles, forcing 23 and 25 to divide the period through the N^3 coefficient. The earlier O(N^3) period L3=232792560 divides any O(N^2) coefficient period. As lcm(L3,23,25)=26,771,144,400, the universal upper bound closes the exact m=1 value conditional on that previous theorem.

## Reproduction, exact evidence and provenance

Run Python 3 on VERIFY.py in the same directory; it uses only the standard library and writes CERTIFICATE.json. The program recomputes the full 31-mask cyclic vectors for d=23,25,27,31; independently recomputes both d=23,25 vectors with a *separately implemented sparse seven-mask representation*; checks the exact cyclotomic coefficient witnesses; checks all candidate orders, 27/31 zero vectors, and both lcm identities. The run completed locally with:

PASS 26771144400 m=1 exact period conditional on prior O3 theorem

The finite cyclotomic certificates are proof witnesses for the new prime-power factors; no numerical approximation or finite extrapolation to arbitrary m is needed. This run is author-side exact computation, not an independent formal Review. Parent frozen scientific pin: enterprise-math@2c995f1106ecd67a5896a9d1aad257fbd485d116. Earlier genuine-intersection correction: @75d986aa23b68a7ecf9b29dc1006f0e322b35a15. P000 and ACTIVE worldview are not modified.

## Next open research problem

Determine the **all-threshold exact period at O_m(N^2)** by calculating genuine three-load intersection numerator classes at primitive 23rd and 25th roots, proving where their fourth-order terms do or do not vanish. Independently review the inherited 232792560 theorem before promoting the conditional m=1 closure. Other error orders can be investigated with the same pole-order hierarchy and explicit residual-preserving event constraints.

Historical author provenance for the parent branch: Researcher EM-DIRECT-DB6902, Activity RA-CA24908A12714FE0C60497AA. This independent portable scientific extension neither borrows its old private session capability nor claims a formal CLAiM/RUN, independent Review or Activity mutation.
