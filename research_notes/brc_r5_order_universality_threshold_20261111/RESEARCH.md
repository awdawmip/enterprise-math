# R5 — exact universal-order threshold and the first two feasibility phases

Date: 2026-11-11 (Asia/Shanghai). Status: **researcher-side exact theorem + integer/Fraction computation**, not independent review or canonical Source Result. Model: the **frozen P/Q–BRC Blackwell auxiliary transport observer**, not native X6 dynamics.

## Frozen scientific provenance

- Global scientific pin: `a01383f825ef9d43b4b754254303298c64041568`.
- Enterprise Math scientific pin: `86149263e38c22292c9def1e0f69092efa1be77e`.
- Prior immutable R5 witness and fifteen atoms: `435e77af0d180eac32bd1f9c4c464bc4010b7551` (Draft PR #2102), files in `research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/`.
- All actual input fractions are inherited byte-for-byte from `VERIFY_R5_SHARP_RAY.py` at the cited parent commit. The added verifier imports that file from the stacked PR base, without silently changing the scientific input.

There are 28 dynamic nonnegative source/target masses, and fifteen **labeled** six-arc elementary atoms $M_a$, each separately in the exact observer kernel. The starting vector $X$ has every coordinate positive. The endpoint ray $Y(\varepsilon)=X+\varepsilon\sum_a M_a$ is nonnegative exactly for $0\le\varepsilon\le\varepsilon_{\max}=9/115400000$. The atom convention here includes the unscaled coefficient $c_{j,i}/36$, so that the parameter \(\varepsilon\) scales all fifteen moves.

## Theorem 1 — universal-order feasibility threshold (general finite lemma)

For any finite family of real coordinate moves $M_1,\ldots,M_m\in\mathbb R^d$ and strictly positive $X\in\mathbb R^d$, write
\[
L_k=\sum_{a=1}^{m}\max(0,-M_a[k]),\qquad
\varepsilon_{\rm all}=\min_{k:L_k>0}\frac{X[k]}{L_k}
\]
(with the minimum of the empty set interpreted as $+\infty$). **Every permutation** of the $m$ moves has all prefix states $X+\varepsilon\sum_{a\in S}M_a\ge0$ if and only if $0\le\varepsilon\le\varepsilon_{\rm all}$. The statement concerns all labeled permutations, not the existence of at least one legal ordering.

**Proof.** Each prefix of any permutation is a subset $S\subseteq\{1,\dots,m\}$. For fixed coordinate $k$, minimizing \(\sum_{a\in S}M_a[k]\) over all subsets picks exactly the negative coordinate contributions, giving \(-L_k\). All subsets can occur as prefixes of some permutation. Thus every prefix of every permutation is nonnegative exactly when $X[k]-\varepsilon L_k\ge0$ for all $k$. For \(\varepsilon>\varepsilon_{\rm all}\), the subset consisting of the negative contributors at a minimizing coordinate yields an illegal prefix, establishing sharpness. All moves separately preserve the observer here, so mass feasibility is the only remaining legality test. QED.

For the frozen fifteen atoms, exact computation yields
\[
\boxed{
\varepsilon_{\rm all}=
\frac{1401139989}{8472895976720000000}
},\qquad
\varepsilon_{\max}=\frac9{115400000}.
\]
The unique first bottleneck is coordinate `(target=0,source=3)`, flat index 14, with total negative contribution \(L_{14}=337/9\), and the unique critical subset is the five atoms `(5,1),(5,2),(5,3),(5,4),(5,5)`. In particular, **all** \(15!=1,307,674,368,000\) permutations are legal at and below the displayed threshold, whereas some become illegal immediately above it. This establishes the exact *order-universality radius* of this previously verified nonlocal ray.

## Theorem 2 — exact first two open phases and critical rational breakpoints

For any subset $S$, define the first coordinate-zero value
\[
\tau_S=\min_{k:\sum_{a\in S}M_a[k]<0}
\frac{-X[k]}{\sum_{a\in S}M_a[k]}\,,
\]
with \(\tau_S=+\infty\) if no coordinate decreases. The subset remains legal for the **closed** interval $0\le\varepsilon\le\tau_S$. Consequently the number $N(\varepsilon)$ of legal permutations is an integer-valued, nonincreasing **left-continuous step function** on $0\le\varepsilon\le\varepsilon_{\max}$, with changes only just *above* one of the finitely many rational \(\tau_S\). The last claim is for the rational frozen R5 model.

The exact integerized scan of all $2^{15}=32768$ subsets produces the first three distinct thresholds:

| Threshold | Exact value | Newly invalid subset mask immediately above threshold |
|---|---|---|
| \(\tau_1\) | \(1401139989/8472895976720000000\) | 31744: all five compensator-port-5 atoms |
| \(\tau_2\) | \(155682221/930258608720000000\) | 32256: those five plus \((2,5)\) |
| \(\tau_3\) | \(1401139989/8359756416200000000\) | 31748: those five plus \((1,3)\) |

Each threshold has exactly one attaining subset in this first-three census. In the open-closed phases \(\tau_1<\varepsilon\le\tau_2\) and \(\tau_2<\varepsilon\le\tau_3\), respectively, precisely one and two subsets are illegal. Hence inclusion–exclusion of orders with forbidden prefix sets gives:

\[
N(\varepsilon)=
\begin{cases}
15!=1307674368000,&0\le\varepsilon\le\tau_1,\\
15!-5!\,10!=1307238912000,&\tau_1<\varepsilon\le\tau_2,\\
15!-5!\,10!-(6!-5!)\,9!=1307021184000,
&\tau_2<\varepsilon\le\tau_3.
\end{cases}
\]

For the second change, all permutations starting with the six-element set in any order number \(6!9!\). The overlap with the first forbidden five-element prefix contributes \(5!9!\). Their difference is \((6!-5!)9!\), exactly as claimed. The first loss is \(5!10!=435456000\) legal permutations.

## Independent exact count checks at later ray positions

The verifier enumerates all subsets at each stated parameter, uses an exact common integer denominator to test every coordinate, and evaluates
\[
\mathrm{ways}(S)=1_{S\text{ feasible}}\sum_{a\in S}\mathrm{ways}(S\setminus\{a\})
\]
with \(\mathrm{ways}(\varnothing)=1\). It verifies:

| Parameter | Legal orders | Legal subsets |
|---|---:|---:|
| \(\varepsilon_{\rm all}\) | 1,307,674,368,000 | 32,768 |
| any interior point of \((\tau_1,\tau_2)\) | 1,307,238,912,000 | 32,767 |
| any interior point of \((\tau_2,\tau_3)\) | 1,307,021,184,000 | 32,766 |
| \(\varepsilon_{\max}/2\) | 3,663,483,824 | 7,164 |
| \(3\varepsilon_{\max}/4\) | 3,548,345,936 | 7,127 |
| \(\varepsilon_{\max}\) | 3,514,190,816 | 7,109 |

The endpoint tally reproduces the previous independent R5 order census of PR #2102. `VERIFY_ORDER_THRESHOLD.py` and the captured `EXACT_OUTPUT.txt` record all enumerations and check the exact identities. No floating point comparison, random sampling, or changed source/target label is used.


## Theorem 3 — the complete 1144-jump phase census, and the dominant discontinuity

For the unchanged fifteen labeled atoms, exact enumeration identifies **1,145 distinct rational first-zero thresholds** in the closed ray (the final threshold equals the endpoint), realized by 25,958 of the 32,768 atom subsets. All **1,144 interior thresholds** produce a strictly positive drop in the number of fully legal labeled permutations; there are **zero redundant interior feasibility thresholds** in this particular model.

To prove this as a finite exact classification, assign each subset $S$ a rank $r(S)$: the one-based position of its first-zero threshold among the 1,145 sorted rational values; use the sentinel 1,146 if no coordinate can reach zero within the closed ray. The exact signed integerization from Theorem 2 determines every rank.

For each integer $i=0,\dots,1144$, define $W_i(\varnothing)=1$ and
\[
W_i(S)=\mathbf 1_{r(S)>i}\sum_{a\in S}W_i(S\setminus\{a\}).
\]
Then $W_i(\{1,\dots,15\})$ counts the schedules valid **strictly above** the $i$-th interior threshold and up to the next one (when $i=0$ it counts all initial schedules). This equality is a bijection between labeled atom permutations and maximal Boolean-lattice chains, checked at each prefix by the exact nonnegativity condition. The verifier evaluates all 1,145 rank-cuts using integer additions and certifies that their 1,144 successive count differences are all **strictly positive**. In particular, the whole ordering-count step function has no unknown phases in this exact R5 ray.

The **single largest drop** occurs at interior phase index **607**:
\[
\varepsilon_{607}
=\frac{155682221}{377131868400000000},
\]
where the number of valid schedules falls from
\[
851207682192\quad\longrightarrow\quad470447833008,
\]
a loss of **380,759,849,184** schedules at one breakpoint. Intriguingly, this exact rational parameter is precisely the previously verified **lexicographically sorted fifteen-atom order's first failure point** in parent PR #2102; the numerical equality is checked against the previously frozen rational value, not inferred from floating-point coincidence. (The theorem states a phase-count equality, not that the sorted order alone causes all this loss.)

The endpoint count remains **3,514,190,816**. The ordered phase ledger, including all 1,145 rational thresholds and adjacent counts, is generated deterministically by `VERIFY_ALL_ORDER_PHASES.py`. `ALL_PHASES_SUMMARY.txt` contains the captured local exact output and a digest of a canonical ledger encoding for independent rerun comparison. The full ledger is algorithmically specified rather than copied into a long textual appendix.

All three theorems apply to the **fixed labeled fifteen-atom multiset** and its parameter ray. This establishes an exact scheduling phase diagram, not the minimal number of atoms between arbitrary positive hidden-fiber states. The parent R5 frozen scientific pins and source/target indices remain unchanged.

## New practical rule and next unresolved question

For a prescribed multiset of observer-preserving BRC atoms, the **universal scheduling radius** requires only \(O(md)\) coordinate additions: compute \(L_k\) then take the minimum ratio. Above that radius, existence and counting of *some* legal order remains a subset-DP problem; this R5 instance has at least 3,514,190,816 successful orders even at the endpoint. Distinguish *all schedules safe* from *at least one schedule safe*.

Next: compute an exact compact representation of the entire step function \(N(\varepsilon)\) over the ray (merge redundant threshold values and certify reachable forbidden-prefix cuts), then test whether the optimized scheduling approach can assist the still-open universal \(\le15\)-atom legal-connectivity question for **arbitrary** positive hidden-fiber endpoints. This note does not claim such a universal fifteen-step bound and does not change P000/native X6 claims.

No shared Task CLAIM or other researcher's owner state was changed. Formal Result admission and independent mathematical review remain pending.
