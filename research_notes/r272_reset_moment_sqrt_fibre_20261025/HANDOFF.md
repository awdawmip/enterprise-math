# R272 — continuation handoff

Status: AUTHOR_PROVED / SYMBOLIC_AND_INTEGER_CHECKED / NATIVE_OWNER_UNVERIFIED / DRIVER_UNREVIEWED / NOT_ADMITTED.

Global fixed read: main@5aae392dc3b79b95eaf2b7a0fae6eec385d2e983, P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. EM base read: main@54bcded9638e71659784c2d5673ffc88f31cfcdf. Reuse R271 commit be4d5bb132f99fd932be70201161faab7a8f334d and R262 author-side anti-concentration commit be6b89f3b2b9a477f747d68919625dcd0d025a95.

Exact new proved unit: for q=r=0 reset paths, GF for total a_m, marked t=epsilon*k sum U_m and V_m=sum t²; E(t)->(1-sqrt5)/4, Var(t)/m->3/2+7sqrt5/10. Pointwise H_n((0,0),g)=P_n(g), hence Lambda_(n-7)<=B_n<=Lambda_n. With R_m=ceil(sqrt(2V_m/a_m)), for n>=10 B_n>=ceil(a_(n-7)/(4(R_(n-7)+1))), yielding liminf sqrt(n)B_n/phi^n >= phi^-7/(20sqrt(2sigma²))>0. Reusing the still-unreviewed R262 all-eight-endpoint coefficient bound implies B_n=Theta(phi^n/sqrt(n)). Neither the proof nor the numerical checks are native P000/R193 physics.

Checker and evidence on this branch. Exact DP 0..150, raw 8191 words 0..12, 141 finite lower-bound checks, anchors B37/B67. Finite observation NOT theorem: B_n=Lambda_n for 12<=n<=150 only; unequal n=7..11.

Activity: RA-EMR3-20261025-0343-R272RESETMOMENT, local key scheduled-em-research3-20261025-0343-run11; no Source-backed session or CLAIM. Research material may be branch-durable without canonical main promotion. Preserve exact author/review distinction.

Next smallest research objective: prove B_n=Lambda_n for every n>=12 via six-channel same-effect injections (or find a counterexample); alternatively compute a rigorous lattice local-limit constant for Lambda_n. D(6) aggregation realizability and R193/P000 mapping remain separate unresolved objectives.
