# R149C — Every shared gcd residue is recoverable by time lag: full spectral support

**Date:** 2026-11-14 (Asia/Shanghai).  
**Scientific pin:** \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.  
**Scope:** S23 external scalar modular phase-fiber observer; not a native X6 transfer.  
**Status:** author-side general algebraic proof, finite exact integer verification, \`NOT_REVIEWED\`.  
**Dependencies:** R149.1 universal modular covariance kernel, same directory \`PROOF.md\`; R147 and R148 for the Sturmian interpretation.

## Theorem R149C.1 — Exact minimal lag period and nonvanishing spectrum

Let \`n,m>=1\`, \`s,t,u,v\` be integers with \`gcd(s,n)=gcd(t,m)=1\`, and \`g=gcd(n,m)\`. Define for every integer lag \`h\`:

\`\`\`
F(h) = Cov_{L mod lcm(n,m)}(
    ((sL+u) mod n)/n,
    ((t(L+h)+v) mod m)/m )
     = H(n,s,u; m,t,v+t*h).
\`\`\`

If \`g=1\`, \`F(h)=0\` identically. If \`g>=2\`, **every nontrivial discrete Fourier coefficient of \`F\` over Z/gZ is nonzero**; consequently:

1. The minimal positive period of the lagged covariance is exactly **g**, not merely a divisor of g.
2. At least one lag has nonzero covariance, for every unit-slope and offset choice.
3. A zero simultaneous covariance \`F(0)=0\` does not remove the joint residue dependence: other lags necessarily reveal a nonzero covariance.
4. The lag average is zero: \`sum_{h=0}^{g-1}F(h)=0\`.

This is an exact finite algebraic result. Fourier coordinates are a derived representation of the external modular observer.

### Proof by explicit nonzero finite characters

For \`g>=2\`, put \`q=(g-1)/2\` and centered permutations

\`\`\`
A_j=((s*j+u) mod g)-q,
B_j=((t*j+v) mod g)-q,       0<=j<g.
\`\`\`

Since the multipliers are units mod g, these are permutations of \`0-q,...,(g-1)-q\`. R149.1 gives the circular cross-correlation

\`\`\`
F(h)= [1/(g*n*m)] sum_{j=0}^{g-1} A_j B_{j+h mod g}.   (1)
\`\`\`

Fix a primitive g-th root of unity \`zeta\`. Define \`hat A(k)=sum_j A_j zeta^(k*j)\` and similarly for B and F; \`k=0,...,g-1\`. Let \`s^{-1}\` and \`t^{-1}\` denote inverses modulo g. For every \`1<=k<g\`, permuting the summation index by \`x=(s*j+u) mod g\` yields

\`\`\`
hat A(k)=zeta^(-k*s^{-1}*u) *
  sum_{x=0}^{g-1}(x-q) zeta^(k*s^{-1}*x).
\`\`\`

For any \`z^g=1\` with \`z!=1\`, geometric differentiation gives

\`\`\`
sum_{x=0}^{g-1}(x-q)*z^x = -g/(1-z) != 0.
\`\`\`

Therefore, for \`k=1,...,g-1\`,

\`\`\`
hat A(k)=-g*zeta^(-k*s^{-1}*u)/(1-zeta^(k*s^{-1})),
hat B(k)=-g*zeta^(-k*t^{-1}*v)/(1-zeta^(k*t^{-1})).
\`\`\`

Taking the lag Fourier transform of (1), using \`ell=j+h\`:

\`\`\`
hat F(k)=hat A(-k)*hat B(k)/(g*n*m)
        =g*zeta^(k*(s^{-1}u-t^{-1}v)) /
          [n*m*(1-zeta^(-k*s^{-1}))*(1-zeta^(k*t^{-1}))],    (2)
\`\`\`

where all exponents are modulo g. All denominators are nonzero when \`k!=0\`, and \`hat F(0)=0\` by centering. Hence \`hat F(k)!=0\` for every nonzero k, proving full nontrivial spectral support and zero lag-mean.

If F had period p with \`0<p<g\`, the shift identity would force \`hat F(1)=zeta^(+/-p)*hat F(1)\`, whence \`zeta^p=1\`, contradicting primitivity. Thus its minimal period is g. Nontrivial spectral support also implies F is not identically zero. QED.

## Corollary R149C.2 — Sturmian word phase-coupling detection

For each actual finite Sturmian word \`w\` with reduced rational slope endpoints \`a/b<c/d\`, let \`Gamma_w(h)\` be R149's mixed lower/upper integer residue covariance. Then \`g=gcd(b,d)\` is the exact minimal lag-covariance period when \`g>1\`, and \`Gamma_w(h)\` is identically zero iff \`g=1\`.

Proof: its kernel is R149.1 with \`(n,s,u;m,t,v)=(b,a,-U;d,-c,V)\`; reduced endpoints imply both multipliers are units modulo g.

This is a more informative joint-residual invariant than \`Gamma_w(0)\` alone: observing a complete lag cycle detects all noncoprime endpoint residue couplings, even when a chosen lag has zero covariance.

## Exact arithmetic example, including vanishing lag zero

Take \`n=m=g=5\`, \`s=t=1\`, \`u=0\`, \`v=1\`. Then

\`\`\`
(F(0),F(1),F(2),F(3),F(4))=(0,-1,-1,0,2)/25.
\`\`\`

The zero-lag covariance is zero, yet the period is five and lag four has covariance \`2/25\`. This is an example of the general modular kernel, not a claim that these four parameters correspond to a particular finite Sturmian word.

## Verification

\`check_r149c.py\` exhausts all \`g=2,...,12\`, all unit residues \`s,t mod g\`, and all offsets \`u,v mod g\`: **22,356 combinations**, verifying the exact lag cycle has sum zero, minimal period exactly g, and a nonzero value. **1,336** tested combinations have zero covariance at lag zero but nonzero at another lag. Uses integer numerator \`4g n m F(h)\`; no floating point, no root evaluation. The general nonvanishing theorem is proved above; the integer checker is a finite implementation recheck. Marker: \`R149C_FULL_GCD_LAG_SUPPORT_PASS\`.

## Next

Investigate whether the complete lag signature (with its guaranteed full gcd harmonic support) gives an efficient, sufficient observable for detecting changes in single-word phase-fiber presence across the critical coefficient range. General cross-word four-kernel covariance, word support and exact integer-fiber counts remain distinct observables.
