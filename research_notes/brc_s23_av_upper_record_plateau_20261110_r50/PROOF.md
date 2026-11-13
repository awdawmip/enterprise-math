# R50 — Upper one-sided Farey record and maximal terminal phase plateau

Status: author-side exact mathematical derivation and finite computation; independent review pending. Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor: R49 Draft PR #2007 @5737faa62202b633dcf7e1183d0a8480fd88222f. This is the original-labelled irrational circle-rotation auxiliary model; no native X6 transfer is asserted.

## Theorem A — One bounded Stern–Brocot pair determines the last phase cut

Fix irrational 0<theta<1, integers m,H>=1, and K=m+H-1. Put e_k=ceil(k theta)-k theta for 1<=k<=K. Distinct k have distinct fractional phases, so the minimizer s*=argmin e_k is unique. R49 identified s* as the index of the rightmost nonzero phase cut and q*=e_(s*) as its terminal-cell threshold.

Start with Stern–Brocot neighbors a/i=0/1<theta<c/j=1/1, satisfying ci-aj=1. Follow mediants until the *first* state i+j>K. Then j=s*, c=ceil(s* theta), and v=c-j theta=q*.

**Proof:** Neighbor integer pairs (a,i),(c,j) form a Z² basis. Every (p,q) with q>0 and p/q>theta has unique integer coefficients (p,q)=k(a,i)+l(c,j). Let u=i theta-a>0 and v=c-j theta>0. Then p-q theta=l v-k u>0. If k<=0, necessarily l>=1, so p-q theta>=v. If k>=1,l<=0, the difference is negative. If k,l>=1, then q=ki+lj>=i+j. Hence any upper approximation with q<i+j has positive numerator error at least v. At the first terminal state i+j>K, the current upper j<=K (its most recent update used a previous sum <=K), and v<1. Therefore c=ceil(j theta) and j minimizes e_k among 1..K. Uniqueness yields j=s*. Every prior upper error exceeds q*, while later upper errors are nonincreasing. QED.

**Quotient-batched implementation:** If u>v, replace (a,i) by (a+k c,i+k j) with k=min(floor(u/v),floor((K-i-j)/j)+1). If v>u, replace (c,j) by (c+k a,j+k i) with k=min(floor(v/u),floor((K-i-j)/i)+1). The second cap stops precisely at the first denominator-sum overflow. Every residual remains positive for irrational theta. There are O(log K) Euclidean quotient blocks on integers of O(B+log K) bits given a certified B-bit theta enclosure. A final determinant and endpoint inequality provide a compact source-checkable minimizer certificate without sorting K+1 phases.

## Theorem B — Maximal terminal plateau improves transfer

R49's labelled state A_H(x)[z] is the smallest source age r in 1..H with {x-r theta} in the right-half-open historical arc I_z, or an explicit empty marker. The phase cuts {s theta},0<=s<=K partition the circle into right-half-open cells; A_H is constant on each. Sort the cuts x0=0<x1<...<xK<1 and call their state vectors V0,...,VK. Let V*=VK, and let ell be the smallest index such that Vt=V* for all t>=ell. Then [x_ell,1) is the **maximal contiguous terminal interval** with state V*. Put q_A=1-x_ell, so q_A>=q*.

Any upper Farey neighbor satisfying 0<v<=q_A, and every later upper neighbor, has the same entire original-labelled vector V*. At equality, the right-hand cell is selected. Within a batched upper update, the first crossing is k=ceil((v-q_A)/u) steps, capped at the positive-residual run. Proof: successive upper errors are nonincreasing, upper phases are 1-v, and the whole terminal interval has constant state. The predecessor cell differs by the minimality of ell. QED.

The compressed carrier retains one latest age *per original history label*. It is exact for this observer and future upper Farey transfers, rather than a count-only or unlabeled mass summary. Theorem A finds the geometric last cell without a phase atlas. To find the larger observer-specific plateau, sorting and inspecting adjacent final cells is a separate, potentially amortizable choice.

## Exact new non-S23 witness

Let theta=sqrt(2)-1,m=5,H=8,K=12. The last geometric phase cut is s*=12, upper c/j=5/12, q*=5-12theta ≈0.029437251523. The last two cells have the same entire labelled age vector (2,1,5,4,3). Their maximal terminal plateau begins at cut s0=7, with q_A=3-7theta ≈0.100505063388. Thus upper 3/7 is the *first guaranteed permanent state-transfer stage*, earlier than geometric threshold 5/12. The preceding upper 1/2 has state (2,1,7,6,5), an exact failure witness. For m=5,H=1, the last-cell vector contains empty history labels: permanence of the vector and full history coverage are distinct predicates.

## Frozen S23 and complete affine regression

For m=128,H=225,K=352, frozen theta lies strictly between LO/D and HI/D where D=10^24, LO=262204504569236716045286 and HI=LO+1. Both rational endpoints produce the identical seven Euclidean quotient blocks (13 unbatched mediants) until i+j>352. Their terminal upper is 59/225, so s*=225, q*=59-225theta. Here the maximal terminal state plateau contains just one phase cell. Integer phase/boundary floor comparisons for differences -352..352 remain stable throughout the interval.

The R50-linked exact compiler chooses the initial basis upper denominators 61 and 225 automatically: 2+76 of 78 Farey stages use them. The two rational endpoints together need 778 newest-source age inspections (225+164 per endpoint); 516 difference floors certify the frozen basis labels. It regenerates 9,697 positive events and the same 298 maximal affine runs as the R32/R49 reference. Final exact risk:
R_(10^12+128)=-4017401528447+15321634290944 theta.
The 15,356-byte TSV SHA256 is 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6.

## Complete comparable cost ledger and validation

With enclosure precision B, denote B-bit multiplication and division by M(B) and Div(B). Bounded upper-record discovery requires O(log K) Euclidean quotient blocks using O(B+log K)-bit integers, plus the cost P(theta,B) of constructing/refining the exact enclosure. Original history cuts cost O(m log m) comparisons. A basis source state costs O(H log m) labelled phase classifications, shortened by first full coverage. Theorem B's maximal plateau requires ordering K+1 phases (O(K log K) comparisons) and O(h H log m) phase-owner tests for h suffix cells including the first different predecessor; the entire generic atlas costs O(K H log m) tests and O(m K) age entries. The frozen production route uses 778 source age inspections, 516 certified difference floors, 78 stage decisions, 9,697 event records and 298 output runs, plus precision preparation, sorting, serialization, and independent validation. End-to-end bit cost depends on B and stage denominators. The 353-cut full atlas remains useful when many arbitrary endpoint queries amortize its preprocessing.

Six exact rational-enclosure families and two independently formed arithmetic routes were executed: the direct finite-phase/upper-record verification and the R49-based complete S23 compiler with R50 automatic threshold selection. Python stdlib integer/isqrt arithmetic is used; the non-S23 enclosure is the certified 10^32-denominator interval for sqrt(2)-1. Review, shared CLAIM/Result, and native X6 interpretation retain their separate authorities.

## Next research R51

Find the top two or few one-sided phase cuts from continued fractions without O(K) phase sorting; test observer-state change events and maximal terminal plateau across non-S23 families; measure actual bigint arithmetic bit lengths and many-endpoint atlas amortization. Source provenance and immutable scientific pin remain unchanged.
