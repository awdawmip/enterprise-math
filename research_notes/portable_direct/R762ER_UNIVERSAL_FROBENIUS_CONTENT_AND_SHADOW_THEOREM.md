# R762ER — Universal 3-adic Frobenius lift for all three-power BRC terminal moduli q >= 9

Date: 2026-11-18. Model: frozen six **named positive** BRC branches, with terminal observer in the complete three-coordinate group algebra. Original task: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Historical researcher provenance: EM-X6-3050F6. This is a new author-side proof dependent on the exact q=9 base theorem R762EQ (PR #2731, immutable head de0801418e293ceb056b9c5ca40a113379742588). Independent mathematical review: NOT_REVIEWED. No new Source CLAIM, PROGRESS, Result, Review or native-event authority is asserted.

## Theorem (all q = 3^a, a >= 2; all n >= 0)

Let G_q=(Z/qZ)^3 and R_q=Z[G_q], with variables X,Y,Z denoting the three retained terminal coordinates. The complete six-branch BRC operator is

\[
P_q=1+X+Z+XY+YZ+XYZ .
\]

Let c_q(n)>0 be the gcd of **all** q^3 integer coefficients of P_q^n. Write d=q/3 and

\[
f_q(n)=\max(0,\lfloor n/d\rfloor-2),\qquad
S_q(n)=3^{-f_q(n)}P_q^n\bmod3 \in {\bf F}_3[G_q].
\]

Then, for **every** a>=2 and n>=0,

\[
\boxed{c_q(n)=3^{f_q(n)}} \tag{1}
\]

and S_q(n) is a well-defined nonzero vector. For q>=9, set h=q/9=3^{a-2}; uniquely write n=hm+r, 0<=r<h. Let
\(\iota_h:{\bf F}_3[G_9]\hookrightarrow{\bf F}_3[G_q]\) send each of X,Y,Z to its h-th power. The **coefficientwise** factorization is

\[
\boxed{S_q(hm+r)=\iota_h(S_9(m))\, (P_q\bmod3)^r.}\tag{2}
\]

This is an explicit, provenance-aware terminal-coefficient observer identity, not a native signed Cell/Link/Port event licence.

### Consequences

1. R762EQ establishes S_9(m+18)=S_9(m) for every m>=9; hence for every a>=2,

   \[
   \boxed{S_q(n+2q)=S_q(n)\quad(n\ge q).}\tag{3}
   \]

2. Let N_1(r), N_2(r) be counts of digits 1,2 in the base-3 expansion of r. Denote the number of nonzero terminal coefficients of the normalized shadow by supp. Since r<h, every monomial in P_q^r has each coordinate exponent <h, so no two distinct residue triples collide across the H=(hZ/qZ)^3 cosets. The characteristic-3 digit identity, with supp(P mod3)=6 and supp(P^2 mod3)=18, gives

   \[
   \boxed{\operatorname{supp}S_q(hm+r)=\operatorname{supp}S_9(m)\,6^{N_1(r)}18^{N_2(r)}.}\tag{4}
   \]

   This specifies the all-horizon support from the q=9 base shadows and the low base-3 digits. For m>=9, only the 18 q=9 period vectors are needed.

3. The 2q vectors S_q(q),...,S_q(3q-1) have F_3 rank

   \[
   \boxed{\dim_{\mathbf F_3}\operatorname{span}\{S_q(q),\ldots,S_q(3q-1)\}=17h=17\cdot3^{a-2}.}\tag{5}
   \]

   Thus the 2q-vector displayed period has nullity exactly h. The base rank 17 is the exact R762EQ q=9 finite-rank certificate, independently rechecked by the companion script.

These results are exact for every time horizon n; the only fixed-input numerical computation needed for this theorem is the independently reproducible q=9 base certificate in R762EQ. The new lift is symbolic and uniform in a and n.

## Proof: 3-adic Frobenius comparison lemma

Let q=3^a with a>=2, d=q/3>=3, and let Q=3q. Define the integral embedding
\(\iota:R_q\rightarrow R_Q\) by X,Y,Z -> X^3,Y^3,Z^3. It sends the six individually named branch monomials to their cubes. The integer multinomial theorem gives

\[
P_Q^3=\iota(P_q)+3D,\qquad D\in R_Q . \tag{6}
\]

Assume for the induction step that P_q^u is coefficientwise divisible by 3^{f_q(u)} for every u>=0. For any m>=0 and 1<=j<=m, the binomial expansion term in
\((\iota(P_q)+3D)^m\) has 3-adic coefficient divisibility at least

\[
j+v_3\binom mj+f_q(m-j). \tag{7}
\]

We claim this is >= f_q(m)+1. The step function f_q obeys
\(f_q(m)-f_q(m-j)\le\lceil j/d\rceil\).
For j>=2 and d>=3, \(\lceil j/d\rceil\le j-1\), so the claim follows. For j=1, if f_q(m)=f_q(m-1), its single 3 factor suffices. If the difference equals 1, then m is a multiple of d; as d is a positive multiple of 3, \(v_3(m)\ge1\), so the binomial factor supplies the additional 3. This also covers m near the truncation where f is zero.

Therefore

\[
\boxed{P_Q^{3m}\equiv \iota(P_q^m)\pmod{3^{f_q(m)+1}}}\quad(m\ge0).\tag{8}
\]

Both sides are divisible by 3^{f_q(m)}. Multiplication by P_Q^r, r=0,1,2, yields after exact division and reduction modulo3,

\[
3^{-f_q(m)} P_Q^{3m+r}\bmod3
=\iota(3^{-f_q(m)}P_q^m\bmod3)\,P_Q^r\bmod3. \tag{9}
\]

Because floor((3m+r)/q)=floor(m/d), \(f_Q(3m+r)=f_q(m)\), so (9) is exactly the one-level version of (2).

The subgroup H=(3Z/QZ)^3 decomposes G_Q into 27 disjoint residue cosets. For r=0,1,2, the H-coset with residue (0,0,0) in P_Q^r has coefficient exactly 1: none of the nonidentity six-branch paths of length <=2 returns every coordinate to 0 modulo3. Hence the H-coset component of the right side of (9) is precisely \(\iota(S_q(m))\), which is nonzero whenever S_q(m) is nonzero. This establishes **sharp** divisibility at q'=Q, not merely a lower bound.

The base case q=9 is R762EQ: c_9(n)=3^{f_9(n)} for all n>=0. By induction (9), all q=3^a>=9 have coefficientwise 3-content precisely f_q(n). The augmentation of P_q^n is 6^n, so c_q(n) divides 6^n; only primes 2 and 3 can occur. For odd q>=3 and n>=1, in characteristic 2 choose a nontrivial qth root z and evaluate X=Y=1, Z=z. The image of P is 1+z, nonzero, so P^n cannot have all coefficients even. (For n=0 the identity coefficient is 1.) Thus 2 does not divide c_q(n), proving (1).

## Proof: factorization, support and period

Iterate (9) from q=9 through q=3^a. In characteristic 3, \(P_q^{3^j}=\sum_{b\in\text{six named branches}}b^{3^j}\), by Frobenius. Reassembling the successive low base-3 digits of r gives (2). The exponent f_q(hm+r)=f_9(m) follows directly from q=9h and d=3h.

For support, group coefficients by residue classes modulo h in each coordinate. An individual monomial of P_q^r has three nonnegative coordinate exponents <=r<h. Therefore no two *distinct* monomials of its reduction modulo3 lie in the same H-coset. Multiplication by \(\iota_h(S_9(m))\) produces disjoint copies of that nonzero vector for every nonzero mod3 monomial of P_q^r. Applying characteristic-3 Lucas factorization to r's base-3 digits, supp(P_q^r mod3)=6^{N_1(r)}18^{N_2(r)}: P^2 has 18 nonzero coefficient monomials, and digit positions do not overlap. This proves (4) as well as nonvanishing. Apply the q=9 period to (2) to obtain (3).

## Proof: exact rank and the lossless residue splitting

For fixed r in 0,...,h-1, multiplication by P_q^r is injective on \(\iota_h({\bf F}_3[G_9])\), since the H-coset (0,0,0) of P_q^r has coefficient 1 (again r<h), so its H-coset component recovers the original input. In fact the h maps for different r are **jointly independent**. Suppose
\(\sum_{r=0}^{h-1}\iota_h(u_r)P_q^r=0\).
Project onto the H-cosets whose residues are (s,0,0) for s=0,...,h-1. Since all branch steps have nonnegative coordinates, r<h prevents Y,Z from wrapping their residues to zero unless both total Y and Z exponents are zero. This restricts these paths to the 1 and X branches, yielding the triangular equations

\[
\sum_{r=s}^{h-1}\binom{r}{s}u_r=0
\quad(s=0,\ldots,h-1)
\]

in the coefficient ring F_3[H]. Each diagonal binomial coefficient is 1. Descending induction from s=h-1 gives all u_r=0. Therefore these h images form a direct sum. Over one 2q-period, m runs through q=9 base indices m=9,...,26 and r runs through 0,...,h-1, so the rank is h times the rank of the 18 q=9 base vectors, namely 17h. This proves (5).

## Exact author-side checks and reproducibility

Companions: R762ER_VERIFY.py and R762ER_EVIDENCE.json. The standalone standard-library Python implementation runs the **six named positive BRC shifts**, with all arithmetic done exactly modulo powers of 3: q=9, n=0..65, modulus 3^20; q=27, n=0..300, modulus 3^34. Each modulus exceeds the largest predicted content exponent by at least one; 367 full mass and sharp-content checks pass. All 195 q=27 shadows at n=0..194 equal their q=9 Frobenius-lift predictions. All 220 period comparisons S_27(n+54)=S_27(n) for n=27..246 pass. The q=9 18-vector rank is 17, with reproducible pivots and SHA-256. The q=27 period-base rank is 51 by the proved direct-sum argument; a separate author NumPy finite calculation also found 51. The q=27 base 54-vector SHA-256 is b418807a353d6f56a0cc50c1d270b283a2659abcdf5989500cc4137a5b77f889. No floating point, phase cancellation, trigonometric or non-BRC update is used.

Evidence classification: all-q theorem = symbolic induction conditional on the R762EQ author-proved q9 base, with exact finite checks; independent review NOT_REVIEWED, formal checker NOT_PERFORMED. The operator is the positive full three-coordinate terminal BRC projection. Its relation to the locked six-dimensional P000 Heartbeat World is an observer-level model, and no claim about actual signed TRIADIC_CLOSURE_E permission, Cell/Link/Port future-operation transport or V17/V29/V39 is made.

## Next meaningful science

1. Obtain an independent review of the R762EQ q9 monic-recurrence finite certificate, since the entire all-q lift depends on it.
2. Use (2) to construct a compressed all-q exact terminal coefficient/power-of-3 observer without enumerating q^3 endpoints for every horizon, with explicit conversion and verification costs.
3. Independently specify the genuine signed native Cell/Link/Port event alphabet and future-operation observer transport required by the parent task.
