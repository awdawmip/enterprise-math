# R107 — Persistent rational atom refinement, equality leases, and an exact explicit-output lower bound

Date: 2026-11-13 (Asia/Shanghai). Continuation of R106 author-side frontier at immutable commit \`4f76a79dd7878573dd618728a6986d6d8d396865\`. Scientific input pin: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.

## Domain

This is the finite rational directed-circle source *auxiliary model* of R104–R106; it does not assert a bridge to native X6 dynamics. Complete source identities \(u=(t,branch)\) have integer coordinates and descending lexicographic rank. Fix \(\sigma=(j,x,a,b)\), with \(j,a,b\in\mathbb Z\), \(x\in\mathbb Q\), \(k\ge1\), and a rational closed interval \(I=[L,U]\) with \(L<U\). At \(\theta\in\mathbb R\), eligibility \(M_u(\theta)\) holds when \(\{x+(t-j)\theta\}\) lies in the directed half-open circular arc from \(\{a\theta\}\) to \(\{b\theta\}\); coinciding endpoints mean an empty arc. \(\operatorname{Top}_k(F,\theta)\) is the ordered descending list of up to \(k\) eligible complete identities.

For a finite source set \(V\), let \(K(V)\) contain \(L,U\) and all rational integer-crossing points in \(I\) of the six affine forms

\[
a\theta,\ b\theta,\ (t-j)\theta+x,\ (t-j-a)\theta+x,\
(t-j-b)\theta+x,\ (a-b)\theta
\]

for each \((t,branch)\in V\). Zero-slope forms contribute no isolated crossing. Every membership predicate is constant on each open gap between adjacent cutpoints; each cutpoint is its own singleton atom, and each gap has an exact rational midpoint representative.

## R107.1 — Hereditary refinement under finite source edits

Let old versions be \(F,G\), with \(V=F\cup G\), \(C=F\cap G\), \(\Delta=F\triangle G\). Suppose the old certificate has an exact cut list \(T\supseteq K(V)\), and stores for every old discrepancy \(u\in\Delta\), and old atom \(J\), either OUT or the **complete** higher-common-source guard fiber

\[
S_{\rm old}(u,J)=\{v\in C:v>u,\ M_v(\theta)\}.
\]

Consider *arbitrary* new finite versions \(F',G'\), and put \(V'=F'\cup G'\), \(C'=F'\cap G'\), \(\Delta'=F'\triangle G'\). Then

\[
T'=T\cup K(V'\setminus V)
\]

is a valid exact cut list for the new union. If \(r=|T'\setminus T|\), the number of singleton-and-gap atoms increases by exactly \(2r\). Each new atom \(J'\) belongs to a unique old atom \(P(J')\).

For a retained discrepancy \(u\in\Delta\cap\Delta'\), old OUT remains OUT on \(J'\). Otherwise, with \(\theta_{J'}\) the exact representative,

\[
S_{\rm new}(u,J')=
 \big(S_{\rm old}(u,P(J'))\cap C'\big)
 \cup
 \{v\in C'\setminus C:v>u,\ M_v(\theta_{J'})\}.
\]

For any newly discrepant \(u\in\Delta'\setminus\Delta\), calculate eligibility and all higher eligible common identities in \(C'\) directly on \(J'\). The new Top-k functions are equal on every \(\theta\in I\) **if and only if** every active discrepancy entry has at least \(k\) guards. Otherwise, an active entry with fewer than \(k\) guards supplies a rational difference witness \(\theta_{J'}\).

**Proof.** Every retained source in \(V'\cap V\) already had all its phase boundaries in \(T\); every newly present source in \(V'\setminus V\) contributes all its boundaries through \(K\). Each new gap therefore has constant eligibility. For a retained discrepancy, its own membership is unchanged by set edits, so the old OUT/IN status persists in the containing old atom. Old common guards retained in the new common set are exactly \(S_{\rm old}\cap C'\); the other possible guards are precisely the higher eligible sources newly entering the common set \(C'\setminus C\). Newly discrepant rows are evaluated directly. Apply the pointwise R104 rank-shield equivalence on each atom, including singleton boundaries. Each new interior cut replaces one open gap with two open gaps and one point, increasing the atom count by two. QED.

**Representation scope.** The attached reference implementation retains immutable old versions and reuses unchanged full guard-fiber objects, but allocates new row tuples. Up to \(O(|\Delta'|\,|T'|)\) certificate entries may be copied; it does not claim a logarithmic-time persistent balanced-DAG update. Exact rational bit operations and memory allocation remain relevant costs.

## R107.2 — Zero-refinement equality lease

For any finite \(F,G,H\), any real \(\theta\) and \(k\ge1\),

\[
\operatorname{Top}_k(F,\theta)=\operatorname{Top}_k(G,\theta)
\ \Longrightarrow\
\operatorname{Top}_k(F\cup H,\theta)=\operatorname{Top}_k(G\cup H,\theta).
\]

Hence a previously complete interval *equality* certificate remains sound after adding any same finite set \(H\) to both versions, without constructing new phase cuts or guard fibers. The added \(H\) can include an identity previously discrepant in exactly one version.

**Proof.** For any \(S,H\), \(\operatorname{Top}_k(S\cup H,\theta)=\operatorname{Top}_k(\operatorname{Top}_k(S,\theta)\cup H,\theta)\). Every eligible source excluded from \(\operatorname{Top}_k(S,\theta)\) was already dominated by at least \(k\) eligible identities of \(S\), none of which disappears after adding \(H\). Thus equal original Top-k lists induce equal lists after any shared addition. This argument holds at each real \(\theta\), proving the interval assertion. QED.

An immutable equality lease may retain a reference to the old certified equality and the newly added identities. Such a lease establishes equality, **not** a fully updated guard-incidence table. Before using a later common deletion to assert inequality, compute or validate any guards and cutpoints that were added lazily. An unequal pair may become equal after a common addition; the implication is not reversible.

## R107.3 — Lower bound on explicit atom enumeration

Fix \(\sigma=(0,1/4,0,1)\), \(I=[1/4,3/4]\), \(k=1\), initially \(F=G=\varnothing\). For integer \(T\ge4\), add the sole source \(u_T=(T,0)\) to \(F\). Its Top-1 discrepancy function changes eligibility at \(\Omega(T)\) points of \(I\), although the binary representation of \(T\) has \(\Theta(\log T)\) bits.

**Proof.** For each integer \(n\) such that \(\theta_n=(n-1/4)/T\in(1/4,3/4)\), the source phase is \(\{1/4+T\theta_n\}=0\), and the circular arc is \([0,\theta_n)\); the source is IN. With \(\varepsilon=1/(64T)\), the source phase just to the left is \(63/64>\theta_n-\varepsilon\), so it is OUT, whereas just to the right it is \(1/64<\theta_n+\varepsilon\), so it is IN. The interval contains \(\Omega(T)\) such distinct transition points. An explicit constant-output atom representation must distinguish these transitions; a symbolic membership query at a chosen rational parameter need not enumerate them. QED.

## Executable exact verification

The independent Python program \`check_r107.py\` uses standard-library \`fractions.Fraction\` for every mathematical comparison. In 34 seeded root histories it makes 374 branched edits: 10 positive equality leases and 364 full refinement updates. It checks all stored active guard fibers against direct current-source scans and compares exact Top-k lists at 28,952 rational atom representatives. It checks half-open singleton boundary \(\theta=3/4\), history persistence, and the explicit transition family \(T=N+1\) for \(N=7,31,127,255\).

Recorded output: \`R107_PASS 374 10 364 28952 4\`. Detailed exact counters are in \`verification_r107.json\`. The finite program validates the implementation in these cases; the theorems above have independent symbolic proofs. The encoded \`check_r107.py.gz.b64\` decodes via \`base64\` and \`gzip\` to the full script.

## Frontier and status

R107 is independently authored auxiliary-model research continuing the R106 source frontier. Frozen scientific input remains \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Source task authority, Researcher Activity checkpoint, CLAIM and independent review require separately verified receipts.

R108: construct a balanced persistent interval certificate DAG with demand-driven atom splits and equality leases. Compare sparse/dense point queries and edits in the \(\Omega(T)\) family; measure exact rational bit operations, updates, historical memory, witness recovery, and crossover versus R103 net overlay and full function materialization.
