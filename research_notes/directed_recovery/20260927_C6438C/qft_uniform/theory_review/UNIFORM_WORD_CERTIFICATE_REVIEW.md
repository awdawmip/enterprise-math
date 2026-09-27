# Reusable complete-word bounds: review and next certificate

Status: SHARED_CONTEXT_SYMBOLIC_REVIEW / NOT_ADMITTED. No new professional query, scientific arithmetic, propagation or admission was performed. Reading/decompressing an existing native receipt and hashing source files are provenance operations only. The current implementation remains the sibling's original `B^2=sB` sufficient-witness family; the additional bounds below are recommendations, not an implemented certificate claim.

## Reviewed sources and conclusion

The frozen EM source is `c0f04346c520fddc8016c86227b3b6cc2e9f30f6`, prefix `research_notes/directed_recovery/20260927_C6438C/qft_adaptive/`.

- `precision_theory/PREFIX_INDEPENDENT_WORD_CERTIFICATE.md`, SHA256 `3e99b6060e9e018689268692cd72218a12e645de1eeb2f1d65409ad823739f3a`.
- `precision_theory/ADAPTIVE_NATIVE_PRECISION_INTERFACE.md`, SHA256 `a0b95c02554e85c3693022bd309a4486f008be80491e1a1f0679d8f40b75d1d6`.

No substantive error was found in the first note. Its PSD argument, omission conjugacy, increasing local charge and state-independent reuse follow under its stated complete orthogonality premises. Checking all entries of `B^2=sB` is sufficient. Failure of this identity rejects this witness only: it does not show the word lacks a useful norm bound, or that dropping it is necessarily inaccurate.

The main improvement recommended for a separate version is that a certified orientation-preserving word already has the **same safe half-trace bound**, without the quadratic matrix identity. This can reduce certificate setup substantially. The original identity remains useful to show the half-trace bound is exact and to bind a particular rank-two structure.

## 1. Complete columns give universal certificates

Let G be the actual D-by-D orthogonal matrix with all residual columns retained, and set

    B=(I-G)^T(I-G)=2I-G-G^T,    tau=tr(B)=2(D-tr(G)).

Then B is symmetric PSD and `0<=B<=4I`. These statements follow from complete orthogonality; they must not be inferred from an intended target angle or a few clean input columns. For any actual PSD covariance C with M=tr(C)>0,

    tr(B C)/M <= lambda_max(B)=||I-G||^2.

The following rational upper bounds are available without any spectral numerical solver:

    s_F = tau,
    s_G = max_j (B_jj + sum_(k!=j) |B_jk|),
    s_universal = min(4,s_F,s_G).                         (1)

For the trace bound, the largest nonnegative eigenvalue is at most their sum. For Gershgorin, choose a maximum-magnitude coordinate of an eigenvector; the row equation bounds its eigenvalue by that row's diagonal plus off-diagonal absolute sum. B is real symmetric, so the relevant eigenvalue is real. Absolute values must apply to every retained off-diagonal entry; cancellation among them cannot replace the absolute sum.

Given already admitted complete columns, tau can be obtained from the D diagonal entries of G, using exact signed observations. B itself needs only `2 delta_jk-G_jk-G_kj`, hence O(D^2) entry observations for the Gershgorin bound; forming `(I-G)^T(I-G)` or B^2 by a dense O(D^3) product is not necessary for (1). Word replay, column admission, rational bit lengths and receipts remain setup costs. D is fixed in this profile, but these constants and evidence sizes are still charged.

An optional positive rational diagonal scaling improves the Gershgorin candidate to `max_j[B_jj+sum_(k!=j)|B_jk|w_k/w_j]` for certified w_j>0. This is similarity by diag(w), not a changed physical metric or propagator. Its construction and exact divisions cost work; no optimal weights or generic improvement are assumed.

## 2. Orientation gives a stronger trace bound

**Lemma.** If G is real orthogonal and det(G)=+1, then

    lambda_max(B) <= tau/2 = D-tr(G).                   (2)

Proof. Over the complex numbers, nonreal eigenvalues of a real orthogonal matrix occur in conjugate pairs z,conj(z), with |z|=1. B has the same eigenvectors and eigenvalue `2-z-conj(z)` on both. Eigenvalue +1 of G contributes zero. Eigenvalue -1 contributes 4, and its multiplicity is even: all nonreal pairs have product one and det(G)=+1. Thus every nonzero eigenvalue of B occurs at least twice. Its largest value contributes at least twice itself to tau. This proof uses no ideal angle, floating-point eigenvalue, or claimed planar behavior.

Consequently, with a certified positive determinant one may use

    s_SO = min(4,tau/2,s_G).                             (3)

The determinant condition is essential. The reflection `diag(-1,1,...,1)` has B=`diag(4,0,...,0)`; tau/2=2 incorrectly bounds its norm squared 4. It is a useful negative control. Nor does positive determinant imply B^2=(tau/2)B: two orthogonal rotation planes with distinct nonzero B eigenvalues supply a counterexample. Formula (2) remains valid for that example and retains both planes and every residual mode.

If the original candidate s=tau/2 is positive and B^2=sB holds, every nonzero eigenvalue is s and `tr(B)=rank(B)*s=2s`, hence rank(B)=2. Thus the original witness certifies exact norm squared s. It gives no smaller numerical charge than the generally valid SO half-trace bound; its additional value is exact rank/spectrum certification. For B=0 use the canonical s=0.

When B^2 has already been computed, a rational u with `u>=0` and `u^2>=tr(B^2)` is another universal norm-squared upper bound. In the SO case `u^2>=tr(B^2)/2` suffices by the same multiplicity proof. One may take its minimum with (1) or (3). This is an optional reuse of paid data, not a recommendation to build B^2 merely to avoid the cheaper trace calculation.

## 3. Orientation is available from actual native provenance

The existing `new_word_compiler/NATIVE_REFLECTION_PAIR_CERTIFICATE.json.gz` was read, not rerun. Its archive SHA256 is `6b500a26d6112fb30dff3e0ebc9c7320b8d4ef02252f2bd8b07547b9d16c9062`; the complete decompressed payload SHA256 is `05424867b64a27146e1073c658682771c7a733e46fc10e4fd9a85042720c347d`. The primitive receipt records the actual H4 as one half of

    [ 1  1  1  1 ]
    [ 1 -1  1 -1 ]
    [ 1  1 -1 -1 ]
    [ 1 -1 -1  1 ].

This is not a determinant inferred from the name "H4". The displayed actual matrix is symmetric; its character columns give H^2=I, and its trace is zero. Therefore its four eigenvalues are two +1 and two -1, so det(H)=+1. The same receipt has actual negation -1 and swap columns `(0,1),(1,0)`, each with determinant -1. Embedding in any ordered distinct coordinate tuple is permutation conjugacy with identity on the other coordinates, preserving these determinants.

The binding chain is frozen primitive source `0852cad130c1d877174d235687cf60c19f318c58`: `stage78/shor_benchmark.py::native_quartet` records the actual C12/sign-companion columns and checks their character entries; `stage80/fixed_phase.py::primitives` and `apply_word` use those returned columns. `new_word_compiler/compiled_streaming.py::CompleteNativeWord` replays the normalized temporal word on every full basis input, records forward/inverse columns and retains exact dyadic scaling. The compiler's `positive_determinant` routine already counts non-H4 letters, but that routine alone is not an independent primitive proof.

For a legal normalized word whose native source and complete columns are bound to this chain,

    det(G)=(-1)^(number_of_neg + number_of_swap).          (4)

A future orientation certificate should retain the normalized word, legal distinct indices, primitive receipt hash and count/parity derivation. An unchecked user-supplied `determinant=1`, a phase-index label, or an old certificate for changed columns is insufficient. No new orientation shortcut has been executed in this unit; the sibling explicitly keeps its current B^2 witness interface unchanged.

## 4. Policy charge, composition and limits

For a single omission with reference T=LGR and candidate S=LR, left and right factors are common complete orthogonal products. Then `||T-S||=||G-I||`, without commuting any letters. Inverse reuse is also exact: B for G^T is `2I-G-G^T`, identical to B for G. Conjugated omissions retain the same operator bound even if an entrywise Gershgorin recomputation would change with basis.

If 0<=s<=4 is any valid squared-norm upper bound, the sibling instrument lemma gives a local charge at most

    f(s)=sqrt(s/2-s^2/16).

The radicand derivative is `(4-s)/8>=0` on [0,4]. A rational e in [0,1] is sufficient exactly when

    8s-s^2 <= 16e^2.                                    (5)

The [0,4] gate is essential: beyond 4 the polynomial turns downward, and beyond 8 it becomes negative, falsely passing arbitrarily small e. Clipping a proven nonnegative upper bound at 4 is legitimate because G is orthogonal. Clipping an unverified negative scalar to zero is not a proof. Trace/PSD nonnegativity and positivity of denominators belong to certificate validation.

Multiple omissions do not justify adding squared bounds. With T and S built from differing factors in the same positions, the ordered telescoping identity gives `||T-S||<=sum_j sqrt(s_j)`. A rational certificate may choose d_j>=0 with d_j^2>=s_j and use `s_total=min(4,(sum d_j)^2)`. Without square-root isolation, `min(4,k sum s_j)` is a safe weaker bound for k omissions. As a symbolic warning, a two-dimensional rational rotation with diagonal 3/5 and off-diagonal +/-4/5 has single-step squared distance 4/5; its square has distance 64/25, greater than the sum 8/5. This is a mathematical counterexample to squared-error addition, not a newly executed native fixture.

The policy should preserve the low-prefix/reference-suffix hybrid and its cumulative rational charge ledger. Decisions must be determined from public history and previously committed words, never a private sampled work label or prospective next bit. A reference fallback has zero new charge even though the prefix still reflects earlier omissions. Failing the uniform certificate does not authorize retroactively replacing old words. Zero-mass syntactic prefixes may use the same uniform word rule, but conditional probabilities remain undefined there.

Serialized reuse requires exact rational integers/strings, strict bit/index types, normalized word order, complete forward/inverse column and source hashes, bound method, scalar s, optional orientation evidence, and deterministic replay of the policy ledger. On restore, verify/admit a serialized certificate before trusting its accepted flag. Trusted in-process reuse may avoid repeated arithmetic after a binding check; report that boundary separately from cold admission. A budget interruption must not commit a bit, consume a charge twice, or silently lose a pending decision.

These are full-carrier Euclidean bounds. A reduced codec needs a proved common isometric invariant subspace for every compared word; a small display dimension or a codec admitted for a different family is insufficient. A nonorthonormal coordinate change requires its actual metric, not these unmodified traces.

## 5. Concrete bounded recommendation

Finish the existing B^2 witness run and its full-column negative controls without changing its certificate schema mid-run. Compare cold admission plus all reuse costs against the prior covariance-policy cost; removal of prefix-specific defect work does not remove underlying Gram/mass/probability work.

The next separate certificate version should try the actual signed trace first, with the native orientation proof when available: s=min(4,D-tr(G)) for SO, otherwise min(4,2(D-tr(G))). If that is insufficient, add the complete-entry Gershgorin bound and take the minimum. Only pay for B^2 or a stronger PSD certificate when the expected reuse can justify it. Rejected rank-two witnesses remain evidence and may receive a valid trace/Gershgorin fallback; they are not erased or relabeled as rank-two successes.

This is a reusable gate-certification optimization. It proves neither a cheap general Shor sampler nor uniform factor-success at a chosen fixed precision. Old query 2499 remains failed with zero records; no new professional query was issued.

Global-Knowledge-Sync: main@4b04602 / GLOBAL_KNOWLEDGE_V1
