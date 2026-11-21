# EC49FVN — three-denominator 11-adic mesh, exact local count and discrepancy

Date: 2026-11-21 (Asia/Shanghai)
Status: AUTHOR_PROVED / EXACT_INTEGER_PERIOD_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED
Lineage: EC49FVM at immutable commit \`e101e5110c533803bbb1fd91b070f6419303f5ff\`; frozen scientific input BRC16943. Independent portable mathematical research, not a formal CLAIM/Result/Review.

## Context, objects, precise claim

Retain the frozen rational Bernoulli observer
\[
U=4822040484/8132285009,\quad \gamma=141024/1653649,\quad
L_a(z)=(637-3z)/637,\quad L_b(z)=U(1+\gamma z),
\]
\[
a(z)=1-(1-z)L_a(z),\quad b(z)=1-(1-z)L_b(z),\quad
t(x)=\log R(x)/\log S(x).
\]
We consume the EXACT projective finite-field implication of EC49FVM/EC49FVJ: if the divided-difference polynomial
\[
H_{h,n}(z)=[a(z)^hL_a(z)^n-b(z)^hL_b(z)^n]/[L_a(z)-L_b(z)]
\]
has no zero on \(\mathbb P^1(\mathbb F_{11})\), the reduced phase \(h/(h+n)\) is impossible for EVERY rational observer width \(x\in(0,1)\). This is a theorem about the frozen derived readout; it makes no claim about native X6 dynamics. The upstream FUQ/FUR compound-minimax transfer remains unresolved.

For integer \(j\ge 7\), let \(k=2^j\), and introduce three denominators
\[
k_0=k,\qquad k_1=7k/8,\qquad k_2=13k/16.
\]
Define \(T_j\) as the union of all reduced fractions \(h/k_i\in(0,1)\) with \(1\le h<k_i\), \(\gcd(h,k_i)=1\), for which the EXACT same p=11 projective no-zero certificate holds on \((h,k_i-h)\). Let \(S_H\) be the set of certified excluded phases with reduced denominator at most \(H\) as in EC49FVM. Thus \(T_j\subseteq S_H\) whenever \(k\le H\).

**Theorem 1 (stronger all-interval mesh).** For every integer \(H\ge128\), every real interval \(I\subseteq[0,1]\) of length
\[
|I|>\boxed{122/(7H)}
\]
contains a reduced rational phase excluded for every rational width of the frozen observer. The previous EC49FVM constant was \(20/H\); the present constant \(122/7H=17.428571\ldots/H\) is 12.8571% smaller.

**Theorem 2 (explicit local count with bounded discrepancy).** For every \(j\ge7\), every real half-open interval \(I=[a,b)\subseteq[0,1]\), \(w=b-a\):
\[
\boxed{\#(T_j\cap I)=\frac5{11}\,kw+E_j(I),\quad |E_j(I)|\le976/143.}
\]
This increases the single-denominator EC49FVM certified-point intensity from \(2k/11\) to \(5k/11\), and reduces its previous explicit \(|E|\le20\) bound. Theorem 2 is about the constructed subfamily only; it is NOT a \(90.4687\%\) local proportion for all reduced fractions.

For \(j\ge11\) the maximum gap of \(T_j\cup\{0,1\}\), measured in physical phase, is **exactly**
\[
\Delta_j=\frac1{91k}\begin{cases}696,&j\text{ odd},\\793,&j\text{ even}.\end{cases}
\]
The bounds in Theorem 1 cover the smaller initial exponents \(j=7,8,9,10\) as well.

## Proof and finite complete certificate

As established in EC49FVM, the p=11 quotient has one singular finite point \(z=3\), where \(a=b=L_a=L_b=10\pmod{11}\), and its singular value is nonzero exactly when \(9h+10n\not\equiv0\pmod{11}\). At the other ten projective points, nonvanishing depends only on \((h\bmod10,n\bmod10)\). The exact finite-field enumerator finds 44 allowed non-singular exponent pairs mod10. With the singular condition this yields a predicate \(\mathrm{valid}(h,n)\) depending only on \((h,n)\bmod110\). The accompanying verification code recomputes all finite points, the point at infinity, the singular divided difference, and independently compares the compact predicate with direct evaluation on 110×110 positive exponent pairs.

For the combined construction, use a common integer chart
\[
y=91k\theta,\quad \theta=h/k_i.
\]
The three coordinate maps are, **exactly**, \(y=91h\), \(y=104h\), \(y=112h\). Reducedness is, respectively, \(\gcd(h,2)=1\), \(\gcd(h,14)=1\), and \(\gcd(h,26)=1\); the odd factors 7 and 13 have NOT been silently erased. The exact masks depend on
\[
k\bmod110,\quad (7k/8)\bmod110,\quad (13k/16)\bmod110.
\]
For \(j\ge7\) these three masks repeat after 20 increments of \(j\), since \(2^{j+20}\equiv2^j\pmod{110}\) for all positive \(j\).

The first chart is periodic in \(y\) with period \(91\cdot110=10010\); the second with period \(104\operatorname{lcm}(110,7)=80080\); the third with period \(112\operatorname{lcm}(110,13)=160160\). Hence their union is periodic with
\[
M=\operatorname{lcm}(10010,80080,160160)=160160.
\]
There are finitely many candidate coordinates in one \(y\)-period. For each of the 20 exponent-period states \(j=11,\dots,30\), the exact enumerator gives **800 distinct certified points** per period. The cyclic maximum integer gap is 696 for odd \(j\), 793 for even \(j\). Since every \(y\in(0,91k)\) from the periodic mask corresponds to a genuine reduced numerator of one of the three denominators, and \(91k\ge186368>M\) for \(j\ge11\), restricting to \([0,91k]\) with endpoints added cannot increase the gap beyond 793. For \(j=7,8,9,10\), direct complete enumeration gives maximum \(y\)-gaps 546, 712, 696, 793. This proves the upper gap bound at all \(j\ge7\). For \(j\ge12\), \(91k>2M\) and a full cyclic maximum gap necessarily occurs inside the interval, while \(j=11\) is directly checked, proving the exact formula for \(j\ge11\).

Choose \(j=\lfloor\log_2H\rfloor\). Then \(k\le H<2k\), so the gap in phase is at most \(793/(91k)<1586/(91H)=122/(7H)\). Any interval of strictly larger length meets \(T_j\subseteq S_H\). This proves Theorem 1.

For Theorem 2, the exact periodic density in the \(y\)-chart is \(\rho=800/160160=5/1001\). Since \(dy=91k\,d\theta\), the phase intensity is \(\rho\cdot91k=5k/11\). Define the periodic discrepancy function \(F_j(y)=\#\{\text{mask points in }[0,y)\}-\rho y\), extended across periods. In each period, extrema occur immediately before or after a certified integer coordinate. Compute the exact rational values \(i-\rho y_i\) and \(i+1-\rho y_i\) at every sorted point \(y_i\), together with the period endpoints. For all 20 states the oscillation \(\max F_j-\min F_j\) equals \(812/143\) when \(j\) is odd and \(976/143\) when \(j\) is even. Thus for arbitrary interval \([a,b)\), subtracting the endpoint discrepancy gives
\[
E_j(I)=F_j(91kb)-F_j(91ka),\qquad |E_j(I)|\le976/143.
\]
This uses the full integer mask; it is unaffected by the positions of the interval endpoints. QED.

## Reproduction, exact scope and result ledger

Run \`python EC49FVN_MULTIDENOM_MESH_VERIFY.py\` with the Python standard library. The checker performs 12,100 direct projective comparisons; recomputes all 20 period masks (800 points each); checks their gaps and rational discrepancy oscillations; and crosschecks all three denominators directly for \(j=7,\dots,13\). Companion text \`EC49FVN_MULTIDENOM_MESH_OUTPUT.txt\` is the unedited captured execution output of that checker. No floating-point arithmetic or random search enters the proof.

Relevant exact outputs: periodic states \(j=11\ldots30\), 800 points/state; odd-state gap 696 and oscillation 812/143; even-state gap 793 and oscillation 976/143. Direct \(j=7,8,9,10\) gaps are 546,712,696,793. Terminal output: \`ALL PASS\`.

Science provenance: EC49FVM@e101e5110c533803bbb1fd91b070f6419303f5ff and its earlier EC49FVJ@34284e2c73c711c3ae80e53e762051b76c01b6cd. Current P000 V5 and ACTIVE Heartbeat/X6 remain unchanged; this is exact arithmetic in an externalized readout, not an untyped native physical computation. GitHub publication proves preservation only; author-level derivation has not undergone independent mathematical review.

## Next questions

Improve the effective covering constant by adding other fixed-ratio denominators and deriving an exact periodic mask, or determine a lower bound on the best fixed-family mesh. Investigate whether the four-prime \(90.4687\%\) certificate proportion admits a comparable uniform local estimate at scale \(w_H\gg1/H\). FUQ/FUR compound-minimax reduction and independent review remain open.
