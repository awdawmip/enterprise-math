# Stage140 — exact full-real sequential-test optimum and sharp right support (author)
 
**Research scope:** The external ternary iid horizon-14 test only, with arbitrary literal-prefix/history-dependent randomized stopping and binary decision. Author-level exact finite computation-assisted proof; no Research Driver independent acceptance, formal Source Result/CLAIM, P000/X6 or physical Heartbeat transfer.
 
## 1. Inherited exact author frontier
 
The model is P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14. A policy must stop and declare P or Q by depth 14. Define `eP=P(declare Q)`, `eQ=Q(declare P)`, `tP=E_P(tau)`, `tQ=E_Q(tau)`. Let `V14(alpha)` minimize max(tP,tQ) subject to eP,eQ<=alpha.
 
Stage139 author theorem (not independent Driver reviewed) gives
 
```
alpha139=12237333294307497565/35205614928358539264
V139=217197900202344934409/17602807464179269632
```
 
and the Stage139 support is right-sharp. At its right endpoint `C=(6,3,0)` has immediate-P probability 1 while `B=(11,0,1)` remains Q/continue mixed.
 
## 2. Theorem — every real parameter in an exact interval
 
For **all real** `0<=delta<=eta140`, with
 
```
eta140=24969022995875/1100175466511204352
```
 
the exact optimum satisfies
 
```
V14(alpha139+delta)=V139-(658636777856/696000641)*delta.
```
 
The exact right endpoint is
 
```
alpha140=12238132303043365565/35205614928358539264
V140=72273280897285196803/5867602488059756544
```
 
This supporting line is **strictly below** V14(alpha) for every alpha>alpha140. The statement does not claim infeasibility at higher alpha or a native-world theorem.
 
## 3. Universal dual Bellman lower bound
 
Take exact positive dual multipliers
 
```
K140=335982923928/696000641
L140=46093407704/99428663
K140+L140=658636777856/696000641.
```
 
For `s=(n,a,b)` with counts of symbols 0 and 1, `r(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a`. Backwards Bellman recursion is
 
```
H(s)=min{K140*r(s) [decide P], L140 [decide Q],
         1+sum_j P_j*H(child_j(s)) [continue when n<14]}.
```
 
Exact rational evaluation covers **all 680 count states**, with **1238 strictly positive** nonchosen action gaps, zero negative action gaps and smallest strictly positive gap `40470889820281/876760359475392`. The only two ties are
 
```
B=(11,0,1): decide Q or continue
F=(5,3,0): decide P or continue
```
 
and the exact root is
 
```
H0=2478452141684058136092975647/7262338635725166688075776.
```
 
Because the suffix laws and likelihood ratio of every literal history depend only on its counts under this specified iid experiment, the finite Bellman recurrence is a lower bound over **all** literal-history randomized rules:
 
```
H0 <= tP + L140*eP + K140*eQ
   <= max(tP,tQ)+(K140+L140)*alpha.
```
 
The policy comparison is valid for every prefix and every private randomization, not just policies choosing on count states.
 
## 4. Positive labeled branches and exact four-observer affine law
 
The literal-prefix BRC carrier retains ordered ternary word identity and exact positive weights P=(3,1,20)/24 and Q=(1,1,10)/12. Under the strict Bellman policy before any tie, actual first-hit word inventories are:
 
| Tie state | Literal first hits | P mass | Q mass |
| --- | ---: | ---: | ---: |
| B=(11,0,1) | 11 | 107421875/1451188224 | 107421875/725594112 |
| F=(5,3,0) | 10 | 125/9216 | 125/31104 |
 
The two tied cones are **disjoint**: F has three symbol-0 events whereas B has none and counts cannot decrease; B occurs at depth 11, later than depth-5 F. Thus no literal history hits both ties, so dual-optimal coin choices contribute without a bilinear interaction.
 
Let w∈[0,1] be the B immediate-Q probability and h∈[0,1] the F immediate-P probability. On all other states choose the unique Bellman-minimizing action, including immediate P at earlier tied Stage139 state C=(6,3,0), which is no longer tied.
 
With `M=(eP,eQ,tP,tQ)`, exact rational recursions yield
 
```
M(w,h)=M00+w*dB+h*dF
M00=(
 2429371427877190769/7011906707722862592,
 447547235823541/1283918464548864,
 10858963541677823711/876488338465357824,
 1273585294852433/106993205379072
)
dB=(
 4619140625/2229025112064,
 -751953125/417942208512,
 -25673828125/278628139008,
 -17939453125/104485552128
)
dF=(
 -1795416771625/24346898290704384,
 5693384375/53496602689536,
 -5812470087875/338151365148672,
 -3122642375/495338913792
)
```
 
A second author implementation enumerated ordered literal prefixes with **integer P/Q weights**, never propagating the four observer vectors by the Fraction Bellman quotient. It matched all four exact observer vectors at deterministic corners (w,h)=(0,0),(1,0),(0,1),(1,1); visited 672820, 672688, 650290, 650158 literal prefixes, respectively. Every corner had precisely 11 B hits and 10 F hits, with the displayed exact P/Q masses. The mixed four-corner defect is exactly the zero four-vector.
 
## 5. Continuous optimality by exact primal construction
 
Solving `eP=eQ` in the affine observer law gives
 
```
w(h)=44499628101323437/81438720000000000
     +(315830826757/6786560000000)*h.
```
 
Both endpoints lie inside [0,1]:
 
```
w(0)=44499628101323437/81438720000000000
w(1)=48289598022407437/81438720000000000.
```
 
For every **real** h∈[0,1], this is a valid behavioral policy, and exact substitution yields
 
```
eP=eQ=alpha139+eta140*h
tP=V139-(K140+L140)*eta140*h.
tP-tQ at h=0:
  83841137177769484807/158425267177613426688 > 0
tP-tQ at h=1:
  82703190692937556807/158425267177613426688 > 0
```
 
Since tP−tQ is affine and strictly positive at both endpoints, tP=max(tP,tQ) on the whole real interval. Furthermore exact substitution yields equality `tP+L140*eP+K140*eQ=H0`. Thus the policy family **attains the Bellman universal lower bound at every real parameter**, proving the theorem including both endpoints.
 
## 6. Strict right sharpness
 
The finite-horizon behavioral strategy space is a finite product of compact simplexes, so a feasible optimum attains. If the displayed support also attained at alpha>alpha140, positivity of K140,L140 and equality in both inequalities of the Bellman bound would require eP=eQ=alpha and all reached decisions Bellman-minimizing. The 1238 strict positive action gaps rule out all alternative actions except randomization at B and F. Even arbitrary literal-history-dependent coins average to two effective parameters w,h because the tied prefix cones are disjoint and the suffix laws are count-sufficient for this exact model. Equal errors force the displayed compensation w(h), and hence alpha=alpha139+eta140*h<=alpha140; contradiction. Therefore the right support is sharp.
 
## 7. Verification boundary, sources and next step
 
Locally executed: exact bottom-up Fraction Bellman/observer program and a different top-down integer-weight literal prefix DFS program; both passed all asserted exact equalities and four deterministic corners. The GitHub portable adaptation of the Stage139 checker saved beside this proof is not claimed byte-identical with either locally executed program or remotely executed by GitHub.
 
Fixed GLOBAL_KNOWLEDGE_V1 read snapshot: `161bf0e1b76d81ea489a1358996cbf749d840e1b`. This proof continues the immutable Stage139 author artifact `503260c9c3dfd8ba8919a51f9fa95fa7f3cb1093`; P000 was verified against original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`; ACTIVE residual-faithful worldview applies. Native control Task listing returned `CONTROL_QUOTA`; active owner, Task CLAIM, native Result and independent Research Driver validation are **unverified**. Do not promote the theorem to native P000/X6 or physical dynamics.
 
Stage141 exact question: From alpha140, F has immediate-P probability 1 but B remains mixed. Determine the next legal dual ray and action-gap closure. Check new tied cones, errors, feasibility of an affine primal interval and right sharpness, keeping this finite auxiliary scope.