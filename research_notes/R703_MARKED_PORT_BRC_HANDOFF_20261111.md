# R703 continuation — one marked-source BRC bit

Task RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142; frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor R702 author commit f1163f26b4eff01fd20a31303381ec903667b1c3. No change to P000, ACTIVE worldview or frozen science.

**New exact result.** In the phase-(0,0) positive BRC 60-label source model with four class sizes (24,18,6,12), give one named e-group label q probability alpha to toggle and any of the remaining 59 labels beta=(1-alpha)/59. For alpha≠1/60, old two-moment states M0=s/60, M1=(96e+5t+92c+47z)/60 collide under next-step class-count observations. Sharp witness: only q active versus only other e label active, with next e-down probabilities alpha versus beta. At alpha=1/2, these are 1/2 vs 1/118.

**One-bit repair and minimum.** Add B_q=x_q/60. The exact G_q-orbit quotient (b,h,t,c,z) has 82992 states (17-bit optimal) and a strongly lumpable kernel; even future count-only observations distinguish every orbit by time 0 or time 1. All-off two-step return probability is 15/59. Full analytic proof and the standard-library exact checker are linked from this PR. Upstream named-path provenance is retained.

**Verification.** The checked candidate quotient has 82992 legal states; exhaustive rank/inverse, transition normalization, injective marked moments, exact one-step collision, and independent sparse Fraction DP for n=0..8 pass. P000 triadic dynamics, native port admission, V29 PASS/TRANSFER, V39 j, and rotation covariance are still open. Independent Driver review and formal Result not obtained by the author's calculation.

**Next unit.** Read a frozen legal native X6 Cell/Link/Port event with actual occupancy/rotation and test two decorated packets with same old moments. Check whether a marked bit is a future sufficient repair, or whether interacting-port/signed-loop residuals are required; then connect to TRIADIC_CLOSURE_E.
