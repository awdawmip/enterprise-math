# EC49DJ — 三类仿射正权 BRC 参数的负 E1 极端返回纤维精确秩

**2026-11-01 · AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_X6_FINITE_AUDIT_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED**

Frozen source: GLOBAL_KNOWLEDGE_V1 main@944038342fa74e70abe2bdd11fcb02c58051768f; Enterprise Math main@15009ebc884193a7713c4e81e2ad9f007068bd74. Canonical P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, verified against the startup projection. Source context: EC49DI in PR #1730 @c60360294b6b0578826ca4db927154d1d6df2659. P000 / ACTIVE worldview unchanged.

## Exact scope

Use actual ordered native signed-six-axis primitive prefixes of length n=2h+2m, h>=1, m>=0, displacement D=(-2h,0,0,0,0,0). For every positive +Ej give two BRC product-channel weights x_j>0, y_j=a*x_j+b with a,b>0; every negative -Ej has weight 1. Observe two positive products and path count in each of the four disjoint final labels none / A-only / B-only / both, where A=(+E1,+E2), B=(+E2,+E1), including prefix-suffix seams. The complete future alphabet of whole operations is a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3); use either exactly h or at most h operations.

At this extreme displacement, the unique returning suffix is e^h in both languages: each operation contributes at most +2 to E1 and only e reaches +2, so at most h operations totaling +2h force all e. e^h has neither A nor B. Our witnesses have negative last primitive letter, so no seam tag arises. The suffix multiplies the first two channel columns by nonzero fixed factors, preserving rank.

For each h,m write R_h(m) for the rank of the resulting 12-column four-tag/three-instrument observation matrix on all native prefixes of the given length and displacement.

## Exact classification (analytically proved for ALL h>=1 and m>=0)

| Affine weight regime | m=0 | m=1 | m=2 | m=3 | m=4 | m>=5 |
|---|---:|---:|---:|---:|---:|---:|
| All x_j equal | 1 | 1 | 3 | 4 | 4 | 4 |
| x1=x2, with x nonconstant | 1 | 2 | 5 | 8 | 11 | 12 |
| x1 != x2 | 1 | 2 | 5 | 9 | 12 | 12 |

In particular **x1 != x2 iff the negative-E1 extreme fibre has rank 12 at n=2h+8** among nonconstant positive affine parameters. This is an extreme-fibre iff, not an all-return-fibre saturation claim. If x1=x2 but x is nonconstant the extreme fibre first reaches rank 12 at 2h+10; if x is constant its maximum rank is 4, first attained at 2h+6.

## Proof

The signed length-displacement identity fixes exactly m positive primitive letters. In a fixed tag, two BRC products depend only on the multiset of those positive letters, whereas the ordered A/B tag limits permitted multisets. Four tags have separate output coordinates and each block rank at most 3. A or B requires at least two positive letters; both requires at least three. At m=1 all possible rows (x_j,a*x_j+b,1) are affine-collinear, giving rank <=2, or <=1 for constant x. At m=2 each A-only or B-only tag has product (x1*x2,y1*y2,1), so contributes <=1; both is absent. At m=3 each one-tag block contains positive +E1,+E2 and one +Ej; rows (x1*x2*x_j,y1*y2*y_j,1) have rank <=2. Both-tag paths at m=3 must have all three positives consecutively as 1,2,1 or 2,1,2, giving rank <=2, or <=1 if x1=x2. At m=4 with x1=x2=c, a both-tag path has three mandatory positives on axes 1,2 and only one other positive; rows (c^3*x_j,(ac+b)^3*(a*x_j+b),1) have rank <=2; other tags <=3. When x is constant both weighted channels are constant for fixed h,m, and every tag contributes only its count direction. These give the upper ranks in the table.

For constructive lower ranks, choose any two distinct positive axis weights u!=v, and put U=au+b,V=av+b. Three fixed-degree-four positive weight rows for k=0,1,2 or k=1,2,3, respectively, have exact determinants:

det [[u^k v^(4-k), U^k V^(4-k), 1]]_(k=0,1,2)
  = -a*b*v^2*(u-v)^3*(a*v+b)^2 != 0.

det [[u^k v^(4-k), U^k V^(4-k), 1]]_(k=1,2,3)
  = -a*b*u*v*(u-v)^3*(a*u+b)*(a*v+b) != 0.

For total positive degree two and k=0,1,2, the analogous determinant is -a*b*(u-v)^3 != 0. Adding identical positive letters to each selected word merely scales the two weighted columns by nonzero factors.

Each positive core C is realized as an actual native six-axis prefix by appending the negative-only tail (-E1)^(2h+count_1(C)) (-E2)^(count_2(C)) ... (-E6)^(count_6(C)). The resulting prefix has length 2h+2|C| and endpoint (-2h,0^5), and its tag is exactly that of C. It returns under e^h. Thus all following core certificates are genuine fully typed signed-X6 path witnesses.

If x1!=x2: for tag none and m=2, choose axis r=1 or 2 with x_r != x3, and cores (3,3),(r,3),(r,r): the degree-two determinant supplies rank 3. At m=1 cores (1),(2) yield rank 2. For m=3 the A-only cores (1,1,2),(1,2,2), B-only (2,2,1),(2,1,1), and both (1,2,1),(2,1,2) give two independent rows in each nonempty block, while none contributes 3. At m=4, A-only cores 1^k 2^(4-k), B-only cores 2^(4-k)1^k, k=1,2,3, and both cores (2,1,2,2),(1,2,2,1),(1,1,2,1) each realize k=1,2,3 positive E1 letters and the nonzero degree-four k=1..3 determinant. Prefixing identical E3 positives to all selected cores extends each rank to all m>=4. Hence ranks 1,2,5,9,12,...

If x1=x2=c and x is nonconstant, take q>=3 with x_q!=c. Tag none gets rank 2 at m=1 from (1),(q), and rank 3 at m=2 from (q,q),(1,q),(1,1). At m=3 A-only has independent (1,1,2),(q,1,2); B-only has (2,2,1),(q,2,1); both has a single product (1,2,1), giving rank 8 total. At m=4 a two-positive free prefix over axes 1,q followed by (1,2) or (2,1) gives rank 3 in each one-tag block, and (1,1,2,1),(q,1,2,1) yield rank 2 in both, totaling 11. At m=5 the two-positive free prefix over 1,q followed by (1,2,1) gives rank 3 also in both. Padding extends the 12 total to all m>=5. If x is constant, the four labels first appear at m=0,2,2,3 and each contributes rank one. Upper and constructive lower bounds match, proving the trichotomy.

## Actual finite evidence and limitations

An independent standard-library Python verifier reconstructs full primitive six-component endpoints, positive counts, labels including seams, both exact integer BRC products and modular ranks for every constructed witness. Seven positive integer parameter examples across all three regimes, h=1..30, m=0..6, primes 1,000,003 and 1,000,033: **PASS; 11,760 modular rank checks, 4,920 nonzero 3-by-3 checks, 10,050 native paths**. The actual executed checker, output JSON, command log and SHA256 manifest are in the co-located EC49DJ full-evidence archive. The analytic identities, not these finite tests, support arbitrary h and arbitrary positive real parameters.

Gateway status v0.6.11: research_authority_granted=false, executor_binding_configured=false, 5/5 active quota; a scoped owner query returned CONTROL_QUOTA. Current owner could not be verified. This is an author-side portable result, not CLAIM, native Result, independent Driver review or Foundation admission.

## EC49DK: next independent research unit

Determine true rank (not the rank of a restricted path family) of internal returning fibres for affine-positive x1!=x2 at n=2h+8. Start at h=2, D=(0,0,0,0,0,0), n=12 and x=(2,3,1,2,3,4), y=2x+1; expected formal dimension is 18 in both future modes. A one-neutral-gate lift of the fixed EC49DE six-feature bases achieved only 12/18 for this input: **that is a witness-family limitation, not a rank-deficiency proof**. Search additional actual six-axis paths or establish a complete upper bound. Audit the predecessor six-feature representation separately; the extreme-fibre proof above is self-contained.
