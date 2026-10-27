# Stage188 portable continuation — exact primal problem, dual already certified

2026-10-27. **Stage188 is DUAL ONLY.** The preceding Stage187 author-level exact interval was proved in `PROOF_STAGE187.md` on the same research branch. Do not repeat Stage187's 680-state sweep or 787528-node full ordered-history computation unless a genuine discrepancy is identified. The external auxiliary model is *not* a native P000 X6 theorem and has not received independent Research Driver admission.

## Mother question and immutable input

For ordered-history-dependent randomized ternary IID stopping, horizon 14,
[
P=(1/8,1/24,5/6),quad Q=(1/12,1/12,5/6),
]
minimize `max(E_P T,E_Q T)` subject to `P(decide Q),Q(decide P)<=alpha`. Keep separate P and Q exact masses and the ordered-path source; no signed-amplitude interpretation. Frozen Stage187 boundary:
[
alpha_{187}=47564236941933996508186187/135753377754634620902572032,qquad
V_{187}=47526009692613945133124984819/4344108088148307868882305024.
]
Stage187 support slope: `-61261145548467/175004717024`.

Stage188 **exact dual-only** candidate:
[
K_{188}=39993714743501421/226849611128761,quad
L_{188}=39205434834768424/226849611128761,quad
H_{188}=552023450050793309312530706424493/4142313307078339047903008391168.
]
Bellman count-state scan from `h(n,a,b)=min{K*2^(a+b)/3^a, L, 1+sum_i P_i h(child)}` (last option omitted at n=14) has 680 states, only two ties: `R=(5,2,0)` P/C and `X=(8,0,1)` Q/C; other 1,238 alternatives have strictly positive gap, minimum `1858369546682908/55124455504288923`. Stage187 terminal strategy exactly attains the Stage188 dual root. These are author-level precise rational calculations, **not** primal optimality of any new interval.

## Immediate scientific unit

Compute `O(r,x)=(eP,eQ,tP,tQ)` for four deterministic corner choices at R (P vs continue), X (Q vs continue), using (A) rational suffix DP and (B) a separate unmerged full ordered-history integer-weight DFS under both P and Q. Show R cannot be X's ancestor because its zero-symbol count is 2 while X's is 0 (reverse ancestry is impossible by time), and establish vanishing mixed term for *this* pair, not Stage187's ancestor-linked pair.

Solve exact `eP=eQ` for an admissible real coin segment continuing the Stage187 endpoint. Check legal `0<=r,x<=1`, monotonic alpha with exact derivatives or affine coefficients, `tP>=tQ`, Bellman equality, full-real support equality, continuity and strict right sharpness under *history-dependent* stopping policies. If any fails, give the first exact rational obstruction and preserve the source witness. End with an explicit Stage189 dual-only candidate if justified.

## Method and completion evidence

Reuse BRC positive-rational branch representation, path multiplicities and observer-safety scope. A compressed count-state Bellman calculation is justified here only for the explicitly IID finite-horizon model; independent DFS retains full ordered histories. Preserve every corner vector, root/tie/gap certificate, no-negative-gap check, balance identity, exact endpoint, verified executable source/log, and next open scientific obligation. The expected deliverable is an actual proof, counterexample or exact arithmetic obstruction, not merely activity bookkeeping.

Use the current project's Source publication/admission rules and current genuine role. If a formal Source CLAIM is inaccessible, preserve independent author-level research on a unique branch with immutable GitHub receipt; activity `RA-EMR2STAGE18720261027T1008AUTO11` is bookkeeping only. Recheck control ownership before mutation of any canonical Task/Result/Review; do not infer owner from the local label.
