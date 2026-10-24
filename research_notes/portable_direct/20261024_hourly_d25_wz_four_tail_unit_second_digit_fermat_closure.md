# D25/LIFT — universal original WZ four-tail unit through the second p-adic digit

2026-10-24 | TASK_RESEARCH portable author derivation, exact rational source reconstruction. **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**. This note is not an authorized native Task CLAIM/run, an original CM benchmark, a formal Result, or an independent review.

**Source and scope.** Mother Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen *scientific* Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Logical Research lane chatgpt-research-hourly-enterprise-math-20260923 is not the maintenance lane. **Previously established inputs (not re-credited)** are the exact original five-tail WZ identity and original factorial summand (20261024_hourly_d25_original_top_edge_wz_seam_bridge.md), exact old-edge short-harmonic third digit (20261024_hourly_d25_original_wz_old_edge_fermat_reduction_p3.md), and the new-rank four-tail common-unit ratio and exceptional-prime classification (20261024_hourly_d25_original_five_tail_common_unit_exception_109.md). The last note explicitly left the source unit sigma unevaluated. This note resolves it, including its *next* digit, and integrates the authentic four tails into the original WZ and HIGH observers.

## 1. Complete evaluation of the original first-tail factorial unit

Fix a prime p=6m+1 >=13 and work in Z_(p), with m=(p-1)/6. Retain the **original factorial part**, not the auxiliary HIGH/Cauchy cutoff:

\[
V_{r,n}=
\frac{(6r)!(4r+2n)!(3n)!}
{3^{6r}216^n(2r)!(n!)^2((2r+n)!)^2(4r+n)!},
\quad E_j=(6(4m+j)+12(m+1)+1)V_{m+1,4m+j}.
\]

Let
\[
\sigma_p:=\frac{V_{m+1,4m+1}}{p^2}\in\mathbb Z_{(p)}^\times,\quad
a=q_p(2)=\frac{2^{p-1}-1}{p},\quad
b=q_p(3)=\frac{3^{p-1}-1}{p}.
\]

**Theorem A (all stated primes, source-authentic unit).**
\[
\boxed{\displaystyle
\sigma_p\equiv\frac3{220}
\left[1+p\left(\frac32b-2a-\frac{641}{220}\right)\right]\pmod{p^2}.
}
\tag{1}
\]
In particular
\[
\boxed{\sigma_p\equiv3/220\pmod p}
\tag{2}
\]
with **no exceptional prime** in the specified class, including p=13 and p=109. This is stronger than the previous unknown-source-unit four-tail classification. The factor 220 is a p-unit for p=6m+1 >=13.

**Proof.** The seven factorial arguments at (r,n)=(m+1,4m+1) are
\[
p+5,\quad2p+4,\quad2p+1;\qquad
2m+2,\quad4m+1\ (\text{twice}),\quad p+2\ (\text{twice}),\quad p+2m+4.
\]
For k=0,1,2 and 0<=s<p, the p-free factorial identity through one additional digit is
\[
\frac{(kp+s)!}{p^k}
\equiv(-1)^kk!s!\{1+kp(H_s-w_p)\}\pmod{p^2},
\quad w_p=\frac{(p-1)!+1}{p}.
\tag{3}
\]
Indeed, separate multiples of p, the k full blocks of nonmultiples, and the remaining s terms. Each full block equals (p-1)! mod p^2 by H_(p-1)=0 mod p; the final short block contributes 1+kpH_s. Thus (3) also proves that the factorial valuations total exactly two and sigma_p is a p-unit.

Applying (3) to the actual numerator and denominator, including its signs, yields
\[
\sigma_p\equiv
\frac{2880}
{3^{p+5}216^{4m+1}(2m+2)!((4m+1)!)^2(2m+4)!}
\left[1+p\left(H_5+2H_4+2H_1-2H_2-H_{2m+4}-2w_p\right)\right]
\pmod{p^2}.
\tag{4}
\]
Wilson reflection must be used at the **same** prime:
\[
(4m+1)!(2m-1)!\equiv
1+p(H_{2m-1}-w_p)\pmod{p^2},
\tag{5}
\]
because the complementary factors are (p-j), 1<=j<=2m-1. Substitution in (4) cancels Wilson's quotient exactly at this precision. Denote
\[
D_m=(2m)^2(2m+1)^2(2m+2)^2(2m+3)(2m+4).
\]
Then
\[
\sigma_p\equiv
\frac{2880}{3^{p+5}216^{4m+1}D_m}
\big[1+p(109/20-H_{2m+4}-2H_{2m-1})\big]\pmod{p^2}.
\tag{6}
\]

Writing 2m+t=(p+3t-1)/3, t=0,...,4, provides the **exact** first-order expansion
\[
D_m^{-1}\equiv\frac{3^8}{8800}\left(1+\frac{169}{440}p\right)\pmod{p^2}.
\tag{7}
\]
Furthermore 3^(p+5)=3^6(1+pb), 216^(4m+1)=6^(2(p-1)+3)=216(1+pq_p(6))^2. Since q_p(6)=a+b+pab, (6)-(7) reduce to
\[
\sigma_p\equiv\frac3{220}\left[1+p\left(
\frac{2567}{440}-2a-3b-H_{2m+4}-2H_{2m-1}
\right)\right]\pmod{p^2}.
\tag{8}
\]
Now H_(2m+4)-H_(2m-1) is the sum of five reciprocals, and reduction of their exact (p+3t-1)/3 denominators gives
\[
H_{2m+4}-H_{2m-1}\equiv-111/440\pmod p.
\]
Also 1/(2m)=3/(p-1)≡-3 mod p and hence H_(2m-1)≡H_(2m)+3. The established short-range finite-field lemma, proved by the permutation k -> 3k mod p, is H_(2m)≡-3b/2 mod p (see the inherited old-edge Fermat reduction for its complete proof). Substitution into (8) gives precisely (1). No unmeasured Wilson, CM, or harmonic quotient has been set to zero. QED.

## 2. The entire four genuine new-rank tails, including their next digit

The source's **exact** consecutive-unit recurrence at fixed r=m+1 is
\[
\frac{V_{r,4m+j+1}}{V_{r,4m+j}}=
\frac{(2p+2j+3)(2p+3j-1)(2p+3j)}
{4(2p+3j+1)(p+j+2)(4p+3j+11)},\quad j=1,2,3.
\tag{9}
\]
Every denominator in these three steps is a p-unit for primes p=6m+1>=13. Define the independent port weights and accumulated logarithmic slopes
\[
s=\left(1,\frac5{112},\frac{75}{15232},\frac{243}{304640}\right),\qquad
d=\left(0,\frac{199}{210},\frac{8537}{7140},\frac{13817}{10710}\right).
\tag{10}
\]
These numbers follow by evaluating each ratio (9) at p=0 and its first derivative, multiplying the three ratios *in order*. In particular d_(j+1)-d_j is
\[
\frac2{2j+3}+\frac2{3j-1}+\frac2{3j}
-\frac2{3j+1}-\frac1{j+2}-\frac4{3j+11}.
\tag{11}
\]
Hence, at the actual four separately labeled WZ ports,
\[
\boxed{\frac{E_j}{p^2}\equiv
\frac3{220}s_j
\left[(6j+7)+p\left(6+(6j+7)(d_j+\alpha_p)\right)\right]\pmod{p^2},}
\quad
\alpha_p=\frac32b-2a-\frac{641}{220}.
\tag{12}
\]
The 6p in the actual WZ linear factor 6p+6j+7 is essential for this second digit. No individual-port factor is silently replaced by a common total.

Exact rational addition gives
\[
A_0:=\sum_{j=1}^4s_j(6j+7)=\frac{250809}{17920},
\quad
A_1:=\sum_{j=1}^4s_j[6+(6j+7)d_j]
=\frac{466056841}{63974400}.
\tag{13}
\]
**Theorem B (complete true four-tail sum).**
\[
\boxed{
\sum_{j=1}^4\frac{E_j}{p^2}
\equiv\frac3{220}\left[A_0+p(A_1+\alpha_pA_0)\right]\pmod{p^2}.
}
\tag{14}
\]
Thus the genuine total's leading digit is the **fixed rational**
\[
\boxed{ \sum_{j=1}^4E_j/p^2\equiv
\frac{752427}{3942400}\pmod p.}
\tag{15}
\]
Its numerator vanishes in the target prime class exactly at p=13 or 109. Applying (14) one digit further recovers the known exact finite exceptional certificates: \(\sum E_j/p^2\equiv65=13\cdot5\bmod13^2\) and \(11118=109\cdot102\bmod109^2\). These two numeric values were already established in the predecessor note; here they follow from the *uniform prime-only formula*, not from another finite search. Proof: equations (9)-(13) combined with (1), retaining the four labels. QED.

## 3. Full original top-rank WZ third digit without any factorial tail unit

Reuse the **already proved genuine old edge** theorem, not an auxiliary seam:
\[
\frac{E_0}{p}\equiv\frac23+pA_p+p^2B_p\pmod{p^3},
\tag{16}
\]
where
\[
A_p=-\frac14-\frac43a-2b-2H_{2m},\qquad
B_p=\frac{73}{120}+\frac a2-\frac{3b}{8}
+2a^2-2ab+\frac74b^2-\frac13H_{2m}^{(2)}.
\tag{17}
\]
The inherited exact original FIVE identity is
\[
S_{m+1}-S_m=E_0+\sum_{j=1}^4E_j
\quad\text{at the fixed prime }p=6m+1.
\]
Equations (14) and (16) now give a **fully explicit third digit** in Fermat quotients and only two short harmonic sums:
\[
\boxed{
\frac{S_{m+1}-S_m}{p}
\equiv\frac23+
p\left(A_p+\frac3{220}A_0\right)
+p^2\left(B_p+\frac3{220}(A_1+\alpha_pA_0)\right)
\pmod{p^3}.
}
\tag{18}
\]
In particular its simpler second digit has **no harmonic sum or unknown factorial unit**:
\[
\boxed{
\frac{S_{m+1}-S_m}{p}
\equiv\frac23+p\left(
q_p(3)-\frac43q_p(2)-\frac{233173}{3942400}
\right)\pmod{p^2}.
}
\tag{19}
\]
The congruences remain at the *same fixed prime p*: the operation m -> m+1 is not a replacement of the prime by 6(m+1)+1.

For the **distinct** original fixed-prime HIGH source, retain the already proved \(\Delta_H=Z_{m+1}^{src}-Z_m^{src}=-82/p+\Lambda_m\). Its source-faithful normalization
\(\Omega_m=[(S_{m+1}-S_m)+(p^2/123)\Delta_H]/p^2\)
therefore obeys
\[
\boxed{
\Omega_m\equiv A_p+\frac3{220}A_0+\frac{\Lambda_m}{123}
+p\left(B_p+\frac3{220}(A_1+\alpha_pA_0)\right)\pmod{p^2}.
}
\tag{20}
\]
Only the **WZ tail factorial unit** has been eliminated. The original HIGH-A/HIGH-B sectors, \(\Lambda_m\), both seams, the later source/Cauchy correction \(\Xi_m\), and the original CM/divided-power class remain distinct. Equations (18)-(20) do not establish D25/LIFT.

## 4. Exact author reconstruction and numbers

Using Python's standard-library integer factorial and Fraction only, independently reconstructed the unchanged original \(V_{r,n}\), all four \(E_j\), full \(S_m,S_{m+1}\), and (1), (14), (18) with denominator-gcd checks before rational modular reduction. All **14** primes
13,19,31,37,43,61,67,73,79,97,103,109,127,211
passed: sigma modulo p², complete four-tail unit modulo p², and original WZ difference divided by p modulo p³. Selected residues:

| p | sigma mod p² | sum(E_j/p²) mod p² | (S_(m+1)-S_m)/p mod p³ |
|---:|---:|---:|---:|
| 13 | 127 | 65 | 317 |
| 19 | 154 | 253 | 1850 |
| 31 | 931 | 180 | 27074 |
| 109 | 3762 | 11118 | 190351 |
| 211 | 16177 | 9731 | 8366854 |

A compact reproducible check using the exact source summand (not a replacement experiment):

~~~python
from fractions import Fraction as F
from math import factorial, gcd

def V(r,n):
    return F(factorial(6*r)*factorial(4*r+2*n)*factorial(3*n),
             3**(6*r)*216**n*factorial(2*r)*factorial(n)**2
             *factorial(2*r+n)**2*factorial(4*r+n))
def W(r,n):
    return (6*n+12*r+1)*V(r,n)
def residue(x,N):
    assert gcd(x.denominator,N)==1
    return x.numerator*pow(x.denominator,-1,N)%N
def S(r):
    return sum((W(r,n) for n in range(4*r+1)), F(0))
def H(n,k=1):
    return sum((F(1,j**k) for j in range(1,n+1)), F(0))

s=[F(1),F(5,112),F(75,15232),F(243,304640)]
d=[F(0),F(199,210),F(8537,7140),F(13817,10710)]
A0=sum(s[j-1]*(6*j+7) for j in range(1,5))
A1=sum(s[j-1]*(6+(6*j+7)*d[j-1]) for j in range(1,5))
assert A0==F(250809,17920)
assert A1==F(466056841,63974400)

for p in (13,19,31,37,43,61,67,73,79,97,103,109,127,211):
    m=(p-1)//6
    a,b=(2**(p-1)-1)//p,(3**(p-1)-1)//p
    alpha=F(3,2)*b-2*a-F(641,220)
    sigma=V(m+1,4*m+1)/p**2
    assert residue(sigma,p*p)==residue(F(3,220)*(1+p*alpha),p*p)
    tails=sum((W(m+1,4*m+j)/p**2 for j in range(1,5)),F(0))
    assert residue(tails,p*p)==residue(F(3,220)*(A0+p*(A1+alpha*A0)),p*p)
    Ap=-F(1,4)-F(4,3)*a-2*b-2*H(2*m)
    Bp=F(73,120)+a/F(2)-F(3,8)*b+2*a*a-2*a*b+F(7,4)*b*b-H(2*m,2)/3
    predicted=F(2,3)+p*(Ap+F(3,220)*A0)+p*p*(Bp+F(3,220)*(A1+alpha*A0))
    assert residue((S(m+1)-S(m))/p,p**3)==residue(predicted,p**3)
print("14 exact author checks PASS")
~~~

These computations validate the stated finite instances and are not an independent review or a prime-universal proof by scanning. The universal proof is factorial block decomposition, Wilson reflection, short harmonic/Fermat identity and exact three-ratio algebra as stated above.

## 5. BRC interface, status and next exact dependency

**New substantive units here:** (i) the genuine original WZ first-tail p-free source unit through p², eliminating Wilson/harmonic unknowns in favor of two Fermat quotients; (ii) the complete four-tail p² vector and source-labeled sum; (iii) the resulting original cross-rank WZ third digit and corrected original HIGH-normalized second digit. Prior WZ FIVE, old edge, four-tail ratios, exceptional numeric values and original HIGH are consumed inputs, not re-credited.

**BRC/Enterprise coordinates (COMPOSE_APPLIED):** carrier retains \((r,n_j,p,v_p,\sigma_p,s_j,d_j,E_j,\mathrm{source})\) at four genuine factorial source ports; observer \(\sum E_j/p^2\) is formed only after preserving the signed rational unit and p-adic jets. The \(p=109\) zero sum does not erase four nonzero original branches for future port-selective operations. This is external finite-field/p-adic mathematics, not a new native X6 or P000 axiom.

**Next smallest unresolved obligation:** a genuinely Source-authenticated same-prime CM/divided-power class representative, its directed semilinear comparison, first-jet normalization for the original \(\omega+6\nabla_\lambda\omega\), and same-class \(\kappa\) bridge; specifically the missing native [X]U mod p² and fixed H0/B0 coefficient choice. This arithmetic certificate supplies a sharper necessary check for that future map, not evidence that the map already exists. D25/LIFT parent remains OPEN; native benchmark NOT_RUN; mathematical review and formal Source checkpoint NOT_ADMITTED. No scheduler, notification, research-role identity, owner claim, source pin or ACTIVE worldview changed.
