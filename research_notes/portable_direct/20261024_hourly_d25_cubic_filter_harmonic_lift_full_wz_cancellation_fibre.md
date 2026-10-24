# D25/LIFT: cubic-filter harmonic lift and complete cancellation-fibre WZ third-digit reduction

2026-10-24 · TASK_RESEARCH portable author certificate · **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

## Identity, fixed scope, provenance

Research logical conversation: chatgpt-research-hourly-enterprise-math-20260923, separate from CONTROL_PLANE_MAINTENANCE. This note is **portable author mathematics**, not a canonical Task execution, CLAIM, authorized run, native CM experiment, Source checkpoint, independent review, or Result. Immutable scientific Source pin stays c47e13e4aba0e006366f989d6334d443f6333ae3. D25/LIFT mother objective remains OPEN.

Consume (do not recredit or replay) these previously published portable author derivations:
- prior third-digit shifted-Wieferich/character reduction: https://github.com/awdawmip/enterprise-math/blob/4f7169291a872467496de179666f456e67869749/research_notes/portable_direct/20261024_hourly_d25_shifted_wieferich_bernoulli_third_digit_reduction.md
- inherited original five-tail/source seam: https://github.com/awdawmip/enterprise-math/blob/a7f7995560ed30a6db081f3519ed5ee0d678a1bc/research_notes/portable_direct/20261024_hourly_d25_original_top_edge_wz_seam_bridge.md
- inherited four labeled tail units: https://github.com/awdawmip/enterprise-math/blob/df65eaf2df0c973b7f815090f5d74929005e8349/research_notes/portable_direct/20261024_hourly_d25_wz_four_tail_unit_second_digit_fermat_closure.md

**New mathematical increment:** a self-contained cubic-root-of-unity proof of the *mod-p-squared one-third harmonic lift*; it eliminates the formerly unevaluated harmonic lift h. On the exact second-digit cancellation fibre it also eliminates both Fermat-quotient coordinates, leaving an integer shifted-Wieferich quotient, a finite inverse-square harmonic sum (or one explicitly typed character-Bernoulli number), and a rational constant. This is not a bridge to the actual Source CM/divided-power representative.

## 1. Exact typed input and statement

Let p=6m+1 >= 13 be prime, n=(p-1)/3=2m, and work in the p-local ring Z_(p). Define the integer Fermat quotients

\[
a=q_p(2)=\frac{2^{p-1}-1}{p},\qquad b=q_p(3)=\frac{3^{p-1}-1}{p},
\]
\[
H=H_n=\sum_{j=1}^{n}\frac1j,\quad H_2=H_n^{(2)}=\sum_{j=1}^{n}\frac1{j^2},\quad h=\frac{H+3b/2}{p}.
\]

### Theorem A (all-target one-third harmonic lift)

\[
\boxed{H\equiv-\frac32b+p\left(\frac34b^2-\frac13H_2\right)\pmod{p^2}},
\qquad
\boxed{h\equiv\frac34b^2-\frac13H_2\pmod p.}                 \tag{A}
\]

In particular h is p-integral. The formula retains the summation domain n=(p-1)/3; it is not a replacement of H by a different full-period harmonic sum.

### Theorem B (fully collapsed cancellation fibre)

Let D=3942400, k=233173/D, and set the **integer**

\[
M_p=D\left(27^{p-1}-16^{p-1}\right)-699519\,p\,16^{p-1}.
\]

Write the original-source *fixed-prime moving-rank* WZ readout
\(F_p=(S_{m+1}-S_m)/p\).
Under its precisely inherited second-digit cancellation hypothesis

\[
p^2\mid M_p
\quad\Longleftrightarrow\quad F_p\equiv2/3\pmod{p^2},
\]

the following is a p-local **integer-defined third digit**:
\[
\eta_p=\frac{F_p-2/3}{p^2}
      =\frac{S_{m+1}-S_m-2p/3}{p^3}.
\]

Let
\[
C_{\rm final}=\frac{455695314072269}{3170673623040000}.
\]
Then
\[
\boxed{\eta_p\equiv\frac{M_p}{3Dp^2}+\frac13 H_2+C_{\rm final}\pmod p.} \tag{B}
\]

The quotient \(M_p/p^2\) in (B) is an actual integer only after checking the stated hypothesis. All rational denominators are p-units for primes p=6m+1 >= 13. By the already-derived character identity \(H_2\equiv\frac94B_{p-2,\chi_{-3}}\pmod p\), equation (B) is equivalently

\[
\boxed{\eta_p\equiv
\frac{M_p}{3Dp^2}
+\frac34 B_{p-2,\chi_{-3}}
+C_{\rm final}\pmod p.} \tag{B'}
\]

Thus **fourth-order cancellation for this declared WZ observer** is equivalent to the vanishing of the right-hand expression of (B) or (B'). It is NOT an all-prime classification of cancellation primes, NOT an original D25 LIFT counterexample or proof, and the auxiliary conductor-3 Dirichlet character is NOT by itself the authentic CM primitive class.

## 2. Proof of Theorem A: exact finite cubic filter and shuffle

All calculations in this section with sums of p-unit denominators take place in F_p, except explicitly lifted congruences modulo p^2 or p^3.

Since p≡1 (mod 3), choose a primitive cubic root of unity z in F_p. For residue classes r=0,1,2 define
\[
I_r=\{1\le j\le p-1:j\equiv r\bmod3\},\quad
A_r=\sum_{I_r}j^{-1},\quad
B_r=\sum_{I_r}j^{-2},\quad
W_r=\sum_{j\in I_r}\frac{H_{j-1}}{j}.
\]
Here H_0=0. The involution j↦p-j maps I_0↔I_1 and I_2↔I_2. The complete reciprocal sums of orders 1 and 2 vanish modulo p. Accordingly
\[
A_0=H/3,\quad A_2=0,\quad A_1=-A_0;\qquad
B_0=H_2/9,\quad B_1=B_0,\quad B_2=-2B_0 \pmod p.       \tag{2.1}
\]

Introduce finite polynomials
\[
L(Z)=\sum_{j=1}^{p-1}\frac{Z^j}{j},\quad
L_2(Z)=\sum_{j=1}^{p-1}\frac{Z^j}{j^2},\quad
W(Z)=\sum_{j=1}^{p-1}\frac{H_{j-1}Z^j}{j}.
\]
Direct coefficient convolution in F_p[Z] yields the **finite polynomial identity**
\[
\boxed{L(Z)^2=2(1-Z^p)W(Z)-2Z^p L_2(Z).}             \tag{2.2}
\]
For 2≤d≤p-1, both sides' coefficient is \(2H_{d-1}/d\). At d=p it is zero because \(\sum_{j=1}^{p-1}j^{-2}=0\). For d=p+r, 1≤r≤p-2, it is \(-2H_r/r\), by pairing j and p+r-j (and using \(H_{p-1-r}=H_r\bmod p\)). Thus no analytic or infinite-series shuffle assertion is imported.

Using z^p=z and (2.1),
\[
L(z)=A_0(1-z),\quad L_2(z)=-3B_0 z^2,\quad
W(z)=\frac{A_0^2}{2}(1-z)-\frac{3B_0}{1-z}.
\]
The analogous identity holds at z^2. Moreover \(W(1)=\big(H_{p-1}^2-H_{p-1}^{(2)}\big)/2=0\). By cubic filtering and \(1/(1-z)+1/(1-z^2)=1\),
\[
3W_0=W(1)+W(z)+W(z^2)=3A_0^2/2-3B_0,
\]
hence
\[
\boxed{W_0\equiv A_0^2/2-B_0
=\frac{H^2}{18}-\frac{H_2}{9}\pmod p.}             \tag{2.3}
\]

Next set \(Q=(-27)^m\in\mathbb Z\). In characteristic p, \((1-z)^p=1-z\), while \((1-z)^6=-27\); hence \(Q\equiv1\bmod p\). Its exact square is
\(Q^2=3^{p-1}=1+pb\), giving the integral lifted expansion
\[
\frac{Q-1}{p}\equiv \frac b2-\frac{pb^2}{8}\pmod{p^2}. \tag{2.4}
\]
Consider the *integer binomial polynomial* \((1-Z)^p\). The coefficient of 1 minus the coefficient of Z^2 in its reduction modulo \(Z^2+Z+1\), excluding endpoints j=0,p, equals Q-1 (since p≡1 mod3). For 1≤j≤p-1 the exact finite binomial expansion gives
\[
(-1)^j\binom pj
=-\frac pj\prod_{\ell=1}^{j-1}\left(1-\frac p\ell\right)
\equiv-\frac pj+\frac{p^2 H_{j-1}}j\pmod{p^3}.
\]
Consequently, with A and W now understood as their natural rational p-local lifts,
\[
\frac{Q-1}{p}\equiv-(A_0-A_2)+p(W_0-W_2)\pmod{p^2}.   \tag{2.5}
\]
For I_2 the reflection j↦p-j fixes the class and gives
\[
A_2\equiv-\frac p2 B_2\pmod{p^2},\qquad
W_2\equiv-\frac12 B_2\pmod p.
\]
Thus its two terms cancel in (2.5), leaving
\[
\frac{Q-1}{p}\equiv-A_0+pW_0=-H/3+pW_0\pmod{p^2}. \tag{2.6}
\]

Combining (2.4)–(2.6), first \(H\equiv-3b/2\pmod p\). Therefore (2.3) becomes \(W_0\equiv b^2/8-H_2/9\pmod p\). Lift (2.6) one digit:
\[
H\equiv-3\left(\frac b2-\frac{pb^2}{8}\right)+3p\left(\frac{b^2}{8}-\frac{H_2}{9}\right)
=-\frac32 b+p\left(\frac34 b^2-\frac13 H_2\right)\pmod{p^2}.
\]
This proves (A) for all stated primes. No finite scan or CM hypothesis enters the proof.

## 3. Proof of Theorem B and the all-prime third-digit corollary

Consume the previously derived original-source WZ mod-p-cubed identity, preserving its five endpoint/tail provenance:
\[
F_p\equiv\frac23+pc+p^2(T-2h)\pmod{p^3}, \tag{3.1}
\]
where
\[
c=b-\frac43a-k,\quad
T=B+\frac3{220}(A_1+\alpha A_0),\quad
\alpha=\frac32b-2a-\frac{641}{220},
\]
\[
B=\frac{73}{120}+\frac a2-\frac{3b}{8}
+2a^2-2ab+\frac74 b^2-\frac13H_2,\quad
A_0=\frac{250809}{17920},\quad A_1=\frac{466056841}{63974400}.
\]

Inserting the independently proved (A), the unresolved h *disappears for every target prime*, yielding the useful unconditional observer identity
\[
\boxed{
\begin{aligned}
F_p\equiv{}&\frac23+pc+p^2\bigg[
\frac{73}{120}+\frac a2-\frac{3b}{8}
+2a^2-2ab+\frac14b^2+\frac13H_2\\
&\qquad+\frac3{220}
\left(A_1+\left(\frac32b-2a-\frac{641}{220}\right)A_0\right)
\bigg]\pmod{p^3}.
\end{aligned}} \tag{3.2}
\]

For the second-digit cancellation fibre \(p^2\mid M_p\), the previously proven integer-lift formula supplies
\[
\eta_p\equiv \frac{M_p}{3Dp^2}-2h+\frac83a^2+4ka
+C_\star-\frac13H_2\pmod p,\quad
C_\star=\frac{472332426338543}{3170673623040000}.   \tag{3.3}
\]

By (A), \(-2h=-3b^2/2+2H_2/3\pmod p\). On this fibre \(b\equiv4a/3+k\pmod p\), so
\[
\frac83a^2+4ka-\frac32b^2
\equiv-\frac32k^2\pmod p.
\]
Consequently
\[
\eta_p\equiv\frac{M_p}{3Dp^2}+\frac13H_2+
\left(C_\star-\frac32k^2\right)\pmod p.
\]
An exact rational simplification gives
\(C_\star-3k^2/2=455695314072269/3170673623040000=C_{\rm final}\).
This proves (B). The inherited classical-character identity
\(H_2\equiv9B_{p-2,\chi_{-3}}/4\pmod p\) proves (B'). This elimination is specific to the declared scalar observer on the cancellation fibre; it neither discards original port labels in the source certificate nor establishes a lossless CM comparison.

## 4. Deterministic author checks and exact finite witnesses

An exact integer/rational mod-p-squared regression of (A) passed **all 329 primes p=6m+1 with 13≤p<5000**. The finite polynomial identity (2.2) was separately coefficient-checked for five small target primes. These checks support the algebra but are **author validation, not independent review or proof of the quantified theorem**.

The only two *previously found* cancellation primes at most ten million are checked **without rerunning that search**, by modular exponentiation modulo p^3:

| p | H2 mod p | M_p / p^2 mod p | h mod p | New collapsed eta_p mod p |
|---:|---:|---:|---:|---:|
| 1423 | 427 | 43 | 544 | **1240** |
| 5827 | 2917 | 786 | 2513 | **2918** |

In both cases eta_p≠0, agreeing with the *inherited* independently calculated five-tail original-factorial witnesses. Therefore in precisely these two already-verified cases,
\(v_p(S_{m+1}-S_m-2p/3)=3\).
Only p=5827 belongs to the original 13/19 mod-24 D25 target class. No general exception classification follows.

Small reproducible **pure standard-library integer check** for (A) and these two known witnesses:

~~~python
from fractions import Fraction as Q

def loc(x, modulus):
    x = Q(x)
    return x.numerator * pow(x.denominator, -1, modulus) % modulus

def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))

checked = 0
for p in range(13, 5000):
    if p % 6 != 1 or not prime(p):
        continue
    n = (p - 1) // 3
    b = (pow(3, p - 1, p**3) - 1) // p
    H = sum(pow(j, -1, p*p) for j in range(1, n+1)) % (p*p)
    H2 = sum(pow(j*j, -1, p) for j in range(1, n+1)) % p
    hnum = (H + loc(Q(3, 2), p*p) * b) % (p*p)
    assert hnum % p == 0
    assert hnum // p == (
        loc(Q(3, 4), p) * b*b - loc(Q(1, 3), p) * H2
    ) % p
    checked += 1
assert checked == 329

D = 3942400
Cfinal = Q(455695314072269, 3170673623040000)
for p, expected in ((1423, 1240), (5827, 2918)):
    n = (p-1)//3
    M = (D * (pow(27, p-1, p**3) - pow(16, p-1, p**3))
         - 699519*p*pow(16, p-1, p**3)) % p**3
    assert M % p**2 == 0
    H2 = sum(pow(j*j, -1, p) for j in range(1, n+1)) % p
    eta = (loc(Q(1, 3*D), p) * (M // p**2)
           + loc(Q(1, 3), p)*H2 + loc(Cfinal, p)) % p
    assert eta == expected
print("PASS: 329 harmonic lifts and two inherited WZ witnesses")
~~~

## 5. Residual-fidelity/BRC observer boundary; next action

BRC **COMPOSE_APPLIED in this exact observer scope**: source labels remain the five original WZ tail/edge ports; the allowed operation is a fixed-p moving-rank difference, followed by a specifically declared second-digit cancellation and third-digit scalar projection. The new cancellation-fibre compression is proved adequate only for that scalar projection: its necessary arithmetic coordinates are \(M_p/p^2\) and \(H_2\) (equivalently the conductor-3 Bernoulli port). No CM class identity, six-dimensional native dynamics, original-class source lift, or universal elimination of structural residuals is inferred.

**Parent D25/LIFT remains open.** Source continuation currently exposes no new authorized winning CLAIM/run and explicitly requires an *authenticated same-prime, same-primitive-class CM/divided-power representative*, actual semilinear map direction, Frobenius compatibility and exact companion normalization. In particular the genuine [X]U mod p^2 with fixed H0/B0 coefficients and source-bound \(\kappa\) is missing; the original CM experiment remains NOT_RUN. The auxiliary \(\chi_{-3}\) Bernoulli scalar does **not** fill that source requirement.

Do not repeat original five-tail certificate, four-tail factorial units, one-million/ten-million prime searches, source fixed-x versus fixed-xi vanishing, or the inherited two witness factorial checks. The mathematical successor for an authorized owner is to establish a source-valid CM representative/normalization map and compare its exact native observable to the already typed WZ/LOW/HIGH ports; no direct equality should be assumed. This portable theorem is author evidence, not a source-admitted continuation unit or a claim on another owner's task.
