# CM24 finite quadratic transport: decisive bounded local review

**Verdict: BOUNDED_PASS; no must-fix mathematical or checker defect found in the frozen p² unit.** The coefficientwise bridge, its exact rational-half lift, first divided digit, derivative orientation, and stated counterexamples are supported. UR, the literature period-normal comparison, and LIFT remain unproved. This is a directed, nonblind local review, not formal DR or Source mathematical acceptance.

## Identity, authority and contribution disclosure

Reviewer: **EM-ENTERPRISE-836489**, existing session **MCP-4b54b117968d433d9f37b9df3787d0a8**, existing activity **RA-24B7795F1AF12AD108A5ED13**. Before reviewing, I fetched my two immutable registration records in full through the GitHub connector at Source **818a25d3e307d72710a33c015e695d1cf9568932** and independently matched bytes, SHA256 and Git blob. The existing role is RESEARCHER with DIRECTED_CONTEXT_EXPOSED; review/claim/working-truth authority is false. The registration identifies this same Task and supplies identity provenance for Root's authorized read-only local work; it grants no formal review power. No new session, Task, claim, run, remote write or provider query was made, and no old author claim/run was reused. The review neither inspects nor takes over other chats' work.

The current frozen author is **EM-ENTERPRISE-A1D9B5** (claim MCP-634560f210aa28118cb281a0, epoch 6109143010, run RUN-725aa319e999e96ac1a99acb). Root **EM-DVR-4C90FB** supplied the original quadratic direction and valuation hint in shared context. I did not author this new p² proof or its checker. I did author the adjacent completed unit15 source-interface audit as EM-ENTERPRISE-836489, and previously contributed the unit14 marked local-map work under EM-ENTERPRISE-C98514. Accordingly this is not blind or whole-chain independent. The new reproduction below independently computes the frozen unit's algebra and code-sensitive values; it does not erase those relationships. My child hesse_formula_readcheck separately checked only §§2–3 in the same directed context, with no claim or acceptance authority.

## Exact frozen inputs

The entire author manifest and all five files were copied before mathematical review, then matched by complete byte count, SHA256 and Git blob. **AUTHOR_FROZEN_CORE_MANIFEST.json** is 2159 B, SHA256 **cce4ebfb8107a6e6f0553ece3ba775b61940cfd5596f37ddb017d43f0a34e7a7**. The core pins are:

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| CM24_QUADRATIC_MOD_P2_TASK_LIFT_PROOF.md | 12379 | dbe74c73a06875332cf12e7d550eedbcacf9f9a46367c447e875347490ce5632 | 515c49d26daf6de6b0a182e211e55573397f2436 |
| check_quadratic_transport.py | 9905 | 2540b3de9fe0f429a1fa43e870773691799de9eb4fe6f65e7093a31e40bde9b4 | 9dcd5890b47594c38b56cd3955b1b93271401f14 |
| QUADRATIC_EXACT_REGRESSION_RESULTS.json | 15056 | a1141723cb38f98197f209b8991fa6baf96866d012cc3a16da8b4cd0109cb6f9 | 8ef8f9a096d301be1e053a8ebd395df143e8a69d |
| QUADRATIC_EXACT_REGRESSION_RUN.log | 855 | aafc3755d9decb6f8295022899ae40aad6c3255090bd8e20d86ac035a447ef26 | 23d2f353fa0b4f4e82bc751fc2a1365637a4fa31 |
| REUSED_PRECISION_SOURCE.py | 11558 | d8a19c7e4a319b5e9b17b66a1b5ef4ac563bd984815c7355bd73784e0bc521d8 | 0f028d00b2126b7a3b13bcfb8db627fc542af195 |

INPUT_FULL_HASH_VERIFICATION.json binds the originals and immutable review copies; INHERITED_EXACT_PINS.json binds the three inherited inputs. Author files were not edited or used as output destinations. The frozen author checker was read in full and not imported or executed by my reproduction. Its stored ten-prime output is author evidence; only the five rows selected below were independently reproduced here.

## Decisive mathematical checks

**Characteristic zero and finite truncation (proof §§2–3, lines 46–104): PASS.** Put q=4x(1−x). Separately collecting the coefficients of F″(q), F′(q), F(q) in the chain rule gives exactly 4 times the stated Gauss operator, with all three symbolic residuals zero. The Hesse recurrence is (n+1)²c_(n+1)=(n+1/3)(n+2/3)c_n. Uniqueness from constant term 1 is used over Q, so no division by a zero mod-p coefficient is involved.

For prime p=6m+1 and n<p the factorial denominators are p-units. A multiple rp in 6j+1<6p must have r≡1 mod6, hence only r=1; the unique factor enters at j=m. The analogous 3j+1<3p factor is p at j=2m, while 3j+2<3p contributes 2p at j=4m. Each has valuation one. The entries are n>j, including the boundary indices exactly as written. Thus v_p(a_n)=1_(n>m)+1_(n>2m), and v_p(b_n)=1_(n>2m)+1_(n>4m).

Modulo p², deg f_p≤2m and deg L_p≤4m; deg(f_p∘q)≤4m<p. A coefficient x^k with k<p in the characteristic-zero identity only uses n≤k<p, since q has zero constant term. Both finite sums retain all those terms exactly. For k≥p the effective degrees force both coefficients to vanish mod p². This covers every coefficient up to degree 2p−2 without an assertion about p-integrality of the infinite tail. The argument proves Q2 for every admissible prime, without CM0 or supersingularity.

**Exact lift and divided value (proof §§4–6, lines 106–191): PASS with the declared inherited assumptions.** In Z_(p)[s]/(s²−2), x±=(2±s)/4 have x−=1−x+ and q(x±)=1/2 as exact algebraic equalities, not merely residue-field equalities. The discriminant 8 is a unit; for the Task classes 13,19 mod24 the completion is the unramified quadratic field. Therefore the global coefficientwise congruence evaluates to L_p(x±)=g_p mod p². Under inherited CM0, both values are p-divisible and division gives the same signed first digit g_p/p mod p. This is a bidirectional equality at that precision, since reducing a p² representative after division changes the result only by a multiple of p.

The exact automorphism σ(s)=−s exchanges the two specified lifts and induces residue Frobenius in the target classes. It extends as the lifted unramified automorphism after completion. Literal p-th powering is not that automorphism mod p². Differentiation of a coefficientwise integral polynomial congruence is legitimate and yields L′_p(x±)=q′(x±)f′_p(1/2) mod p², with q′=∓2s. These derivatives are conjugate and opposite; the scalar value and divided digit coincide. A value-only observer cannot identify the branch derivative without retaining its Jacobian. Conversely there is no need to take a norm of the signed first digit.

The finite Taylor formulas give g/p → g/p+δf′ at a rational-half shift by pδ, and L/p → L/p+εL′ at a branch shift by pε. Terms of second order contain p² and vanish after division modulo p. This relies on integral finite coefficients, not on an unspecified p-adic period. Under inherited SIMPLE, the relevant derivatives are units, so a residue-field marking alone does not fix the divided digit. The exact algebraic lift resolves this ambiguity for this bridge, not for a separately defined period.

**Task variable/sign and UR-COMPARE (proof lines 157–169): PASS as an inherited conditional translation.** The frozen Taskbook at Source8d21 has the target (g/p)(−6Q′_m(1/2))=1 mod p (lines 73–85), not a derivative with respect to an unmarked H coordinate. The frozen parent return at Source45e67, SHA256 **54ab94a1899f649ae1488bececaa7c57aafbc89aef44bdd1e40cc0b45590e827**, §3 lines 79–105 defines H_m(w)=Σ binom(m,k)binom(2m,k)w^k, P_(2m)(T)=Q_m(T²), and H_m(w)=Q_m(1−w) in F_p[w]. The fixed Fricke audit, SHA256 **083e7ae69b9b326d7d50f0c380ece51cb1ac666c98c86114398a005ff21528d4**, explicitly consumes this same derivative sign in §2.

Reduction of the finite Gauss coefficients gives f_p≡H_m mod p; differentiation of the inherited reflected-variable identity gives f′_p(1/2)=−Q′_m(1/2). Substituting the newly proved L′=q′f′ and L/p=g/p makes (L/p)(6/q′)L′=(g/p)(−6Q′). The factor 6/q′=∓3/s follows independently from the coordinate map; it is not chosen from the desired target value. The author checker's exact h=g+6f′ check (lines 149–152) alone does not verify Q′. I separately built Q from the closed Rodrigues coefficients of P_(2m), then checked its reflected polynomial and derivative sign in the five finite cases. The all-prime QL/CM0/SIMPLE facts remain inherited consumed inputs, not new proofs or formal acceptances in this unit. UR-COMPARE is an equivalent target, with no proof that either side equals 1.

**Precision restrictions and negatives (proof §7 and lines 248–259): PASS.** The coefficient of x^(2p−2) in f_p(q)−L_p is (−4)^(p−1)a_(p−1), which has valuation exactly two. No other term reaches that degree. This proves failure of the uniform polynomial bridge modulo p³ for every admissible prime. It does not prove failure of every pointwise specialization; the explicit p13 example separately disproves the relevant exact-half extension there. These failures restrict this shortcut, without a global no-go or literature-exhaustion claim.

## Independent bounded computation and code assessment

The independent script check_independent_transport.py uses direct product/factorial coefficients, iterative polynomial convolution/substitution, and successive-power evaluation in the quadratic ring. It imports no author checker and does not use the stored results as expected values in the mathematical checks; author rows are compared only after the independent calculations pass. Its selected primes **7,13,19,37,73** cover the smallest admissible prime, both Task classes, another target case, and a split ordinary class. All coefficients in the full degree range, valuation entries, reflection, differentiated congruence, lifts and marked derivatives passed. This is not a repeat of the previous 77-prime audit.

| p | g mod p² | f′(1/2) mod p | Q′(1/2) mod p | g/p mod p (Task cases) | digit at 1/2+p |
|---:|---:|---:|---:|---:|---:|
| 7 | 23 | 2 | 5 | — | — |
| 13 | 143 | 1 | 12 | 11 | 12 |
| 19 | 152 | 2 | 17 | 8 | 10 |
| 37 | 851 | 11 | 26 | 23 | 34 |
| 73 | 1912 | 22 | 51 | — | — |

An additional shift ε=1+s checked both quadratic coordinates, rather than only a rational Hesse shift. The shifted digits were (7,11), (0,15), (16,15) at p=13,19,37. All independently computed selected author rows matched the frozen results.

The excluded p5 polynomial has the nonzero mod25 coefficients (degree,residue) **(5,3),(6,9),(7,20),(8,20)**. At p13, literal x+^13−σ(x+) is **13+78s mod169** and L_p at that literal-power lift has divided digit **9+2s**, versus the correct digit 11. At the exact algebraic half lift, **L_13(x+)−f_13(1/2)=507+1690s=13²(3+10s) mod2197**. After division by p its second-digit discrepancy is **39+130s mod169**. These reproduce the claimed negatives independently.

Static inspection of the author's full checker found exact Fraction recurrence/composition, explicit p-unit denominator checks, assertion-based value/valuation checks, and no swallowed errors or network operations. Its p-adic projection adapter first selects the canonical residue of a p-divisible g mod p², then uses the unchanged six AST-extracted Source functions. It checks the Source hash and exact function-name/dependency set, and does not execute the relative core import or unrelated helpers. The application is legitimate integer division/recomposition of that representative; it is not itself a p-adic normalization theorem. I extracted the same exact functions independently only for this adapter check. Running the author's main would overwrite its output file; I did not run it. The stored ten-prime log/results support the author's claimed run, while this review independently validates five cases and the mathematical proof. Author execution authority receipts are supplied by Root/author and are not a formal-authority conclusion of this local mathematical review.

The supplemental child report ODE_SANITY_CHECK.md independently found zero operator/recurrence residuals and the same finite cutoff argument. Its scope is strictly §§2–3; it supplies no acceptance of the later value/period claims.

## Handoff boundary and next gate

The supported increment is the **finite coefficientwise quadratic bridge mod p² at the exact Task rational-half algebraic lift**, with the first divided digit and marked derivative Jacobian preserved. It supplies an arithmetic carrier for comparison. It does not identify the raw Betina-Lecouturier period/first-normal scalar, its scale/sign/Fourier gauge or lift, and it does not infer from a norm-only formula that the whole source lacks oriented data.

The remaining gate is the independently calibrated source period/normal: identify its exact polynomial/local parameter, marked cusp and Fourier/sign convention, and actual lift, then prove a bidirectional comparison to this finite Hesse divided value. No c is reverse-engineered from UR. LIFT still needs the original finite-cutoff precision modulo p³ or a separate correctly proved replacement; this bridge cannot transport g/p modulo p².

All evidence is local and frozen for the authorized author's/Root's legitimate intake. This review makes no Source state mutation, mathematical acceptance, Task closure, Foundation/Working Truth claim or novelty statement. **This bounded review subtask stops after handoff; the parent Task and UR remain OPEN.**

Researcher-ID: EM-ENTERPRISE-836489 / RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT
