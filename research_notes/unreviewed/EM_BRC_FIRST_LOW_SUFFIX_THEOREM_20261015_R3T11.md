# First-low-feedback compression for Boolean support BRC

Fix positive integer thresholds 1<=Q<T. Let each public action be a nonempty subset of finitely many labelled sources, and let a secret choice reset one source's nonnegative integer residual to zero. After each action, report bit 1 iff the remaining total is >=T. At the end, output TRUE iff every positive-support hidden path has remaining total >=Q.

**Claim.** If some finite adaptive policy is universally safe from X but has an unsafe hidden path from Y, there exists an equally distinguishing comb policy with a feedback spine consisting of zero or more HIGH bits, one LOW bit, then only LOW bits. All off-spine feedback branches immediately stop. No more than T-Q actions follow the first LOW feedback. More sharply, if the Y residual at first LOW is r>=Q, the subsequent bound is r-Q+1; if r<Q, none are needed.

**Proof.** Choose a Y unsafe hidden path in the original policy. Its final total is <Q<T, so a first LOW bit occurs after some move, at which time Y's remaining mass r<=T-1. Monotone resetting forces LOW forever after that moment. Stop this witness at its first unsafe time. Delete every subsequent move in which the Y hidden choice resets an already-zero source (or any source with zero residual). The retained moves each decrease the integer total by at least one, and it takes at most r-Q+1 <= T-Q such decreasing moves before the first crossing below Q. The shorter witness has the same relevant residual and remains unsafe.

Consider any X hidden path compatible with the original feedback prefix through first LOW and with the shortened suffix. Restore all deleted public moves in their original positions, secretly choosing any permitted source each time. This restores an X path through the original suffix: because all its residual totals were already <T at the first LOW, they remain <T after every inserted move, so the public bits match the all-LOW spine. The original restored path can only have *less* remaining mass than the shortened X path. Original universal safety therefore implies shortened universal safety. Stop on every other feedback branch immediately, which is safe in X because an earlier stopping prefix has at least the remaining mass of any original safe terminal descendant.

Thus the shortened comb policy still distinguishes X from Y.

The result bounds only the suffix after first LOW, not the length of the earlier all-HIGH prefix, the complete-state horizon, exact path counts, signed amplitudes or native X6 evolution.

In the tested special cases, T=3 gives a suffix budget <=2 when Q=1 and <=1 when Q=2. A matching-based or directed public-belief search may exploit this canonical form without discarding labelled source support.
