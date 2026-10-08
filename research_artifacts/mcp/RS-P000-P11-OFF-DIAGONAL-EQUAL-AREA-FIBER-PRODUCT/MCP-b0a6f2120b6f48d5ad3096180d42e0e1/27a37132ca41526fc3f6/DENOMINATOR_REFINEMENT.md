# Increment 2 — exact minimal denominator on the fixed off-diagonal core

Researcher EM-P000-298FC9. Same task, claim and run as OFFDIAG_INCREMENT_1.md. This addendum strengthens the denominator/gcd port without a new Task or a new elliptic search. It does not enlarge the mathematical classification claim.

Write a rational point of the fixed cut curve
\[
d^2+\mu^2=1945,\quad d^2+\nu^2=265,\quad d>0
\]
as d=p/q with p,q positive coprime integers. Then
\[
r=q\mu,\quad s=q\nu
\]
are nonnegative integers because their squares are the integers 1945q^2-p^2 and 265q^2-p^2. A rational number whose square is an integer is an integer. Modulo 4, q even would force r^2=3 mod 4, so q is odd. If p is even, modulo 8 forces 4|p. If p is odd, both r and s are divisible by 4, since their squares vanish modulo 8. If p is even, r and s are odd.

Let N be the multiset of the following sixteen integer numerators:
\[
132q^2-p^2\pm41pq,\quad132q^2-p^2\pm29pq,
\quad132q^2-p^2\pm pq,
\]
\[
132q^2\pm rp,\quad132q^2\pm sp,
\]
\[
132q^2+p^2\pm47pq,\quad132q^2+p^2\pm37pq,
\quad132q^2+p^2\pm23pq.
\]
These are precisely the cell-labeled rational root numerators with common denominator 2pq. Put g=gcd{|n|:n in N}. Since the top c=1 pair differs by 2pq, g divides 2pq. Hence the least common denominator of all roots is exactly
\[
D=2pq/g. \tag{D1}
\]
The normalized integer roots are exactly n/g for n in N; their gcd is 1 by definition. This is the explicit reconstruction-level gcd, not a gcd of only the triangles or sums.

Set o=gcd(p,33). Then
\[
g=\begin{cases}
2o,&p\text{ odd},\\
8o,&v_2(p)=2,\\
4o,&v_2(p)\ge3.
\end{cases} \tag{D2}
\]
Consequently
\[
D=\begin{cases}
pq/\gcd(p,132),&p\text{ odd or }v_2(p)=2,\\
2pq/\gcd(p,132),&v_2(p)\ge3.
\end{cases} \tag{D3}
\]

**Odd-prime proof.** If an odd prime ell divides q, the top numerators are -p^2 modulo ell, hence ell does not divide g. If ell divides p, the difference 2pq gives v_ell(g)<=v_ell(p). If v_ell(p)<=v_ell(132), every numerator is divisible by ell^{v_ell(p)}, so equality holds. If v_ell(p)>v_ell(132), a top numerator has valuation exactly v_ell(132), since 132q^2 has that valuation and the other two terms have strictly larger valuation. Thus the odd part of g is exactly gcd(p,33); no other primes can divide g because g|2pq.

**Prime 2 proof.** The impossible case v_2(p)=1 has already been excluded. If p is odd, q is odd and every numerator is even; g|2pq forces v_2(g)=1. If v_2(p)=2, write p=4u with u odd. Dividing each numerator by 4 leaves odd plus or minus odd (and for outer rows an additional multiple of 4), so every numerator is divisible by 8. Since v_2(2pq)=3, v_2(g)=3. If v_2(p)>=3, a top numerator 132q^2-p^2 plus or minus a pq has valuation exactly 2, while all numerators are divisible by 4. Thus v_2(g)=2. This proves (D2) and (D3).

The same gcd identity holds for artificial integer p,q,r,s obeying only the displayed coprimality and parity restrictions; the proof uses no other cut equations. That is the precise scope of the small arithmetic regression in DENOMINATOR_REFINEMENT_PLAN.md. Such artificial inputs are not P11 solutions.

For any valid integer scale L of this fixed core, L must be an integer (the coprime legs 21 and 20 force this). It clears all roots iff D divides L. The full sixteen-root gcd is then L/D. The unique primitive scale is D, and its ordered factors, coupling sign, products, parity and zero roots are recovered exactly as in Increment 1.

No-repeat: the denominator/parity/gcd port for this fixed core is now explicit. Do not replace g by a triangle-only gcd, ignore the v_2(p)>=3 factor of two, or claim that artificial gcd-control inputs lie on the elliptic cut curve.
