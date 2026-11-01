# D25/LIFT — universal CM stencil response and the prime 283 resonance

2026-10-31; TASK_RESEARCH portable author-side result. Logical Research lane: chatgpt-research-hourly-enterprise-math-20260923 (not maintenance).
Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / CONDITIONAL / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
Frozen scientific Source: c47e13e4aba0e006366f989d6334d443f6333ae3 (UNCHANGED). P000 ACTIVE worldview unchanged. This is external p-adic arithmetic, not the native six-axis H0/B0 experiment.

## Inherited, source-scoped premises

For p=6l+1, p mod 24 in {13,19}, retain the ORIGINAL denominator and signed weight:
a_n=binom(2n,n)^2 binom(3n,n)/216^n;
A_p(X)=sum_{n=0}^{p-1}(6n+1)a_n X^n.
G_l(z)=sum_{k=0}^{l}binom(l,k)binom(2l,k)z^k; g=G_l'(1/2) mod p.

The established finite Clausen reduction gives sum a_n X^n = G_l(X/2)^2 mod p as a polynomial; the inherited CM zero is G_l(1/2)=0 mod p. The Gauss ODE at the ordinary point 1/2 implies g != 0 mod p. The earlier fixed-216 curvature/cubic lemma and concurrent first-jet Green reduction remain separate inherited works.

## Theorem: universal response for all fixed r <= p-2

There is a unique formal rational series f(w) with f(0)=0, f'(0)=1 and
(1-w^2)f''+(1-3w)f'/2-f/18=0.
Writing f=sum b_n w^n yields
b_0=0, b_1=1,
(n+2)(n+1)b_{n+2}=-(n+1)b_{n+1}/2+(n^2+n/2+1/18)b_n.

Define the universal observer
R(s)=[f(w)^2+6(1+w)(f(w)^2)']/4 at w=-s/(1+s)
=sum_{r>=1}c_r s^r,
kappa_r=r!c_r.

For every target prime p and 1<=r<=p-2, these rational coefficients are p-integral. For every p-local t, let
D_{r,p}(t)=sum_{j=0}^r (-1)^(r-j) binom(r,j) A_p((1+jpt)^(-1)).
Then the exact conditional all-target-prime result is

  D_{r,p}(t) = p^r t^r kappa_r g^2 (mod p^(r+1)).

Proof: The Gauss equation for G is z(1-z)G''+[1+(3l-1)z]G'-2l^2G=0. Modulo p, l=-1/6; the change w=2z-1 reduces it to the fixed f equation. From the CM zero and g=G'(1/2), local uniqueness gives G((1+w)/2)=(g/2)f(w) mod p through degree r+1 (<p). Square this and use the existing coefficientwise finite Clausen reduction. Apply the ORIGINAL operator 1+6X d/dX and substitute X=(1+s)^(-1). The s^r coefficient is g^2 c_r mod p. For the actual original p-adic finite sum, Taylor expansion at s=0 is valid modulo p^(r+1) on s=jpt. The binomial signed-difference identities sum_j (-1)^(r-j)binom(r,j)j^k=0 for k<r and =r! at k=r annihilate all lower jets. This proves the claimed congruence, including p^r divisibility, without replacing the original denominator or source provenance.

This is an observer/operator statement only: it preserves p,n,original a_n,weight 6n+1,216,t and the signed finite-difference order. It neither reconstructs the entire p-adic sum nor transfers a theorem into native P000 X6.

## First five leading symbols and exact sharpness classification

R(s)=-3s+4s^2-(119/18)s^3+(1265/108)s^4-(277057/12960)s^5+O(s^6).
(kappa1,...,kappa5)=(-3,8,-119/3,2530/9,-277057/108).
119=7*17; 2530=2*5*11*23; 277057=11*89*283.

Since g is a p-unit, for all frozen target primes and p-unit t:
  v_p(D_{r,p}(t))=r for r=1,2,3,4.
At r=5, this exact valuation still holds for every target p except 283. For p=283, the universal coefficient is zero mod p, so v_283(D_{5,283}(t))>=6 for all p-units t.

An **exact individual-prime modular certificate** calculated from the full ORIGINAL 216 sum at t=1 gives
  D_{5,283}(1)/283^5 = 0 (mod 283),
  D_{5,283}(1)/283^6 = 7 (mod 283).
Thus the valuation for this specific p,t is exactly 6. It is not asserted that all t have exact valuation 6 at p=283.

## Executed verification and provenance

The accompanying standalone Python program uses stdlib Fraction for the rational f-recurrence; exact modular inverses for every original a_n; and independent full-integer binomial a_n anchors at p=13,19,37,283,373. For every target prime p<1001 and t=1,2, it checks all r=1..5 directly from the complete original A_p modulo p^7. All 45 primes and 450 signed-stencil checks passed. Marker: PASS_D25_UNIVERSAL_CM_STENCILS_EXACT. Anchor tuples (p, g, D1/p, D2/p^2, D3/p^3, D4/p^4, D5/p^5) modulo p:
(13,1,10,8,8,11,3)
(19,2,7,13,6,14,12)
(37,11,7,6,35,32,28)
(283,255,195,46,220,280,0)
(373,215,81,157,325,243,166).
These checks corroborate the argument but do not promote project mathematical admission.

## Unfinished mother objective and next action

The frozen D25/LIFT/JT2 base-point requirement A_p(1)=p (mod p^3) remains OPEN. In the now-current first-jet finite Green reduction, the actual unclosed four-source scalar is [integer carry]+[first jet]-[finite Green functional]-[independent original signed R_p]. The next substantive action is a finite source-preserving WZ/adjoint transport combining the Green functional and signed R_p **with** the integer carry, discriminated by the nonzero branches at 19,67,373; do not equate Green E and original R or assume ports vanish separately. The universal stencil theorem is a source-preserving operator check for candidate identities, not the missing base-point proof.

As read on 2026-10-31 from Gateway 0.6.11: research_authority_granted=false; executor_binding_configured=false; active_jobs=5/5; source_sync.control.state=CODE_REVIEW_REQUIRED; UPSTREAM_CODE_REVIEW_REQUIRED. No new native claim, open, Source checkpoint, Result or formal admission is established by GitHub author publication. Current client does not expose direct recovery_status; historical own bridge #6424/#6425 merely establish past read transport. The existing control support issue is enterprise-math #1558. Do not close or swap protected old session/staging. This file is the author's portable research result, not a Source-native checkpoint.