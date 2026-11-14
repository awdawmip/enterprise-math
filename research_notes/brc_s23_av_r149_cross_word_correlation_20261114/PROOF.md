# R149 — Exact cross-word covariance and lagged fiber autocorrelation via common-residue kernels

**Date:** 2026-11-14 (Asia/Shanghai)  
**Scientific input (unchanged frozen pin):** \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`  
**Scope:** external scalar S23 tied-phase finite Sturmian observer, integer phase-fiber multiplicity.  
**Status:** author-side exact general proofs, executable rational recheck; \`NOT_REVIEWED\`.  
**Dependencies:** R146 \`b02b0c242b274bc6a82111dbd3600126a2867319\`, R147 \`2b81c43614889ccb638bb7d8feb329c3c467ff02\`, R148 \`06f79f0d3c04f6c73a056c552793f48b9254ad08\`.

## 1. Input and definitions

For a finite Sturmian word \`w\` of length \`m>=1\`, let its strict free-intercept slope-support endpoints be reduced rationals \`alpha_w=a/b<beta_w=c/d\`, with \`b,d>=1\`, and prefix sums \`s_0=0,...,s_m\`. The integer intercept offsets are

\`\`\`
U=min_{0<=j<=m} [b(s_j+1)-ja],   V=max_{0<=j<=m} [d*s_j-jc].
\`\`\`

R146 establishes the exact number of integer phase fibers at \`K>=2\`, \`L=K-1\`:

\`\`\`
C_w(K)=ceil((Lc-V)/d)-floor((La-U)/b)-1.
\`\`\`

Write \`delta_w=c/d-a/b\`, \`h_w=U/b-V/d\`, \`e_w(L)=C_w(L+1)-L*delta_w\`. With nonnegative least residues:

\`\`\`
X_w(L)=(aL-U) mod b,    Z_w(L)=(V-cL) mod d,
e_w(L)=h_w-1+X_w(L)/b+Z_w(L)/d.               (1)
\`\`\`

The identity holds for physical \`L>=1\`, and its right-hand side extends periodically to all integers. Thus a signed lag \`h\` is allowed algebraically; direct phase-fiber interpretations use \`L>=1\` and \`L+h>=1\`. Mean/covariance always refer to uniform \`L\` over one complete common period. For a word \`w\` the mean of its periodic discrepancy is

\`\`\`
mu_w=h_w-1/(2b)-1/(2d).                         (2)
\`\`\`

## 2. R149.1 — Universal two-residue covariance kernel

For positive integers \`n,m\`, unit multipliers \`gcd(s,n)=gcd(t,m)=1\` (unit modulo 1 is vacuous), integer offsets \`u,v\`, put \`G=gcd(n,m)\`, \`q=(G-1)/2\`. Define the exact rational kernel

\`\`\`
H(n,s,u; m,t,v) =
  1/(G*n*m) * sum_{j=0}^{G-1}
   ( ((s*j+u) mod G)-q ) * ( ((t*j+v) mod G)-q ).       (3)
\`\`\`

**Theorem.** For \`R_L=((sL+u) mod n)/n\` and \`S_L=((tL+v) mod m)/m\`, the covariance over \`P=lcm(n,m)\` is exactly \`H(n,s,u;m,t,v)\`. With \`G=1\` it vanishes. For every integer lag \`h\`,

\`\`\`
Cov_P(R_L,S_{L+h})=H(n,s,u; m,t,v+t*h).         (4)
\`\`\`

**Proof.** Under uniform \`L mod P\`, condition on \`L mod G=j\`. The two residues are in classes \`(sj+u) mod G\` and \`(tj+v) mod G\`. By the generalized CRT, every pair of residues in those congruence classes corresponds to exactly one \`L mod P\`: the underlying linear congruences are invertible because \`s,t\` are units. Therefore the conditional residues are independent and uniformly traverse respectively \`n/G\` and \`m/G\` elements. Their centered conditional means relative to the unconditional means \`(n-1)/(2n)\`, \`(m-1)/(2m)\` are precisely \`(r_j-q)/n\`, \`(z_j-q)/m\`. The conditional covariance is zero; the law of total covariance gives (3). Replacing \`v\` with \`v+th\` yields (4). The same reasoning works at denominator one. QED.

The proof immediately yields

\`\`\`
|H| <= (G^2-1)/(12nm).                            (5)
\`\`\`

For \`G>=2\`, the positive equality holds iff \`t=s (mod G)\` and \`v=u (mod G)\`; negative equality iff \`t=-s (mod G)\` and \`v=g-1-u (mod G)\`, where the last \`g\` denotes \`G\`. This follows by applying Cauchy–Schwarz to two centered permutations; positive equality forces identical permutations, negative equality forces reversed ones. Formula (4) inserts \`v+th\` in the two offset conditions.

**Lag-averaging and parity.** Summing (4) over \`h=0,...,G-1\` gives zero: for fixed \`j\`, the centered second residue traverses all \`G\` values. If \`G=2\`, both slopes are odd, the only two permutations either align or reverse, and the lag sequence alternates between \`+1/(4nm)\` and \`-1/(4nm)\`.

## 3. R149.2 — Cross-word covariance in four gcd-scale sums

For each word \`w\`, form two triples

\`\`\`
T_w = {(b,a,-U),(d,-c,V)}.
\`\`\`

**Theorem (any pair of finite Sturmian words).** For words \`w,v\` and integer \`h\`, let \`Q\` be the lcm of their four endpoint denominators. Then

\`\`\`
Cov_Q(e_w(L),e_v(L+h))
  = sum_{(n,s,u) in T_w} sum_{(m,t,z) in T_v}
        H(n,s,u; m,t,z+t*h).                     (6)
\`\`\`

**Proof.** Apply the exact residue decomposition (1) to both words, remove constants, expand the covariance into four bilinear terms, and use (4). Every component is periodic with a denominator dividing \`Q\`; averaging over \`Q\` is equivalent to averaging over its own natural period. QED.

The evaluator needs at most the sum of the **four pairwise denominator gcds**, rather than enumerating the possibly much larger common period \`Q\`. If all four cross-denominator gcds equal 1, the two centered fiber discrepancies are uncorrelated at **every lag**. This is an exact zero-covariance statement, not a claim of full statistical independence.

## 4. R149.3 — Closed autocovariance and short-lag structure

For \`n>=1\` and integer \`k\`, set \`r=k mod n\` and

\`\`\`
A_n(k)=(n^2-1-6*r*(n-r))/(12*n^2).             (7)
\`\`\`

It is the covariance of \`((sL+u) mod n)/n\` with its lag-\`h\` copy for \`k=sh\`, whenever \`s\` is a unit modulo \`n\`. To prove this, a uniform residue \`x\` and its translated residue \`y=(x+r) mod n\` have \`y-x=r\` with probability \`(n-r)/n\` and \`y-x=r-n\` with probability \`r/n\`. Thus \`Var(y-x)=r(n-r)\`, while \`Var(x)=Var(y)=(n^2-1)/12\`. The identity \`Var(y-x)=2Var(x)-2Cov(x,y)\` proves (7), including \`n=1\`.

Define the shifted mixed kernel

\`\`\`
Gamma_w(h)=H(b,a,-U; d,-c,V-c*h).               (8)
\`\`\`

Then the entire discrepancy autocovariance sequence is

\`\`\`
Cov_Q(e_w(L),e_w(L+h))
  = A_b(a*h) + A_d(-c*h) + Gamma_w(h)+Gamma_w(-h),   (9)
\`\`\`

where \`Q=lcm(b,d)\`. The sequence is even in \`h\`, periodic with period dividing \`Q\`, and its period sum is zero. At \`h=0\`, (9) recovers R147's exact variance; (8) recovers R148's covariance and its shifted extension. If \`gcd(b,d)=2\`, \`Gamma_w(h)=(-1)^h Gamma_w(0)\` and \`|Gamma_w(0)|=1/(4bd)\`.

## 5. Worked exact witnesses

1. \`w=00001000010000\`, with \`(a,b,c,d,U,V)=(1,6,3,14,2,0)\`. The actual mixed term alternates \`Gamma_w(0)=1/336\`, \`Gamma_w(1)=-1/336\`. Its full discrepancy variance is \`899/5292\`, while its lag-one autocovariance is \`23/5292\`. The latter is a new temporal statistic of the same legitimate Sturmian word.
2. The words \`0101\` with endpoint denominators \`(3,3)\` and \`0110\` with \`(2,4)\` have all four cross-gcds equal 1. Their centered fiber discrepancies have covariance exactly zero for every integer lag, although both arise from the same underlying \`L\` clock.

## 6. Executable crosscheck and boundary

Companion script \`check_r149.py\` reconstructs every binary word of lengths 1 through 8, keeps those with exact nonempty strict Sturmian slope support (**218 words**), and tests the direct full-period rational covariance against (6) and (9). It checks **1,090 autocorrelation cases**, **1,400 deterministically selected two-word/lag cases**, **196 gcd lag-sum cases**, and **86 gcd-two sign-alternation cases**, all exact. The finite tests confirm the implementation for their declared domain; the universal statements above follow from the algebraic proofs.

**Next problem.** Use (6) to classify which pairs of words share temporally correlated phase-fiber discrepancies, and test whether the lagged conditional residue structure yields a sharper criterion for single-fiber loss near the conjectured all-length word-saturation threshold \`E(m)=(m-2)floor((m-1)/2)+1\`. Keep S23 scalar multiplicity and native X6 claims distinct.
