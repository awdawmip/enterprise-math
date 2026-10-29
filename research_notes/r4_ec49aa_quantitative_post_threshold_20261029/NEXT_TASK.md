# EC49AB — Exact lower-bound section at the first post-wedge rational target

**Immediate predecessor:** EC49AA, auxiliary positive source-labelled BRC sensor model, eta=1/200, with per-source stage costs C1=43/48 and C2=7/8, all real unseeded causal behavior. Universally proved alpha >= 3delta+(2673/3232)max(0,delta-17/288). At delta=1/16, the rigorous enclosure is 19689/103424 <= alpha_min <= 9/46.

**First bounded target:** Obtain a strictly narrower exact rational enclosure or an exact algebraic expression for alpha_min(1/16). The rational witness (alpha,beta)=(9/46,49/368) is feasible and supplies an upper comparison, not proof it is optimal.

**Frozen exact source:** Three histories w=0,1,2 with uniform prior 1/3; A0,A1 cost1, B0,B1 cost2; t_w(u)=1/2+(2u-1)(1-w)/200 for u in {0,1}. P(w,u,z)=t_w(u)*(1/6 if w=z else 1/12), Q(w,u,z)=t_w(u)/9. Initial probabilities x_wc (row sum at most 1), stop mass h_w, post-signal S-purchase probability s_cu after w erasure, terminal sensed acceptance a_cuz; STOP/no-S terminal observations have P=Q. Exact cost constraints hold separately under both sources. No retained ex-ante shared random seed.

**Proof strategy:** Keep the products x_wc*t_w(u)*s_cu*a_cuz and each source/observer fiber; improve the near-pure collision charging bound, or derive a complete quantified polynomial/semi-algebraic obstruction. Explore whether a small subset of code support patterns suffices for an all-real classification and identify a tighter rational witness.

**Success:** Prove a strictly improved universal lower bound, produce a smaller exact feasible upper witness, or give an exact finite algebraic certificate valid for the original full behavior domain. Execute a rational reproducibility checker and publish full assumptions, proof, sources and remaining gaps. Floating search alone is exploratory.

**Longer horizon:** Determine alpha_min(delta) for 17/288<delta<=59/576, boundary transitions, algebraicity and rational implementability. No automatic signed BRC, native X6 or heartbeat theorem transfer; retain P000 and ACTIVE worldview.
