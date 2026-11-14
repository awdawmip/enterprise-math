# R149B — Complete shifted covariance waveform for the R148B infinite family

**Date:** 2026-11-14 (Asia/Shanghai)  
**Frozen input:** \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`  
**Scope:** external S23 scalar tied-phase Sturmian integer-phase-fiber discrepancy.  
**Status:** author-side exact proof; finite rational checks; \`NOT_REVIEWED\`.

## Theorem R149B.1 (all r>=1 and all integer lags h)

Retain R148B's valid finite Sturmian word family

\`\`\`
w_r = 0^r 1 0^r 1 0^r,   m=3r+2,
(a,b,c,d,U,V) = (1,r+2,3,3r+2,2,0).
\`\`\`

Let \`Gamma_r(h)\` denote R149's lagged covariance between its lower-endpoint residue part at coefficient \`L\` and upper-endpoint residue part at coefficient \`L+h\`, over one complete period of \`L\`. Define

\`\`\`
g=gcd(r+2,3r+2)=gcd(r+2,4) in {1,2,4},
k=(h+2) mod g.
\`\`\`

Then the following **closed exact rational formula** holds for all positive \`r\` and all integer \`h\`:

\`\`\`
Gamma_r(h) =
   [ (g^2-1)/12 - k(g-k)/2 ] / [(r+2)(3r+2)].             (R149B.1)
\`\`\`

Equivalently, with \`B=(r+2)(3r+2)\`, the full lag waveforms are:

\`\`\`
r odd, g=1:                Gamma_r(h)=0                  for all h.
r = 0 mod 4, g=2:          4B*Gamma_r(h)=+1 if h even, -1 if h odd.
r = 2 mod 4, g=4:
  h mod 4:                      0       1       2       3
  4B*Gamma_r(h):               -3      -1      +5      -1
\`\`\`

For each \`r=4k+2\`, \`k>=0\`, the **shifted** correlation at lag \`h=2\` is

\`\`\`
Gamma_r(2)=5/[4(r+2)(3r+2)]
          =(g^2-1)/(12*b*d),    g=4.
\`\`\`

Thus an infinite family of actual Sturmian words realizes the **sharp positive R148 bound with nontrivial gcd 4**, while the same words have *negative* simultaneous covariance \`Gamma_r(0)=-3/[4bd]\`. The smallest family member is \`w_2=00100100\`, length 8, with \`b=4,d=8\`, \`Gamma_2(0)=-3/128\`, \`Gamma_2(2)=+5/128\`.

This is a temporal-residual phenomenon: retaining relative coefficient lag changes the observable covariance sign and extremality without changing the word, endpoints, offsets or underlying scalar model.

## Proof

R148B proves the displayed word's slope-support and offsets. R149.1 supplies the exact gcd-residue covariance for any lag:

\`\`\`
Gamma_r(h) = [1/(g*b*d)] sum_{t=0}^{g-1}
 ((t-2 mod g)-(g-1)/2) *
 ((-3(t+h) mod g)-(g-1)/2).
\`\`\`

As \`g|4\`, \`-3=1 (mod g)\`. Set \`x=(t-2) mod g\`. Then the second residue is \`(x+h+2) mod g\`. Hence the product average is exactly the covariance of the uniform integer residue \`x=0,...,g-1\` with \`(x+k) mod g\`, divided by \`bd\`, where \`k=(h+2) mod g\`.

For any \`g>=1\`, the translated residue \`y=(x+k) mod g\` satisfies \`y-x=k\` on \`g-k\` residue values and \`y-x=k-g\` on \`k\` values. This gives \`Var(y-x)=k(g-k)\`. Because \`Var(x)=Var(y)=(g^2-1)/12\`,

\`\`\`
Cov(x,y)=(g^2-1)/12-k(g-k)/2.
\`\`\`

Substituting yields (R149B.1). For \`g=1,2,4\`, evaluating the stated residue classes gives the three tables. At \`g=4,h=2\`, \`k=0\`, so \`Gamma=(g^2-1)/(12bd)\`: the positive sharp bound is attained. QED.

## Exact checking and next question

\`check_r149b.py\` computes the original centered gcd-residue sum and the compressed lag formula independently as Python \`Fraction\` for **all 200 integers r=1..200**, **21 lags h=-10..10 per r** (4,200 exact agreements), plus the whole-gcd-cycle sum, both g=2 values and all four g=4 values. Distribution: 100 words with gcd 1, 50 with gcd 2, 50 with gcd 4. Marker: \`R149B_SHIFTED_EXTREMAL_WAVEFORM_PASS\`.

Next: classify the whole lag waveform for larger gcd classes of actual Sturmian words and determine whether long-lag residue alignments offer a shorter certificate for presence/loss of a single integer phase fiber at the critical coefficient \`E(m)\`.
