# PREFIX-594-R2 — Native X6-BRC positive 49-coordinate chamber and optimal 49/48 readout rank

Date: 2026-11-08. Author-side exact proof + integer execution, unreviewed. Researcher-ID `EM-DIRECT-EEAACA / TASK_RESEARCH`, native activity `RA-0EF8EF41E688E715E5CB9419`. Scientific source frozen at `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Builds on PREFIX-593, retaining all original 96 native ports, 576 labelled actions, original gate and six axes.

## Proposition 594.1 — 49-dimensional positive carrier for the sharp gate chamber

Let the original 48 phases have three native successors `N(i)`, source axis `a(i)`, unique gate-target phase `g`, and `eta_i = [g in N(i)]`. In original X6-BRC, `eta_g=0` and `sum_i eta_i=3`. Given nonnegative original port state `r_(t-1)`, nonnegative native axis weights `x_(t,a)`, and gate weights `z_t >= 1`, define

`b_i(t)=r_(t-1,i,0)+r_(t-1,i,1)`,  
`delta_t=(z_t-1) r_(t-1,g,1)`,  
`q_i(t)=x_(t,a(i)) sum_(j in N(i)) b_j(t)`.

Every one of these 49 coordinates `(b_i,delta)` is nonnegative. The exact **linear 49×49 next-state map** is

`b_i(t+1) = 2*x_(t,a(i))*sum_(j in N(i)) b_j(t) + x_(t,a(i))*eta_i*delta_t`,

`delta_(t+1) = (z_(t+1)-1)*x_(t,a(g))*sum_(j in N(g)) b_j(t)`.

All 49×49 coefficients are nonnegative for each `x_t>=0, z_(t+1)>=1`. The **full native 96-port output map** is nonnegative and exact:

`r_(t,i,0)=q_i(t)`,  
`r_(t,i,1)=q_i(t)+x_(t,a(i))*eta_i*delta_t`.

Thus arbitrary finite varying-weight native BRC propagation with `z_t>=1` admits one single **positive 49-coordinate** intermediate state, positive update and positive readout, with no signed double-channel split. Initial encoding `(b_i(1),delta_1)` is positive for the same parameter chamber.

## Proposition 594.2 — exact generic dimension and z=1 boundary

The native operator is `A(x,z)=Xhat Shat D(z)`; `S` is invertible with determinant `3^12` (PREFIX-586). For all six `x_a != 0` the diagonal `Xhat` is invertible. The 48 branch-bit blocks of `D(z)` consist of 47 rank-one ordinary blocks `[[1,1],[1,1]]` and one gate block `[[1,1],[1,z]]`, determinant `z-1`. Therefore

`rank A(x,z)=49` for every `z!=1`, and `rank A(x,1)=48`.

Every **linear intermediary** `A=L R` with all 96 native port outputs observable from every original right endpoint has dimension at least `rank A`. The 49 positive carrier attains 49 at generic `z>1`. At `z=1`, delta vanishes, and the 48 phase-sums form an exact positive 48-carrier, attaining rank48.

For `x_(t,a(g))>0` and `0<=z_(t+1)<1`, the displayed 49×49 update in coordinates `(b,delta)` has exactly three negative coefficients in its delta row (one for each successor of g), each equal to `(z_(t+1)-1)*x_(t,a(g))`. The original nonnegative singleton input at port `(g,1)` gives `delta_1=z_1-1<0`. Accordingly the sharp orthant-positivity chamber **for these specific coordinates** is `z_t>=1`. This does NOT rule out a different positive 49-dimensional cone/realization when `0<=z<1`.

This theorem concerns complete native **linear future port readouts**, not preservation of separately named source bit identities or ordered native path itineraries. Full labelled action source semantics remain on the original native BRC operator; any individual provenance observer keeps its additional annotations.

## Exact executed certificate

`PREFIX594_R2_49state_positive_chamber_cert.py` reconstructs original BRC from `PREFIX589_R2_dual_carrier_certificate.py`, builds exact 49×49 update and 96×49 output matrices, checks all 9,604 transition and 18,816 output coefficient values at four nonnegative axis/gate assignments (including zero axes), verifies 288 exact original 96-port single-input readouts across gate z=0,1,2, and checks exactly the three negative gate-row entries when z=0. All integer assertions passed, `ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED`. The universal statements follow from the displayed formulas and rank proof, not numerical fits.

## Next smallest unresolved question

Does the full `z>=0` native family admit a **common** 49-dimensional positive realization with nonnegative input/output maps for all 96 native port readouts? If not, give a scoped exact positive-realization lower bound and a concrete obstruction. Compare equal-optimization implementations of native `X S D`, dual `W E` and this positive 49/48-state recurrence, counting total conversion, operation and integer bitlength costs. P000 and frozen scientific input unchanged; author-side research is pending independent Driver review and native Result.
