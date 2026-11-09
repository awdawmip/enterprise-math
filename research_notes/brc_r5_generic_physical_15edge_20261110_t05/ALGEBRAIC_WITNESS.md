# R5 — Explicit lawful algebraic physical pair requiring exactly 15 Blackwell edges

Date: 2026-11-10 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_BOUND_CERTIFIED / INDEPENDENT_REVIEW_PENDING. Companion to `RESEARCH.md` in this directory, on the same frozen R5 science pins as PR #1913.

## A completely specified exact physical counterexample to the uniform 14-edge conjecture

Retain the frozen 14-parameter physical map, two stopping-time equalities, capacity constraints, 30 allowed Blackwell edges and seven likelihood-ratio labels stated in `RESEARCH.md`. The rational physical baseline `P0=(X0,Y0)` is explicitly reconstructed in `VERIFY.py` from frozen PR #1894; `VERIFY.py` also reconstructs a strictly positive 30-edge rational transport `E0` with minimum weight `1/10^7`.

Let `N_0,...,N_8` denote the nine rational physical tangent vectors returned by ordinary RREF free-variable order in `kernel(jac(constraints))` inside `VERIFY.py`. Let

`I=(0,1,2,4,5,6,7,8)`

and take the eight vectors `n_k=N_(I[k-1])` for k=1,...,8. Their 21-dimensional Blackwell RHS observation images `v_k` have **exact rank eight**, and `{RHS(P0),v_1,...,v_8}` has exact rank nine. The RREF convention, full original physical formulas and index list make these directions explicit, reproducible **rational** vectors without a free choice of basis.

Define the positive real algebraic number

`alpha = 10^(-10) * (1/10)^(1/9) = 10^(-91/9)`

and the *explicit, fully lawful* physical pair

`P* = P0 + sum_(k=1)^8 alpha^k n_k.`

This pair has all five original matched-time / `g=b` / target seedless-F equalities identically, because the `n_k` are in the exact physical equality kernel. `alpha` has algebraic degree **9** over Q: its inverse is `10^10 * 10^(1/9)`, and `x^9-10` is irreducible by Eisenstein at prime 2.

To establish positivity and Blackwell feasibility, let `S15` be the explicitly listed 15-edge invertible set in `VERIFY.py`; solve exactly for rational edge directions `d_k` supported in `S15` with `C d_k=v_k` using its specified 15 pivot rows. Define

`E* = E0 + sum_(k=1)^8 alpha^k d_k.`

Then all **21 Blackwell equations** hold identically. The exact verifier finds `max_{k,physical-coordinate}|n_k|=10` and `max_{k,edge}|d_k|=7`. Because `0<alpha<10^-10`, every physical coordinate changes in absolute value by less than `10*alpha/(1-alpha)`, and every edge weight by less than `7*alpha/(1-alpha)`. The basepoint minimum non-forced capacity slack is **7/2,000,000**; the 1-norm of the coefficients of any capacity slack is at most 3, so every non-forced capacity stays strictly positive. The basepoint minimum transport weight is `1/10^7`, and `7*alpha/(1-alpha)<1/10^7`, so all 30 edges of `E*` stay strictly positive. The four strict deficits are each >1/1000 at the baseline and change by less than `12*7*alpha/(1-alpha)<1/1000`. Thus `P*` lies in the lawful strict-deficit physical Blackwell chamber.

Finally consider any putative nonnegative realization of `P*` using ≤14 positive edges, with support S. By the exact span-exclusion theorem proved in `RESEARCH.md`, its 21-column span cannot contain the entire nine-dimensional linear physical RHS span W. Hence there exists a **rational linear functional** `ell_S`, annihilating every column of S but not W. Evaluating it at the proposed RHS gives

`ell_S(RHS(P*)) = ell_S(RHS(P0)) + sum_(k=1)^8 alpha^k ell_S(v_k).`

This is a nonzero polynomial in `alpha` with rational coefficients of degree at most eight, since the basepoint and eight directions span W. As `alpha` has algebraic degree nine, the polynomial cannot vanish. Yet a realization on S would make it vanish, contradiction.

Therefore

`min{|supp(E)| : E>=0, C E=RHS(P*)}=15.`

**This is an explicit algebraic, capacity-legal matched-time `g=b` physical counterexample to a universal 14-edge realization bound.** It is an exact finite-expression witness; the mother question “do all such lawful Blackwell-feasible physical pairs have a ≤14-edge realization?” has the answer **no** under the frozen R5 model. The unresolved finer classification concerns explicit *rational* small-denominator witnesses, special low-support chambers, and exact chart geometry.

## Verification and source

Run `python3 VERIFY_WITNESS.py` next to `VERIFY.py`; it imports/reuses the latter's exact checks. The test constructs eight RREF-indexed physical directions, checks their independent RHS images, solves eight exact 15×15 systems and all 21 equations, verifies maximal perturbation coefficients and physical/transport strict positivity **bounds**. `WITNESS_OUTPUT.txt` is the actual executed stdout. The final polynomial argument uses the independently established irreducibility of `x^9-10`. All numerical inequalities and equalities are rational; no floating-point representation of `alpha` is used.

Independent mathematical review and formal project result acceptance remain separate; no Owner/CLAIM is asserted by this branch.
