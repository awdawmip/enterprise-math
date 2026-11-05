# D25 — A source-preserving scalar directional jet for the signed Lucas carry

Date: 2026-11-06. Status: AUTHOR-DERIVED EXACT ALGEBRA / 428-PRIME FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific input c47e13e4aba0e006366f989d6334d443f6333ae3; research logical lane chatgpt-research-hourly-enterprise-math-20260923. Previous four-jet, q^2 Lucas, diagonal palindrome and original-216 bridge are inherited, not recredited.

## Exact theorem for every prime q >= 5

Set n0=(q^2-1)/6, r=n0 mod q, s_i=i*r mod q (i=2,3,4; residues 0..q-1) and a=-1/2 in F_q. For every 0<=j<q define the finite polynomial/rational germ

M_j(t)=a^j * product_{i=2,3,4} binom(s_i+t,j) * j!/(1-3t)_j.

Its denominator is a unit at t=0. Write u_j=M_j(0), e_j=M_j'(0), Z=sum_j u_j, L=sum_j(6j+1)u_j, S=sum_j(6j+1)e_j in F_q. For the previous four-parameter jet D_2,D_3,D_4,D_alpha, the chain rule proves

S = D_2 + D_3 + D_4 - 3*D_alpha.

The inherited oriented signed carry B therefore obeys the exact new two-register representation

B = 6Z + (H_{s_2}+H_{s_3}+H_{s_4}-phi_q(2))*L - S (mod q),

where H_m=sum_{h=1}^m h^{-1}, phi_q(2)=(2^(q-1)-1)/q mod q. If L=0 mod q, this reduces to B=6Z-S.

The inherited diagonal q^2 criterion and original-216 bridge, under L=0 and W_q=0 mod q, now give

q^2 divides C_{(q^2-1)/6} iff Z*Theta_q=0 mod q,
Theta_q = W_q/q - Z + S/6 mod q.

This is an exact equivalent observer reduction; Theta_q=0 universally is still an open evaluation problem, not established by the theorem.

## Proof and finite-ring algorithm

For j=0,...,q-2 write t_i=s_i-j, P=t_2*t_3*t_4, Q=t_2*t_3+t_2*t_4+t_3*t_4. The exact quotient

M_{j+1}(t)/M_j(t)=a*product_i(s_i+t-j)/[(j+1)^2*(j+1-3t)]

has value c_j=aP/(j+1)^3 and derivative d_j=a[Q+3P/(j+1)]/(j+1)^3 at t=0. Hence, with u_0=1,e_0=0,

u_{j+1}=c_j*u_j,
e_{j+1}=c_j*e_j + d_j*u_j.

This holds as polynomial identities, including positions where u_j=0. Denominators j+1<q are always invertible. Accumulate Z,L,S in O(q) field operations and O(1) working field elements for fixed three channels; no division by u_j and no explicit harmonic/carry loops. P,Q, Z,L,S are symmetric in the three s_i, while labelled D_i remain available to retain per-channel BRC provenance. Substituting (x_2,x_3,x_4,alpha)=(t,t,t,-3t) into the previous F and applying the chain rule proves S=sum D_i-3D_alpha; insertion into the previous exact B-jet formula completes the proof.

## Independent exact finite checks

The accompanying Python integer/finite-field program independently implements (i) the two-register directional recurrence, (ii) the full four-partial-derivative recurrence, and (iii) the original 216 W_q recurrence modulo q^2. All 428 primes 5<=q<=3000 pass scalar-versus-four-jet, B-port, first-digit, and finite Theta checks; 211 have Z!=0 and 217 have Z=0. Separately written Node implementation independently checks scalar/four-jet equality for all the same 428 primes (428 PASS).

Examples (q; Z,L,S,B,W_q/q,Theta): (5; 3,0,4,4,4,0); (13;0,0,7,6,1,0); (19;0,0,13,6,1,0); (373;0,0,367,6,1,0); (1009;482,0,868,6,1,0); (2003;512,0,1075,1997,2002,0). This is exact finite evidence, not an all-prime proof of Theta_q=0.

## Next exact unit and control boundary

Prove or refute Theta_q=0 for the Z!=0 branch by parameter reflection, contiguity or a signed creative telescoper for W_q/q against the one-directional jet; preserve the three original carry channels when lifting back to BRC. After a certified relation, re-use the earlier prime-square transport and separately return to D25 frozen LIFT Delta_p-R_p (p=13,19 mod24). Native p373 H0/B0, [X]U mod139129, Frobenius direction/eta/kappa, signed odd branch, and independent review are still open.

At latest read Source d50e364c686414f6afc5c8783a462f8ccd57acd7 the D25 native checkpoint was SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED; HANDOFF_READY, NO_LIVE_CLAIM, execution_authorized=false. Recovery route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION. This tool surface did not expose callable recovery_status/session_preserve_staging for old service-session protected staging, so no session switch, CLAIM, OPEN, Result, or native checkpoint was undertaken. This report is author-side portable research evidence only.