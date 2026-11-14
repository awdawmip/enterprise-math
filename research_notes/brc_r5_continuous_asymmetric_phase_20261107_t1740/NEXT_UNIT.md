# R5 next unit — joint-time normal directions, beyond fixed-time support

Frozen pins unchanged: Global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Current author-side frontier: exact FULL_HIST=seedless LR optimum in the entire real strip epsilon∈[-1/56,9/344], lambda∈[-1/10,1/10], with 9 regions and constant signed-support switching lines; see RESEARCH.md and VERIFY.py.

Mother target: O4(FULL_HIST) ?= O4(seedless LR) for W=(eP,eQ,TP,TQ).

A discriminating next experiment is optimize the unrestricted four-dimensional normal
`V_{lambda,rho,sigma}=eQ-(1+lambda)*(1-eP)+rho*(TP-31/10)+sigma*(TQ-31/10)`.
Start with lambda=-1/20, 0, +1/20 and rho,sigma drawn from {0,+1/100,-1/100}, comparing a FULL_HIST rational LP dual with a globally reoptimized seedless LR family. The FULL_HIST objective remains piecewise-linear in terminal declarations; seedless LR retains 9*b*z=4*a*(v-z). Compute exact rational candidate separating W only after excluding *every* globally admissible seedless flow (not only flows having prescribed times). If no separator, derive a reusable exact lift/factorization lemma covering a larger class of normals.

The new ε-band optimum does not assert full O4 image equivalence. Maintain current native owner state as unconfirmed until the authenticated control service becomes available; preserve Draft PR #1767 author-side provenance and independent review boundary.
