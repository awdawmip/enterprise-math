# Stage175 — corrected off-diagonal exact full-real N14 minimax interval

**Status:** AUTHOR_EXACT / NOT_ADMITTED / EXTERNAL_N14_TERNARY_IID. A valid *diagonal* Stage175 dual certificate from Stage174 is **not** a primal continuation; this note proves an alternative non-diagonal interval. No native CLAIM, Source Result, independent Driver acceptance, six-dimensional P000 transfer, physical observation or Lean proof is claimed.

## Frozen provenance and scope

GLOBAL_KNOWLEDGE_V1 main `150f7544fae2920c2f3092d3602a2e3a59d2bc86`; Enterprise Math control/scientific main `6abbd1af7d754933d5aa2293e451e8e54dbfc4e7`; immutable Stage174 author branch source `4ce181fc49b127781d98c4734f8844d574fe5355`. The active P000 STARTUP projection was checked against original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`; ACTIVE residual-faithful worldview and portable research protocol were read.

Fix length N=14 and three-symbol IID distributions
[
P=(1/8,1/24,5/6),\quad Q=(1/12,1/12,5/6).
]
For any full-ordered-history randomized sequential policy with stopping time `tau<=14`, let `eP=P(decide Q)`, `eQ=Q(decide P)`, `tP=E_P(tau)`, `tQ=E_Q(tau)`. Define `V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ)`. Full-history policies form a finite product of simplices, so the minimum is attained. These are probabilities and times in an **external finite IID auxiliary model**, not native X6 Cell dynamics.

## 1. Exact obstruction to diagonal Stage175 from Stage174

The Stage174-published diagonal first-gap candidate is `K=L=4964732675352/21931669411`. Its Bellman equality states are `B=(6,3,3)` with actions Q/continue and `Z=(14,0,0)` with terminal P/Q. The prior `T=(8,2,0)` now has unique action P.

Write `b=P(choose Q at B)`, `z=P(choose Q at Z)`, with both in `[0,1]`. Exact independent suffix-DP/unmerged-DFS observations yield the only possible balanced-error equation
[
z(b)=\frac{413782840542005409}{409600000000000000}
-\frac{102742439843}{409600000000000000}b.
]
Even at `b=1`, `z(b)=206891368899782783/204800000000000000>1`. Since B and Z have disjoint first-hit cones and positive P,Q path masses, history-dependent coins reduce to weighted effective coins. Consequently *no Bellman-optimal policy for that diagonal candidate has balanced errors*. In particular its affine lower bound cannot be matched with both error constraints tight; Stage174 `dual175.json` remains a valid **dual-only** observation, not the requested primal theorem. This is an exact rational obstruction, not a numerical near miss.

## 2. Corrected non-diagonal dual ray and first closure

Retain the Stage174 equality `T=(8,2,0)`: P vs continue. At the Stage174 right endpoint `Z` already has uniquely selected Q (`z=1`), and `T` has fractional P-choice `t0=3537410849994591/7720251392000000`. The exact affine difference (P minus continue at T) for the current strict-action suffix is
[
-\frac{148561}{124416}+\frac{21205}{1679616}K-\frac{11069}{1492992}L.
]
Therefore preserve the T tie along
[
K(\varepsilon)=\frac{16044588}{70019}-\varepsilon,
\quad L(\varepsilon)=\frac{16044588}{70019}-\frac{169640}{99621}\varepsilon.
]
At positive epsilon, `L<K`, so terminal Z selects Q strictly. Exhaustively evaluate the affine action gaps for all 680 count states: the existing T gap remains zero, the Z gap opens strictly positive, and among 760 positive gaps with negative derivative the smallest root is
[
\varepsilon_*=\frac{11785669755441343155}{12738854379742782826}
]
at B=(6,3,3), action Q. All other gaps remain nonnegative along the segment.

At this first closure,
[
\boxed{K_{175}=\frac{41521222013193063}{181934251842254}},
\quad
\boxed{L_{175}=\frac{20701458469704504}{90967125921127}},
]
[
\boxed{H_{175}=\frac{53122292194902540973485450586445}
{311451660365537449574670532608}}.
]
Independent backward Bellman Fraction evaluation verifies **680 states, exactly two equality states T=P/C and B=Q/C, 1238 strictly positive gaps, zero negatives**, minimum positive gap `152464420746873000396113/3337744988485269306998784`. At state `s=(n,a,b)` the likelihood ratio is `ell(s)=2^(a+b)/3^a` and the exact Bellman recursion is
[
h(s)=\min\{K\ell(s),L,1+\sum_iP_i h(s+i)\},
]
with no continuation at n=14. Its one-step inequality holds *at each ordered prefix*; induction gives every full-history policy
[
t_P+K e_Q+L e_P\ge H,qquad V_{14}(\alpha)\ge H-(K+L)\alpha.
]

## 3. Exact primal construction and full-real theorem

Let `t` be P-decision probability at T (otherwise continue), `b` be Q-decision probability at B (otherwise continue), and all other actions follow the strict Bellman winner. Because T has two zero symbols and zero symbol-1 counts, while B has three zero symbols and three symbol-1 counts, **neither state can be an ancestor of the other**. The first-hit cones are disjoint. There are 28 first-hit ordered words at T with P-mass `109375/746496`, Q-mass `109375/1679616`, and 8 at B with P-mass `1/884736`, Q-mass `1/373248`. Thus
[
M(t,b)=(e_P,e_Q,t_P,t_Q)=M_{00}+t d_T+b d_B,
]
with a provably zero mixed coefficient. Exact four-corner observations from Fraction suffix DP and a separately implemented unmerged integer-mass DFS give
[
M_{00}=(306336326032364149/876488338465357824,18625316716453/53496602689536,1267557322258081771/109561042308169728,149481213853831/13374150672384),
]
[
d_T=(-1210671875/1114512556032,2319296875/1253826625536,-16248859375/92876046336,-9353640625/104485552128),
]
[
d_B=(85510363/3606947894919168,-2466149/160489808068608,-851291611/450868486864896,-49876445/13374150672384).
]
The two independently executed corner methods match in all four observables and both stop masses equal one. Unmerged DFS node counts for `(t,b)=00,01,10,11` are `285916,282916,282052,279052`, total **1,129,936**.

The unique balanced-error line is
[
\boxed{t(b)=\frac{3537410849994591}{7720251392000000}
+\frac{102742439843}{7720251392000000} b.}
]
Both coin probabilities are legal for **every real** `b in [0,1]`. At `b=0`, `t=t0`, the policy matches Stage174 at `alpha174=10295869835213079092569/29500515812940089131008` and `V174=677877812657492293580503/59001031625880178262016`. At `b=1`, it reaches
[
\boxed{\alpha_{175}=\frac{5147935054057228427975}{14750257906470044565504}},
\quad
\boxed{V_{175}=\frac{338938781942537717887145}{29500515812940089131008}}.
]
The width is
[
\Delta\alpha=\frac{90967125921127}{9833505270980029710336}>0.
]
For both endpoints the equality `eP=eQ` holds, P-time dominates Q-time with margins `20850768317972957412191/59001031625880178262016` and `10425404935270598468897/29500515812940089131008` (>0), and `tP+K eQ+L eP=H`. Since every observable is affine in b, these facts hold for all real b throughout [0,1]. The common error grows strictly and the time falls strictly.

**Theorem (full real interval).** For every real `0<=delta<=90967125921127/9833505270980029710336`,
[
\boxed{V_{14}(\alpha_{174}+\delta)
=V_{174}-\frac{82924138952602071}{181934251842254}\delta}.
]
The constructible policy meets the universal Bellman dual bound, proving equality for all real delta—not a grid.

**Strict right-support:** suppose `alpha>alpha175` attained equality with the *same* support line `H-(K+L)alpha`. Positivity of K,L and the inequality chain force both errors equal alpha, P-time dominance and Bellman-optimal actions at every reached positive-probability prefix. Away from T/B the winners are strict. Count-state likelihood-ratio constancy and identical optimal suffixes permit P-weighted averaging of possible history-dependent tie coins. Disjoint first-hit cones reduce them to the affine family above. Error equality forces `t=t(b)`, and legality `0<=b<=1` implies `alpha<=alpha175`, contradiction. This proves the **line**, not the full value function, is strictly below V14 to its right.

## 4. Verification, boundaries and next frontier

Actual Python Fraction suffix DP and distinct integer-numerator DFS independently checked four deterministic corners; all invariant assertions passed with the marker `STAGE175_CORRECTED_FULL_REAL_PASS`. Original executed code, exact JSON witnesses, stdout logs and the invalid diagonal scan obstruction are included in the locally retained author artifact. The repository reference checker preserves the essential formulas; remote file readback is evidence of storage, **not independent remote execution**.

BRC reuse: `REUSE_APPLIED` to positive rational labeled first-hit paths, separate P/Q masses and provenance-preserving observer semantics. This is not native BRC–Shor, does not prove X6 model/three-dimensional slice transfer, and grants no Foundation/Working Truth status.

A separate exact tangential scan retaining T=P/C beyond Stage175, with B now strictly Q, finds Stage176 **dual-only** first closure at W=(4,1,2), Q/C; all other 1238 positive gaps persist. See `NEXT_TASK_PACKET_176.md` and `dual176.json`. The unproved next question is the Stage176 original primal interval, not replaying this result.
