# S23/AV — universal inversion-charge rank identity and the four-displacement window

Date: 2026-11-08. Status: author-side exact derivation and finite implementation checks; independent mathematical review pending. Researcher session: `EM-DIRECT-EC5C10`, native activity `RA-30DF56E21A5303FA53D45870`; neither creates a formal CLAIM.

Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Continue the exact auxiliary two-point S23/AV threshold-order observer of PR #1777; retain the joint (label-1, label-4) count carrier and label-3 padding. Prior exact integer-key theorem and adjacent swap/four-point rotation: `research_notes/brc_s23_av_four_point_rotation_window_20261108_r1/PROOF.md` at `c43c0279fb4b53b7b7e0d53b1ae4836994fa382b`.

## Theorem 1 — exact finite-H rank via inverted displacement charge

Let `H>=0` be an integer and

```text
S_H = {(v,j) in Z_{≥0}^2: v+j <= H}
r = ln(7) / ln(10/7)
theta(v,j) = r*v-j
u = (79,431),  w=(380295,2074774),  M=|w|_1=2455069
P=2074774, D=380295
K(v,j) = P*v-D*j
L(v,j) = (K(v,j),-v), compared lexicographically
epsilon = 79*r-431 > 0
eta = P-D*r > 0
```

Write `rank_L` and `rank_theta` for *zero-based* ranks on `S_H`; no real-value ties occur. Form the finite displacement set

```text
D_H = {d=A*u+B*w :
        A,B positive integers,
        510*A+M*B <= H,
        A*epsilon < B*eta}.
```

Then for **every** `p in S_H`,

```text
rank_theta(p) = rank_L(p)
 + sum_{d in D_H} [p+d in S_H]
 - sum_{d in D_H} [p-d in S_H].                           (1)
```

Equivalently, letting `F(t)=#D_t` (zero if `t<0`) and

```text
G(v,j) = #{(A,B) in Z_{>0}^2 :
           A*epsilon < B*eta,
           79*A+380295*B <= v,
           431*A+2074774*B <= j},
```

one has the *inversion-charge identity*

```text
rank_theta(v,j) = rank_L(v,j) + F(H-v-j) - G(v,j).       (2)
```

The exact number of inverted *pairs* between the two full orders is

```text
I(H) = sum_{d in D_H} T(H-|d|_1),  T(n)=(n+1)(n+2)/2. (3)
```

This formula holds at **every finite H**, regardless of overlap between local inversion blocks. It reuses the previous floor-sum integer-key rank/select oracle without globally sorting the real thresholds. For large H the cost of computing `D_H`, `F` and `G` remains a separate algorithmic question; formulas (1)–(3) are exact finite identities, not a claim of globally constant complexity.

### Proof

1. Since `79*P-431*D=1`, every integer displacement `d` has a unique integer decomposition `d=A*u+B*w`, and `K(d)=A`, `theta(d)=A*epsilon-B*eta`. The ratio `r` is irrational: if `r=m/n` with positive integers, then `7^(m+n)=10^m`, impossible by prime factors. Thus distinct points have distinct `theta` values.
2. On the `K`-tie fibers, `d=B*w`: the ordering by `-v` agrees with the sign of `theta(d)=-B*eta`. For different keys choose the direction of positive key difference, `A>0`. If `B<=0` its real difference is positive, so there is no inversion. An inversion occurs exactly when `B>0` and `A*epsilon < B*eta`.
3. Such an inversion displacement has both coordinates positive. Its points `x, x+d` occur in `S_H` precisely for `x in S_{H-|d|_1}`. The lex order places `x` before `x+d`, whereas the true order reverses them. Consequently this inverted pair moves the true rank of `x` by `+1` and that of `x+d` by `-1`. Each discordant pair appears exactly once by the unique unimodular decomposition. Adding pairwise rank changes proves (1), and observing the outgoing condition `|p|_1+|d|_1<=H` gives (2).
4. The number of possible starts for any fixed inversion displacement is `|S_{H-|d|_1}|=T(H-|d|_1)`; summing proves (3). These pairwise arguments remain valid when numerous displacements overlap.

## Theorem 2 — exact rank/select to H=12,275,854

The established 45-term rational atanh logarithm enclosure in `VERIFY.py` certifies

```text
0 < eta < epsilon < 2*eta
2*epsilon > 3*eta.
```

Let `q_b = u+b*w` and

```text
H0 = |q2|_1 = 4,910,648
H1 = |q3|_1 = 7,365,717
H2 = |q4|_1 = 9,820,786
H3 = |2*q2|_1 = 9,821,296
H4 = |q5|_1 = 12,275,855.
```

For `H < H4`, the *complete* inversion set consists of precisely those directions in

```text
{q2, q3, q4, 2*q2}
```

whose Manhattan length is at most `H`. Thus the exact non-enumerative ranking correction (1) uses at most **four** vector tests for every integer `0<=H<=12,275,854`.

In particular:
- `H2<=H<H3`: the only directions are `q2,q3,q4`; this resolves the first `q4` overlap window.
- `H3<=H<H4`: the directions are `q2,q3,q4,2*q2`; this also resolves the first double-`q2` inversion window.
- At `H=H4`, `q5` is the next new inversion direction, so this exact four-direction list is sharp.

**Proof of completeness.** For an inverted displacement `A*u+B*w`, the condition from Theorem 1 forces `A,B>=1`. For `H<H4=510+5M`, necessarily `B<=4`. If `B=1`, no `A>=1` works because `epsilon>eta`. If `B=2`, only `A=1` works because `epsilon<2eta<2epsilon`. If `B=3`, only `A=1` works because `2epsilon>3eta`. If `B=4`, `A=1,2` work, whereas `A>=3` do not because `3epsilon>4eta`. Feasibility by Manhattan cost gives exactly the stated entrance horizons. At `H=H4`, `q5` enters since `epsilon<5eta`.

Define `m(H)` as the number of feasible directions (at most four in this range). For any requested zero-based true rank `i`, the desired point must have original `L` rank among `max(0,i-m),...,min(|S_H|-1,i+m)`, because equation (1) changes each rank by at most `m`. Query at most `2m+1<=9` candidates through the existing exact `L` select oracle and return the unique point satisfying corrected rank `i`. This gives exact *select* as well as rank through `H4-1`. Cost: at most nine base-select calls plus a fixed number of integer triangle tests; integer bit arithmetic and the base oracle's own cost remain included.

For this full interval, equation (3) reduces to the finite formula

```text
I(H) = sum_{d in {q2,q3,q4,2q2}, |d|_1<=H}
       T(H-|d|_1).
```

At `H=12,275,854` it equals **45,203,985,098,054** inverted pairs, established by exact integer evaluation.

## Validation and scope

`VERIFY.py` independently checks the earlier logarithm interval using rational atanh partial sums and rigorous tails. It compares the general formula against complete true/lex sorting of all `H=0..35` in a scaled unimodular model `u=(1,1),w=(2,3),r=61/44`, covering **8,436** exact point-rank checks and all corresponding inversion totals. At five actual S23/AV boundary horizons it enumerates only the *finite admissible lattice directions* with exact rational endpoint comparisons; it does not enumerate trillions of threshold states. Actual execution output is in `RUN_EVIDENCE.txt`.

BRC reuse: `REUSE_APPLIED` for the existing joint (1,4) label-count carrier and integer lattice ordered-readout; signed orientation and simultaneous pair provenance remain explicit. This is a precise result for the auxiliary observer's order/rank/select interface; no new mother-model decoder, minimax error, or capacity plateau assertion is made. The source task remains frozen at its original scientific pin. Authorship and math review are separate.

## Next discriminating questions

1. At `H=12,275,855` add `q5` and derive a fast exact count for `F(H-|p|_1)` and `G(v,j)` avoiding all direction enumeration; the universal identity survives unchanged.
2. Apply the strengthened rank/select to incremental prefix occupancy of all newly split gaps at `H=2,455,579`; determine whether the known seventh platform's `N(H)` rises.
3. Retain the distinct lawful six-source ten-label observer bridge and four-observation minimax `delta_4` as unresolved mother-objective units.

Historical source: prior theorem `c43c0279fb4b53b7b7e0d53b1ae4836994fa382b`; applicable current norms read from project main `e488f46541858937efdee71476ba966dc564931e` and GLOBAL_KNOWLEDGE main `27fe8c04627244368991bfb36235db8d4c5e3ea1`. Review status: author-side derivation plus actual arithmetic execution; independent admission pending.
