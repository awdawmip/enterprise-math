# EC49AG — Sharp global causal support on a new eta interval

2026-10-29. Author-side context-exposed TASK_RESEARCH continuation of EC49AF. Scientific status: AUTHOR_PROVED / EXACT_BIGINT_CHECK_PASS / UNREVIEWED / NOT_ADMITTED.

## Precise model and result

For w,z∈{0,1,2}, u∈{0,1}, real 0≤η<1/2, define t(w,u)=1/2+(2u−1)(1−w)η, P(w,u,z)=t(w,u)(1/6 if z=w, otherwise 1/12), and Q(w,u,z)=t(w,u)/9. Each source has 18 normalized, strictly positive leaves. The observer knows w only when choosing STOP,A0,A1,B0,B1 (costs 0,1,1,2,2), then erases w and its strategy seed. It observes u on paid branches, chooses whether to buy S (cost 1) based only on observable (c,u), then uses fresh private randomness for acceptance after seeing z if bought. There is no stored shared random seed. Impose source-identical expected costs C1=43/48 and C2=7/8.

Let α=P(accept), β=Q(accept), H=α−(177/172)β, and [r]_+=max(0,r). Fix the lawful prefix X: w0→A0; w1→A1; w2→(9/16)A0+(1/16)B0+(3/8)STOP. After a paid action X always buys S, and accepts exactly those terminal observation atoms with positive P−(177/172)Q contribution.

**Theorem AG1.** For every real η∈[0,123/430] and every lawful real-valued causal behavioral policy under the exact budgets,

    H ≤ h(η)
    h(η) = 249/2752
         + (499/8256)[η−13/998]_+
         + (3/43)[η−1/4]_+ .

Prefix X attains equality with the stated terminal rule for each η. In particular the exact **global** value at η=1/4 is 3461/33024; at η=123/430 it is 113/1032. This covers all interior first-stage and second-stage real behavioral randomization, not only deterministic prefixes.

## Proof

**First-stage feasible polytope.** Put x_wc=Pr(first paid action c | w), with four labels c∈{A0,A1,B0,B1}, and x_wSTOP=1−Σ_c x_wc. Let b=Σ_{w,c∈B}x_wc and h=Σ_w x_wSTOP. Because Σ_u t(w,u)=1 and the P and Q marginal laws on (w,u) agree, C1=(3−h+b)/3=43/48, hence h=5/16+b. The second-stage cost is at most the paid first-action probability (3−h)/3=(43/16−b)/3. From C2=7/8 follows 0≤b≤1/16. All legal first-stage x therefore lie in the compact *linear* polytope K.

**Causal dual upper bound.** Write k=177/172, λ=1/20, y_w=x_wc t(w,u), and Y=Σ_w y_w. The common P/Q probability of a paid observation (c,u) is q_cu=Y/3. The per-z signed support atom is exactly

    d_cuz = Σ_w x_wc[P(w,u,z)−k Q(w,u,z)]
          = y_z/12−(4/129)Y.
    Φ_cu(x,η)=Σ_z [d_cuz]_+ .

STOP and each skipped-S observation have P=Q, hence for k>1 their maximal positive support is zero (reject). For the true conditional S-buy probability s_cu∈[0,1], optimal terminal acceptance gives H≤Σ_cu s_cu Φ_cu, with Σ_cu s_cu q_cu=C2. For each c,u,

    s Φ ≤ λ s q + [Φ−λq]_+ .

Consequently

    H ≤ Fλ(x,η):=λ C2+Σ_cu [Φ_cu(x,η)−λq_cu(x,η)]_+ .

For fixed η, Φ is a sum of positive parts of affine functions of x, so Fλ is convex in x. Its maximum on K is attained at a vertex. This upper bound does not modify or relax any strategy into a claimed *feasible* policy; only X supplies lower-bound attainability.

**Complete vertices.** Since total STOP plus B mass h+b=5/16+2b≤7/16<1, each of the three rows has positive A mass. A0 and A1 cannot both be positive at an extreme point: transferring mass between those two labels is a nonzero feasible direction. Once one A label is chosen per row, the remaining coordinates h_w=x_wSTOP and b_w=Σ_B x_wc satisfy h_w,b_w≥0, Σ h_w−Σ b_w=5/16, Σ b_w≤1/16. Row capacities are strictly slack. Their vertices have b=0 with the entire h=5/16 in one history, or b=1/16 with h=6/16 in one history and b=1/16 in one (possibly the same) history. All other row mass uses a single A label, and a nonzero B mass uses B0 or B1. There are 24 distinct vertices for b=0 and 144 for b=1/16, hence 168 distinct vertices; the verifier runs 288 indexed cases, including duplicated b=0 labels.

**Exact finite certificate.** Executed BigInt rational code VERIFY.js exhausts all indexed vertices at the four η knots, with the complete 1152 vertex evaluations preserved in VERTEX_CERT.tsv and assertions in EXACT_REPORT.json:

| η | max Fλ (b=0) | max Fλ (b=1/16) | h(η) |
|---|---:|---:|---:|
| 0 | 1801/20640 | 249/2752 | 249/2752 |
| 13/998 | 1801/20640 | 249/2752 | 249/2752 |
| 1/4 | 401/3840 | 3461/33024 | 3461/33024 |
| 123/430 | 113/1032 | 113/1032 | 113/1032 |

All 18 leaves are normalized and positive at these four knots, and X has exact costs. The same arithmetic was independently recalculated with Python Fraction on the same finite vertex family.

**Analytic extension to all real η.** At fixed vertex x, Fλ(x,η) is convex in η, because the raw observation atom differences are affine in η and positive parts preserve convexity. Direct exact expansion of X's atom differences yields exactly two internal sign-changing η roots, 13/998 and 1/4, and its support h(η) is affine on each of the three adjacent knot intervals. A convex function bounded by an affine function at both ends of such an interval remains bounded throughout. Hence Fλ(vertex,η)≤h(η) for every η between knots. Convexity in x and the complete vertex enumeration give Fλ(x,η)≤h(η) for every x∈K. The actual lawful strategy X attains h(η), completing the theorem.

## Discriminating diagnostic and next frontier

At η=3/10 the **same constant λ** has a dual relaxation excess 1/6880: its best b=0 vertex has Fλ=107/960 while X has H=919/8256. This is not a lawful counterexample. A separate exact greedy S-skip check of all 144 b=0 indexed vertex policies enforces C2 precisely and finds legal max 13699/123840, exactly 1/1440 *below* X. Thus 123/430 delimits this particular constant-λ certificate, not known failure of the causal optimizer. Next question EC49AH is to extend actual optimality with a different multiplier/semialgebraic proof or give a lawful interior counterexample beyond this η threshold.

## BRC, source, authority

The applied BRC carrier is the labelled positive P/Q branch distribution, observer is (c,u[,z]), and erased w is an explicit provenance fiber. The theorem is about observer support under exact two-stage resource constraints; it makes no claim of signed/phase cancellation, native X6 rotation, a native three-dimensional slice, or heartbeat dynamics. P000 and ACTIVE worldview are unchanged.

Parent science: EC49AF Draft PR #1691, immutable commit 39151b8632ac4ff0fe1685b092c382b9e1dbb429. Frozen input source pins: GLOBAL_KNOWLEDGE_V1 main@8acf1c35dc61b5d430678679d82dd4c4ef072bff and Enterprise Math main@1943d5b96de28b35004252747e5b70a2faf76a3b. Native service during run reported directed authority false and active-owner listing CONTROL_QUOTA; no native CLAIM, Result, independent review or mathematical admission has been obtained. This is a complete portable author proof and finite exact certificate, not formal Source acceptance.
