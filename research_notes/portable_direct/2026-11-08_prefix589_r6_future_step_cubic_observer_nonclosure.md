# PREFIX-589-R6 — Explicit native one-step failure of a sharp cubic BRC observer

Date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_NATIVE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
Scientific source pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Native kernel implementation: \`PREFIX565_positive_marginal_certificate.py\`, Git blob \`7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41\`.
Direct predecessor: \`PREFIX-588-R6\`, commit \`755fca13477494e324d4484b38066648eb68f176\`.
This is an independent researcher note. No native Source session or active owner is claimed; the authenticated control backend reported \`BACKEND_IDENTITY_CHECK_UNAVAILABLE\`, \`operation_sent=false\`.

## Question and exact model

Does the PREFIX-588 sharp eight-variable degree-three moment summary admit an exact one-step update under the **original** BRC kernel? Use the frozen zero root, original 96 native ports and six labeled actions. At each step an action is chosen independently and uniformly from the six; the initial port has an arbitrary probability law. No surrogate BRC dynamics or replacement transitions are used.

Let the native cumulative rewards be \`R1,...,R6,K\`, and define
\[
P_0=R_1+R_2,\quad P_1=R_3+R_4,\quad P_2=R_5+R_6,
\]
\[
Y=K-\frac{5R_1-R_2+5R_3-R_4-4R_5-4R_6}{192},\qquad T=192Y.
\]
At fixed length \(n\), define \(\mathcal S_n(\pi)\) as all 20 raw mixed moments \(E_\pi[T^aP_0^bP_1^c]\), \(a+b+c\le 3\), with the initial native port sampled from \(\pi\). The constant is one, so PREFIX-588 proves eight variable coordinates suffice for the static \(\mathcal S_2\).

## Theorem — Static third-order equality fails native future-operation descent

Consider the two **positive original-port probability laws**
\[
\pi_+=\frac{116\delta_{38}+248\delta_{24}+60\delta_{34}}{424},
\qquad
\pi_-=\frac{160\delta_0+165\delta_2+11\delta_7+88\delta_{32}}{424}.
\]
PREFIX-588 proves, and the present certificate independently rechecks:
\[
\boxed{\mathcal S_2(\pi_+)=\mathcal S_2(\pi_-).}
\]
After **one more original native action**, however,
\[
\boxed{E_{\pi_+}[P_1(3)]-E_{\pi_-}[P_1(3)]=\frac{11}{159}}, 
\]
\[
\boxed{E_{\pi_+}[P_0(3)]-E_{\pi_-}[P_0(3)]=-\frac{11}{159}},
\]
\[
\boxed{E_{\pi_+}[T(3)]-E_{\pi_-}[T(3)]=\frac{34}{477}},\qquad
\boxed{E_{\pi_+}[Y(3)]-E_{\pi_-}[Y(3)]=\frac{17}{45792}}.
\]

Consequently, **there is no deterministic update map** \(\Phi\) satisfying
\(\mathcal S_3(\pi)=\Phi(\mathcal S_2(\pi))\) for all initial-port probability laws \(\pi\) in this frozen, zero-root, uniform-action native model. The proof even separates the laws by first-order readouts after one extra action.

### Complete finite proof

Enumerate the original native BRC \`edge(i,action,ZERO_ROOT)\` kernel for three steps for each of the seven ports supporting \(\pi_\pm\); multiplicities are exact integers, and conditional denominators are \(424\cdot 6^n\). At depth two, all 20 rational mixed moments are identical. At depth three, the exact rational moment differences above are nonzero. A single-valued \(\Phi\) on the common degree-three summary would have to return the same value on both inputs, contradicting the displayed first-order differences. The published executable certificate uses exact Python \`Fraction\`, direct BRC edge calls, all 20 moments and explicit assertions.

## One explicit native repair coordinate for the next P1 mean

Define a bounded **port-level** reward expectation
\[
g(j)=\frac16\sum_{a\in ACTIONS}\bigl(r_3(j,a)+r_4(j,a)\bigr).
\]
Here \(r_3,r_4\) are the original native one-step axis rewards, not reconstructed values. Exact enumeration gives \(g(j)\in\{0,1\}\) on all 96 ports, with \(g=0\) on 64 ports and \(g=1\) on 32 ports. For any initial-port distribution and every time \(n\),
\[
E[P_1(n+1)]=E[P_1(n)]+E[g(X_n)],
\]
where \(X_n\) is the true native endpoint port. This is conditional expectation of the next *original* BRC reward, not a new transition model. The two laws satisfy
\[
E_{\pi_+}[g(X_2)]-E_{\pi_-}[g(X_2)]=11/159.
\]
Thus retaining \(E[g(X_2)]\) explicitly repairs the **one-step P1 mean** lost by the cubic-summary compression. It does not alone assert closure of all 20 moments or arbitrary future steps.

## Observer scope and next step

The two-step eight-coordinate static moment quotient is an **exact observer for the declared horizon**, while the genuine BRC time step requires additional endpoint provenance for future operations. This gives an explicit finite-horizon non-descent certificate required by the project's joint-relation preservation rule. No claim about all possible state compressions or other frozen roots is made.

Next discriminate whether the smallest **joint port/moment-lift** retaining endpoint g together with the eight moments closes for the next third-order observation, and test native action-automorphism orbits behind the 23 two-step moment-profile classes. A separate check should repeat the counterexample on the eight other frozen allowed roots.

## Verification

The corresponding published program \`PREFIX589_R6_native_future_observer_nonclosure_certificate.py\` uses the original \`PREFIX565_positive_marginal_certificate.py\`. Locally executed output: \`ALL_CHECKS_PASS\`. Its values, coverage and root restriction are recorded in \`PREFIX589_R6_RESULTS.json\`; exact source files and frozen input provenance are preserved in the project repository.
