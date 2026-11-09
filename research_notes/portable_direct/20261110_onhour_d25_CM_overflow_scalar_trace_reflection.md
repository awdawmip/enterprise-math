# D25 — exact one-coordinate CM overflow test and carry-preserving reflected trace

2026-11-10 | TASK_RESEARCH author-side | UNREVIEWED / NOT_ADMITTED / NOT_NATIVE

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen science c47e13e4aba0e006366f989d6334d443f6333ae3. Immutable Source-native checkpoint b58330b74576153cdadde5d80a3d92df3a819a0e unchanged. Own logical Research lane chatgpt-research-onhour-enterprise-math-20260923; maintenance lane chatgpt-hourly-enterprise-math-20260921 excluded.

## Exact scientific input and scope

For every prime p≡13 (mod 24), p>3, use R=(Z/p²Z)[t]/(t²-2), conjugation σ(t)=-t, s=(3-2t)/6, σ(s)=1-s, sσ(s)=1/36. Let F_p(z)=sum_{k=0}^{p-1}(1/8)_k(3/8)_k z^k/(k!)², G_p(x)=sum_{k=0}^{p-1}(1/4)_k(3/4)_k x^k/(k!)². The preceding author-side finite Gauss identity is F_p(4x(1-x))=G_p(x)+x^p E_p(x), with E_p(x)=sum_{r=0}^{p-2} e_{p+r}x^r and
e_{p+r}=sum_{k=ceil((p+r)/2)}^{p-1} 4^k f_k (-1)^{p+r-k} binom(k,p+r-k), f_k=(1/8)_k(3/8)_k/(k!)².
The predecessor author-side CM(-24) result yields F_p(1/9)=G_p(s)=0 mod p; the predecessor complete-polynomial Legendre reflection yields G_p(1-x)=-G_p(x) mod p². These are explicitly declared dependencies; neither is claimed as an independently reviewed theorem.

Write G_p(s)=p*g_p*t and E_p(s)=p*(u_p+v_p*t) modulo p². All three digits are in F_p. The last equality is valid since s is a unit and F_p(1/9),G_p(s) both vanish modulo p.

## Proven proposition A: odd observer fixes a linear constraint and reduces the open conjecture to one scalar

Since p≡5 mod 8, s^p ≡ σ(s)=1/2+t/3 mod p. Comparing the t-odd and scalar coordinates in
F_p(1/9)=G_p(s)+s^p E_p(s) gives, respectively,

  2*u_p + 3*v_p + 6*g_p = 0 (mod p),
  F_p(1/9)/p = (3*u_p+4*v_p)/6 = (u_p-24*g_p)/18 (mod p).

Therefore the outstanding all-prime assertion F_p(1/9)=0 (mod p²) is **equivalent** to the ONE scalar equality u_p=24*g_p (mod p); when it holds the other coordinate is forced to v_p=-18*g_p (mod p). This is a proved, source-preserving equivalence, not a proof of the open equality.

## Proven proposition B: scalar symmetric-power certificate without a quadratic extension

Put T_r=s^r+σ(s)^r (in Z/p²), so T_0=2, T_1=1 and T_r=T_(r-1)-T_(r-2)/36 for r>=2. Define S_p=sum_{r=0}^{p-2}e_{p+r}T_r. Because the ring trace of E_p(s) equals 2p*u_p, we have S_p=2p*u_p (mod p²), and hence

  36*F_p(1/9) = S_p - 48*p*g_p (mod p²).

Thus the open goal is exactly S_p=48*p*g_p (mod p²). This uses rational mod-p² arithmetic with unit denominators p>3 and preserves all signed raw overflow coefficients e_n. It is a one-scalar target certificate; the t-odd repair coordinate g_p is retained, so no full-ring/native observer-equivalence is asserted.

## Proven proposition C: p² Frobenius-reflected power and exact half-pairing

Define ζ_p=(s^p-σ(s))/p in R/p. This quotient is integral since σ(s)=s^p mod p. For 0<=r<=p,

  T_(p-r)=36^r * [ T_(r+1) + p*Tr(ζ_p*σ(s)^r) ] (mod p²).

Proof: s^{-1}=36σ(s), so s^{p-r}=36^r(σ(s)+pζ_p)σ(s)^r; take the ring trace. Retaining ζ_p is necessary for p² accuracy. In particular S_p can be rewritten with only the paired r=2,...,(p-1)/2 kernel evaluations:

  S_p = 2*e_p + e_(p+1)
        + sum_{r=2}^{(p-1)/2} [ e_(p+r)*T_r
          + e_(2p-r)*36^r*(T_(r+1)+p*Tr(ζ_p*σ(s)^r)) ] (mod p²).

The indices, signs, parity, p-digit carry and original high-degree provenance are kept. This is a precise candidate for a finite WZ/Jacobi pairing proof of S_p-48pg_p=0.

## Exact reproducible checks

The accompanying Python standard-library checker computes f_k and g_k via *separate* rational recurrences, the raw k,j binomial overflow (not F-G masquerading as an edge sum), ring evaluation, a rational trace recurrence, the independent Frobenius-reflected half-pairing, and the direct original F sum. It executed PASS on p=13,37,61,109,157,181,373,397,421,541 (10 primes; last three new beyond preceding overflow check). These finite checks do not prove the open scalar equality for every prime.

Observed p=373: g=115, u=149, v=168, S=111154 mod139129; 2u+3v+6g=0 mod373; u-24g=0 mod373; original F=0 mod139129. New independent examples: p=397 (g,u,v)=(333,52,358), p=421 (156,376,139), p=541 (538,469,54), all satisfy both proved identities and the presently experimental target.

## Explicit research interface and next obligation

BRC COMPOSE_APPLIED: the original signed n>=p overflow coefficients and the sigma-even scalar / sigma-odd repair-coordinate observer form a typed carrier; one-scalar descent is certified ONLY for the output F_p(1/9)/p at p² precision, with original port/source retained. The quadratic ring is an external auxiliary, not native Enterprise X6 space or Frobenius.

NEXT EXACT ACTION: seek a finite telescoper/pairing for the explicit half-sum that proves S_p=48pg_p mod p² uniformly. Do not re-run earlier 157-prime scans or mark the AF4 W/V and original native H0/B0 p373 benchmark completed. Issue #1559 remains a separate OPEN/PENDING_OWNER native same-original-class [X]U modulo139129, rank, Frobenius direction/eta, signed κ/Delta-R and independent reproduction obligation.

Source provenance: predecessor 20261109_onhour_d25_CM_quadratic_overflow_trace.md, its verified script, and CM24 short-root predecessor. This is author-side mathematics with declared dependencies and no new Source CLAIM/run, Result, review, or acceptance.
