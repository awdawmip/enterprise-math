# R537 | signed BRC Toeplitz minor m=60: integer-parameter sign classification

2026-11-04. Frozen scientific source R462@`18783e01e3646c72b7aab3b16d3f565e83e6446f`; continuation R536@`c8c6b0e44b5e6332bb74324b924b3419acde3f21`. Status: author-side exact computer-assisted conditional proof, Driver mathematical review pending.

## Exact object and premises

For integer k≥1 let r=2k+1 and C_k=binom(2k,k)/(k+1)>0. For 2≤t≤r define
H_k(t)=binom(r+t,2t)[x^r](1-x)(1+x)^(2t)(1+x²)^(r-t), and H_k(t)=0 otherwise.
Put D_m(k)=det(H_k(3+i-j)) for i,j=0,...,m-1; D_0=1.
Frozen signed BRC ballot–Catalan identity:
B_k(t)=binom(r+t,2t) Σ_{q=0}^{min(floor((t-1)/2),k)} binom(t-1,2q)4^q C_{k-q}, H_k(t)=B_k(t).
We use premise P: for fixed integer t, p_t(k)=H_k(t)/C_k agrees on all positive integers with a rational polynomial of degree≤2t. R536_POLYNOMIAL_LEMMA.md derives this P from H=B by exact factor cancellation; H=B is retained as frozen shared input.

## Result under P

For every integer k≥1:
* D_60(k)>0 if 1≤k≤8 or k≥23.
* D_60(k)<0 if 9≤k≤22.

There are no zeros on the positive-integer parameter domain. In r=2k+1 notation the negative interval is r=19,21,...,45; from r=47 onward D_60>0. With R536, D_59(k)>0>D_60(k) at k=9,10 and D_59(k)<0<D_60(k) for 23≤k≤50.

## Finite exact certificate proving infinite integer tail

Toeplitz–Hessenberg recursion with f_n=D_n/C_k^n and f_0=1:
f_n(k)=Σ_{a=1}^n(-1)^(a-1) p_(a+2)(k) p_2(k)^(a-1) f_(n-a)(k).
Thus deg f_n≤6n, so deg f_60≤360.
Choose G(k)=[k(k+1)(2k+1)(2k+3)]^60 (k+2), a positive polynomial of degree241.

For k=1,...,120 reduce f_60(k)/G(k) to a rational fraction, take L>0 as the lcm of reduced denominators, and use exact forward differences to define 120 integer coefficients δ_0,...,δ_119, S(k)=Σ_{j=0}^{119}δ_j binom(k-1,j). The complete integers L and δ are in R537_EVIDENCE.json.

A direct BigInt comparison validates
L D_60(k) = C_k^60 G(k) S(k)
at each k=1,...,361. Under P both divided sides are rational polynomials of degree≤360; equality at 361 distinct k establishes polynomial identity on the entire domain.

The certificate shows S(k)>0 for k=1,...,8 and S(k)<0 for k=9,...,22. At k=23 all 120 forward differences ε_j=Δ^j S(23) are strictly positive. Therefore for every integer u≥0,
S(23+u)=Σ_{j=0}^{119}ε_j binom(u,j)>0.
Since L,C_k,G(k)>0, this proves the sign classification.

## Actual checks and reproducibility

`node R537_VERIFY.js > R537_EVIDENCE.json`: R537_EXACT_JS_PASS; 361 exact polynomial identities; 20 original 60×60 Bareiss determinant checks; 1200 H/B checks on k=1..20, t=2..61; 22021 H/B checks on full interpolation grid k=1..361, t=2..62; 120 positive tail differences.

`python R537_INDEPENDENT.py > R537_INDEPENDENT_EVIDENCE.json`: R537_INDEPENDENT_PASS; independent Python math.comb and SymPy Berkowitz verify 12 original 60×60 determinants (including all two sign boundaries), 549 H/B checks and all 120 shifted forward differences. All arithmetic is exact integers. Python independent implementation is an author-side cross-check.

The branch identity and signed cancellation in H_k are retained in the original coefficient extraction and H/B grid; D is the declared auxiliary scalar observer. No changes to P000 or ACTIVE worldview. Native Result/CLAIM/Driver mathematical admission are separate tasks.

## Next research unit

Either s=3,m=61 (degree≤366, 122 Newton coefficients, 367-point identity certificate), or derive the fixed-k rational generating function denominator and its dominant-pole sign mechanisms at k=8,9,22,23. Also review frozen H=B from its original source to discharge the remaining global conditional dependency.
