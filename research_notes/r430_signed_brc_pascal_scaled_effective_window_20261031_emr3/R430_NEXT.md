# R430 research continuation | 2026-10-31

Status: AUTHOR_SIDE_EXACT_DERIVATION / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.

Parent question: preserve the signed BRC branch algebra; quantify higher-order total nonnegativity of finite right-edge Toeplitz windows without promoting the auxiliary scalar observer to native X6.

Pinned research sources:
- GLOBAL_KNOWLEDGE_V1: main@970b5c00edacde19d0a8c5b6a6660e77d9877f57.
- Enterprise Math normative main: d93aeaece6d8d0916680c5de40ad66a7fbeaa18b.
- R429 exact right-edge coefficient bound: 163246e2bbdfe14ec6bd5d7f52dfc95456fab5f7.
- Native DIRECTED_RESEARCH authority_granted=false; active control tasks request returned CONTROL_QUOTA. Never borrow another owner's Source session or imply canonical CLAIM/Result.

New author-side analytic theorem: for K>=1, 1<=p<=K+1 and r>=64 K^3 p! p 2^((K+1)p), every right-edge Toeplitz minor of order <=p is structurally zero or >=(3/4)*product(u!)/product(v!)>0. Full-order effective threshold is exp(O(K^2)), improving R429 exp(Theta(K^2 log K)) at K>=4. Fixed p gives exp(O_p(K)); both remain conservative.

Proof dependency and evidence: R429 uniform coefficient bound |c_h-1/h!|<=32K^3/(r h!), Pascal factorial scaling, LGV integer-minor gap, determinant product telescoping. R430_VERIFY.py generates R430_EVIDENCE.json. Executed finite result:
R430_EXACT_PASS 40 40 2534 1234 1300 25 515591
Raw JSON SHA256 83467abd2d6e477f7a6cecd6da9ca62806c75dbaa82da335c34756b4226a182d.

Next smallest independent mathematical unit: replace the entrywise worst-case 2^(Kp) by a conditional-number bound exploiting nonintersecting Pascal paths for fixed p>=3, aiming at poly(K). In parallel, determine whether a growing window can exhibit a first higher-order negative minor and identify the relevant r-K scaling.

This PR branch provides the portable author-side artifact. Formal Owner/CLAIM/Result, independent Driver review and P000/native-world correspondence remain separate.
