# R749SPM — exact sharpness of the original Walsh zero-center wedge

**Date:** 2026-11-15. **Status:** AUTHOR_EXACT_NOT_REVIEWED. **Frozen source:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. **Predecessors:** R749SPK (PR #2443), R749SPL (PR #2446). This is the complete sixteen-atom auxiliary compatible Walsh model.

## 1. Exact theorem (all real parameters)

For k in F₂⁴, χ_m(k)=(-1)^{popcount(k&m)}, and
\[
p_{t,s,h,u,v,w,z}(k)=
\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]
Let F(t,s) be the complete nonnegative same-(t,s) fiber. Restrict to the closed half-triangle \(S=\{0\le t\le s,\ t+s\le1\}\). Set the **specific** feasible same-fiber center \(q_0(t,s)=p_{t,s,0,0,0,0,0}\) and \(R_0(t,s)=\max_{P\in F(t,s)}TV(P,q_0)\).

**Theorem:**
\[
\boxed{R_0(t,s)\le\frac{1-t}{2}
\quad\Longleftrightarrow\quad
s\ge2t\ \land\ s+3t\le1.}
\]

On the right-hand-side triangle \(T=\operatorname{conv}\{(0,0),(0,1),(1/5,2/5)\}\), R749SPK proved \(R_0=(1-t)/2\), and the same radius is the free and calibrated optimum. Outside T, the following exhaustive four classes have **compatible full sixteen-atom witnesses** whose risk strictly exceeds \((1-t)/2\). The theorem describes sharpness of this specific center/radius, not the global calibration-gap classification outside T (R749SPL explicitly repairs part of that region).

## 2. Exact full-source BRC identity

Write \(a=\chi_3,b=\chi_{12},c=\chi_1,d=\chi_4\), so
\(16p_{abcd}=M_{ab}+cU_a+dV_b\), with \(M_{ab}=1+at+bs+abh\),
\(U_a=u+av\), \(V_b=w+bz\). Complete source positivity is **equivalent** to
\(M_{ab}\ge|U_a|+|V_b|\) for all four blocks. Against q0,
\[
TV(P,q_0)=\frac18\sum_{a,b=\pm1} H(|h|,|U_a|,|V_b|),
\qquad
H(A,B,C)=\max\{A,B,C,(A+B+C)/2\}.
\]
This sums all sixteen source atoms, without changing provenance or coefficients.

Define \(r=(1-t)/2\). We partition all of \(S\setminus T\) as follows.

### Case A — s<2t

Take \(P_A=p_{t,s,h,0,0,0,0}\) with \(h=1+t-s\). Four BRC masses ordered (++),(+-),(-+),(--) are
\(2+2t,0,2(s-t),2(1-s)\), all nonnegative on S.
Therefore
\[
TV(P_A,q_0)=\frac{1+t-s}{2}
=r+\frac{2t-s}{2}>r.
\]

### Case B — s≥2t, s+3t>1, t+s<1, s≤1−2t

Take \(P_B=p_{t,s,-t,0,0,1-t,t+s}\).
Then \(U_+=U_-=0\), \(V_+=1+s\), \(V_-=1-2t-s\ge0\).
The BRC masses are \(M_{++}=M_{-+}=1+s\),
\(M_{--}=1-2t-s=V_-\),
\(M_{+-}=1+2t-s\ge V_-\).
Since \(s+3t>1\), \(t>V_-\), so
\[
TV(P_B,q_0)=\frac{1+s+t}{4}
=r+\frac{s+3t-1}{4}>r.
\]

### Case C — s≥2t, s+3t>1, t+s<1, s>1−2t

Take \(P_C=p_{t,s,t+s-1,0,0,1-t,1-t}\).
Then \(V_+=2(1-t),V_-=0,h=t+s-1<0\).
Its BRC blocks satisfy \(M_{-+}=2(1-t)=V_+\),
\(M_{++}=2(t+s)>2(1-t)=V_+\) because \(s+2t>1\),
and \(M_{+-}=2(1-s)\ge0,M_{--}=0\).
Thus
\[
TV(P_C,q_0)=\frac{3-3t-s}{4}
=r+\frac{1-t-s}{4}>r.
\]

### Case D — t+s=1, t>0

Take \(P_D=p_{t,s,0,t,t,s,s}\). Its BRC components are
\(U_+=2t,U_-=0,V_+=2s,V_-=0\).
All four BRC source inequalities saturate:
\(M_{++}=2=2t+2s\),
\(M_{+-}=2t,M_{-+}=2s,M_{--}=0\).
Since \(s\ge t\), \(H(0,2t,2s)=2s\), giving
\[
TV(P_D,q_0)=\frac{2s+t}{4}
=r+\frac t4>r.
\]

The cases exhaust S\T: if s≥2t and s+3t>1, distinguish the top edge from the strict interior, then split the interior by s≤1−2t. All are explicit full probability sources, so strict outside excess holds for every real point.

## 3. Sufficiency and replication

For (t,s)∈T the R749SPK exact 82-vertex joint rational polytope calculation and convexity prove \(R_0\le(1-t)/2\) for every real parameter. The source diameter pair of total variation \(1-t\) proves the matching lower bound. This completes the iff.

The accompanying stand-alone exact Fraction Python script tests full sixteen-atom normalization, positivity, risk, the witness formulas and strict excess over the 1/40 rational grid for every outside-T point in S. **252** pairs checked: A 140, B 42, C 57, D 13. Maximum arithmetic error 0, PASS. This finite check independently supports the algebra; the universal proof is the complete four-case symbolic argument above plus R749SPK's sufficiency theorem.

**Next:** determine full minimax radii and whether g>0 on diagonal s=t just beyond t=1/5 using exact multi-source dual certificates and matching full-source upper bound. Maintain native X6/V29/V39 correspondence as separately open.
