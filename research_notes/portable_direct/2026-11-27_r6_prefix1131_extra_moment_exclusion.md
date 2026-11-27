# PREFIX-1131 — One additional BRC moment excludes all 115 tail lines

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

Continue PREFIX-1130 at 4ff9e1768436f876e6f498ee5f40477a3c290b72:research_notes/portable_direct/2026-11-27_r6_prefix1130_three_observer_sharpness.md. Own original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322 / TASK_RESEARCH. Current owner query r6-20261127-1754-leased-observe SUCCEEDED, error=null, LEASED tasks=[], next_cursor=null, fixed as_of 2026-11-27T09:54:58.841973Z, Source 25f11ce49667bb82a8ead307bc475fa0165e5b55. No CLAIM or shared Task mutation. Account entries verified at immutable c2a724e932d908f4f297f9d764f322b951c2a047. Frozen P000 V5 and companions at f42f2906d77f24085c123f3ccfe9667d41caa96d; global P000 V4 projection matches blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Preserve inherited signed reversal -5, 5q cover, chart O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. All moment/jet/line coordinates below are auxiliary algebraic observations of the same signed X6 carrier. Inherited carrier correspondence, analytic boundary, root isolation and earlier 8400/8800 command-exit uncertainty remain conditions.

## 1. Add a genuinely independent constraint to the old compact relaxation

Retain the frozen 9600 compact anchor Acal=a0+W[-1,1]^6+diag(dr)[-1,1]^6. Do not rebuild it. The additional BRC moment at k=10000 uses the same first-component moment recurrence and local integral construction as the old anchor_dual in replay_9600_n300_gmp.py. In the inherited notation, let M_k be the row obtained by integrating the first components of the four Frobenius columns on 0<=R<=1 with weight (1-R/36)^k, with the inherited basis power and the two zero constant columns; use integ(k,half,N+5) and floor each term at 10^-120. The exact raw observation is the first-component beta moment

    y_k = 36^(-k) sum_{j=0}^k (-1)^j binom(k,j) 36^(k-j) v_j,

where v_j are the frozen integer moments, computed by the existing GMP recurrence. Inherited coefficient containment, Frobenius majorants and tail argument from anchor_dual give

    |M_k a - floor(10^120 y_k)/10^120| <= eps_k,
    eps_k = (35/36)^k + 10^-120 + sum_{basis} err + (4(N+1)+1)*10^-120, N=300.

All row floors are certified by outward integral intervals whose two endpoint floors agree. This uses the same proof/assumptions as the inherited first-component anchors, now at the new k; it introduces no native coordinates and retains the signed shared directions. Actual k=10000 moment floor is 598562840600612464366486634196135921426599526700837945689649870448946093338044531755825572353810227370031786187856213. The residual center is about -5.12594321084e-107; eps about 1.20600452310e-117. Moments at k=10400,10800 were also actually computed as exploratory alternatives, but are not needed for the final tail exclusion.

## 2. Joint observation exclusion lemma

For each primitive integer line (q,p,h), any true near-integer pair in a window [L,2L) with L>=L0=10^100 lies in the rectangle

    rho in [p/q,p/q+K/L0^2],
    c in [h/q-H/L0,h/q],

where K=d_upper+2E/q0, H=2d_upper+4E/q0, E=400000 and q0=544447235321021556325566186117974922693 (PREFIX-1123/1127). This is the full necessary tail rectangle, not the narrower witness rectangle of PREFIX-1129/1130. The outward rational square-root grid encloses t with rho=36/t^2-1. In the root fiber use G_c=beta F''+(alpha-c)F' from PREFIX-1124. A real candidate requires the SAME a to realize F_a(t)=G_c(a,t)=0 and satisfy the extra moment. No fixed d choice or higher derivative ratio is imposed on this exclusion.

For each candidate, interval evaluation of the first two observer rows and the new moment row gives an outer representation of the joint residual:

    Z = m + sum_j [-1,1] C_j + [-e,e],

where j=1,...,12 retains all shared columns and e includes full row variation, polynomial tails, extra-moment payment and rounding. For any integer n, zero membership implies

    |n dot m| <= sum_j |n dot C_j| + sum_i |n_i| e_i.

Proof: dot the representation of zero with n and apply the triangle inequality, preserving signed column cancellations before absolute values. Thus a single strict violation suffices to exclude the entire parameter rectangle, uniformly over L>=L0. Facet search is only a way to find a separating n, not a prerequisite for checking it. Round every center and each of 12 columns down on grid 10^125 and add 13 units to each outward error; the same inequality then holds using the resulting integer arrays.

## 3. Complete exact computation

The inherited PREFIX-1128 independent unimodular box enumerator is rerun, checking 620 integer points, all 115 primitive lines at L>=10^100 and q<=3*10^60. The output agrees exactly with the frozen list. For each line, tail_observers.py encloses the complete enlarged rectangle as above using exact rational interval Horner and the 301-term Frobenius jet through order two. All 115 slope upper bounds are strictly negative. One additional moment k=10000 suffices for every line. Each 3-row outer zonotope has 15 generators including the independent payment box; the actual search checks 105 pair normals. No numerical optimizer or additional anchor matrix inverse is used. All 115 rows finish with positive exclusion gaps.

More strongly, verify_fixed.py uses just the first line's separating normal for ALL 115 candidates, and does not need to enumerate normals again. The common integer normal is

    (380873982292799835375141926339646935705493731965503450737719374044,
     4404420198721196866057692195307558738385564975218471698347753940,
     110417258684195858620349411108446940860792702735356463946796033011784234655741996811326395).

The exact integer minimum absolute center and maximum support on this normal are in fixed_summary.json. Their ratio is approximately 14038.2083227; the verifier asserts minimum > 14000*maximum, with 56 positive and 59 negative centers. Thus even the uniform bound across the complete list strictly excludes all 115. This breaks the prior three-jet compact relaxation's information limit by adding an actual independent moment; the old counterexamples remain valid in their old relaxation. The 10400 and 10800 probes also exclude the old minimal line in the narrower fixed-d rectangle, but are unnecessary to the new result. No claim that they are rank independent is made.

## 4. Consequences

Under the inherited Stage46 premises, every real pair in a dyadic window L>=10^100 has b-a>=q>3*10^60. With the previous q^2<4 E L/d curvature bound and the sqrt-gap condition q<=sqrt(L), every fixed dyadic window starting below the following respective first not-excluded values is excluded (earlier windows by PREFIX-1128):

    L3=58713564569345830697237014919733425684392063722707996767682274288305225627865211086592474959619217575798374400000000
    L2=15391408670466593442296500039118599142609273152525565104667302111033485066991097895083697755814420172190089058713600000000.

L3 about 5.87135645693e115 and L2 about 1.53914086705e121, each 16 times the corresponding PREFIX-1128 bound. These are exclusion bounds at the current denominator cap, not certified smallest possible denominators or attainable first windows. The original 115 lines are excluded on the entire L>=10^100 tail, including the two earlier witness windows.

## 5. Evidence and next step

Actual primary run completed: compile anchor_moments.cpp with g++ -O2 -lgmpxx -lgmp, run ./anchor_moments 10000 10400 10800 > new_moments.txt; python extra_moment.py; python tail_observers.py 115; python prefix1128_verify.py; python verify_fixed.py. The last verifier returns all assertions passed. A separate monolithic replay attempt prefix1131_verify.py timed out after basis ready; it supplies no additional verification and does not affect the completed segmented run. The full local archive retains it as incomplete. The original execution outputs have SHA256: extra_rows.json 9575a73a2ff437c3e338a6c108e8fdf3256092d187eeb91f3355d50c62e54d98; tail_observers.jsonl d19b1392e56fe8e648cc6041ff372cc71db4e1ff4d58d3b8fff9470d384987ef; new_moments.txt df1ffb4cf9056d292a31a5c7caa5340df704bdb52adae9486e6a89e922871cf6; fixed_summary.json f2c61d2d7fcd7f1baca6427b054b12222ca7f13f011de419ea0a6094a935db95.

Remote readback of actual executed code, all Git blobs matched locally:
- 5e7443f3bd15d0ace50059447eebfb271d1e9fef:research_notes/portable_direct/2026-11-27_r6_prefix1131_extra_moment.py (SHA256 e87495451a00decace2dce76f9bfaef8b1123ad6c8aa17c504dc7c7c1844bf90).
- 191849318da0897350d7df889466f01bd3bb37de:research_notes/portable_direct/2026-11-27_r6_prefix1131_check_extra_core.py (SHA256 7bae10f3a3b49b2621cdfbecf09cc84d3977f561d0575e47860bb70d97a21ea9).
- 182317728fef6ec2d11c99619330136828575029:research_notes/portable_direct/2026-11-27_r6_prefix1131_tail_observers.py (SHA256 d34814d4dff1567f09a5892fd983be447ccb7cd2db019c13fde1e78905c3b670).
- b9c1d2d96b09f2879e467326b518d35019c787b2:research_notes/portable_direct/2026-11-27_r6_prefix1131_verify_fixed.py (SHA256 778d9717f0858644bd87259e15628615eb9a6c05e55fc4cd71f553e8b497f6e5).
- c0e3ebc480b5d05374511b2b8a3bd26ee73359e2:research_notes/portable_direct/2026-11-27_r6_prefix1131_fixed_summary.json.
- 922a34cd728b1cd1f9f2085b33d6de43b16d20dd:research_notes/portable_direct/2026-11-27_r6_prefix1131_new_moments.txt.

The local execution archive includes the frozen input directory of PREFIX-1130, the PREFIX-1128 exact verifier, the original GMP program from PREFIX-1126, and the new outputs/logs. Use the unprefixed filenames from the archive when reproducing. Preserve the prior anchor exits as inherited uncertainty; independent review and Activity observation audit pending.

Next: derive an updated affine lattice band from the common moment direction, using the same signed residual coordinate to eliminate lines before enumeration, then extend q beyond 3*10^60. The remaining single integer endpoint m=47247757565973207955345875119021762026915609 is unchanged; the continuous integer endpoint certificate is unchanged. True fixed-spectrum unbounded separation and B_fix,odd(32) remain open. No repetition of the 9600 anchor is needed.
