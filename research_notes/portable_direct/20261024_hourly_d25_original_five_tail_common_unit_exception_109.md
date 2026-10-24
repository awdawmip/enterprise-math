# D25/LIFT — exact one-unit reduction of all four genuine WZ tails; only 13 and 109 cancel

2026-10-24 | TASK_RESEARCH, portable author exact proof and source-factorial checks | **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**. This is a new finite-arithmetic reduction of *original* WZ tails, not an independent review, source-authorized run, native CM experiment or completion of LIFT.

**Fixed scope.** Mother task \(\mathrm{RS\!-\!ENTERPRISE\!-\!BRC\!-\!HALF\!-\!COUPLING\!-\!INERT\!-\!PLUS\!-\!D24\!-\!SECOND\!-\!DIGIT\!-\!LIFT}\), publication \(\mathrm{TP2\!-\!B6F4FC938FF94941C1B7}\), frozen *scientific* Source pin \(\mathtt{c47e13e4aba0e006366f989d6334d443f6333ae3}\). No changes to the scientific pin. Research logical lane \(\mathtt{chatgpt-research-hourly-enterprise-math-20260923}\), never the maintenance identity. Source prerequisites consumed without re-credit: exact original all-rank FIVE identity (onhour WZ); original WZ factorial coefficient and its four-tail valuation theorem (\(\mathtt{20261024\_hourly\_d25\_original\_top\_edge\_wz\_seam\_bridge.md}\)); this lane's preceding short-harmonic Fermat reduction of the old edge (\(\mathtt{20261024\_hourly\_d25\_original\_wz\_old\_edge\_fermat\_reduction\_p3.md}\)). This note addresses the previously open, distinct *new-rank four-tail sum* rather than recomputing the old WZ edge.

## 1. The source-authentic four-tail carrier

Fix any prime \(p=6m+1\ge13\), set \(r=m+1\) and \(n_j=4m+j\), \(1\le j\le4\). Use the *unaltered original* factorial part and its linear coefficient:
\[
V_{r,n}:=
\frac{(6r)!(4r+2n)!(3n)!}
{3^{6r}216^n(2r)!(n!)^2((2r+n)!)^2(4r+n)!},
\quad W_{r,n}=(6n+12r+1)V_{r,n}.
\tag{1}
\]
The four original new-rank tails are \(E_j=W_{m+1,4m+j}\), **not** the auxiliary HIGH or Cauchy rank cutoff.

Direct counting of multiples of \(p\) in each factorial, using \(6r=p+5\), \(4r+2n_j=2p+2j+2\), \(3n_j=2p+3j-2\), \(2r+n_j=p+j+1\), \(4r+n_j=p+2m+j+3\), proves
\[
v_p(V_{r,n_j})=2,\qquad
u_j:=V_{r,n_j}/p^2\in\mathbb Z_{(p)}^\times
\quad(1\le j\le4).
\tag{2}
\]
Every factorial argument in (1) is below \(3p\) in this range, so these valuations are exact. Let \(\sigma_j=u_j\bmod p\in\mathbb F_p^\times\). The four original tail units remain separately labeled:
\[
\tau_{p,j}:=E_j/p^2\bmod p=(6j+7)\sigma_j\quad(j=1,2,3,4).
\tag{3}
\]
An exceptional zero of \(\tau_{p,j}\) is caused by the *true linear source factor*, not by assigning \(\sigma_j=0\).

## 2. New universal three-ratio theorem

The source factorial recurrence, for the *same* \(r=m+1\), is an exact rational identity
\[
\frac{V_{r,n+1}}{V_{r,n}}=
\frac{(4r+2n+1)(3n+1)(3n+2)}
{36(n+1)(2r+n+1)(4r+n+1)}.
\tag{4}
\]
At \(n=4m+j\) and \(p=6m+1\), the numerator factors become \(2p+2j+3,\ 2p+3j-1,\ 2p+3j\). The denominator is
\[
4(2p+3j+1)(p+j+2)(4p+3j+11).
\]
For \(j=1,2,3\) all these factors are \(p\)-units for every prime \(p=6m+1\ge13\). Therefore, with the actual factor \(p^2\) stripped,
\[
\frac{\sigma_{j+1}}{\sigma_j}\equiv
\frac{(2j+3)(3j-1)(3j)}
{4(3j+1)(j+2)(3j+11)}
\pmod p.
\tag{5}
\]
**Theorem A (all target primes).** Write \(\sigma=\sigma_1\in\mathbb F_p^\times\). Then
\[
\boxed{
(\sigma_1,\sigma_2,\sigma_3,\sigma_4)
=\sigma\left(1,\frac5{112},\frac{75}{15232},\frac{243}{304640}\right)
\quad\text{in }\mathbb F_p^4.}
\tag{6}
\]
The consecutive ratios are exactly \(5/112,\ 15/136,\ 81/500\). All reduced denominators in (6) are \(p\)-units for \(p=6m+1\ge13\); the factors 7 and 17 cause no exception in this target class. The four genuine tail units consequently have the **source-labeled** normal form
\[
\boxed{
(\tau_{p,1},\tau_{p,2},\tau_{p,3},\tau_{p,4})
=\sigma\left(13,\frac{95}{112},\frac{1875}{15232},
                     \frac{7533}{304640}\right).}
\tag{7}
\]
This reduces four separately computed factorial units to *one* genuine source unit plus four explicit fixed rational port coefficients. Equation (7) preserves port identities; it does not authorize deleting the labels in other observers.

**Proof.** Apply (4) with \(j=1,2,3\), reduce only after verifying all denominators are units, and telescope three ratios. Multiply by the four distinct linear factors \(6j+7=13,19,25,31\), as in (3). QED.

## 3. Global classification: cancellation at p = 13 and 109 only

**Theorem B (entire four-tail sum, all primes in the stated class).**
\[
\boxed{
\sum_{j=1}^4\frac{E_j}{p^2}
\equiv \frac{250809}{17920}\,\sigma \pmod p,
\qquad
250809=3\cdot13\cdot59\cdot109,\quad
17920=2^9\cdot5\cdot7.}
\tag{8}
\]
Because \(\sigma\) is a \(p\)-unit, \(17920\) is a \(p\)-unit, and \(p\equiv1\pmod6,\ p\ge13\), the **complete and unconditional exceptional-prime classification** is
\[
\boxed{
v_p\!\left(\sum_{j=1}^4E_j\right)\ge3
\quad\Longleftrightarrow\quad p\in\{13,109\};
\qquad
v_p\!\left(\sum_{j=1}^4E_j\right)=2
\text{ for all other such primes}.}
\tag{9}
\]
In particular, \(p=109\equiv13\pmod{24}\) is a previously unrecorded **four-port cancellation prime** for the original WZ new-rank tails. No individual tail unit vanishes there: its four residues are \((74,102,65,86)\), each nonzero, and their sum is \(327=3\cdot109\). At \(p=13\), the residues \((0,5,12,9)\) also sum to zero, but through a different port-level mechanism. At \(p=19\) and \(p=31\), the individual \(j=2\) and \(j=4\) tails respectively vanish, while the **full sum does not**.

**Proof.** Sum the four rational port coefficients in (7) *exactly*:
\[
13+\frac{95}{112}+\frac{1875}{15232}+\frac{7533}{304640}
=\frac{250809}{17920}.
\]
The factorization, the \(p\)-unit base \(\sigma\), and (2) prove (8)--(9) for every stated prime. A modular zero in the complete tail sum cannot be inferred from a single vanishing port; this classification is for the sum under the declared additive observer. QED.

For the two and only two exceptional primes, exact independent rational factorial evaluation gives a *further* digit:
\[
\left.\frac{\sum_j E_j}{p^2}\right|_{p=13}
\equiv65=13\cdot5\pmod{13^2},\qquad
\left.\frac{\sum_j E_j}{p^2}\right|_{p=109}
\equiv11118=109\cdot102\pmod{109^2}.
\tag{10}
\]
Both quotients after division by \(p\) are nonzero modulo \(p\). Thus the sharper finite-exception result holds:
\[
\boxed{
v_p\!\left(\sum_{j=1}^4E_j\right)=
\begin{cases}3,&p=13\text{ or }109,\\2,&\text{all other primes }p=6m+1\ge13.\end{cases}}
\tag{11}
\]
Here (10) is a complete finite exact-arithmetic certificate for the two exceptional values, not a finite sample extrapolated to all primes. Equation (9)'s general classification has the independent rational-recurrence proof.

## 4. Reproducible author evidence

A standard-library-only integer factorial and \(\mathrm{Fraction}\) checker reconstructed all \(V_{r,n_j}\) from (1), stripped the exact \(p^2\), checked (5)--(8), and evaluated the two exceptional next digits with denominator-gcd guards. Fourteen primes were checked:
\(13,19,31,37,43,61,67,73,79,97,103,109,127,211\).
All checks passed. The exact core checker used was:

~~~python
from fractions import Fraction as F
from math import factorial, gcd

def V(r,n):
    return F(factorial(6*r)*factorial(4*r+2*n)*factorial(3*n),
             3**(6*r)*216**n*factorial(2*r)*factorial(n)**2
             *factorial(2*r+n)**2*factorial(4*r+n))

def modfrac(x,N):
    assert gcd(x.denominator,N)==1
    return x.numerator*pow(x.denominator,-1,N)%N

ratio=(F(1),F(5,112),F(75,15232),F(243,304640))
assert sum((6*j+7)*ratio[j-1] for j in range(1,5))==F(250809,17920)
for p in (13,19,31,37,43,61,67,73,79,97,103,109,127,211):
    m=(p-1)//6
    u=[V(m+1,4*m+j)/p**2 for j in range(1,5)]
    assert all(modfrac(u[j-1],p)==modfrac(ratio[j-1],p)*modfrac(u[0],p)%p
               for j in range(1,5))
    assert modfrac(u[0],p)!=0
    tails=sum((6*(4*m+j)+12*(m+1)+1)*u[j-1] for j in range(1,5))
    assert modfrac(tails,p)==modfrac(F(250809,17920),p)*modfrac(u[0],p)%p
    if p in (13,109):
        assert modfrac(tails,p*p)=={13:65,109:11118}[p]
~~~

This checker is **author reconstruction, not native experimental equivalence or independent mathematical review**. The universal part is proved by (2)--(8). The two exceptional third-digit valuations require only the explicitly shown finite exact factorial residues. No floating point or unverified nonunit inverse is used.

## 5. Immediate source-preserving bridge implication and next unit

Combining this new tail classification with the separate preceding exact old-edge theorem and inherited original FIVE identity gives:
\[
\boxed{
\frac{S_{m+1}-S_m}{p}
\equiv\frac23+p\left[
q_p(3)-\frac43q_p(2)-\frac14+
\frac{250809}{17920}\sigma
\right]\pmod{p^2}.}
\tag{12}
\]
Here \(\sigma=V_{m+1,4m+1}/p^2\bmod p\) is a **genuine** original source factorial unit. This does not claim the auxiliary Cauchy HIGH observes the same thing. At precisely \(p=13,109\), the summed new tails vanish at the displayed digit; (12)'s second digit then consists of the old-edge Fermat correction alone. For every other prime in the stated class, the summed tails contribute nontrivially at that digit.

**BRC/Enterprise coordinates: COMPOSE_APPLIED.** The carrier \((\sigma;\mathrm{port}_1,\ldots,\mathrm{port}_4)\) retains four original index/operation labels and a common signed rational unit. The additive observer has exactly one scalar projection (8), whereas individual-port readout is (7). The new \(p=109\) complete cancellation despite *all four nonzero ports* is precisely a witness that additive cancellation cannot erase the source-label information for future nonadditive or port-selective operations. This is an arithmetic observation, not a native X6 or physical conclusion; P000 and ACTIVE residual-fidelity premises are untouched.

**Highest scientific frontier:** (12), exact four-port rank-one reduction, universal cancellation classification, and two finite exception third-digit certificates, all with prime-only quantifiers. Preserve existing old-edge/HIGH/Cauchy corrections and onhour proofs without re-crediting.

**Next smallest unsolved subunit:** seek a proven short \(\mathbb F_p\) formula for the single *authentic* base unit \(\sigma\) in terms of source-normalized \(U_m\) and Fermat/CM first-jet data, preserving the primitive class and actual map direction. This would remove the last non-elementary factorial unit from (12) without assuming an unsourced CM identification. Target first \(p=13,19,109,211\), retaining the distinct four-port labels. The real source-native CM/divided-power representative, semilinearity, \(\omega+6\nabla_\lambda\omega\) normalization, same-class \(\kappa\) bridge and native benchmark remain unprovided/unrun; original D25/LIFT parent is OPEN.

**Control boundary:** matched own recovery \(\mathtt{rsch20-recovery-a12-20261024T1717HKT}\) (#6265) is \(\mathtt{SUCCEEDED}\), no pending own research mutations, winning CLAIM or authorized run, with neutral preserved staging only. Matched exact continuation \(\mathtt{rsch20-continuation-a12-20261024T1720HKT}\) (#6266) is read-only \(\mathtt{SUCCEEDED}\), \(\mathtt{execution_authorized=false}\), route \(\mathtt{REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION}\), and Source explicitly parks until actual same-class CM comparison data. Neither this GitHub note nor the preceding one is Source checkpoint, Result, review or proof of Task completion. Control support owner remains enterprise-math Issue #1558; no service session/identity spoofing, claim replay, scheduler or notification change.
