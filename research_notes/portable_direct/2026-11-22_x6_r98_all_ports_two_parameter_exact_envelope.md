# X6 R98 — Entire two-parameter positive-count BRC optimum for all Port budgets p≥11

Date: 2026-11-22 (Asia/Shanghai).
Status: SYMBOLIC_AUTHOR_PROOF / EXACT_INTEGER_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Research scope: **conditional positive-count four-channel BRC star-moment histogram observer** under an unknown common offset, not a native X6 heartbeat/triadic-force/Cell/Link observer.

## Scientific provenance and source firewall

This note extends the newly verified R97 theorem (port budgets 11–26), \`research_notes/portable_direct/2026-11-22_x6_r97_port11_26_two_parameter_exact_minimum.md\`, itself continuing R96. Frozen source input remains the R96 pin \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`; current P000 V5, ACTIVE account worldview, project joint-observer preservation and current portable research behavior rules are separately respected. A result in the conditional count observer does not provide a native Cell/path/time fiber-preservation map. No P000 or protected world changes.

## Exact model

For unoriented nonzero \`a=(x,y,z)∈Z³\`, write

\[
q(a)=\max\left\{\sum_i\max(a_i,0),\ \sum_i\max(-a_i,0)\right\},\quad
u=x+3y+6z,\quad v=3x+12y+30z,\quad h=7x+39y+126z.
\]

Let \`S,T≥1\` be arbitrary **real** weights, \`w=(1,1,S,T)\`, and

\[
F(a)=\max\left\{
\frac{|u|}{2},\frac{|v|}{S+1},\frac{|h|}{T+1},
\frac{|v-u|}{S+1},\frac{|h-u|}{T+1},\frac{|h-v|}{S+T}
\right\},
\qquad
\eta^*(p)=\min_{0\ne a\in\mathbb Z^3,\ q(a)\le p}F(a).
\]

## Theorem — complete exact value, every integer p≥11

Define

\[
E_0=\tfrac12,\quad E_d=\frac{12}{T+1},\quad
E_b=\max\left(\frac3{S+1},\frac6{T+1}\right),\quad
E_c=\frac6{S+1}.
\]

Then for every real \`S,T≥1\`,

\[
\boxed{\eta^*(p;S,T)=
\begin{cases}
\min(E_0,E_d,E_b),&11\le p\le26,\\
\min(E_0,E_d,E_b,E_c),&p\ge27.
\end{cases}}
\]

The witnesses are the four exact vectors:

| Vector | (u,v,h) | q | F |
|---|---|---:|---|
| \`s=(10,-5,1)\` | (1,0,1) | 11 | \(E_0\) |
| \`d=(6,-4,1)\` | (0,0,12) | 7 | \(E_d\) |
| \`b=(9,-5,1)\` | (0,-3,-6) | 10 | \(E_b\) |
| \`c=(24,-14,3)\` | (0,-6,0) | 27 | \(E_c\) |

**The full two-dimensional optimal value is thereby closed**, including all Port budgets \`p≥11\`. Once \`p≥27\`, increasing the Port budget can change tie multiplicities but cannot lower the optimal value. No claim is made that the four witnesses list every tied direction.

### Universal proof (no finite-truncation assumption)

The exact inverse moment map (R96/R97) is

\[
(x,y,z)=\left(
\tfrac{h+19u}{2}-4v,\
\tfrac{-h-14u+7v}{3},\
\tfrac{h+11u}{12}-\tfrac v2
\right).
\]

It follows that \(v\in3\mathbb Z\) and \(h-u\in6\mathbb Z\).

**Case I: \(u\ne0\).** The first gap gives \(F\ge1/2\). At \(S,T\ge1\), \(s\) attains exactly \(1/2\).

**Case II: \(u=0,v=0\).** The inverse forces \(h=12k\) and \(a=k(6,-4,1)\). Every nonzero member costs at least \(12/(T+1)\), attained by \(d\).

**Case III: \(u=0,h=0,v\ne0\).** The inverse forces \(v=6k\), \(a=k(-24,14,-3)\), and \(q(a)=27|k|\). Every such direction costs at least \(6/(S+1)\), attained by \(c\) when \(p\ge27\); the entire case is unavailable for \(p\le26\).

**Case IV: \(u=0,v=h\ne0\).** The inverse forces \(v=h=12k\), \(a=k(-42,24,-5)\), \(q(a)=47|k|\). Consequently
\[
F(a)\ge\max\left(\frac{12}{S+1},\frac{12}{T+1}\right)
\ge\max\left(\frac3{S+1},\frac6{T+1}\right)=E_b.
\]
Thus even after such directions become feasible, they cannot improve the optimum.

**Case V: \(u=0,v\ne0,h\ne0,v\ne h\).** Since \(v\in3\mathbb Z\), \(h\in6\mathbb Z\), and \(h-v\in3\mathbb Z\), their nonzero magnitudes obey \(|v|\ge3,|h|\ge6,|h-v|\ge3\). In particular \(F(a)\ge E_b\). Equality is attained by \(b\), since \(S+T\ge S+1\).

The five cases exhaust all nonzero integer directions. The four attainers are feasible at the stated Port cutoffs, proving both formulas. ∎

## Sharp Port onset and concrete comparison

At \((S,T)=(100,12)\), the exact minimum is \(\eta^*(26)=6/13\), but \(\eta^*(27)=6/101\): admitting \(c\) creates a genuine strict improvement at precisely 27 Port. In contrast, for all \(\ p\ge27\) the value remains fixed. This **does not** imply a universal four-direction core for arbitrary four weights: the family \((1,1,S,T)\) is a two-dimensional section of the general four-weight problem.

The R97 lower-Port result remains valid unchanged. R98 newly disposes of the unbounded Port tail, including the \(\ h=v\) integer stratum that first becomes feasible at 47 Port.

## Author verification and limitations

A new independent exact integer-scaled evaluator enumerated every one of **110,740** unoriented nonzero differences with \(q\le40\), and tested **16** integer-weight pairs at budgets \`11,15,26,27,28,38,40\` (**112** exact checks); all passed. Source file \`x6_r98_all_ports_two_parameter_verify.py\` and result JSON \`x6_r98_all_ports_results.json\`. The universal theorem is the symbolic case proof, not the sampled finite check. No independent mathematical review, Lean certificate, Source Result or formal Task admission was obtained.

Boundary: this is a typed positive-count histogram observer of a conditional BRC model. It does not preserve/validate native six-axis Cell identity, signed phase, triadic-force closure, path/branch/multiplicity provenance or heartbeat time, and thus is not a proof of their physical evolution or a certified native quotient. The project P000 and its native-time research frontier are unchanged.

## Remaining problem

Determine **all** tied optima (not only the value) on the four-function switch walls, with Port-sensitive multiplicities; in parallel, find a native, future-operation-safe observer-fiber preservation bridge from the full P000 state to any proposed BRC histogram statistic. Current active owner/CLAIM and Activity linkage must be resolved through the original control authority, not inferred from this GitHub scientific publication.
