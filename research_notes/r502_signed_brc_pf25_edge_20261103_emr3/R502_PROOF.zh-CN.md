# R502 — signed BRC 辅助标量：二十五阶右缘 Toeplitz 子式全参数符号分类

Date: 2026-11-03. Mathematical status: AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE; DRIVER_UNREVIEWED; NOT_ADMITTED.
Frozen scientific input: R462 at 18783e01e3646c72b7aab3b16d3f565e83e6446f.
Immediate predecessor: R501 at 3be6d6c7f2686c08a5e0a25f12ab4f8dddcf0068.
Current behavioral rules were read separately. P000 and ACTIVE worldview are unchanged.

## Precise statement

For each positive integer k put r=2k+1 and C_k=binom(2k,k)/(k+1)>0. For integers 2<=t<=r define

H_k(t)=binom(r+t,2t) [x^r]((1-x)(1+x)^(2t)(1+x^2)^(r-t)),

and set H_k(t)=0 otherwise. Define

D_m(k)=det [ H_k(3+i-j) ] for 0<=i,j<m.

**Theorem R502.** D_25(k)>0 for every integer 1<=k<=9, and D_25(k)<0 for every integer k>=10. The first negative odd parameter is r=21, and D_25 is negative for every odd r>=21.

In combination with R501, D_24(k)>0>D_25(k) for 10<=k<=18. For k>=19 both ranks 24 and 25 are negative. These are statements about the frozen signed BRC scalar observer.

## Reduction to one integer-polynomial identity

Reuse the already verified R452/R462 EOR identity: for fixed t, p_t(k)=H_k(t)/C_k belongs to Q[k] and deg p_t<=2t. In the Hessenberg Toeplitz determinant put f_m(k)=D_m(k)/C_k^m. Then

f_0=1,  f_m=sum_(ell=1)^m (-1)^(ell-1) p_(ell+2)(k) p_2(k)^(ell-1) f_(m-ell)(k).

Induction gives deg f_m<=6m, since the ell-th term has degree <=(2ell+4)+4(ell-1)+6(m-ell)=6m. In particular deg f_25<=150.

Let G_25(k)=k^25(k+1)^25(k+2)(2k+1)^25(2k+3)^25, with deg G_25=101. It is strictly positive for every k>=1.

Evaluate the exact rational f_25(k)/G_25(k) for k=1,...,50. Let L>0 be the least common multiple of the reduced denominators, and let delta_j be the j-th forward difference at k=1 of the resulting 50 integers L*f_25(k)/G_25(k). Define

S(k)=sum_(j=0)^49 delta_j * binom(k-1,j).

Every delta_j and the exact value of L are in R502_EVIDENCE.json. By construction S has degree <=49 and agrees with the scaled data at k=1,...,50.

The executed arbitrary-precision verifier checks the exact identity

L*D_25(k) = C_k^25 * G_25(k) * S(k)

at each of 151 distinct integers k=1,...,151. Cancelling C_k^25, the two rational polynomials L*f_25(k) and G_25(k)*S(k) both have degree <=150. Their 151 equal values prove equality as polynomials over Q, not merely over the checked grid.

## Complete sign certificate

The 9 exact integers S(1),...,S(9) are all positive, as recorded in the evidence.

For the infinite tail, compute the 50 forward differences epsilon_j=Delta^j S(10) at origin 10. The exact expansion is

S(10+u)=sum_(j=0)^49 epsilon_j*binom(u,j).

Every epsilon_j is a strictly negative integer. The largest, nearest zero, is -191744502769392854617000302878661700079234013752476743014508640968042071186011293158352905822244864. Thus for each integer u>=0, all binom(u,j)>=0 and epsilon_0<0, giving S(10+u)<0. Since L,C_k and G_25(k) are positive, the asserted signs of D_25 follow.

## Actual checks and provenance

Executing R502_VERIFY.js using JavaScript BigInt returned R502_EXACT_JS_PASS. It checked 151 polynomial evaluation identities, 20 independent 25x25 Bareiss determinants (k=1..20), and 520 original signed-BRC convolution / ballot-Catalan equalities (k=1..20,t=2..27). All these comparisons use integers and exact division. R502_EVIDENCE.json contains L, all 50 initial Newton coefficients, all 9 positive boundary integers, all 50 strictly negative shifted coefficients, and coverage/counts.

Independent local SymPy matrix determinant evaluation using the separate Catalan/ballot expression at k=1,9,10,15 confirmed signs +,+,-,-; the short independent program is stored as R502_INDEPENDENT.py. The universal conclusion relies on the inherited polynomial theorem, the 151-point equality and the complete tail sign certificate. No formal machine-theorem checker run or independent Driver acceptance is asserted.

## Exact next problem

Compute rank m=26 at s=3 on this same frozen input and classify all integer k>=1. Alongside this, factor the fixed-k rational rank generating-function denominator for k=9,10,19 to study the change of dominant poles between consecutive ranks. Preserve signed branch cancellation and the auxiliary-scalar observer distinction.