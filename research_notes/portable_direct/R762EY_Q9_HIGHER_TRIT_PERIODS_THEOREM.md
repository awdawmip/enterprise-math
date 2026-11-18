# R762EY — Exact q=9 third- and fourth-trit BRC terminal periods

Date: 2026-11-19. Frozen task RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142; taskbook Source 857280d1012943290d141d1317179c40ec3cbdf8, blob 218bf9ce05fd2dd79f477ac269fc3590f83f482e. Portable author-side continuation only; no new CLAIM or protected Source PROGRESS.

Let R=Z[(Z/9Z)^3], P=1+X+Z+XY+YZ+XYZ (six distinct named positive BRC branches), f(n)=max(0,floor(n/3)-2), and S_h(n)=[3^(-f(n))P^n] mod 3^h as the complete 729-component terminal coefficient vector. Antecedent R762ER supplies integrality. All three coordinates are retained.

**Theorem (conditional on the exact author-side R762EM/EO spectral statements and preceding mod9 period R762EX):**

| Precision | Minimum eventual period | Exact preperiod |
|---|---:|---:|
| h=1, mod 3 (R762ET) | 18 | 8 |
| h=2, mod 9 (R762EX) | 54 | 9 |
| **h=3, mod 27 (new)** | **162** | **14** |
| **h=4, mod 81 (new)** | **486** | **16** |

Thus
\[
S_3(n+162)=S_3(n)\quad(n\ge14),\qquad
S_4(n+486)=S_4(n)\quad(n\ge16),
\]
for all integer n in these ranges.

## Symbolic infinite extension

The 127-degree monic integer minimal polynomial mu9(T) of multiplication by P (R762EM) has exact Newton hull (1,58),(13,46),(37,30),(127,0) (R762EO). All nonzero roots have v3 at least 1/3 and the remaining zero root has v3 infinity. The elementary symmetric coefficient formula gives v3(c_j)>=ceil((127-j)/3) for each coefficient c_j of T^j with j<127.

Use the weighted recurrence lemma proved in R762EX: for L divisible by 3, a=L/3, E(n)=P^(n+L)-3^a P^n, and f(n)=floor(n/3)-2 for n>=6, any 127 consecutive checks
\[
E(n)\in3^{f(n)+a+h}R
\]
imply the same at all later n. Indeed mu9(P)=0 makes E(n+127)=-sum_{j<127}c_j E(n+j); the valuation bound v3(c_j)>=ceil((127-j)/3)>=f(n+127)-f(n+j) propagates the desired divisibility.

For h=3 choose L=162, a=54, and the 127 initial lengths n=14..140. For h=4 choose L=486, a=162, and n=16..142. All 127 full 729-coefficient vector equalities pass in both cases (92,583 per case, 185,166 total). The pure-integer checker evolves P^n through n=628 modulo 3^211; f(628)+4=211, so all normalized residues are exact. It checks 629 mass identities and 449,064 integer coefficient divisions. Thus both claimed period statements hold for **all** later n by induction, not solely the sampled n.

## Exact minimum period witnesses

Reduction of S_3 mod9 is S_2, whose minimum eventual period is 54 (R762EX). Since 162 is a verified tail period, its minimum period divides 162 and is divisible by 54, leaving 54 or 162. On the established tail, at endpoint (0,0,0), exact normalized values are
\[
S_3(15)[0]=15,\qquad S_3(69)[0]=24\quad (\bmod 27).
\]
Hence period 54 fails; minimum is 162. For S_4, reduction mod27 has minimum 162 and the established period is 486; the candidates are 162 and 486. The endpoint (0,0,0) gives
\[
S_4(16)[0]=37,\qquad S_4(178)[0]=10\quad (\bmod81).
\]
Thus minimum is 486. Every eventual period in each case is a positive multiple of the respective minimum.

## Exact earliest starts

For h=3, at endpoint (0,0,0), S_3(13)[0]=16 but S_3(175)[0]=7 mod27. All n=13+162t for t>=1 land on the proven stable tail and share the latter value, so no eventual period can start at n=13. It begins at 14.

For h=4, at endpoint (0,0,1), S_4(15)[1]=51 but S_4(501)[1]=24 mod81. All n=15+486t for t>=1 have the stable latter value, so no eventual period begins at 15; it begins at 16. QED.

## Reproduction, scope, remaining question

Run python3 R762EY_Q9_PRECISION3_4_VERIFY.py and compare with R762EY_Q9_PRECISION3_4_EVIDENCE.json. It uses the literal original six BRC shifts on all q^3 endpoints, modular integer arithmetic only, no floating point or state projection. This is an exhaustive exact *finite-window* certificate plus a conditional symbolic infinite extension. Inputs R762EM/EO, R762ET, R762EX are author-side NOT_REVIEWED; this contribution is AUTHOR_PROVED / EXACT_CERTIFICATE_PASS / NOT_REVIEWED, no formal checker.

The result concerns a positive terminal BRC observer, not native signed TRIADIC_CLOSURE_E Cell/Link/Port event permission or V17/V29/V39 future-operation-safe transfer. P000 and ACTIVE worldview and frozen science are unchanged.

Next: prove or refute the all-h precision pattern minimum T_h=18*3^(h-1) and determine exact precision-dependent preperiods. A possible tool is the 3-adic unit action of P^3/3 on the stabilized cyclic lattice, while a separate native-event construction must preserve original signed branch provenance.