# PREFIX-594-R6 — One universal 33-dimensional linear carrier for every full (T,P0,P1) path law across nine native BRC roots

Date: 2026-11-08 Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_NATIVE_OPERATOR_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Source original six-label native BRC kernel: \`PREFIX565_positive_marginal_certificate.py\` at Git blob \`7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41\`.
Established exact 33-dimensional cubic graded carrier: PREFIX-591 (\`2ab77962c8d6830a123915364fc8d97aa9e90f73\`), phase generator PREFIX-592 (\`1161ccdff93ed09141783c3dbd97d50b6e9e4d78\`), all nine roots PREFIX-593 (\`0f921eae3004011bc91264538df607b89e668b34\`).

## Exact original-native question

Original BRC system: 48 physical phases, 96 labeled branch ports, six original labeled native actions, their order, sign/phase and gate retained. Allowed frozen native roots are zero or \(\pm e_k\) for \(k=1,2,3,4\). Each step chooses one of the original six labeled actions with probability 1/6. Define path-additive rewards exactly as before:
\[
T=192K-5R_1+R_2-5R_3+R_4+4R_5+4R_6,\qquad
P_0=R_1+R_2,\qquad P_1=R_3+R_4.
\]
The readout is now the **complete discrete joint probability distribution** of \((T_n,P_{0,n},P_{1,n})\) at **every** original path length n, not merely moments through degree 3. Initial port distribution \(\pi\) is arbitrary. Also allow any externally specified, deterministic sequence of the nine frozen roots, choosing the root anew for each step while retaining the original BRC edge rules.

## Theorem — all moments and exact joint generating polynomials

Let \(U\subset\mathbb Q^{96}\) be the 33-dimensional exact zero-root degree-three port-observer subspace \(W_3(0)\) constructed and certified in PREFIX-591, containing the constant vector \(\mathbf1\). Then for **each of the nine frozen roots** r and **every distinct original reward signature** \(\rho=(\Delta T,\Delta P_0,\Delta P_1)\) attainable under r, the original-native signature-selector operator
\[
(A_{r,\rho}f)(i)=
  \sum_{\substack{a\in\mathrm{ACTIONS}\\
                   (\Delta T,\Delta P_0,\Delta P_1)(i,a;r)=\rho}}
  f(j(i,a;r))
\]
satisfies the **exact rational invariance**
\[
\boxed{ A_{r,\rho}\, U \subseteq U. }
\]

There are **six** distinct reward signatures for zero root and **ten** for each of the other eight roots, hence 86 exact native signature operators. The certificate checks all \(86\times33=2838\) basis images using exact fractions on all 96 original ports.

For formal commuting variables \(x,y,z\), define the original Laurent-polynomial transfer
\[
A_r(x,y,z)=\sum_{\rho=(t,p,q)} x^t y^p z^q A_{r,\rho}.
\]
(Allowing negative powers of x is essential because T can be signed.) For any n and any externally fixed root schedule \(r_1,\ldots,r_n\) in the nine-root set, **every coefficient** of
\[
\boxed{A_{r_1}(x,y,z)\cdots A_{r_n}(x,y,z)\mathbf1}
\]
is a vector in U, by the exact selector-operator invariance. For an arbitrary original start law \(\pi\), pairing that polynomial vector with \(\pi\) and multiplying by \(6^{-n}\) produces the **entire exact original joint path law** of \((T_n,P_{0,n},P_{1,n})\).

Therefore, **one fixed set of 32 variable rational linear statistics of \(\pi\), together with the normalization \(\pi(\mathbf1)=1\), recovers every coefficient of every declared joint distribution at every length and across all nine roots and any predetermined root schedule.**

The 32 variable statistics are **strictly minimal among rational linear summaries** of arbitrary original initial-port laws for these joint distributions: even the zero-root cubic moments, which are linear combinations of the full distribution and are included in the present requirement, already have rank 33 by the exact certified finite-depth lower witness in PREFIX-591.

Moreover, for every other fixed root \(r\) the degree-three carrier \(W_3(r)\) has the same rational span \(U\) as zero root: this is independently checked by reducing all its 33 rational basis vectors against U (and confirming both dimensions are 33). The carrier is **root-independent** even though the grade at which the native phase-42 indicator becomes visible depends on root orientation, as established in PREFIX-593.

## Precise compression semantics and countercheck

This is a **linear initial-law sufficient-statistic theorem for the triple (T,P0,P1)**. It retains original 96 ports for construction and transitions, all original action labels and multiplicities, and full signed BRC rewards before the declared readout. The 33-dimensional carrier is not asserted to be a native 33-port physical-state quotient.

Indeed, the 96 original port evaluation rows on an exact basis of U have **34 distinct types**, despite U having dimension 33. Therefore a naive deterministic partition into 33 classes cannot represent the full U as class-constant functions; the compression uses a genuine linear relation. This provides an exact boundary between minimal linear information capacity and simple port lumping.

As an independent scope check, inspect selector operators that distinguish **all seven original rewards** \((\Delta R_1,\ldots,\Delta R_6,\Delta K)\), rather than the declared triple. Already at the zero root, U is **not invariant** under every such operator. Thus the theorem is scoped to the exact joint triple and root schedules specified above; no other joint reward readout or branch history is declared preserved.

## Proof method and executable verification

The complete finite-dimensional proof is an exact rational invariant-subspace calculation over **original native BRC edges**, not a fit of truncated moments. The published \`PREFIX594_R6_universal_native_reward_signature_certificate.py\` reconstructs the zero-root W3 directly from the published PREFIX-591 certificate and computes all 86 selector operators from published PREFIX-565; every one of the 2,838 rational membership tests passes, as do the cross-root carrier-space and 34-type tests. The independent local exact native reimplementation also passed.

Because the constant function is in the invariant carrier, the all-length assertion follows by induction on path length and polynomial coefficient extraction; the previously verified nonzero finite-depth minor proves exact minimality. Status: \`ALL_CHECKS_PASS\`.

## Next mathematics

Find an explicit 33-coordinate positive or signed *operator representation* of the universal carrier, quantify the cost of converting the original 96-port initial law to it, and characterize the additional information directions required to preserve the **full seven-reward** joint law. Compare exact 34-type partition with the linear 33-dimensional carrier; test whether an operationally useful 34-class nonnegative quotient exists. The zero-root full-seven selector failure is a concrete next discriminating witness.
