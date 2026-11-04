# Independent review of the R004 embedded-defect handoff

Date: 2026-11-04  
Reviewer: `EM-C34-D16900`, local execution `/root/research_cm_formal_1104`  
Verdict: **PASS within the paper's declared external finite-module language.**  
Formal admission / shared Review API / Task completion: none. This report is a local independent mathematical assessment, not a formal vote or shared-state transition.

## Frozen object and independence

I reviewed the following exact files from `../../nt` (actual directory `/workspace/agent_artifacts/balanced_resume_20261104/nt/`):

| File | SHA256 |
|---|---|
| `R004_EMBEDDED_DEFECT_AND_SEQUENTIAL_CONSTRAINTS.md` | `15004aff928f298eab4d052e97a8bd0b0c0ce5e473b280b7e13b38f991b472d8` |
| `interface.json` | `ca45134d54690d39fd346eddefe4320afa84bb7d9d148c759f944c20d5598196` |
| `verify_r004_embedding.py` | `26f7a0c95321c788153837ac214398dd20771532b10c7ad40e7c01e5ebe20953` |
| `verification.json` | `f519509da56fdc2176ae2c257b97dc96bf0ceec4bce78fe382100ff869d15e8a` |

The author is `/root/research_nt_1104`. I did not construct, suggest, edit, or debug these proofs or counterexamples. Our common parent and Source snapshot are shared context; they are not independent mathematical votes. Before this review I authored a separate C34 sampling note. Communication with this author during the review requested the final filenames/hashes and received their scope statement. The mathematical checks below are my own hand derivations. An earlier local draft was visible before the author's freeze notification; this verdict is pinned only to the final hashes above. All four hashes were verified after the final notification.

I read the original August R004 note preserved by inventory, the September profile checkpoint, the actual R004 Task, and the scoped BRC rules at Source `39556bf5207aa5ba559a27ec591c1bc1bf43b457`. General module-isomorphism results, Gaussian counting and fixed-length coding remain standard background; this report makes no global novelty determination.

## Mathematical checks

**1. The layer-profile collision is exact.** In `V=Z/p²Z`, the first state has `A=pR,B=R`, so the defect is `R/pR`. Adding `C=pR` leaves it unchanged. The second has `A=0,B=pR`, with the isomorphic initial defect `pR`; the same addition makes it zero. Both profiles are `(1,0)`. This does not reuse the August example that only separates residue-field rank: here the entire abstract defect module agrees. The rank-one/exponent minimality qualification is correct: at exponent one the only submodules of the free rank-one ambient space are `0,V`, and all nonzero defects arise from `A=0,B=V`; zero defects remain zero. No all-size/global minimality is inferred.

**2. Even a fixed ambient type needs the embedding.** With `A=0` in a labeled `F_p²`, `B_1=<e_1>` and `B_2=<e_2>` have the same profile, but adding the fixed line `<e_1>` kills precisely the first. A labeled ambient module is essential: arbitrary ambient automorphisms are not allowed to move the input line independently of the state.

**3. Individual kernels do not compose.** For `D=<e_1>`, the lines `<e_2>` and `<e_1+e_2>` each intersect `D` trivially but jointly span the entire plane. Two copies of `<e_2>` instead have the same two individual intersection kernels and leave `D` alive jointly. The relation `e_1=(e_1+e_2)-e_2` works over every prime, including characteristic two. The paper correctly limits this claim to a control table whose joint positioning has been erased: its two uncompressed input tables differ. It does not falsely claim a collision with identical fully supplied ambient inputs. Repeated controls are explicitly allowed, so the second table is admissible.

**4. Marked ambient quotient plus embedded target is sufficient.** Set `q:V→Q=V/A`, `D=q(B)` and `U=q(C)`. The image of `A+B+C` is `D+U`; dividing by the image of `A+C` gives `(D+U)/U`. The map from `D` to this quotient has kernel `D∩U`. Its preimage in `A+B` is `(A+B)∩(A+C)`, agreeing with the displayed kernel formula. Iterating quotient maps gives `Q/(ΣU_i)` and the target image `D/(D∩ΣU_i)`. This identifies both the final answer and every prefix answer. In particular, one must transport the second input through the first quotient, not reuse its original individual kernel.

For an onto map `f:V→V'`, the map `v↦f(v)+f(A)` is onto `V'/f(A)` with kernel `A+ker(f)`. The paper therefore correctly represents the cut by quotienting `Q` by `q(ker f)`. It explicitly retains the identification with `V'/f(A)` and subsequent control coordinates. That retained marking closes the otherwise real gap in mixed sequences. A profile, two abstract isomorphism types, or an unmarked quotient is not asserted sufficient. New target rows, reverse lifts and refinement are explicitly excluded, and remain open.

**5. Cyclic controls distinguish embeddings at fixed profile.** If `D≠D'` have equal profile in one finite marked `Q`, then they have equal size, and there is `v∈D\D'`. The cyclic submodule `Rv` lies in `D`; its intersection with `D'` is proper because it does not contain `v`. Thus the two quotient sizes after the same cyclic input differ strictly. For zero-only queries, a generating list of `D` produces a finite cyclic schedule whose sum is `D`; it kills `D` but cannot kill `D'`, since equal cardinalities would turn `D'⊆D` into equality. These are valid pairwise behavioral distinguishability arguments. They do not require the querying observer to know the unknown state in advance: separation by some common future word is the equivalence criterion. The marked-state transport above supplies sufficiency.

**6. Gaussian-binomial capacity has the stated conditions.** Dividing the number `∏_(i<d)(p^n−p^i)` of ordered independent tuples by `∏_(i<d)(p^d−p^i)` bases per subspace counts the possible `d`-subspaces. Pairwise distinguishability forces an injective exact residual code, hence at least `ceil(log₂ N)` fixed-length bits. Enumerating unique reduced-row-echelon descriptions attains this information bound. The endpoint cases `d=0,n` each have one state and need zero additional bits. The context—`p,n,d`, ambient basis, and common control interpreter—is explicitly fixed and excluded from that conditional bit count. No encoder efficiency, update efficiency, variable-length optimality, or unconditioned storage lower bound is claimed.

**7. Resource and scope statements are consistent.** A subquotient of `R^n` has at most `n` generators over this finite chain ring, so its layer entries lie in `0..n` and the stated profile-storage upper bound is valid. The paper does not turn that smaller but insufficient representation into a usable speedup. It accounts for input interpretation, sums/intersections, quotient maps, encoding and decoding as actual work. It does not infer submodularity, solve the Task's full parameter campaign, or close its inverse-refinement obligation.

## Finite verification and the BRC boundary

I inspected the frozen script before running it. Its submodule search starts with zero and repeatedly adds cyclic spans of all missing vectors; every submodule is reachable through a finite generating tuple, so this enumeration is complete for the chosen finite ambient sets. Explicit cosets and layer cardinality ratios implement the stated finite-module objects. The sequential check compares transported cosets rather than only a scalar size. The coordinate-deletion check compares complete layer profiles in the specified finite ring; it does not enumerate all possible coordinate maps.

I reran the exact frozen author script once, without modifying it, using:

`python3 /workspace/agent_artifacts/balanced_resume_20261104/nt/verify_r004_embedding.py > /workspace/agent_artifacts/balanced_resume_20261104/cm_formal/review_nt/reviewer_rerun.json`

It returned PASS, and its complete JSON content matches the saved author result after removing only `elapsed_seconds`. This is an independent rerun of the **same implementation**, not an independent implementation. The explicit covered ranges are:

- all 15 submodules of `(Z/4Z)²`: 3,375 triples, 50,625 two-update quadruples, and 225 pairs for the one specified coordinate deletion;
- every subspace for field pairs `(p,n)=(2,2),(2,3),(3,2),(3,3),(5,2)`;
- rank-one field controls at `p=2,3,5`, plus the displayed collision examples.

These finite checks supplement the hand proofs; they cannot prove the unrestricted theorems or satisfy the entire mother Task's experiment list.

The current `docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md` expressly scopes its restriction to heartbeat, BRC–Shor and native-residual research, stating that it does not extend to a general prohibition on other professional mathematics. The companion JSON lists `enterprise-math/heartbeat`, `enterprise-math/BRC-Shor`, and `native-residual-attribution`. PORTABLE applies `ACTUAL_TYPED_BRC_ONLY` within that scope. The actual R004 Task also explicitly distinguishes module cancellation from positive-mass BRC and requests exact integer/modular checks.

The reviewed program computes finite submodules, cosets and profiles; it does not create native states, evolve heartbeat dynamics, compute Shor behavior, or attribute a physical residual. I agree with the final draft's classification as external finite-module computation outside that scoped restriction. This is a scope determination, not an exception, not authorization for a native execution, and not a claim that ordinary Python is BRC. No new BRC-dependent admission gate is warranted for these exact results.

## Disposition

No mathematical correction is required for these frozen bytes. The paper and interface can be preserved as an independently reviewed, model-conditional local contribution. They must retain the fixed-target, marked-ambient, exact-control-language and conditional-code qualifications. Formal registration, remote persistence and Task acceptance are separate; this review neither performs nor presumes them. Root contributes zero mathematical votes.

Researcher-ID: EM-C34-D16900 / TASK_RESEARCH  
EM-Source-Status: Read=Verified snapshot reused (`39556bf5207aa5ba559a27ec591c1bc1bf43b457`) and frozen NT artifacts; Write=⚠ Not written — Source publication pending; local review artifacts preserved. Identity registration remains pending.
