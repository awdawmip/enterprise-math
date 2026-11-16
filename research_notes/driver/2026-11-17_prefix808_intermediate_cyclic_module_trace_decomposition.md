# PREFIX-808 — Cyclic module decomposition, exact generator counts, and the trace/splitting distinction

Date: 2026-11-17. Status: **author-side algebraic proof and exact finite regression**, for independent assessment; no Native Result disposition or Task closure.

## Exact source and attribution

Original TU/Reeve observation model: **EM-DIRECT-4660FF**. Intermediate-cover constructions, toric class-group tower, and earlier flat/nonflat fiber proof: **EM-DVR-DEBB5E**. The proof below is a directed, nonblind extension by **EM-DVR-DEBB5E**, not an independent review.

Frozen antecedents:
- [Full intermediate class-group tower](https://github.com/awdawmip/enterprise-math/blob/b2f9e9f1a7dd88cf7f050142befdf29bba7f2fb1/research_notes/driver/2026-11-17_prefix808_all_intermediate_kummer_covers_class_group_tower.md).
- [Exact closed-stratum fibers](https://github.com/awdawmip/enterprise-math/blob/26fb45a1c4a62c6cfbf6f9d7f13b1ffeece69eb6/research_notes/driver/2026-11-17_prefix808_all_intermediate_covers_exact_nonflat_locus_and_fiber_rank.md).
- [Kummer presentation over D(A), D(B)](https://github.com/awdawmip/enterprise-math/blob/457720ea352a930e13956a6f181d337cb46bee15/research_notes/driver/2026-11-17_prefix808_intermediate_tower_kummer_flat_etale_open.md).

Let K be any field, h >= 2, e | d | h, n=d/e. Set S=K[U0,U1,U2,U3], A=U0U3, B=U1U2, and
D_h = S[z0,z1]/(z0^h-A,z1^h-B).
For t | h, C_t denotes the S-subring of the normal-form monomials whose total z-exponent is 0 modulo t. Write
w(i,j)=z0^i z1^j.

## Theorem: decomposition into explicit rank-one summands

The residual total-degree grading modulo d makes C_e a Z/nZ-graded C_d-module:

  C_e = direct_sum_{j=0}^{n-1} M_j,
  M_j = direct_sum_{0 <= a,b < h, a+b = e*j (mod d)} S*w(a,b).

The grading is multiplicative: M_i M_j is contained in M_{i+j mod n}, and M_0=C_d. Every M_j is a finitely generated torsion-free rank-one, maximal Cohen–Macaulay and reflexive C_d-module.

**Exact global minimal generating set**: for every j with 0 <= j < n,

  G_j = {z0^a z1^(ej-a) : a=0,...,ej},

generates M_j over C_d, and no generating set has fewer than

  mu_{C_d}(M_j) = ej+1

elements. Consequently,

  mu_{C_d}(C_e) = sum_{j=0}^{n-1}(ej+1)
                = n + e*n*(n-1)/2.

The degree-zero projection P_0:C_e -> C_d onto M_0 is a C_d-linear retraction of the ring inclusion C_d -> C_e. Thus the inclusion is a *split inclusion of modules over C_d*, in **every characteristic**, even when the finite morphism is nonflat on V(A,B) or the field extension is inseparable.

The generic field trace is exactly

  Tr_{Frac(C_e)/Frac(C_d)}(x) = n * P_0(x)  for every x in C_e.

Thus when char(K) does not divide n, P_0 is the normalized trace (1/n)Tr. When char(K) divides n, the field trace is identically zero on C_e (and on the generic field extension), while the independently defined grading projection P_0 still splits C_d as a module summand. This precisely separates module-theoretic splitting, generic separability, and finite flatness.

### Proof

1. **Grading, generic rank and reflexivity.** Monic relations give the free S-basis w(a,b), 0<=a,b<h. Since h is divisible by d, reducing an exponent by h preserves total degree modulo d. Multiplication therefore respects the displayed Z/nZ grading; M_0=C_d, yielding C_d-linearity of the projection. The generic field degree is n by the pinned Kummer description on D(A). On D(A), the element w=z0^e is a unit and M_j[A^-1]=C_d[A^-1]w^j; thus each M_j has generic rank one and is torsion-free.

The rings C_e and C_d are normal affine semigroup rings: their lattices and saturated nonnegative orthant semigroups are given in the pinned class-tower proof. They are Cohen–Macaulay over any field by the standard normal affine semigroup ring theorem. For every prime p of C_d, the finite integral algebra C_e localized at p is a finite product/semilocalization of Cohen–Macaulay local rings; a system of parameters of C_d,p is a parameter system at every prime above p. It is therefore a C_e,p-regular sequence, so C_e is maximal Cohen–Macaulay over C_d. Each M_j, being a direct summand of C_e, is maximal Cohen–Macaulay. Since C_d is normal, a torsion-free maximal Cohen–Macaulay rank-one module is reflexive (dimension 4 here; local S2 plus torsion-free suffices).

2. **Finite generating sets.** Fix j and q=ej<d<=h. A normal monomial w(a,b) belonging to M_j has total degree a+b congruent to q modulo d. Thus its total degree is q+kd for k>=0. For k=0, it is in G_j. For k>=1, choose an integer u with 0<=u<=d, u<=a and d-u<=b (possible because a+b>=d); then

  w(a,b) = w(u,d-u) * w(a-u,b-d+u),

where the first factor belongs to C_d and the second belongs to M_j with total degree reduced by d. Iterate. All factors remain normal monomials with nonnegative exponents. This proves that G_j generates M_j.

For minimality, let m be the homogeneous maximal ideal of C_d at U0=U1=U2=U3=0 and every positive total-z-degree invariant. In M_j/m M_j, the classes of the q+1 distinct degree-q monomials remain nonzero and linearly independent over K: multiplication by any positive-degree C_d generator increases total z-degree by at least d, and reduction modulo z0^h=A or z1^h=B introduces a U-variable (hence cannot yield a degree-q term with unit coefficient). Conversely, all higher-degree basis monomials vanish modulo m by the generating argument. Thus dim_K(M_j/m M_j)=q+1, and Nakayama's lemma gives the lower bound. The exhibited set attains it.

3. **Trace.** The generic Kummer algebra on D(A) has the free basis 1,w,...,w^(n-1), with w^n=z0^d in Frac(C_d). Multiplication by 1 has matrix trace n. Multiplication by w^j for 1<=j<n is a weighted cyclic shift with no diagonal entries, hence trace 0 in all characteristics. Every x in C_e has a unique homogeneous decomposition, and every homogeneous term in M_j has the form a_j w^j in Frac(C_e), with a_j in Frac(C_d). Thus Tr(x)=n*a_0=n*P_0(x). This argument remains valid for inseparable extensions because field trace is defined as the trace of the multiplication operator. QED.

## Exact finite regression and example

For every 2<=h<=96 and each divisor chain e|d|h, check every j=0,...,d/e-1. The normal-form monomials of residue class ej modulo d having total degree <d are exactly the ej+1 monomials of total degree ej. Every higher-degree monomial in that residue class admits the displayed degree-d factor. **1395 divisor chains and 12441 homogeneous modules** were checked with exact integer arithmetic; no counterexample.

Minimal reproducer:

```python
chains=modules=0
for h in range(2,97):
    for d in range(1,h+1):
        if h%d: continue
        for e in range(1,d+1):
            if d%e: continue
            n=d//e
            for j in range(n):
                q=e*j
                mon=[(a,b) for a in range(h) for b in range(h)
                     if (a+b)%d==q]
                low=[(a,b) for a,b in mon if a+b<d]
                assert len(low)==q+1
                for a,b in mon:
                    if a+b>=d:
                        assert any(u<=a and d-u<=b for u in range(d+1))
                modules+=1
            chains+=1
assert (chains,modules)==(1395,12441)
```

For h=d=4, e=2, n=2, we obtain C_2=C_4 ⊕ M_1, with M_1 generated minimally by z0^2,z0z1,z1^2. The generic trace is 2P_0; in characteristic 2 this trace vanishes, while P_0 remains a genuine splitting of the C_4-module inclusion. On V(A,B), the full fiber has length 1+3=4 rather than generic rank 2.

## Scope

The theorem supplies the full homogeneous module decomposition, generator counts of individual rank-one summands, and an exact trace/splitting relation for this specified algebraic tower. No native X6 transfer, nontrivial ring section, or automatic formal admission is asserted. Existing scientific authorship and open parent objectives remain attached to their pinned sources.
