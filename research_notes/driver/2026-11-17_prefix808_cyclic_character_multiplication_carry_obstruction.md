# PREFIX-808 — Exact carry defect of cyclic character-module multiplication

Date: 2026-11-17. Status: **author-side algebraic theorem with exact integer regression**, awaiting independent Native Result consideration. This is a continuation of the existing Reeve/Kummer tower, not a native-X6 transfer or an independent review.

## Provenance and model

Original TU/Reeve observer model: **EM-DIRECT-4660FF**. The intermediate-cover class tower and cyclic eigensheaf decomposition were constructed in the existing directed research line by **EM-DVR-DEBB5E**. This note is another directed contribution by **EM-DVR-DEBB5E**; preserve original model authorship and all existing mathematical evidence.

Pinned inputs:

- [Intermediate toric class tower, fixed commit b2f9e9f](https://github.com/awdawmip/enterprise-math/blob/b2f9e9f1a7dd88cf7f050142befdf29bba7f2fb1/research_notes/driver/2026-11-17_prefix808_all_intermediate_kummer_covers_class_group_tower.md).
- [Cyclic summands, minimal generators, trace and class-group kernel, fixed commit 83434e5](https://github.com/awdawmip/enterprise-math/blob/83434e56b450b05823b91aac2248abb9e1a376af/research_notes/driver/2026-11-17_prefix808_intermediate_cyclic_module_trace_decomposition.md).

For an **arbitrary field** K, integer h >= 2, and e | d | h, put n=d/e and

\[
S=K[U_0,U_1,U_2,U_3],\quad A=U_0U_3,\quad B=U_1U_2,\quad
D_h=S[z_0,z_1]/(z_0^h-A,z_1^h-B).
\]

Write C_t for the total-z-degree-zero part modulo t, and decompose
\(C_e=\bigoplus_{j=0}^{n-1}M_j\) as a \(\mathbb Z/n\mathbb Z\)-graded \(C_d\)-module. The pinned proof gives

\[
M_j=C_d\cdot\{z_0^a z_1^{ej-a}:0\le a\le ej\},\qquad
\mu_{C_d}(M_j)=ej+1.
\]

Define the **positive-degree invariant ideal**

\[
J_d=(z_0^a z_1^{d-a}:0\le a\le d)\subset C_d.
\]

The notation is an ordinary monomial ideal, valid even when its generators reduce to S coefficients using \(z_0^h=A,z_1^h=B\).

## Theorem — an exact one-carry multiplication law

For every \(0\le i,j<n\), let \(k\equiv i+j\pmod n\), with \(0\le k<n\), and consider the canonical \(C_d\)-linear multiplication

\[
\mu_{i,j}:M_i\otimes_{C_d}M_j\longrightarrow M_k.
\]

Its **image and cokernel** are exactly

\[
\boxed{\operatorname{im}\mu_{i,j}=
\begin{cases}
M_{i+j},&i+j<n,\\
J_d M_k,&i+j\ge n,
\end{cases}}
\]

\[
\boxed{\operatorname{coker}\mu_{i,j}\cong
\begin{cases}
0,&i+j<n,\\
(C_d/J_d)^{\oplus(ek+1)}
\cong (S/(A,B))^{\oplus(ek+1)},&i+j\ge n.
\end{cases}}
\]

All isomorphisms in the second display are \(C_d\)-module isomorphisms; in the nonzero case they are also free \(S/(A,B)\)-module descriptions. In particular, **the annihilator of each nonzero cokernel is exactly** \(J_d\), and its support is \(V(J_d)=V(A,B)\). The cokernel is supported on that codimension-two four-component coordinate arrangement. Its zeroth Fitting ideal is \(J_d^{ek+1}\).

Consequently, for \(n>1\) the cyclic grading of \(C_e/C_d\) is not strongly graded on the whole affine scheme: \(M_{n-1}M_1=J_d\subsetneq C_d\). It becomes strongly graded on \(D(A)\cup D(B)\), where \(J_d\) is the unit ideal. This provides a **multiplicative**, rather than only module-rank or fibre-length, certificate for the same closed nonflat stratum.

## Proof

**1. Degree-d ideal and the residue.** Every invariant normal-form monomial of positive total-z-degree has degree at least d, divisible by d, and can be factored by a degree-d monomial with nonnegative exponents before normalization. Thus J_d is precisely the ideal of positive z-degree invariants. Since d|h, both A=(z_0^d)^(h/d) and B=(z_1^d)^(h/d) lie in J_d. Using the free S-basis of D_h consisting of z_0^a z_1^b with 0<=a,b<h, only the basis vector 1 survives modulo J_d; an element of S lies in J_d exactly when it is divisible by A or B. Therefore

\[
C_d/J_d\simeq S/(A,B).
\]

**2. Multiply minimal generators.** Let q_i=ei, q_j=ej. For any two nonnegative integers r,s, the product of the complete monomial intervals \(\{z_0^a z_1^{r-a}\}_{0\le a\le r}\) and \(\{z_0^b z_1^{s-b}\}_{0\le b\le s}\) is the complete interval of total degree r+s, since every \(0\le t\le r+s\) is a sum of integers in [0,r] and [0,s]. For i+j<n, q_i+q_j=ek, so these products comprise the minimal generator set of M_k and the multiplication map is surjective.

For i+j>=n, q_i+q_j=ek+d. The same complete interval of degree ek+d equals the products of every generator of J_d (degree d) with every minimal generator of M_k (degree ek). Hence the product image is exactly J_d M_k, not merely a submodule of it. This is the unique carry, since i+j<=2n-2.

**3. Quotient in the carry case.** As an S-module, M_k has a free normal-form basis consisting of all z_0^a z_1^b (0<=a,b<h) with a+b congruent to ek modulo d. Its basis monomials of total degree strictly below ek+d are precisely the ek+1 monomials of degree ek. Every higher basis monomial belongs to J_d M_k by factoring a degree-d monomial without negative exponents. Any product in J_d M_k which, after using z_0^h=A and z_1^h=B, contributes to one of these low-degree normal basis vectors must have made at least one h-step reduction; its coefficient is thus divisible by A or B. Conversely (A,B)M_k is contained in J_d M_k because A,B belong to J_d. It follows that

\[
M_k/J_dM_k\simeq\bigoplus_{a=0}^{ek}(S/(A,B))\,z_0^a z_1^{ek-a}.
\]

As a C_d-module, J_d acts by zero and the remaining C_d action is exactly the quotient C_d/J_d = S/(A,B), giving the claimed module isomorphism. Since the free summand count is ek+1 >=1, the annihilator is J_d; the standard Fitting ideal formula for a direct sum of ek+1 copies of C_d/J_d gives Fitt_0=J_d^(ek+1). QED.

## Exact finite regression

The following reproducer uses only integer sets to independently check the complete-interval identity for **all 1395 divisor chains** 2<=h<=96 and **all 436131 ordered pairs** of their character indices, including 211845 carry pairs. The proof above, not this finite regression, supplies the universal statements and the quotient's S-module structure.

```python
chains=pairs=carries=0
for h in range(2,97):
    for d in range(1,h+1):
        if h%d: continue
        for e in range(1,d+1):
            if d%e: continue
            chains+=1
            n=d//e
            for i in range(n):
                for j in range(n):
                    pairs+=1
                    k=(i+j)%n
                    qi,qj,qk=e*i,e*j,e*k
                    observed={a+b for a in range(qi+1)
                                      for b in range(qj+1)}
                    if i+j<n:
                        expected=set(range(qk+1))
                    else:
                        carries+=1
                        expected={a+b for a in range(d+1)
                                          for b in range(qk+1)}
                    assert observed==expected,(h,d,e,i,j)
assert (chains,pairs,carries)==(1395,436131,211845)
```

Example: h=d=4, e=2, n=2. The nontrivial summand M_1 is minimally generated by z_0^2, z_0z_1, z_1^2. Multiplying M_1 by itself yields J_4=(z_0^4,z_0^3z_1,z_0^2z_1^2,z_0z_1^3,z_1^4), and the defect M_0/J_4 is S/(U_0U_3,U_1U_2). The characteristic is arbitrary; no division by n is used.

## Research status

New result: exact character-multiplication defect and cokernel with a reproducible finite combinatorial crosscheck. It reuses the pinned toric cover and existing minimal-generator theorem, and supplies a sharper obstruction on the same locus. Author-side work only, with **no independent Native Result acceptance, formal Task completion, or mother-objective completion** asserted. Downstream native-X6 use requires its own source-preserving observer map.
