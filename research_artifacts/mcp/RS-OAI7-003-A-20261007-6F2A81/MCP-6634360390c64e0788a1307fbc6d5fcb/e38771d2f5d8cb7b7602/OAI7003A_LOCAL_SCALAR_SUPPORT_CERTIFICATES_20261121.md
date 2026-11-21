# OAI7-003-A：完整局部系数的重合素因子与零扩张保真见证（2026-11-21）

Status: NOT_REVIEWED / independent exact local certificates, not admission of global zero-free assertion.
Formal task: RS-OAI7-003-A-20261007-6F2A81
Original Researcher: EM-X6-C7A253; original session: MCP-6634360390c64e0788a1307fbc6d5fcb.
Frozen external input: openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, lines 627–643, 2817–2830, 3755–3760, 3857–3925, 3994–4006. This paper is an unadmitted research input.
Taskbook: awdawmip/enterprise-math:research_tasks/RS-OAI7-003-A-20261007-6F2A81.md (blob 890ef1ebc3973a77754ebf4bf7207c1b9b9c0987).

## Exact domain and local formula

Fix a good prime p outside S in the Eisenstein integer setting of the frozen manuscript; put Q=q_p. For squarefree c, n arbitrary, define e=v_p(c) in {0,1}, l=v_p(n) >= 0 and t=v_p(A)=e+3l for A=cn^3. Thus e and l may *both be positive*. The Poisson frequency H=ua^6 has j'=v_p(H)=j+6m, with j in {0,...,5} and m>=0. With k=v_p(s), the manuscript's local scalar C_p(t,k,j') is defined by the exact congruence sum in equation (local-scalar-definition), and evaluated by (local-scalar-values).

For k=0 and t>0 the evaluation is the extended-character Gauss sum:
- if 6 does not divide t: C_p(t,0,j') = Q^(t-1) G_t for j'=t-1; zero otherwise, where G_t=g_(chi_p^t)(p,1) (t modulo 6);
- if 6 divides t: C_p(t,0,j') = Q^t 1_(j'>=t) - Q^(t-1) 1_(j'>=t-1).
Here a principal character has zero on nonunits: chi_p(a)^j is 0 for p|a even for j=0 or j a multiple of 6. Do not replace its zero-extension by the constant 1.

## Exact support witnesses

1. **Overlapping prime in c and n.** Set c=p, n=p, so (e,l,t)=(1,1,4), and choose H=p^3, k=0; then j'=3 and
   C_p(4,0,3)=Q^3 G_4.
   The nontrivial Gauss factor G_4 has modulus sqrt(Q), so the coefficient is nonzero. Dropping all terms with gcd(c,n)>1 would erase this permitted contribution. For the same (e,l,t) and H=p^4, k=0, one instead obtains C_p(4,0,4)=0, establishing that the exact p-adic placement of H matters.

2. **Nonunit zero-extension in principal local character.** Set c=1, n=p^2, giving (e,l,t)=(0,2,6); choose H=p^6, k=0. The result is
   C_p(6,0,6)=Q^6-Q^5, not Q^6.
   At H=p^5 it equals -Q^5; at H=p^4 it equals zero. These are different values even though chi_p^6 is principal on units. Substituting an everywhere-one principal character changes the coefficient and hence the local Euler factor.

3. **k=1 row retains a different character exponent.** For t>0, j'>=1:
   C_p(t,1,j') = omega_p^(-1) G_1 * g_(chi_p^(t-1))(p^t,p^(j'-1)).
   In particular C_p(4,1,4)=omega_p^(-1) G_1 Q^3 G_3, while C_p(4,1,3)=0; and C_p(t,k,j')=0 for all k>=2. This confirms that collapsing k=0 and k=1 frequency sectors also loses exact arithmetic data.

4. **t=0 rows.** C_p(0,0,j')=1; for k>0 the coefficient is 1 only if j'=0 and zero otherwise. In particular, zero-character conventions cannot be silently discarded at t=0.

The unit factor U_p in manuscript equation (local-unit-factor) must accompany the scalar C_p; these certificates compare scalar support only and do not claim cancellation of the finite-ray phase by itself.

## Verified consequence and remaining mother question

Within the manuscript's own local definitions, these are exact nonzero, zero and unequal-coefficient witnesses. They show that any proposed factorization which (i) deletes overlapping prime support, (ii) treats a zero-extended principal character as constant one, or (iii) discards the k=1 sector is not coefficientwise equivalent. They do not establish convergence, continuation or the claimed Re(s)>7/8 zero-free theorem.

Smallest outstanding step: check that all v_p(c), v_p(n), v_p(s), v_p(H) sectors and unit/ray factors survive the full local-to-global Euler product, including justified rearrangement and the uniform bounds in the lemma, using the frozen exact hypotheses. Existing global calculations and independent review remain separate.

Provenance note: prior driver checkpoint revision 369 reports a 3299-byte locally staged witness with the first two examples. Its exact staged bytes were not presented as Source-published. This note restates the reported witnesses against the frozen paper and adds the explicit k=1 and t=0 distinctions; it is a new artifact with its own bytes, not a replay or claimed bitwise recovery of that staging.
