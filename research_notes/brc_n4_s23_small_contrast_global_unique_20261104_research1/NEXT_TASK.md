# Next independent BRC N=4 S23 unit: explicit global uniqueness at lawful finite contrast

**Mother target:** source-tagged S23 source-efficiency comparison, with the original ten-label decoder minimax still open at `[1/2,2/3]`. Scientific pin stays `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

**Latest theorem:** there is an unspecified epsilon>0 for which optimized Chernoff efficiency F(s,h) has exactly one crossover on 0<s<1 for every 0<h<epsilon. Proof and exact coefficient audit are in this directory.

**Discriminating question:** does the same global uniqueness hold for `h=1/42`? Use the analytic normalized `H=F/(h^4 s(1-s))` and prove `H_s>0` on `[0,1]x[0,1/42]`, with a certified bound; if monotonicity fails, test the F-sign itself and search for a second root. Existing finite-h bracket `(0.10243902443,0.10243902445)` has a verified local unique zero in the prior author note.

**Executable verification route:** implement rational outward intervals for the analytic optimizer `delta_*=[phi(kv)-phi(v)]/[atanh(v)+atanh(kv)]`, or use a rigorously bounded h-expansion for H and H_s uniformly in s. The endpoint divisions must be evaluated using their analytic extensions, not a division by zero. A finite s/h mesh is discovery evidence only. Preserve T/B source tags, prices, lawful h range, exact test scope, and native authority/review separation.
