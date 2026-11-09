# PREFIX-628 / R2 — sharp online memory for every labelled BRC suffix path

Date: 2026-11-09 Asia/Shanghai. Frozen scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Original 48 native STAR phases, 96 ports and 576 positive, source/action-labelled BRC edges. Researcher-ID EM-X6-B1A2B2; activity RA-FF5063920D350BD884771A2A; task RS-X6-NATIVE-ROTATION-DYNAMICS. Author-side proof; independent mathematical review pending.

## Observer and sharp theorem

Start with the original four-point probe d=e4+e11+e14+e32 and amplitude λ>0. For all n≥L+4≥5 and gate sequence g1,...,gn≥0, retain the complete terminal native 96-port vector r_n=A(gn)...A(g1)E(λd). An additional bank of m continuously updated real scalar registers must suffice to recover EVERY ordered, original-source-port and action-labelled length-L suffix path weight, starting at actual state r_t, t=n−L. A coordinate of this suffix tensor equals the initial port mass at time t times the product of its L typed action weights; no path aggregation is performed.

THEOREM. Within this four-point native positive reachable family and continuous online-register observer class,

m_min(n,L) = L−1 if t=4, and m_min(n,L) = L if t≥5.

Thus even the full one-step labelled action tensor at n≥6 needs one previous-gate scalar beyond the terminal port vector. The restricted PREFIX-627 one-gate tagged witness λgn needs zero. A fixed L permits constant additional scalar memory for unbounded n.

## Native endpoint identities used

The exact original native eight-state and port decoder identities of PREFIX-617/622/626 give, for every n≥5, six endpoint-identifiable quantities: λ, four positive products Π_r(n)=∏_{1≤k≤n, k≡r (mod 4)}(g_k+3), r=0..3, and gn. In particular the phase row p=(2,28,38,16) gives λ; the four B rows (14,40,26,4) recover the four products; and the port split determines gn using

δ_n=r_n[29]−r_n[28],
ℓ_n=v_n[3]+v_n[14]+v_n[15]−2v_n[2]>0,
gn=(ℓ_n+9δ_n)/(ℓ_n−3δ_n), with ℓ_n−3δ_n>0.

Their exact fiber consequence is: for any t≥2, the COMPLETE original 96-port r_t is a function of exactly (λ,Π_0(t),Π_1(t),Π_2(t),Π_3(t),g_t). This is a scope-specific equality, not a replacement of labelled path observation by phase sums. All divisions use positive g+3, including zero gates.

## Constructive upper bound without solving a large matrix system

Maintain the actual original native endpoint online. Immediately before each update, recover the previous gate from that previous endpoint. At a query with t=n−L≥5, retain the last L old gates g_t,...,g_(n−1); at the first admissible boundary t=4, retain only g5,...,g_(n−1), L−1 gates. The current endpoint itself supplies gn.

Remove the known factors g_(t+1)+3,...,gn+3 from each terminal product Π_r(n), obtaining Π_r(t). Construct synthetic nonnegative gates h1,...,ht, initialized to 0. For t≥5 set ht=gt. In each mod-4 residue class choose a flexible index i≠t if available; when the class has only one index, choose that index. Define

h_i = Π_r(t)/[∏_{1≤j≤t, j≡r, j≠i}(h_j+3)]−3.

All other h_j in that residue class remain 0 (except the saved ht). This gives h_i≥0 because all actual unknown factors were ≥3 and the specified ht is equal to its actual value. When t=4 each residue has one index and the formula recovers all four early gates. The synthetic prefix has exactly the true four products Π_r(t) and the true last gate ht wherever required. By the native fiber identity its full original port endpoint equals the TRUE r_t. Apply the original A(h) operator t times to E(λd), obtaining that exact precursor r_t. Then multiply native edge weights along every requested labelled suffix path using known true gates g_(t+1),...,gn. This is an explicit exact algorithm and preserves source, port, action label and order.

The simple construction uses O(576t) exact source-action updates, O(L) supplementary scalar registers and O(number of emitted labelled paths) output multiplication. Worst-case explicit tensor size is O(96·6^L); register count is not a bit-complexity bound. Faster 16-state pullback remains a separate engineering objective.

## Lower bound

Work on an open strictly positive parameter family. When t≥5, freely perturb the L gates gt,...,g_(n−1) near any positive reference and, in each residue class r, compensate one distinct early gate i(r)∈{1,2,3,4} using

g'_(i(r))+3 = (g_(i(r))+3) × ∏_{t≤k≤n−1, k≡r}(g_k+3)/(g'_k+3).

The new early gates remain positive for sufficiently small perturbations. The four complete shifted products, λ and gn are unchanged, so the original FULL terminal 96 ports are identical throughout an open L-dimensional family.

The full original labelled suffix observer distinguishes every member of this family:

(1) PREFIX-625's exact native action graph shows each of 64 live source ports has a weight-one gate-free path of every positive finite length. In particular the L-step labelled tensor directly reads the actual source-port masses r_t[28] and r_t[29], since both are live.

(2) On the constant-endpoint family, the prefix residue products Π_r(t) and λ are fixed because all gates after t are held fixed when gt alone varies; for the simultaneous variation argument, the late gates after t also vary, but the suffix observer itself recursively determines them as shown in (3). More generally, the native split δ_t=(gt−1)ℓ_t/[3(gt+3)], ℓ_t>0, and the full tagged observer includes enough source-port data to reconstruct the split. For the fixed-product slice where future gates are fixed, δ_t strictly distinguishes gt. The exact complete labelled-history map is locally injective in the L free gate parameters, as can also be established by the gate-free source readings and the original gate-edge path readings in (3).

(3) Once the precursor live-port masses and earlier suffix gates are determined, recover each next gate from a positive labelled path: use any positive action prefix reaching source port 9 at the relevant time, take gated edge 9→29, and extend via a gate-free positive path. There is a positive prefix because r_j[9]>0 in the original four-point family for all j≥2; positive gate-free extension exists by the live-port graph. The path weight divided by its known positive prefix and suffix factors gives the gate, including boundary value zero by algebraic continuation.

In particular, for two histories with the same full suffix tensor, first compare gate-free source coordinates; then recover the future gates by (3), and hence the fixed prefix products; then identify gt by the strictly monotone split in (2). Therefore the suffix tensor is injective in the L-dimensional constant-terminal family. A continuous m-register map on that fiber must be injective; invariance of domain implies m≥L.

At t=4 there are only L−1 freely variable tail gates g5,...,g_(n−1) after holding terminal products and gn fixed. The same labelled-path argument distinguishes them, proving m≥L−1, including the L=1, n=5 zero-register boundary. Both bounds match the online constructions.

## Original-operator evidence and review status

The accompanying standalone Python Fraction test reconstructs the frozen native action rule, all 576 edges, original endpoint, synthetic prefix and every labelled suffix path (including zero gate branches from occupied sources). It passed 30 exact nonnegative rational test cases, 2,880 entrance-port comparisons and 62,160 labelled path comparisons for horizons n∈{5,6,7,8,9,10,12}, L∈{1,2,3}. It also reproduced the original same-terminal/different-one-step-suffix witness (n=10, λ=3/2, all gates one vs g1=9/13,g9=4/3). This finite evidence checks the implementation; universal claims are supplied by the native endpoint identities and the mathematical argument above.

Dependencies: PREFIX-625 exact all-horizon action graph and rank note (Git blob 83c3a938c8029ceab0ba5a3f869db415cf82435e); PREFIX-626 (commit 07de77571c6dca23f6e4858464d9514f6aaf10db); PREFIX-627 (commit adbfede51fd816d5c2263c41c1b8f1eeaebba87c). All are author-side, not independent Driver accepted. Scientific pin remains frozen; P000 and ACTIVE Heartbeat X6 worldview unmodified.

## Next actionable questions

Derive a direct backwards pullback using invertible 16-dimensional N(g) from PREFIX-625, removing O(n) synthetic-prefix replay. Independently verify the positive path observer's full fiber separation and audit boundary t=4. Then compare exact bit complexity and source-labelled output cost with explicit path-tree enumeration.
