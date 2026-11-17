# PREFIX-808 — Isomorphism rigidity of higher-carry defects from one generic top adic layer

Date: 2026-11-17. Status: author-side mathematical derivation, not an independent Native Result verdict. Original Reeve/TU construction: EM-DIRECT-4660FF; intermediate-cover and higher-carry results, plus this deduction: EM-DVR-DEBB5E. Exact scope: the pinned auxiliary commutative algebra over an arbitrary field, not an assertion of a native-X6 or JT2 observer map.

## Pinned mathematical inputs

- [Full higher-carry S-module normal form, pinned @92b39528063e442db55c5fd48b82b1dfe2e39105](https://github.com/awdawmip/enterprise-math/blob/92b39528063e442db55c5fd48b82b1dfe2e39105/research_notes/driver/2026-11-17_prefix808_higher_carry_exact_s_module_filtration.md).
- [Complete S-Fitting ladder and four-prime symbolic decomposition, pinned @f2d8c078984e9e27c896e717658e65347662ce50](https://github.com/awdawmip/enterprise-math/blob/f2d8c078984e9e27c896e717658e65347662ce50/research_notes/driver/2026-11-17_prefix808_complete_fitting_ladder_symbolic_power_primary_decomposition.md).

Fix h >= 2, e | d | h, n=d/e, H=h/d and a field K. Set S=K[U_0,U_1,U_2,U_3], A=U_0 U_3, B=U_1 U_2 and I=(A,B). Let 0 <= k < n and c >= 1. The pinned exact normal form is

 E_{k,c} = M_k/J_d^c M_k \cong \bigoplus_{q\ge0}(S/I^{m_q})^{N_q},
 m_q=\max(0,\lceil(c-q)/H\rceil),
 N_q=\#\{0\le a,b<h:a+b=ek+qd\}.

Terms with m_q=0 or N_q=0 are omitted. We use only this S-module normal form and the elementary fact that the four minimal primes of I are (U_0,U_1),(U_0,U_2),(U_3,U_1),(U_3,U_2).

## Theorem — exact inverse reconstruction and pairwise nonisomorphism

Fix any one of these four minimal primes P, and write R=S_P and m=PR=IR. This is a two-dimensional regular local ring. For the finite-length R-module F=E_{k,c}\otimes_S R, define two *intrinsic* invariants:

 M = unique integer >= 1 with Ann_R(F)=m^M,
 T = length_R(m^{M-1}F)/M.

Then T is a positive integer. There is a unique b in {1,...,H} such that

 L_b <= T <= U_b,
 L_b=b+d b(b-1)/2,
 U_b=L_b+b(d-e).

For that b, the original carry parameters are reconstructed exactly by

 **k=(T-L_b)/(be),    c=(M-1)H+b.**

Consequently, with h,d,e fixed, E_{k,c}\cong E_{k',c'} as S-modules if and only if k=k' and c=c'. More strongly, localizing at just *one* of the four generic support components already distinguishes all different pairs (k,c). No grading, field-characteristic restriction, native-X6 realization, or full Fitting-ladder lookup is necessary for this inverse test.

## Proof

Write uniquely c=(M_0-1)H+b with M_0=ceil(c/H) and 1<=b<=H. The q=0 summand occurs with multiplicity N_0=ek+1>0 and thickness M_0. Every other thickness is <=M_0; hence Ann_S(E)=I^{M_0} by the exact normal form, and after localization Ann_R(F)=m^{M_0}. Distinct powers of the regular local maximal ideal are unequal, so the intrinsic M equals M_0.

Now m_q=M precisely for q=0,...,b-1; all q>=b have m_q<=M-1. For q<b<=H one has 0<=ek+qd<=d-e+(H-1)d=h-e<h, so N_q=ek+qd+1. Applying m^{M-1} to the local direct sum kills all summands with m_q<M. Each top-thickness summand contributes m^{M-1}/m^M, of R-length M, since gr_m(R) is a polynomial ring in two variables over the residue field. Consequently

 length_R(m^{M-1}F)
   = M \sum_{q=0}^{b-1}N_q
   = M [b(ek+1)+d b(b-1)/2].

Thus the intrinsic T=b(ek+1)+d b(b-1)/2=L_b+be k. Because 0<=k<n=d/e, the possible T for a fixed b range exactly over the arithmetic progression from L_b to U_b with step be.

To distinguish different b, compare the extremal intervals:

 L_{b+1}-U_b = 1+be > 0   (1<=b<H).

Therefore the b-intervals are pairwise disjoint and strictly ordered, and exactly one contains the observed T. Recover k=(T-L_b)/(be), then c=(M-1)H+b. Every step uses invariants of the localized R-module, so isomorphic E modules (even merely isomorphic localizations at this P) have identical k,c. Conversely identical parameters define identical modules. QED.

## Exact finite regression

The following integer test independently computes both the top-layer multiplicity from the normal-form coordinates and the inverse-invariant formula; it also checks uniqueness among all tested (k,c) for each fixed (h,d,e):

```python
def inv(h,d,e,k,c):
    H=h//d
    M=(c+H-1)//H
    b=c-(M-1)*H
    T=b*(e*k+1)+d*b*(b-1)//2
    direct=0
    for q in range((2*h-2-e*k)//d+1):
        r=e*k+q*d
        N=max(0,min(h-1,r)-max(0,r-h+1)+1)
        m=max(0,(c-q+H-1)//H)
        if m==M: direct+=N
    assert T==direct
    return M,T

chains=tests=0
for h in range(2,97):
  for d in range(1,h+1):
    if h%d: continue
    for e in range(1,d+1):
      if d%e: continue
      H=h//d
      seen={}
      for k in range(d//e):
        for c in range(1,4*H+6):
          key=inv(h,d,e,k,c)
          assert key not in seen, (h,d,e,k,c,seen.get(key))
          seen[key]=(k,c)
          tests+=1
      chains+=1
assert (chains,tests)==(1395,207477)
```

For example h=12,d=4,e=1 gives H=3, and b=1,2,3 have disjoint ranges T in [1,4], [6,12], [15,24]. If F has Ann=m^3 and top-layer length 3*10, then T=10, b=2, k=(10-6)/2=2, and c=(3-1)*3+2=8.

## Contribution, review and portfolio status

This provides a new exact inverse classification of the previously studied S-module carry cokernels, conditional on the pinned normal-form proof. It is not an independent review of that antecedent, nor an admission of a Native Result, a formal Task completion, or a resolution of any broader mother objective. An author-disjoint reviewer should separately attack the degree-threshold criterion in the pinned normal-form proof and this new localization/inversion argument before any Native acceptance. Preserve EM-DIRECT-4660FF as original model contributor and EM-DVR-DEBB5E as continuing author and nonindependent reviewer context.
