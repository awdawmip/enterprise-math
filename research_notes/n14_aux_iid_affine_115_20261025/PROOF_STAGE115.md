# Stage115 — exact adjacent affine interval after Stage114 A saturation

**Status:** AUTHOR_EXACT_FINITE_PROOF; two separately written exact arithmetic implementations passed locally. This is not a native research Result, an independent Driver review, a P000/X6/Heartbeat theorem, or Foundation admission. Frozen reads: GLOBAL_KNOWLEDGE_V1 main@900a0332bcdcec62b3ba32fa4f3c26ecba3e3e0d; Enterprise Math main@bb10c4dbe1badc4adad436d075f2fd93f732e89c (prior to publication). Native owner control returned CONTROL_QUOTA and native session registration returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Formal owner/CLAIM/Result are unverified.

## Exact theorem and finite model

Let at most 14 ternary observations have iid laws
\[
P=(1/8,1/24,5/6), \qquad Q=(1/12,1/12,5/6).
\]
Stopping and terminal decision may be randomized and depend on the **entire ordered symbol history**. Define
\[
e_P=P(\mathrm{decide}\ Q),\ e_Q=Q(\mathrm{decide}\ P),
\quad t_P=E_P\tau,\ t_Q=E_Q\tau,
\quad V_{14}(\alpha)=\inf_{e_P,e_Q\le\alpha}\max(t_P,t_Q).
\]
The inherited author-proved Stage114 right endpoint is
\[
\alpha_{114}=\frac{900372060659842701793}{2592933255351443128320},
\quad
V_{114}=\frac{132764620121352969281069}{10371733021405772513280}.
\]
Put
\[
K=\frac{2533113}{2734},\quad
L=\frac{1181272}{1367},\quad
S=K+L=\frac{4895657}{2734},\quad
\eta=\frac{2712640625}{390765645398016}.
\]
**Theorem:** for **every real** \(0\le\delta\le\eta\),
\[
\boxed{V_{14}(\alpha_{114}+\delta)=V_{114}-S\delta.}
\]
The exact right endpoint is
\[
\boxed{\alpha_{115}=
\frac{900390060440962701793}{2592933255351443128320}},
\qquad
\boxed{V_{115}=
\frac{132635694365041929281069}{10371733021405772513280}}.
\]
This specific supporting affine line is **strictly below** the actual optimal value for every \(\alpha>\alpha_{115}\). We do not assert the optimal formula beyond this right endpoint.

## Full ordered-prefix Bellman dual certificate

At state \(s=(n,a,b)\), where \(a,b\) count outcomes 0 and 1, the conditional likelihood ratio is
\[
R(s)=\frac{Q(s)}{P(s)}=\frac{2^{a+b}}{3^a}.
\]
Set, in conditional P-units, at \(n<14\),
\[
H(s)=\min\left\{K R(s), L,\
1+\frac18H(n+1,a+1,b)+\frac1{24}H(n+1,a,b+1)
+\frac56H(n+1,a,b)\right\},
\]
omitting continuation at \(n=14\). The three actions mean stop/declaration P, stop/declaration Q, or continue. The direct exact-fraction enumeration evaluates all
\(\sum_{n=0}^{14}\binom{n+2}{2}=680\) count states and all their available actions. Its exhaustive result:

- exactly **1,238 strictly positive** non-minimizing action gaps, minimum \(11023/7086528\);
- zero negative gaps and exactly two tied states:
  \[
  D=(9,1,2):\ {\rm Qstop}={\rm continue},\quad
  E=(12,4,1):\ {\rm Pstop}={\rm continue};
  \]
- all other actions have unique minimizers;
- exact root
  \[
  H(0,0,0)=
  \frac{23760619012724853347605}{37442486208817004544}
  =V_{114}+(K+L)\alpha_{114}.
  \]

For **every** randomized rule depending on full ordered histories, induction on the full ordered-prefix tree (not restriction to count-only competitors) proves
\[
H(0,0,0)\le t_P+L e_P+K e_Q.
\]
The count state is sufficient **for the conditional iid future law and this four-moment objective**, since all histories with the same state have the same \(R(s)\) and conditional symbol laws. Consequently, for \(e_P,e_Q\le\alpha\),
\[
V_{14}(\alpha)\ge H(0,0,0)-(K+L)\alpha.
\]
Both dual multipliers are strictly positive. A sweep of the Stage114 D-tie dual ray produced this point when E's first strict gap closed; the independent full 680-state inequalities above, not the ray heuristic, establish global dual validity.

## Explicit primal family, full ordered first-hit carrier

At D, stop and declare Q with probability \(w\), else continue; at E, stop and declare P with probability \(v\), else continue. Elsewhere take the unique Bellman-minimizing action; in particular the Stage114 old A=(10,3,0) is now strictly Pstop.

The two genuine **ordered-history cones are disjoint**: D has already accumulated two symbol-1 observations, E only one, so D cannot precede E; E has depth 12 and D depth 9, ruling out the opposite ancestry. Distinct ordered words and their positive rational P/Q weights are retained before any moment-specific aggregation. Literal first-hit enumeration finds

| State | Ordered first-hit words | P-mass | Q-mass |
|---|---:|---:|---:|
| D=(9,1,2) | 172 | 671875/53747712 | 671875/20155392 |
| E=(12,4,1) | 3048 | 9921875/1146617856 | 9921875/2902376448 |

Conditional continuation moments \((e_P,e_Q,t_P,t_Q)\) at D are
\[
\left(\frac{97421}{98304},\frac{641}{248832},
\frac{51509}{36864},\frac{25831}{20736}\right),
\]
and at E they are
\[
\left(\frac1{576},\frac{143}{144},\frac{25}{24},\frac{13}{12}\right).
\]
Disjointness implies the root vector \(M(w,v)=(e_P,e_Q,t_P,t_Q)\) is **exactly affine** in \(w,v\), with zero mixed \(wv\)-coefficient. Exact derivatives:
\[
\partial_wM=\left(
\frac{593265625}{5283615080448},-
\frac{430671875}{5015306502144},-
\frac{34607609375}{1981355655168},-
\frac{17355203125}{417942208512}\right),
\]
\[
\partial_vM=\left(-
\frac{9921875}{660451885056},
\frac{9921875}{417942208512},-
\frac{248046875}{27518828544},-
\frac{128984375}{34828517376}\right).
\]
The exact Stage114 right endpoint is realized by
\[
(w,v)=\left(w_{114},0\right),\quad
w_{114}=\frac{170386233161181}{1042086080000000},
\]
where \(e_P=e_Q=\alpha_{114}\) and \(t_P=V_{114}>t_Q\).
Solving the **two actual error equations** \(e_P=e_Q\) yields
\[
\boxed{w(v)=w_{114}+\frac{637032}{3256519}v},
\qquad 0\le v\le1.
\]
Every intermediate pair is legal. The endpoint is
\[
(w_{115},v_{115})=\left(
\frac{374236473161181}{1042086080000000},1
\right).
\]
Thus **E saturates at Pstop probability 1**, while \(0<w_{115}<1\), so D is still mixed. For the entire real interval,
\[
e_P=e_Q=\alpha_{114}+\eta v,\qquad
t_P=V_{114}-S\eta v.
\]
Moreover \(t_P-t_Q\) is affine and positive at **both** endpoints:
\[
(t_P-t_Q)_{v=0}=
\frac{444777657503394885715}{691448868093718167552}>0,
\quad
(t_P-t_Q)_{v=1}=
\frac{444360026883234885715}{691448868093718167552}>0.
\]
Therefore \(t_P=\max(t_P,t_Q)\) at every real \(v\in[0,1]\). The constructed policies take only Bellman-minimizing actions, so they attain the global lower bound. This proves the whole claimed interval, not just a sampled grid.

## Sharp right endpoint for arbitrary history-dependent strategies

An optimal policy exists because the full finite-horizon randomized strategy space is compact. If some \(\alpha>\alpha_{115}\) attained the **same** affine dual line, strict positivity of \(K,L\) would force both \(e_P=e_Q=\alpha\), and Bellman equality would force every positive-mass decision to be a minimizer. Thus only D and E can be randomized. History-specific randomization at either count state can be averaged under the **positive P first-hit mass**: fixed \(R(s)\) makes this preserve Q mass too, and all conditional iid suffix moment laws coincide. This reduction is certified *only* for \((e_P,e_Q,t_P,t_Q)\) through horizon 14 and does not erase literal provenance or assert a universal path quotient. Their cones cannot interact. Accordingly all equality cases are parametrized by aggregate \(w,v\in[0,1]\). Error equality enforces the displayed \(w(v)\), and hence
\[
\alpha=\alpha_{114}+\eta v\le\alpha_{114}+\eta=\alpha_{115},
\]
contradiction. The exact right-sharpness statement follows.

## Executed evidence and limitations

The author ran two separately written implementations with **only exact integer/rational arithmetic**:

1. CHECKER_STAGE115.py: 680-state Fraction Bellman/action gaps, exact root and two real parameters, 1,238 positive gaps, two ties, precise first-hit mass, all identities and endpoints. PASS_STAGE115_EXACT_BELLMAN_680_1238_2_TIES_FULL_REAL_SHARP.
2. INDEPENDENT_ORDERED_STAGE115.py: constructs Bellman separately, traverses literal ordered prefixes at each of all four deterministic corners \(w,v\in\{0,1\}\), using path numerators over \(24^{14}\) under P and \(12^{14}\) under Q. Independently checks both ordered first-hit counts, both mass pairs, all eight derivative components and zero interaction. PASS_STAGE115_INDEPENDENT_INTEGER_LITERAL_DFS.

The source repository stores both portable reproduction programs and certificate115.json; local executed scripts, output logs, and complete extended proof are additionally in the user-accessible Stage115 ZIP. Source bytes were read back, **not remotely executed**, and independent Research Driver review is pending. BRC resolution is REUSE_APPLIED for positive rational ordered-history carriers; count-state compression has only the explicitly proved iid/four-observer/horizon-14 scope. No new native six-dimensional Cell assertion, signed cancellation result or infinite-horizon theorem follows.

**Stage116 next:** E is saturated at \(v=1\), D interior; sweep the next exact D-tie dual boundary with E strictly Pstop, find the next genuine tie and a full-real extension or a certified obstruction. Formal owner/CLAIM and mathematical admission remain separately pending.
