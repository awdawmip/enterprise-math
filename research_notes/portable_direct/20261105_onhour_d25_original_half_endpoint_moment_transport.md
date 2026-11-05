# D25 SECOND-DIGIT-LIFT — signed half-endpoint factorial-unit and moment transport

Date: 2026-11-05. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3.
Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923. Classification: AUTHOR-SIDE EXACT DERIVATION / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED. Native original-class fixed-373 H0/B0 [X]U experiment NOT_EXECUTED (Issue #1559).

## Consumed results and original signed branches

Guo–Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019), 329–358, arXiv:1803.01830v6, prove both full and half-truncated 2304 Ramanujan sums congruent to p*(-3/p) mod p^3 for all p>3. We consume, rather than reprove, their theorem and previously known vanishing of the weighted 2304 upper shell.

For each prime p>3 let H=(p-1)/2 and define original rational coefficients
a_k=binom(2k,k)^2 binom(3k,k)/216^k=(2k)!(3k)!/(216^k(k!)^5);
b_k=binom(2k,k)^2 binom(4k,2k)/2304^k=(4k)!/(2304^k(k!)^4).
Let W_p=sum_{k=0}^{p-1}(6k+1)a_k, V_p=sum_{k=0}^{p-1}(8k+1)b_k, and W_H,V_H the respective sums from 0 through H.

Define the original upper p^2 valuation-band *factorial units* in F_p:
A_p(k)=(2k-p)!(3k-p)!/[216^k(k!)^5],  H<k<=floor((2p-1)/3);
B_p(k)=2(4k-2p)!/[2304^k(k!)^4], H<k<=floor((3p-1)/4).
Define the signed, branch-preserving observers
C_A=sum(6k+1)A_p(k) over A band;
M0=sum B_p(k), M1=sum k B_p(k) over B band.

## Proven theorem (all primes p>3)

(i) a_k/p^2 ≡ A_p(k) mod p on the A band, and b_k/p^2 ≡ B_p(k) mod p on the B band.
(ii) M0+8*M1 ≡ 0 mod p.
(iii) W_p-V_p ≡ W_H-V_H+p^2*C_A mod p^3.

Proof: For 0<=k<p, v_p(a_k)=floor(2k/p)+floor(3k/p), v_p(b_k)=floor(4k/p), since 216 and 2304 are p-units. For 0<=q<p,0<=r<p Wilson block decomposition yields (qp+r)!/p^q ≡ (-1)^q q! r! mod p: q complete nonmultiple-of-p blocks contribute (-1)^q, q multiples contribute q!, remaining r terms contribute r!. On the A band the two numerators each have q=1, hence the sign cancels and unit factor 1. On the B band 4k has q=2, hence factor +2. All later terms have valuation >=3. Thus W_p-W_H ≡ p^2*C_A and V_p-V_H ≡ p^2*(M0+8*M1) mod p^3. Guo–Zudilin prove V_p≡V_H≡p*(-3/p) mod p^3, giving (ii), and subtraction gives (iii). No extrapolation from finite checks enters this proof.

The B weighted vanishing itself is PREEXISTING; the new useful presentation is the explicit exact factorial-unit zero-order/first-moment pair with original k labels and its use in the same-half-endpoint source-preserving transport. For p=13, M0=7 and M1=4 are individually nonzero, whereas M0+8*M1=39≡0 mod13. The signed readout cannot be replaced by two separate zero assertions.

## Precise remaining target

On target p≡13,19 (mod24), prior accepted first-digit/source results ensure p^2 divides W_H-V_H. Write E_p=((W_H-V_H)/p^2) mod p. Consuming the existing original-source equality Delta_p-R_p=(W_p-p)/p^2 modp and Guo–Zudilin V_p≡p modp^3, the frozen parent target is equivalent to exactly
                     E_p + C_A ≡ 0 mod p.
This is a proved equivalence, NOT yet a uniform proof of the right-hand identity. It is a more focused finite half-endpoint 216-to-2304 transform target, retaining both weighted source ports and the 216 valuation-two shell.

## Executed exact check, arithmetic meaning

The companion checker independently forms factorial-unit moments and original p^4 modular recurrence coefficients for every prime 5<=p<=997 (166 primes; 45 in the target classes); all identities passed. Independent original binomial coefficient calculations separately matched W,V,W_H,V_H modulo p^4 for p=7,13,19,139,373. In the 45 target-prime window, the conjectural E_p+C_A=0 also passed (FINITE evidence only).

| p | M0 | M1 | C_A | E_p | E_p+C_A modp |
|---:|---:|---:|---:|---:|---:|
| 13 | 7 | 4 | 10 | 3 | 0 |
| 19 | 14 | 3 | 9 | 10 | 0 |
| 139 | 27 | 14 | 13 | 126 | 0 |
| 373 | 63 | 132 | 266 | 107 | 0 |

BRC usage: COMPOSE_APPLIED. Carrier (M0,M1) has finite-field signed first moments, labeled model A/B, p-adic valuation 2, explicit weight and future operation M0+8M1. Keeping both moments explains cancellation; zero final weighted tail alone discards causal algebraic information. The p373 arithmetic is PORTABLE, not native H0/B0 divided-power Frobenius.

## Continuation and unresolved independent native benchmark

Next exact mathematical action: construct a p-parametric TERMINATING half-endpoint 216↔2304 WZ/transformation certificate proving E_p=-C_A on the frozen classes; retain A shell and B signed moment until the established B cancellation is invoked, and test boundary normalization at p=13/19 first.

Native support Issue #1559 still seeks original same-class p373 divided-power H0/B0 and [X]U mod139129, module rank, semilinear direction/eta, kappa, odd Green/Hesse observer and independent replication; no executor was assigned in the last observed issue. This report is not a native benchmark, Source checkpoint, formal Result or mathematical review.

Last succeeded Source continuation: onhour11-20261105-1405-d25-cont (execution_authorized=false). New same-lane read onhour11-20261105-1505-d25-own-read QUEUED at last check; reconcile that original request ID, do not repeat its mutation. No native session/key, CLAIM or run in this lane is asserted.
