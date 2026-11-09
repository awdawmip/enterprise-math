# D25 AF4: grade-two first jet from factorial blocks (fourth-digit input)

2026-11-09 (Asia/Hong_Kong). TASK_RESEARCH / AUTHOR_PROVED / EXACT_REGRESSION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923`. Follow-up to the separately published grade-three AF4 reciprocal-tail certificate.

## Exact prime-factorial first-jet lemma

Let p>3 be prime, 0<=a<p, 0<=r<p, k=ap+r. In Z/p²Z define the Wilson quotient w_p=((p-1)!+1)/p mod p and harmonic H_r=sum_{i=1}^r 1/i mod p (H_0=0). Then

\[
\boxed{\frac{k!}{p^a}\equiv (-1)^a a!\,r!\,[1+pa(H_r-w_p)]\pmod{p^2}.}\tag{FB1}
\]

Proof: separate multiples p,2p,...,ap from k!, leaving complete blocks (bp+i), 0<=b<a, 1<=i<p, and partial block (ap+i), 1<=i<=r. The exact identity over p-adic units is
\[
\frac{k!}{p^a}=a!((p-1)!)^a r!\prod_{b=0}^{a-1}\prod_{i=1}^{p-1}(1+bp/i)
\prod_{i=1}^r(1+ap/i).
\]
Every complete-block factor equals 1 mod p² because H_{p-1}=0 mod p. Wilson's theorem gives ((p-1)!)^a=(-1)^a(1-apw_p) mod p². The partial block is 1+apH_r mod p². Multiplying proves (FB1). No floating-point or factorial approximation.

## Original W216 and V2304 grade-two coefficient units

For 0<=n<p define A_n=(2n)!(3n)!/((n!)^5 216^n), C_n=(4n)!/((n!)^4 2304^n), and retain the exact original weights (6n+1) and (8n+1). The second valuation grade has:
- W216: p/2<n<2p/3, hence a=floor(2n/p)=b=floor(3n/p)=1, r2=2n-p, r3=3n-p;
- V2304: p/2<n<3p/4, hence c=floor(4n/p)=2, r4=4n-2p.

Define the explicit p²-unit bases (factorial divisions are invertible at n<p):
\[
 B^W_n=\frac{(2n-p)!(3n-p)!}{(n!)^5 216^n}\pmod{p^2},\qquad
 B^V_n=\frac{2(4n-2p)!}{(n!)^4 2304^n}\pmod{p^2}.
\]
The exact fourth-digit input, derived by applying (FB1) to the original factorials, is
\[
\boxed{\frac{A_n}{p^2}\equiv B^W_n[1+p(H_{2n-p}+H_{3n-p}-2w_p)]\pmod{p^2},}
\]
\[
\boxed{\frac{C_n}{p^2}\equiv B^V_n[1+2p(H_{4n-2p}-w_p)]\pmod{p^2}.}\tag{G2-JET}
\]
Thus put W2^0=sum_{grade2}(6n+1)B^W_n mod p²,
W2^1=sum_{grade2}(6n+1)(B^W_n mod p)(H_{2n-p}+H_{3n-p}-2w_p) mod p, and similarly V2^0,V2^1 with 2(H_{4n-2p}-w_p). Their **original weighted grade-two sums** satisfy:
\[
W_{2,p}/p^2\equiv W2^0+p\,W2^1\pmod{p^2},\qquad
V_{2,p}/p^2\equiv V2^0+p\,V2^1\pmod{p^2}.
\]
This carries the formerly hidden first harmonic/Wilson jet in a direct, p-adic-unit-preserving representation of the actual grade-two sum.

## Independent exact arithmetic regression

For each listed prime, an independent original-binomial evaluation of W2,V2 modulo p⁴ was compared to (G2-JET), entirely in integers. All 10 p passed, including both frozen classes 13 and 19 modulo 24.

| p | w_p mod p | W2^0 mod p² | W2^1 mod p | W2/p² mod p² | V2^0 mod p² | V2^1 mod p | V2/p² mod p² |
|---:|---:|---:|---:|---:|---:|---:|---:|
|13|0|140|8|75|39|0|39|
|19|2|218|16|161|266|11|114|
|37|7|834|36|797|148|8|444|
|43|13|594|20|1454|0|17|731|
|373|224|96873|298|68898|25737|165|87282|

At p=373, the grade-two affine contribution modulo p⁴ is p²(68898-2*87282)=p²*33463 (mod p⁴). Its first-jet correction is (298-2*165)=341 (mod373); this is a nonzero fourth-digit observer. It must be combined with the grade-one second jet, grade-zero third jet and the separately established grade-three reciprocal channel L373=40 before claiming AF4.

## Provenance / next exact action

This is a new *application to the fourth-digit graded source observer* of the elementary factorial block expansion, not a new claim about the historical grade-two mod-p companion. It does not claim the universal AF4 conjecture or the native H0/B0 module.

Next: derive the corresponding grade-one second jet (units modulo p³) and grade-zero third jet (units modulo p⁴) from the same exact block product, so that lower-grade E<=2/p³ can be evaluated without recomputing raw high-index binomials. Attempt a WZ/Fricke proof of its cancellation against the already proved signed L_p for both frozen p classes. Independent native #1559 remains OPEN / PENDING_OWNER.
