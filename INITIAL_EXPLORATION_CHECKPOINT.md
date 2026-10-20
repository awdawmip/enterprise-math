# INITIAL_EXPLORATION_CHECKPOINT — R035

Researcher-ID: `EM-R035-6F2A91`
Arm: `PROJECT`
Timestamp: `2026-08-12T13:23+08:00` (checkpoint preserved before deliberate project-history / reasoning-tool-library search)

## Candidate representations / entry points thought of before search

1. **Lower-index map plus endpoint bit.** Write
   `F_{s,r}(k) = L_s(r P_s(k))` and distinguish whether `r P_s(k)` is itself polygonal. A parent then has either the singleton `{F(k)}` or the adjacent pair `{F(k),F(k)+1}`. Study monotonicity and increments of `F` before studying full support unions.
2. **Quadratic discriminant / gap coordinate.** Since consecutive polygonal gaps are linear in `k`, compare `r P_s(k)` exactly with `P_s(m)` and `P_s(m+1)` via integer inequalities or the discriminant. This should expose an exact residual/phase inside the polygonal basin without floats.
3. **Support geometry through ordered parent images.** Because `P_s`, multiplication by `r`, and `L_s` are monotone, parent-to-child blocks should be ordered. Test whether a support generated from one root has interval structure, bounded gap structure, or a more rigid ordered-block description.

## First conjectures / questions

- `F_{s,r}(k)` is nondecreasing (likely strictly increasing for most/all `r>=1` once trivial roots are separated); its leading scale should be about `sqrt(r) k`, but the exact finite-k offset may matter.
- The endpoint support of one parent always has diameter at most 1 by definition, but after unions the global support may develop gaps when successive `F(k)` jumps by more than 2. I do not know whether reachable supports from a singleton can nevertheless remain unusually small because the initial branching is constrained.
- Special case `r=1` should be frozen: `r P_s(k)` is exactly polygonal, so every root is a fixed point.
- Exact hits `rP_s(k)=P_s(m)` may be an important arithmetic subproblem; they could create deterministic branches/frozen substructure inside otherwise two-child dynamics.
- Possible question: does support cardinality stay uniformly bounded for fixed `(s,r)`, grow polynomially/exponentially in time, or depend on arithmetic hit patterns?

## Boundaries I most want to attack

- Smallest nontrivial `r=2`, then larger square/non-square `r` to see whether `sqrt(r)` being integral changes the dynamics.
- `s=4` (squares) versus `s=3` (triangular numbers), because squares may yield an exactly solvable control case.
- Roots `k=0,1` versus large `k`, to separate origin artifacts from stable dynamics.
- Whether reachable supports can have internal gaps; find the smallest witness if yes.
- Whether two distinct parents can produce the same child (true recoalescence) and the smallest witness.

## Main uncertainty

The main uncertainty is whether the set-valued iteration creates genuinely expanding combinatorial supports, or whether the quadratic scaling plus ordered endpoint projection collapses it to a very small carrier (for example one/two adjacent indices, a short interval, or a finite phase state) for each fixed `(s,r)`. I have not yet searched prior project work, external literature, or a reasoning-tool registry for an answer.
