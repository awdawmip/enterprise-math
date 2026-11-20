# Stage315-B — exact full-eight-rate global transition versus one-fiber cusp

Status: portable next research unit; not a native CLAIM, Result, or admitted theorem. Research2 role provenance; do not assume that the apparent current author is the live canonical task owner.

## Frozen scientific model

Read immutable Stage314-B `PROOF_STAGE314B.md` and `REPRO_STAGE314B.py`, and reuse parent Stage313-B `1108f7eb1706d3f5daeef6bb3f78584d978a7657`. Eight private histories `(J,W,Y)` have joint masses `(63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63)` over `256`; hidden source rates `p0=1/4,p1=3/4`, three future Bernoulli F visits; H is independent fair. Public observer `(W,Y,trace)` and source-tagged observer `(S,J,W,Y,trace)`. MAP risks `P0=11/256, T0=77/1024`.

## Verified theorem frontier

Stage312-B proved **full eight-dimensional** optimum `F_P(P0-eps)=T0+g(q^-1(eps))` for `0<=eps<=18117/4000000`, with two symmetric optimizers when eps>0. Stage313-B gave a later strict counterexample and Stage314-B now proves **the complete one-fiber optimization over every real rate in `[0,1]`**:

`V_100(eps)=min(T0+g(q^-1(eps)),Tdag)` for all `0<=eps<=Edag`, where `Tdag=(319-sqrt(13))/4096`, `Edag=19/256-9sqrt(13)/512`. Its first (restricted) global optimizer jump occurs exactly at `eps_c=q(u_c)`, `g(u_c)=(11-sqrt(13))/4096`, `109/1000<u_c<11/100`, and it is symmetric under `h100` / `h011`.

The first public sign flip of the departing small branch occurs much later at the unique root `t2 in (392/1000,393/1000)` of `32t²(1-t)=3`; tagged-cost turning point is `u=13/92`. These are *not* evidence of full eight-rate admission or the first eight-rate transition.

## Smallest hard problem

Prove or refute `epsilon_first^8 = epsilon_c`: either give an exact global eight-variable semialgebraic/interval certificate excluding every competing `t_h` for `eps<eps_c`, or produce an **exact rational/algebraic** multi-fiber vector with `eps in (18117/4000000,eps_c)` that strictly beats the one-fiber polynomial.

Use the finite four-word residual arrays and `D3(p,t)` TV chambers as the base representation. Preserve all eight private rates, `S` source masses and both public/tagged observers; a single-fiber theorem alone is insufficient. A numeric nonlinear optimizer may generate candidates but must not be cited as a global proof. Provide exact code and executed checks, state exclusion scope/coverage, and retain separate native-X6 mapping obligation.

## Deliverable

One new exact full-eight competitor, certified exclusion interval, or reduced algebraic cone lemma with explicit assumption/coverage; source-backed proof/negative result and next unresolved frontier; publication/readback through the authorized current project route. No native admission is implied.
