# D25: The ordinary valuation-one first carry splits into two zero rectangular ports (2026-11-02)

**AUTHOR-DERIVED / CONDITIONAL EXACT PROOF / FINITE EXACT VERIFICATION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_NATIVE_H0_B0.** This is research evidence, not a native Source checkpoint or Result.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane: `chatgpt-research-onhour-enterprise-math-20260923`; maintenance lane is separate. D25 mother objective remains original `Delta_p-R_p=0 mod p` for primes `p=13,19 mod24`.

## Original statement and p-adic carrier

For primes `p>=5` set `k=ap+b` with `0<=a,b<p`. For each stream `J,d,lambda,j*` below, define `alpha_J(k)=prod_{j in J}(jk)! / ((k!)^(sum J) d^k)`, original weight `lambda*k+1`, `nu_J(k)=v_p(alpha_J(k))`:
- W216: `J=(2,3),d=216,lambda=6,j*=3`.
- S2304: `J=(4),d=2304,lambda=8,j*=4`.

Define `c_j=floor(jb/p)`, `q_j=floor((ja+c_j)/p)` and `delta_j=floor(((ja mod p)+c_j)/p)`. By Legendre, since `j*k<4p²<p³`,
`nu_J(ap+b)=sum_j(c_j+q_j)` exactly. The **ordinary** population has every `delta_j=0`; anomalous positive-valuation terms are retained separately.

Let `h=floor((p-1)/j*)`, `H=(p-1)/2`, `M0=sum_{b=0}^h alpha_J(b)`, `M1=sum_{b=0}^h b*alpha_J(b)` in `F_p`.

**Theorem (conditional on source-specific CM moments).** If `M0=M1=0 mod p`, then for each individual original stream,
`sum_{0<=k<p², nu_J(k)=1, all delta_j=0} (lambda*k+1)alpha_J(k)=0 mod p²`.
In fact each of two source-tagged subpopulations vanishes modulo `p²` separately; no W/S subtraction is used.

## Proof by explicit two-digit source factorization

Put `u_J(k)=p^(-nu_J(k))*alpha_J(k)` in `F_p^×`. Removing factorial p-blocks and applying Wilson gives, if all `delta_j=0`,
`u_J(ap+b)=u_J(ap)u_J(b)*prod_j binom((ja mod p)+c_j,c_j) mod p`.
The denominator `d` is a p-unit and `d^(-ap)=d^(-a) mod p`.

The ordinary valuation-one support is exactly two rectangles:

1. **L (one low-digit carry)** `0<=a<=h, h+1<=b<=H`: only `c_{j*}=1`, the other c and all q are zero. At an endpoint with `j*a+1=p`, that cell has an extra carry, is omitted from L, and contributes zero to the formal mod-p factor. Thus
`alpha_J(ap+b)/p = (j*a+1)*alpha_J(a)*[alpha_J(b)/p] mod p`.
After retaining the original signed weight, the total `L/p` equals
`(M0+j*M1)*sum_{b=h+1}^H (lambda*b+1)[alpha_J(b)/p]` in `F_p`.

2. **U (one high-digit carry)** `h+1<=a<=H,0<=b<=h`: all c vanish and only `q_{j*}=1`, so
`alpha_J(ap+b)/p=[alpha_J(ap)/p]*alpha_J(b) mod p`.
The total `U/p` equals
`(sum_{a=h+1}^H [alpha_J(ap)/p])*(M0+lambda*M1)` in `F_p`.

Both parenthesized moment factors vanish under the two stated hypotheses, proving separately `L=U=0 mod p²`. The premise `M0=M1=0` must come from an independent source-proved CM result for a universal conclusion; the nine tested primes verify it exactly on their finite domain.

## Two independent arithmetic executions and a new p=373 port split

Executed exact-integer scripts `d25_ordinary_v1_factorization_20261102.py` (p-free factorial-unit factorization) and `d25_positive_strata_20261102.py` (original weighted recurrence, independent full `k<p²` p-adic valuation). At `p=13,19,37,43,61,67,109,139,373`, **43,059** ordinary valuation-one source terms were individually factor-checked, with all expected moment and separate rectangle cancellations passing. Both original streams independently have ordinary valuation-one sums divisible by p² in all nine finite tests.

The fixed-373 original `W-2S+p²` p² digit splits further (all original source/sign data retained in corresponding local calculation JSON):

| component | W | S | signed W−2S |
|---|---:|---:|---:|
| ordinary valuation 0 | 284 | 257 | 143 |
| ordinary valuation 1, **second digit** | 111 | 201 | **82** |
| ordinary valuation 2, first digit | 265 | 61 | **143** |
| anomalous valuation >=2 | 87 | 228 | **4** |
| original +p² baseline | — | — | **1** |

Thus `143+82+143+4+1=373=0 mod373`. The earlier unresolved ordinary-positive-plus-baseline digit `226` is resolved into `82+143+1=226`. The `nu=1` *first* digits vanish separately by the proved conditional rectangular factorization. These finite raw calculations are not a native H0/B0 test.

**BRC / precision reuse:** The exact carrier `(model,a,b,c_j,q_j,delta_j,nu,original signed weight)` preserves branch provenance before the modulo-p³ additive readout; `T5_PRECISION_REFINEMENT` supplies the existing finite integer carry/detail law. This application is `REUSE_APPLIED` at its finite precision interface, not a new tool or native-X6 equivalence.

**Next smallest science unit:** Derive a one-dimensional moment/telescope for the **ordinary valuation-one second digit** (requires factorial units mod p²), then combine with the valuation-two ordinary first digit and the previously established val-zero and anomalous ports, and reconnect to the frozen original `Delta_p-R_p`. The p373 benchmark #1559 remains `PENDING_OWNER / NOT_EXECUTED`; original `[X]U mod139129`, actual H0/B0 rank, semilinear Frobenius/eta, signed odd Green/Hesse and independent verification are still required. The historical failed request `research-onhour-20261031-0205-dispatch-r15` is not reissued and confers no session, claim or run authority.
