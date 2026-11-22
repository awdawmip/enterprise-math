# X6 R121 — Exact small-Port optimizer: complete 18-row six-pair Pareto certificate

Date: 2026-11-23 (Asia/Shanghai). Mathematical status: **AUTHOR FINITE EXHAUSTIVE PROOF / EXACT INTEGER REPLAY PASS / NOT INDEPENDENTLY REVIEWED**.
This is the conditional four-positive-weight, six-pair BRC integer observer of R119–R120; native X6/P000 time-dynamics and R063 remain separate. Do not repin the task's scientific inputs.

## Problem closed: integer Port 1–10

For each nonzero integer triple \(\boldsymbol a=(x,y,z)\), define
\[
q(\boldsymbol a)=\max\big(\sum_{i=1}^3\max(a_i,0),\ \sum_{i=1}^3\max(-a_i,0)\big).
\]
The four heights are
\[
h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z).
\]
For arbitrary **positive real** channel weights \(w=(A,B,C,D)\), let
\[
s=(A+B,A+C,A+D,B+C,B+D,C+D),\quad
F_w(a)=\max_{j=1}^6 g_j(a)/s_j
\]
with all six gap numerators \(g=(|h_1-h_0|,|h_2-h_0|,|h_3-h_0|,|h_2-h_1|,|h_3-h_1|,|h_3-h_2|)\).
Set \(\eta_p(w)=\min_{0<q(a)\le p}F_w(a)\), identifying \(\pm a\).

**Theorem (universal small-Port optimizer).** Let \(\mathcal B\) denote the following set of 18 integer triples. Then for every choice \(A,B,C,D>0\) and every integer \(1\le p\le10\),
\[
\boxed{\eta_p(w)=\min_{\substack{a\in\mathcal B\\q(a)\le p}}\max_{1\le j\le6}\frac{g_j(a)}{s_j}.}
\]
The bank is a union of all exact componentwise Pareto frontiers of six-gap vectors for Port 1–10. It is *Pareto-covering*, and no claim is made that all 18 members are separately needed for some admissible physical weight vector. It is a fixed universal candidate list valid without sorting or relabeling the four weights.

| Integer direction \(a=(x,y,z)\) | First Port | Port phases on which it is Pareto-minimal | Six exact gap numerators \(g\) |
|---|---:|---|---|
| (1,0,0) | 1 | 1–10 | (1,3,7,2,6,4) |
| (0,2,-1) | 2 | 2–2 | (0,6,48,6,48,42) |
| (1,-3,1) | 3 | 3–3 | (2,3,16,1,18,19) |
| (2,-3,1) | 3 | 3–3 | (1,0,23,1,24,23) |
| (3,-1,0) | 3 | 3–6 | (0,3,18,3,18,15) |
| (1,3,-1) | 4 | 4–4 | (4,9,2,5,6,11) |
| (3,-4,1) | 4 | 4–10 | (3,9,9,6,6,0) |
| (4,-1,0) | 4 | 4–10 | (1,0,11,1,12,11) |
| (3,2,-1) | 5 | 5–6 | (3,3,27,0,30,30) |
| (4,-4,1) | 5 | 5–10 | (2,6,2,4,0,4) |
| (5,-1,0) | 5 | 5–10 | (2,3,4,1,6,7) |
| (5,-4,1) | 6 | 6–10 | (1,3,5,2,6,8) |
| (6,-1,0) | 6 | 6–10 | (3,6,3,3,0,3) |
| (3,-7,2) | 7 | 7–10 | (6,15,0,9,6,15) |
| (6,-4,1) | 7 | 7–10 | (0,0,12,0,12,12) |
| (7,-1,0) | 7 | 7–10 | (4,9,10,5,6,1) |
| (7,2,-1) | 9 | 9–10 | (7,15,1,8,6,14) |
| (9,-5,1) | 10 | 10–10 | (0,3,6,3,6,3) |

The phase-column is descriptive of the Pareto frontier, not a constraint on using the universal formula: filter only on the **First Port** column.

## Proof and finite-domain certificate

1. Every vector with \(q(a)\le10\) has \(|x|,|y|,|z|\le10\). The nonzero \((x,y,z)\in[-10,10]^3\cap\mathbb Z^3\) are exhausted by three nested integer loops. Exactly one of \(\pm a\) has first nonzero coordinate positive; retaining that representative yields the full unoriented population and preserves all six gaps.
2. For two representatives \(a,b\), if \(g_j(b)\le g_j(a)\) for all six \(j\), then for every \(w>0\), \(F_w(b)\le F_w(a)\). This implication requires only positivity of all six pair capacities, and retains *every* joint observation.
3. The attached independent executable enumerates the full population for each integer \(p=1,\ldots,10\), computes \(g\) using only integers, compares **all** ordered candidate pairs, and extracts precisely the nondominated rows. The union of these fronts is the displayed 18-row bank. As a second check, for *every* feasible \(a\) at *every* \(p\), the program explicitly finds at least one bank row \(b\) with \(q(b)\le p\) and \(g(b)\le g(a)\) componentwise.
4. Therefore \(\min_{\text{bank feasible}}F_w\le\min_{\text{all feasible}}F_w\) by domination, and the reverse inequality is automatic because every bank row is a genuine feasible integer vector. Equality follows for every positive real \(w\), including strict ties and all boundary weights.

The finite calculation is a complete certificate because the search domain covers every integral vector allowed by the Port bound, the sign quotient is exact, and all comparison predicates use integer arithmetic; the second domination check avoids reliance on only the reported front sizes.

| Integer Port \(p\) | Unoriented nonzero directions examined | Exact Pareto-front size |
|---:|---:|---:|
| 1 | 6 | 1 |
| 2 | 27 | 2 |
| 3 | 73 | 4 |
| 4 | 154 | 5 |
| 5 | 280 | 7 |
| 6 | 461 | 9 |
| 7 | 707 | 10 |
| 8 | 1028 | 10 |
| 9 | 1434 | 11 |
| 10 | 1935 | 12 |

At Port 10 exactly **1,935** unoriented directions are covered; the universal bank contains **18**, and the Port-10 Pareto frontier contains **12**. The exact replay is research_notes/portable_direct/x6_r121_small_port_optimizer_verify.js (run \`node x6_r121_small_port_optimizer_verify.js\`) with reported output research_notes/portable_direct/x6_r121_small_port_optimizer_certificate.json. An independently constructed local Python integer enumeration of the same 1–10 domains reproduced the counts/front sizes and bank membership; the published JavaScript is the persistent complete replay.

## How this connects to the current frontier

The existing [R120 all-Port optimizer](https://github.com/awdawmip/chatgpt-global-knowledge/blob/23327fe6dcfaf86f8ad5cfa31b58d05e2387292a/journal/enterprise-math/2026-11-23/x6-r120-all-port-optimum-and-ten-bank.md) covers all integer Ports **p≥11**, with four layout-dependent witness tables and their own Port thresholds. This result supplies the missing **p=1–10** segment, yielding a finite exact evaluation rule for *every* integer Port p≥1 in the same four-positive-weight observer. This is an optimization theorem, **not** an exact near-optimal direction atlas: dominated non-optimal rows can still be strictly 3/2-near.

Provenance: R119 exact height/Port/moment definitions at \`a025ec1bac8846cf684613aea7ed0d82dff6ba8b\`, R120 at \`ca85b7dc0568cd9d4a832a38360380866798f403\`. Source read: Enterprise Math main \`cb3dc62b80b808781d5fe9058a4f0d657ed8e2f3\`; global normative snapshot main \`a978ec6f4db62e865cf219a1b982f72375efcd57\`; applicable P000 V5, ACTIVE Heartbeat World, BRC and research-method policies were loaded. All numerical claims use exact integer arithmetic.

**Next:** determine the minimal actual optimizer bank under the constrained six pair-capacity sums (as opposed to coordinatewise domination), or classify the complete strict 3/2 near-direction atlas at Ports 1–10. Original X6 time-dependent R063 six-file benchmark remains pending under its native owner and frozen pins.
