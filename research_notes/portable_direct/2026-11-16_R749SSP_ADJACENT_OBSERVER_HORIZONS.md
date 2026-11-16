# R749SSP — Exact adjacent-cutoff observation horizons

Date: 2026-11-16. Scientific status: AUTHOR_EXACT_NOT_REVIEWED; complete author exact algebra and independently runnable SymPy certificates. Source: independent portable research under frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessors: R749SSK/SSL at cff1f9e3a101d9291a505dfa8990df76775597e0; R749SSM at 7ea79c50d4f448c515719b1f883b5fb68fe4d69a; R749SSO at f24fa2becad95c5ef9d8fbbf12832f43573526c6. No formal shared CLAIM or native X6 theorem asserted.

## Model

Five *labeled* sources, weights w=(1,1,2,3,6), with the first unit-weight source marked. For q>=6 let

\[
\Omega_q=\{k\in\mathbf Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]

Set S(q)=18q^4+54q^3-345q^2+2070q-16315 and

\[
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108},\qquad {\cal O}^{(m)}_q(e,d)=(Y_{q+6j}(e,d))_{0\le j<m}.
\]

The two candidate cutoff states independently choose (e,d),(E,D) in the closed real square [-2,2]^2, each pair reused unchanged over its state-wise ordered observation history. Denominators stay strictly positive. The cutoff/source provenance q is unknown to the observer.

## Theorems

**A — Infinite adjacent tail.** For every integer q>=9,
\[
{\cal O}^{(3)}_q([-2,2]^2)\ \cap\ {\cal O}^{(3)}_{q+1}([-2,2]^2)=\varnothing.
\]
The same three-read disjointness holds for (6,7). The q>=9 statement is infinite and algebraically certified over every real permitted error pair.

**B — Sharp small-cutoff horizons.** The minimum number m of consecutive six-shift reads that distinguishes all error pairs at a specified adjacent-cutoff pair is m=3 for (6,7) and m=4 for (7,8) and (8,9). The three-read intersection and four-read separation for (7,8) were already established in R749SSL/R749SSM. This work proves a new three-read collision and four-read exclusion for (8,9). The known R749SSK two-read coincidence proves sharpness for (6,7).

**C — Explicit (6,7) margin.** For all permitted real error pairs,
\[
\|{\cal O}_6^{(3)}(e,d)-{\cal O}_7^{(3)}(E,D)\|_\infty
\ge \frac{936564238139152873}{13797485059436106048}
>0.
\]
Independent per-coordinate additive absolute observation noise less than half this bound preserves discrimination between these two cutoff classes. The bound is conservative.

## Necessary determinant and exact 6/7 proof

For compared cutoffs q and p=q+1, at j=0,1,2,3 put a=q+6j and b=p+6j, and define

\[
V_j=b^3(C_a+d),\quad U_j=a^3(T_a+e)+\frac{S(b)-S(a)}{108}(C_a+d),\quad
L_j=(V_j,-U_j,C_bU_j-T_bV_j).
\]

Equality of the j-th observed values forces L_j.(E,D,1)=0; hence three equal reads force det(L0,L1,L2)=0; four equal reads force det(L0,L1,L3)=0 as well. No inversion or exceptional subtraction denominator is used.

At q=6 define H6(e,d)=216 det(L0,L1,L2). The *exact* polynomial is

\[
\begin{aligned}
H_6={}&86847704637475d^3+807806095895664d^2e-300944247922632867d^2\\
&-218376345835008de^2+263012470830130320de-3268509180682454118d\\
&-1373312747538432e^2+1847422399731613632e-19994601433113510136.
\end{aligned}
\]

For |e|,|d|<=2 the absolute-weighted sum of all nonconstant terms is strictly less than the magnitude of the constant coefficient, yielding
\[
-H_6(e,d)\ge7492513905113222984>0.
\]
Thus no three-read collision at 6/7. The pre-existing exact two-read witness is (e,d)=(0,0) at cutoff 6 and (E,D)=(445301541473/452834122344,-16718273227/37736176862) at cutoff 7.

For an explicit margin let v_j=b^3(C_a+2), u_j=a^3(T_a+2)+ceil(|S(b)-S(a)|(C_a+2)/108), and k_j=(C_a+2)(C_b+2). Write \Delta_j=Y_a(e,d)-Y_b(E,D). Exactly,
\[
L_j.(E,D,1)=(C_a+d)(C_b+D)\Delta_j.
\]
Replacing the third determinant column by itself plus E times the first plus D times the second gives
\[
|\det(L_0,L_1,L_2)|\le B \max_j|\Delta_j|,\quad
B=\sum_{j=0}^2 k_j(v_k u_l+u_kv_l)
=511017965164300224,
\]
where {k,l} is the complementary index pair. Combining with H6=216det and the lower bound gives Theorem C.

## Infinite q>=9 proof: six exact polynomial signs

The generating function of exact sums for the five separate weights is

\[
\prod_{w\in(1,1,2,3,6)}(1-z^w)^{-1}=\frac{P(z)}{(1-z^6)^5},\qquad\deg P=17,
\]
with P(z)=prod_w sum_{j=0}^{6/w-1} z^{jw}. For 0<=r<6, the coefficient of z^{6m+r} is sum_{k=0}^2 [z^{6k+r}]P(z) binom(m-k+4,4), polynomial in m>=0. The binomial polynomial vanishes at negative combinatorial indices (m=0,1, k>m). Since C and T are respectively cumulative exact-source and marked-unit-source sums, C_{6m+r}, T_{6m+r} have residue-class polynomial formulas of degree <=5 and <=6. Their identities are checked against the exact six-shift recurrences in the companion script; the recurrence plus base values proves validity for every m>=0.

For q0 in {9,10,11,12,13,14}, write q=q0+6t, t>=0 integer, and use the above exact C and T polynomials in the three-read determinant. Multiply det(L0,L1,L2) by a positive denominator-clearing integer s to obtain
\[
H_{q0}(t,e,d)=\sum_{i,j}h_{ij}(t)e^i d^j.
\]
Set sigma=sign(h00(0)). For h(t)=sum_k h_k t^k let major(h)(t)=sum_k |h_k|t^k, so |h(t)|<=major(h)(t) for t>=0. The integer polynomial
\[
D_{q0}(t)=\sigma h_{00}(t)-\sum_{(i,j)\ne(0,0)}2^{i+j}\operatorname{major}(h_{ij})(t)
\]
is a certified lower bound on sigma H. The reproducible full symbolic certificate calculates each degree-24 D polynomial and asserts positivity of **every coefficient** (25 for each of six residue classes, 150 exact integers). Each polynomial therefore stays strictly positive for every t>=0. The summary, with all entries derived from the certificate, is:

| q0 | positive scale s | sign sigma | deg(D) | smallest of 25 coefficients |
|---:|---:|---:|---:|---:|
| 9 | 1458000 | -1 | 24 | 8331090195456 |
| 10 | 1944000 | -1 | 24 | 14281868906496 |
| 11 | 162000 | +1 | 24 | 3305988172800 |
| 12 | 5832000 | -1 | 24 | 119015574220800 |
| 13 | 486000 | +1 | 24 | 3570467226624 |
| 14 | 648000 | +1 | 24 | 3702706753536 |

Hence for every real |e|,|d|<=2, every t>=0 and each residue q0, the necessary three-read determinant is nonzero. This proves Theorem A over the full infinite range of integer q>=9.

## New sharp (8,9) pair

**Three-read collision:** At q=8 set d=-1 and let e* be the unique root in (-163/500,-13/40) of

\[
\Phi(e)=86485661024256e^2-75908891607492816e-24689030348714335.
\]
Phi has opposite strict signs at these rational endpoints and strictly negative derivative there. For p=9 define the competing errors exactly by
\[
D=\frac{3161870784e_*+155094721265}{2(632114352e_*-110882822705)},\qquad
E=\frac{143842148352e_*^2-23723179174944e_*-29856214143065}{216(632114352e_*-110882822705)}.
\]
These satisfy the first two observation equations by direct algebraic inversion. The third-read difference numerator is exactly divisible by Phi(e), so it vanishes at e*. The rational interval computations in the companion certificate prove |E|,|D|<2, with denominators nonzero on the bracket. Therefore
\[
{\cal O}_8^{(3)}(e_*,-1)={\cal O}_9^{(3)}(E,D).
\]

**Four-read disjointness:** For q8/p9 define f=24det(L0,L1,L2), g=24det(L0,L1,L3). Their exact quadratic resultant eliminating e factors as a nonzero constant K times
\[
(d+98)(d+662)(79435415d+612671694)Q(d)
\]
where
\[
\begin{aligned}
Q(d)={}&26462686334042645429945701137787854d^5\\
&+2665724529495411954752877400836869271273d^4\\
&+225665575370900725811848376223012798253276d^3\\
&+259206111485804009334400947416274794358340d^2\\
&-10607977574627059592249580049853570554088576d\\
&+19042774742613941301134787391164065250594816.
\end{aligned}
\]
On -2<=d<=2 the three linear factors are positive. Substitute d=-2+4x, 0<=x<=1, and express Q(-2+4x)=sum_{i=0}^5 beta_i binom(5,i)x^i(1-x)^{5-i}. All six *exact rational* Bernstein coefficients beta_i are positive, as recomputed and recorded in the companion executable script and output. The Bernstein basis is nonnegative and sums to one, hence Q>0 on the whole real interval. Thus the resultant cannot vanish, so four-read equality is impossible. Combined with the exact three-read collision, four is the sharp horizon for q8/p9.

## Scope, evidence and continuation

Pair (6,7): sharp minimum 3; pair (7,8): predecessor sharp minimum 4; pair (8,9): sharp minimum 4; every adjacent (q,q+1) with integer q>=9: 3 reads *sufficient* by an infinite proof. The smallest horizon for q>=9 and separation of non-adjacent cutoffs remain open.

Verification requires Python 3 and SymPy. Certificates reconstruct labeled-source counts, polynomial recurrence identities, 150 positive coefficient tests, exact q6/7 margin, exact 8/9 algebraic collision, resultant and Bernstein positivity, then emit companion JSON results. Both author runs returned PASS on 2026-11-16. This establishes the specified abstract scalar observation results with exact computation, pending independent mathematical review. The five labeled sources, cutoff provenance, state-wise common errors and observation order are retained; no native six-dimensional Cell map, Heartbeat dynamics or BRC typed Port transfer is asserted by these scalar calculations.

Next: determine one-/two-read classification for each q>=9, extract a q-normalized explicit noise bound from the six D polynomials, classify nonadjacent cutoff pairs, and construct a provenance- and observer-fiber-preserving typed BRC/Cell bridge if the task demands it.
