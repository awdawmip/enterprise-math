# Every seven-prime cover on R2 containing 5 and 13 also contains 19 and 73

**Status and scope.** This is an author mathematical proof for the existing direct research Activity `RA-D2EC212845B63844081F9A14`, Researcher `EM-DIRECT-970E1C`. Its exact arithmetic checks are in `verify_prefix.py` and `prefix_certificate.json`. It is not an independent project Review, formal acceptance, or Foundation promotion. No remote write or control-plane mutation is part of this work.

The current canonical entry pins supplied by the parent are GK `b7f1066501848d4f1abee3949119115ce98928f5` and EM `213c3ec64486ac904789902cd4c13481b881fffd`. The reused six-budget scientific source is EM commit `f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5`, files `research_notes/portable_direct/riesel_finite_observers_20261124/six/proof.md` and `six/r2_proof.md`. The earlier global phase theorem is EM commit `b1de1acbdc97b5e51d486127abd1fadd24babd99`, file `research_notes/portable_direct/riesel_five_cover_20261123/global/proof.md`.

## 1. Statement in the fixed fiber

Use the inherited sequence

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

the fixed twenty-prime old dictionary P, and the root class R2 of the six-budget source. In particular R2 imposes

\[
a\equiv0\pmod{433},\qquad a\equiv38733\pmod{38737},
\]

in addition to the R1 constraints. Let Q be a set of at most seven primes outside P, and suppose P together with Q covers every term of the sequence.

**Conditional prefix theorem.** If \(5,13\in Q\), then

\[
\boxed{19,73\in Q.}
\]

The theorem is over every root in R2 and all primes. It assumes neither that a seven-prime cover extends a budget-six optimum nor that the selected channels occur in an optimal nested order.

The inherited fixed phases of 5 and 13 leave exactly

\[
n=8+12v,\qquad
v\in A=\{1,2,10,11,12,16,17,22,25,26,30,31,32\}\pmod{35}.
\tag{1}
\]

The density of (1) among all exponent indices is \(13/420\). Throughout this note, channel contributions are normalized relative to this remaining set, so complete coverage means relative density one.

The A-counts modulo 7 are

\[
(0,2,3,3,3,2,0).
\tag{2}
\]

In particular A has five nonempty classes modulo 7, each with at least two distinct elements. Distinct elements of the same class modulo 7 have different residues modulo 5, because A is represented inside a complete period modulo 35.

The two active W primes have the fixed phases

\[
19:\ v\equiv0\pmod3,\qquad
73:\ v\equiv1\pmod3.
\tag{3}
\]

The other two W primes, 37 and 109, are inactive. So are 11,61,331 and 433. Prime 38737 has the fixed phase

\[
v\equiv5\pmod6.
\tag{4}
\]

## 2. Incidence bounds and complete small-period inventories

Prime 2 never divides a term, and prime 3 is inactive on the fixed root class. An odd prime q, if active on (1), gives one class of effective period

\[
f_q=\operatorname{ord}_q(2^{12}).
\]

Put \(g=\gcd(f_q,35)\) and \(e=f_q/g\). Its relative contribution to A is exactly

\[
\rho_q=\frac{K_g(c_q)}{13e},\qquad
K_g(c)=|\{r\in A:r\equiv c\pmod g\}|.
\tag{5}
\]

For \(g=1,5,7,35\), the maximum possible K is respectively \(13,5,3,1\). Formula (5) follows by counting in the common period \(\operatorname{lcm}(35,f_q)=35e\), and does not presume independence when the periods have a common factor.

The complete small-period inventories outside \(P\cup\{3,5,13\}\) are:

| Effective period f | Eligible primes | Active possibilities in R2 |
|---:|---|---|
| 1,2,4 | none | none |
| 3 | 19,37,73,109 | 19,73 |
| 5 | 11,61,331 | none |
| 6 | 433,38737 | 38737 |
| 7 | 29,43,1429,5419 | any of the four, depending on the root |
| 10 | 61681,4562284561 | either, depending on the root |

For the f=10 row, the complete factorization is

\[
\begin{split}
2^{120}-1={}&3^2 5^2\cdot7\cdot11\cdot13\cdot17\cdot31\cdot41\cdot61\cdot151\\
&\cdot241\cdot331\cdot1321\cdot61681\cdot4562284561.
\end{split}
\tag{6}
\]

The two surviving primes have respective base-2 orders 40 and 120, so both have effective period 10. The calculator checks complete products, deterministic trial primality of every listed factor, and exact orders. The other inventory rows follow from the complete factors of powers 24,36,48,60,72,84, which are included in the same check. These are complete finite order inventories, not a search up to an empirical prime bound.

For an active channel outside W, (5) and the exclusions above give the four bounds

\[
\left(\frac16,\frac5{26},\frac3{13},\frac1{13}\right)
\quad(g=1,5,7,35).
\tag{7}
\]

Every such channel has contribution at most \(3/13\). It can exceed \(5/26\) only when f=7: every larger f in the gcd-7 column has contribution at most \(3/26\), while the other columns are at most \(5/26\). Thus every non-W, non-f=7 channel has contribution at most \(5/26\), with equality possible only when f=10.

Missing or inactive slots contribute zero. In each argument below they can be padded by zero-contribution slots; an equality or positive lower bound automatically forces those slots to be active.

## 3. Exactly one active W prime is impossible

Suppose Q contains exactly one of 19 and 73. It covers one third of A. There are at most four other slots besides 5,13 and that W prime.

Inactive slots have zero contribution; every other active channel in those four slots is outside W. For such an active channel, consider its contribution outside the selected W class. If \(3\nmid f_q\), the hits are evenly distributed among the three v-classes modulo 3, by CRT. Therefore at most

\[
\frac23\frac3{13}=\frac2{13}<\frac16
\tag{8}
\]

of the original A can remain outside W.

If \(3\mid f_q\), the channel lies wholly inside or wholly outside the W class. In the outside case \(3\mid e\), and (5) gives the bounds

\[
\left(\frac16,\frac5{39},\frac1{13},\frac1{39}\right)
\quad(g=1,5,7,35).
\tag{9}
\]

Equality with \(1/6\) is possible only in the first column with f=6. Consequently complete coverage would require equality in

\[
1\le\frac13+4\frac16=1.
\]

All four additional channels would therefore have to be distinct active primes of effective period 6. But R2 has only one such eligible prime, 38737; 433 is inactive. This contradiction excludes exactly one W prime.

## 4. No active W prime is impossible

Suppose Q contains neither 19 nor 73. There are at most five slots after 5 and 13. Let m count the active effective-period-7 channels among them. The complete inventory gives \(0\le m\le4\).

### 4.1 No period-7 channel

If m=0, the total relative contribution is at most

\[
5\frac5{26}=\frac{25}{26}<1.
\]

### 4.2 One period-7 channel

If m=1, the upper bound is exactly

\[
\frac3{13}+4\frac5{26}=1.
\]

Complete coverage forces all four remaining channels to attain \(5/26\), hence all four must have f=10. There are only two eligible primes of effective period 10 by (6), so this is impossible.

### 4.3 Two period-7 channels

If m=2, each of the other three channels must contribute at least

\[
1-2\frac3{13}-2\frac5{26}=\frac2{13}.
\tag{10}
\]

Applying (5) separately in its four gcd columns, this forces f=6 or f=10:

- For g=1, \(1/f\ge2/13\) forces \(f\le6\), leaving only f=6.
- For g=5, \(5/(13e)\ge2/13\) forces \(e\le2\); f=5 is inactive, leaving f=10.
- For g=7 with f different from 7, the bound is \(3/26<2/13\).
- For g=35, the bound is \(1/13<2/13\).

There are exactly three active possibilities in these two periods: 38737 and the two f=10 primes. Hence all three must be selected.

Temporarily remove 38737. The two f=7 and two f=10 channels contribute at most

\[
2\frac3{13}+2\frac5{26}=\frac{11}{13}<1.
\tag{11}
\]

They therefore miss some A-residue class modulo 70, their full common period with A. Every lift \(v=r+70t\) remains missed by those four channels. These lifts have fixed parity, and run through all three classes modulo 3 because \(70\equiv1\pmod3\). Some lift therefore avoids the single phase \(v\equiv5\pmod6\) of 38737 as well. Positive missed indices follow by adding a common positive period. This contradicts complete coverage.

### 4.4 Three period-7 channels

If m=3, the three period-7 channels remove at most nine of the thirteen A residues modulo 35. Let R be the residues they leave. Then

\[
|R|\ge4.
\tag{12}
\]

At least two of the five nonempty A-classes modulo 7 remain wholly uncovered. Hence R contains at least two different residues modulo 7. Because each remaining whole class contains at least two A-elements, R also contains at least two different residues modulo 5.

There are two other channels. Each must contribute at least

\[
1-3\frac3{13}-\frac5{26}=\frac3{26}.
\tag{13}
\]

For each of them, \(e=f/\gcd(f,35)\) cannot equal one. Indeed e=1 means \(f\in\{1,5,7,35\}\): the first is unavailable, the second inactive, the third excluded by the definition of the two other channels, and f=35 contributes at most \(1/13<3/26\). Thus both e-values are at least two.

Fix any \(r\in R\) and consider all lifts \(v=r+35t\). Each of the two other channels either has no hit on this progression or covers one t-class of period e. In order that their union cover every lift, both must be compatible with r and

\[
\frac1{e_1}+\frac1{e_2}\ge1.
\]

Since both e-values are at least two, necessarily \(e_1=e_2=2\); the two lift classes must have opposite parity. Moreover, the same compatibility condition must hold for every \(r\in R\).

Thus for either channel \(f=2g\) with \(g\in\{1,5,7,35\}\), and R must lie in one class modulo g. The possibility g=1 would give the unavailable period f=2. The other possibilities fail: R has multiple residues modulo 5, multiple residues modulo 7, and at least four residues modulo 35. No such channel can be compatible with every r. This is a contradiction.

### 4.5 Four period-7 channels

If m=4, at least one of the five nonempty A-classes modulo 7 is untouched. Choose two distinct residues \(r,s\in A\) in that class. They have

\[
\gcd(35,r-s)=7.
\]

Only one other channel remains. To cover all lifts of both residues, its period f must divide 35 and also r-s. Thus \(f\mid7\). Period one is unavailable, so f=7. This would require a fifth distinct eligible period-7 prime, while the complete inventory contains only four. This contradiction exhausts the cases.

Sections 3 and 4 prove the conditional prefix theorem.

## 5. Verification and native interpretation

Run `python verify_prefix.py` from this component directory. The calculator uses only the Python standard library and exact arithmetic. It checks the complete factorization inventories, the fixed R2 phases, the old-hole-to-A reduction, all incidence counts and displayed rational thresholds, and the finite residue geometry used in the m=3 and m=4 arguments. It also checks every abstract period-7/period-10 phase combination left in the m=2 reduction over its full common period after adding the fixed 38737 phase. The all-prime necessity is the written proof above; the arithmetic checks do not replace it with a bounded-prime experiment.

The native semantics remain those of the inherited fixed X6 anchor: the full integer register, positive singleton weight and multiplicity one, and updates \(x\mapsto2x+1\), or \(x\mapsto4x+3\) on the even subsequence. Prime residue channels are observations of that state, not new axes replacing it. The argument does not discard cofactors or joint information. No new native execution is claimed by this subtask. The theorem is restricted to the given old dictionary, fixed R2 phases, and budget seven; it does not classify arbitrary Riesel numbers.
