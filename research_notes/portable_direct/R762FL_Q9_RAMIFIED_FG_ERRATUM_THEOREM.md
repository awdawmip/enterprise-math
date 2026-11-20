# R762FL — Ramified q9 character valuations and correction to R762FG

Date: 2026-11-19 (Asia/Shanghai). Scientific task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen taskbook: \`enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md\`. Scope: six separately named positive BRC steps, all 729 terminals of \`(Z/9Z)^3\`, no native signed TRIADIC_CLOSURE_E event. Status: author-side exact proof and computation; NOT_REVIEWED.

## Precise error and correction

R762FG's proposed exact character-valuation law implicitly treated a nonzero residue in \`Z_3[zeta9]/(3)\` as a unit. That quotient contains nilpotents. For its chosen ninth-root character, \`beta^6-1=3u\` with \`u mod 3 != 0\` coefficientwise, yet \`u\` belongs to the maximal ideal \`(zeta9-1)\`. Consequently R762FG's exact valuation formula is false. Its integer-exponent necessary period divisibility **remains valid**, as proved below. Preserve the original R762FG files and record this correction separately.

Put \`P=1+X+Z+XY+YZ+XYZ\`, \`zeta=zeta9\`, and evaluate \`(X,Y,Z)=(1,zeta,zeta^2)\`. Then
\`lambda=2+zeta+zeta^2+2*zeta^3\`,
\`beta=lambda^3/3=-7-2*zeta+2*zeta^2+5*zeta^4+7*zeta^5\`.
Let \`pi=zeta-1\`; the local field \`Q_3(zeta)\` is totally ramified of degree six, and \`v_pi(pi)=1\`, \`v_pi(3)=6\`, \`v_3=v_pi/6\`. For any nonzero integral cyclotomic element \`u\`, \`v_pi(u)=v_3(Norm(u))\`.

Multiplication matrices in the integral basis \`1,zeta,...,zeta^5\`, reduced by \`Phi9(zeta)=zeta^6+zeta^3+1=0\`, have exact determinants

\`\`\`
Norm(beta^2-1) = 227529 = 3^4 * 2809
Norm(beta^6-1) = 332147475315061641 = 3^10 * 5624946659809
\`\`\`

Therefore \`v_pi(beta^2-1)=4\` and \`v_pi(beta^6-1)=10\`; in particular \`v_3(beta^6-1)=5/3\`, not 1. Because \`beta mod pi=-1\`, for **every positive integer m**,

\`\`\`
v_pi(beta^m-1) =
  0                      m odd,
  4                      m even, 3 ∤ m,
  10 + 6*v_3(m/6)        6 | m.
\`\`\`

Proof: odd powers reduce to -1 modulo pi. For \`m=2u\` with \`3∤u\`, factor \`(beta^2)^u-1\`; its geometric quotient is a unit modulo pi, retaining valuation 4. For \`m=6t\`, write \`beta^6=1+w\` with \`v_3(w)=5/3>1/2\`; odd-prime binomial lifting gives \`v_3((1+w)^t-1)=5/3+v_3(t)\` for all positive t.

## Correct exact normalized discrepancies

For \`n=3k>=9\`, let \`f(n)=floor(n/3)-2\` and \`S(n)=P^n/3^{f(n)}\` when interpreted in the integral terminal lattice. For \`L=3m+r>0\`, \`r=0,1,2\`, the character satisfies

\`chi(S(n+L)-S(n))=9*beta^k*(beta^m*lambda^r-1)\`.

Since \`v_3(beta)=0\` and \`v_3(lambda)=1/3\`, its **exact** valuation is

\`\`\`
2                         if 3 ∤ L;
2                         if L=3m and m odd;
8/3                       if L=3m, m even, 3 ∤ m;
11/3 + v_3(m/6)           if L=3m and 6 | m.
\`\`\`

For integer precision \`h>=3\`, a complete 729-terminal eventual period L modulo \`3^h\` necessarily has character discrepancy valuation at least h at sufficiently late n divisible by 3. The first three cases are less than 3; the last forces \`v_3(m/6)>=h-3\`. Hence the **R762FG period lower-bound corollary survives unaltered**:

\`18*3^(h-3) | L\`.

This is necessary divisibility, not an upper bound or a native signed dynamics statement.

## New exhaustive finite classification of all 729 characters

For each \`a,b,c in 0,...,8\`, define \`lambda_abc=P(zeta^a,zeta^b,zeta^c)\` and \`beta_abc=lambda_abc^3/3\`. Exhaustive integral reduction confirms all 729 beta are in \`Z[zeta]\`, with exactly 127 distinct lambda values. The norms of \`beta\`, \`beta^2-1\`, and \`beta^6-1\` give:

| v_pi(beta) | v_pi(beta²−1) | v_pi(beta⁶−1) | Distinct lambda | Named characters |
|---|---:|---:|---:|---:|
| 0 | 3 | 10 | 54 | 270 |
| 0 | 4 | 10 | 36 | 216 |
| 6 | 0 | 0 | 24 | 144 |
| 12 | 0 | 0 | 12 | 39 |
| infinity (beta=0) | 0 | 0 | 1 | 60 |
| **Total** | | | **127** | **729** |

Thus all 486 unit-beta characters satisfy exactly \`v_pi(beta^6-1)=10\`; the R762FH modulo-3 character identity has **four additional powers of the ramified uniformizer**. For every positive t and any unit-beta character, \`v_3(beta^{6t}-1)=5/3+v_3(t)\`. If \`n=3k+r>=9\`, \`r in {0,1,2}\`, its normalized discrepancy for \`L=18t\` has exactly \`11/3+r/3+v_3(t)\` valuation. These assertions belong to the cyclotomic character observer. R762FH–FI's integral Hasse jets retain the terminal information that ordinary Fourier characters lose at the same modulus.

## Reproduction, scope and next question

Run \`python3 R762FL_VERIFY.py > R762FL_EVIDENCE.json\`. Standard-library integer arithmetic enumerates every character triple; operations use the exact basis quotient by \`Phi9\`; 6x6 field norms are fraction-free Bareiss determinants. The checker asserts 729 characters, 127 distinct eigenvalues, all five classification rows, the exact two displayed norms, and m=1..36 of the corrected law. Author run: PASS. This is a finite exhaustive certificate for the 729-character classification plus symbolic lifting for the all-m/all-h statements; independent mathematical review remains NOT_REVIEWED.

The next question is whether a small **integral** Hasse-jet observer can establish \`18*3^(h-1)\` as the full-vector period for all h, without the 57-trit worst-case return-observer surcharge. Retain P000, the native six signed axes and three-dimensional research-slice semantics; signed Cell/Link/Port event/transport remains an independent task.
