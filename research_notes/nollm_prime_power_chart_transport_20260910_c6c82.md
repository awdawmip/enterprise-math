# Prime-power chart transport: natural additive towers, unavoidable permutations, and bounded observer debt

Status: RESEARCH_NOTE / ELEMENTARY_DERIVATIONS_AND_EXACT_FINITE_CHECKS / NOT_PROMOTED
Progress-Event-ID: NOLLM-TOWER-CHART-TRANSPORT-20260910-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-20260909-c6c82 (local continuity key, not an authenticated server ID)
Mode: TASK_RESEARCH / direct user continuation / no Task-ID or CLAIM
Date: 2026-09-10
Source read snapshot: enterprise-math@4e93f879f252ffcdd76152b45f0cf23139be7a9e
Parent: research_notes/nollm_phase_rigidity_charts_20260909_c6c82.md at e59f44244bce8745cb806e5331b183f6666615ae
Recovered parent executable: experiments/nollm_phase_rigidity_charts_20260909_c6c82.py at 2a74de1525713fd17b145e632777e2021815034b
Parent executable SHA256: 4690d7a3bf882b7682b628f02799f000e442f0f86d4ed9b5f5ab5f7522b1fcdf
Executable: experiments/nollm_prime_power_chart_transport_20260910_c6c82.py

## 1. Exact question and recovery

The parent established fixed squarefree-index chart-label bijections but explicitly left their compatibility with higher prime-power refinements open. This turn constructs that compatibility, distinguishes additive transport from mere digit relabeling, and computes the information required for unchanged ambient-coordinate semantics.

The previously local-only parent note and executable were pushed without changing their bytes; immutable Git blob readbacks match the original package. Its prior results were recovered, not presented as newly discovered. The six earlier activity events remain intact.

This is ordinary rank-two lattice mathematics with Q(q,r)=q^2+qr+r^2. It is a comparison/research slice, not a modification of P000, native dimensions, or Nollm runtime. Quotient refinement and its additive group law are NOT an intrinsic planar embedding of ordinary integer-label multiplication. All transfers below are prime-local; they are not one common ambient integer matrix acting on every prime component.

## 2. The rotating prime-power tower

Fix p=5 or 11 and W=[[0,-1],[1,1]]. Represent a projective line by l in {0,...,p-1,infinity}. Put

H_l={(q,r):r-lq=0 mod p}, H_infinity={(q,r):q=0 mod p}.

For t>=0 define

L_(l,2t)=p^t Z^2,
L_(l,2t+1)=p^t W^t H_l,
Q_(l,k)=Z^2/L_(l,k).

These are the parent's exact two-phase chains, with an arbitrary initial line. They are nested and |Q_(l,k)|=p^k. Let pi_(l,k):Q_(l,k+1)->Q_(l,k) be ambient reduction. Every fiber has p elements. The exponent of Q_(l,k) divides p^ceil(k/2), so modular arithmetic at that precision is sufficient.

All statements can be formulated with these finite modules. Their even levels also form the usual inverse system (Z/p^t Z)^2; referring to Z_p^2 is a shorthand for compatible finite residues, not an additional empirical assumption.

## 3. An explicit additive chart connection at every depth

For a finite line l write

B_l=I+lW=[[1,-l],[l,1+l]], n_l=1+l+l^2,
C_l=B_l/n_l.

For infinity use C_infinity=-W, with denominator one. Since p=2 mod3, n_l is nonzero modulo p. Thus all denominators are units at p. With chi_l(q,r)=r-lq and chi_infinity(q,r)=q,

chi_l C_l=(0,1).

Every C_l commutes with W and maps the horizontal line to l modulo p. Define the prime-local rational matrix

U_(b<-a)=C_b C_a^(-1).

At finite depth evaluate its denominator inverse modulo p^ceil(k/2), then reduce to the target quotient. This is explicit integer arithmetic, not floating division. It gives

T_(b<-a,k):Q_(a,k)->Q_(b,k).

Proof of well-definedness: at even levels U preserves p^t Z_p^2; at odd levels it commutes with W^t and maps H_a to H_b over Z_p. Equivalently its modular numerator sends every source lattice generator to zero in the target quotient. Its determinant is a p-unit, so the induced map is bijective.

The SAME rational U is used at every depth, hence

pi_(b,k) T_(b<-a,k+1)=T_(b<-a,k) pi_(a,k),
T_(c<-b,k) T_(b<-a,k)=T_(c<-a,k).

The maps preserve addition and commute with multiplication by every integer scalar on each finite quotient. The latter is an endomorphism of the quotient, not the p-way capacity expansion and not ordinary integer-label geometric multiplication.

At k=1 the identity chi_b U=chi_a proves exact agreement with the parent's numerical CRT-label transport. No unrelated bijection has been substituted.

For example, at p=11, horizontal chart to slope 3:

U=(1/13)[[1,-3],[3,4]].

Modulo 11 this is [[6,4],[7,2]]. The denominator 13 is invertible at 11. It is NOT invertible at the 13 component; the construction must therefore use this U only at 11 and use the identity at the separate 13 component.

## 4. Coprime products and adaptive displayed charts

For the finite intersection family, lattice CRT identifies the quotient with its prime-power components. Apply the above T independently to the 5 and/or 11 components; keep each split-prime component unchanged. These transports commute with every component projection and with one another. Therefore both orders of coprime refinement have corresponding fibers, not merely equal endpoint totals.

If a displayed chart c(s) is selected from the parent's finite geometric cost table at each exponent state s, define the displayed coarse projection from t to s by first projecting in chart c(t), then transporting at s from c(t) to c(s). Naturality and the cocycle identity imply that these displayed projections compose independently of intermediate charts. Thus changing the displayed chart does not force a loss of quotient identity or a path-dependent label convention.

This closes the parent's all-depth algebraic transport question for these towers. The previous restricted geometric bound, for example two-chart squared radius ratio <=172/25 at doubly active states, remains a separate shape certificate. It does not become an all-parity roundness theorem. Physical representatives may move when the chosen chart changes. Encoding a global nearest representative and measuring semantic-neighbor quality are not implemented by the small algebra-only prototype.

## 5. Even checkpoints cannot erase the chart change

All charts have the SAME lattice at depth 2: p Z^2. Nevertheless setting T_2 to identity is incompatible with a change of the preceding line. Naturality would make chi_b factor bijectively through chi_a, which requires equal kernels. Distinct lines have distinct kernels.

Concrete p=11 witness: a=0, b=3, x=(1,0). The transported source depth-1 label is 0, while keeping x fixed at depth 2 gives target label -3=8 mod11. The correct U sends x to (6,7) mod11, whose target label is 0.

There is a stronger additive rigidity statement for these rotating towers. Any compatible family of additive isomorphisms induces a matrix V in GL2(Z_p) on the cofinal even levels. Its reduction mod p must carry the three distinct lines W^t a (t=0,1,2) to W^t b. After composing with C_a C_b^-1 appropriately, a projective map fixes three distinct lines and is scalar. Thus V mod p is a scalar multiple of C_b C_a^-1 mod p.

For a!=b this is a nonscalar element of the field F_(p^2)=F_p[W]. It cannot have eigenvalue 1 over F_p. Consequently V-I is invertible modulo p and every p^t. Only the ZERO class can be fixed at an even checkpoint.

Therefore any all-depth ADDITIVE natural transport between distinct rotating charts must move p^(2t)-1 of the p^(2t) local even classes. For p=11, depth 2 means 120/121; depth 4 means 14640/14641. With an unchanged mod-5 component, this becomes 600/605 moved at (5^1,11^2). This is a conditional rigidity theorem for these towers, not a universal claim about arbitrary memory layouts or nonadditive bijections.

## 6. A lower-motion alternative loses addition

A second explicit construction is to write x in coordinate-wise base-p digits x_t and apply the frame

F_l(q,r)=(r-lq,q) mod p, F_infinity(q,r)=(q,r).

Use l_t=W^t l, order the two labels of each digit pair, and truncate after k labels. This encodes Q_(l,k) by a length-k p-ary word. Reading the same word in another chart yields natural bijections and a cocycle. This is a structured quotient-digit construction, not a claim of new scalar multiplication.

It need not preserve addition across carries. For p=11, source line 0, target line 3 and depth 4:

x=(10,0), y=(1,0),
T_digit(x+y)=(0,11),
T_digit(x)+T_digit(y)=(11,11) mod 121.

The digitwise map fixes 11 of 121 classes at depth 2, versus one for an additive all-depth map. It also fixes 11 of 14641 at depth 4 in this example. These finite counts are not a general optimization theorem. They separate refinement identity from the stronger additive contract; reducing migration does not automatically preserve arithmetic operations.

## 7. Keeping all ambient views costs only the missing next digit

The preceding transports change the ambient meaning of identity. For arbitrary ambient x, preserving its natural readouts in two DISTINCT initial charts instead requires their common refinement.

At even depth all chart lattices coincide. At odd depth,

L_(a,2t+1) intersect L_(b,2t+1)=p^(t+1) Z^2=L_(any,2t+2).

Two distinct lines already have trivial intersection modulo p; adding the other p-1 lines imposes no further constraint. Thus the minimal carrier for all natural chart readouts is

Z^2/p^ceil(k/2) Z^2,
number of states=p^(2ceil(k/2)).

Relative to one chart, the extra factor is p at odd depths and one at even depths. The additional information is ONE base-p digit, independent of t, not an accumulating p-fold factor at every step and not p physical copies of a memory.

For an unchanged mod-5 first layer and varying 11 charts:

11-depth | single-chart states | all-chart ambient states
1 | 55 | 605
2 | 605 | 605
3 | 6655 | 73205
4 | 73205 | 73205.

The joint carrier's successive refinement degrees are p^2,1,p^2,1,..., not p at every step. Each individual chart still refines p-to-one; the look-ahead observer has already retained the second coordinate at odd steps. This burst is a real interface cost; no fanout<=7 implementation is claimed. Minimality is for the stated arbitrary-ambient population and all-view observer contract. A chosen population of lifted labels is a different contract.

For several independently varying inert primes, the joint factor is the product of p over the currently odd active exponents. It is independent of depth for a fixed finite prime set but not uniformly bounded as new inert primes are added.

## 8. Executed validation and real reuse

The published standalone prototype uses only exact Python integers. It fully checks every ordered chart pair through depth 3 for p=5 and 11, and all depth-4 classes for three selected pairs per prime. There are 546 pair rows and 262050 class appearances, not that many distinct memories.

- 264450 naturality checks, including 2400 deep samples up to depth 101;
- 1092 source-lattice generator well-definedness checks;
- 524100 additive generator checks on the fully enumerated finite groups;
- 13608 exact chart-cocycle matrix checks, at depths 1,2,3,4,10,40,101;
- 2400 integer scalar checks;
- 52360 two-prime product projection checks;
- 1620 complete forward parent fibers, 16884 child appearances, with exact p-to-one correspondence;
- 50652 digitwise bijection/naturality checks;
- 30824 ambient joint-state checks, including all chart readouts through depth 4;
- enumeration of all 625 and 14641 two-by-two matrices modulo 5 and 11 for a representative rigidity constraint; exactly p-1 satisfy the three-line condition, and all have V-I invertible;
- the identity-reset and nonadditive-carry witnesses above;
- two fresh executions of the final core program produce byte-identical result JSON.

An additional executed compatibility check imports the preceding SHA256-pinned experiment unchanged, uses its cycle, label and labels functions and its complete saved 55-point sections, and verifies 47520 agreements with the original fixed-index geometric transports. It does not rerun the previous research as new discovery.

BRC: REUSE_EXECUTED for those exact prior interfaces. EXTEND_EXISTING_TOOL for the prime-power transport and observer audit, not a new global tool family. The retained data are prime, depth, chart, exact quotient residue and the declared identity contract. Additive maps, digit maps and ambient observers remain separately typed. Totals or shape scores cannot certify a commuting square. All-depth statements follow from the explicit modular identities and lattice intersections; finite tests supplement rather than replace them.

## 9. Remaining boundary

Resolved: the parent's fixed-index transports admit an explicit additive natural extension to all depths of the two-phase towers; CRT products preserve refinement order; even checkpoints require nontrivial label permutations; and the full ambient repair is exactly one look-ahead digit per odd active prime.

Not resolved: ordinary-number multiplication intrinsic to a planar address field; useful semantic neighborhoods under chart switching; an optimized migration/storage policy; unrestricted all-prime shape bounds; physical fanout and runtime integration. The next useful experiment should compare the two honest contracts, transported IDs versus ambient look-ahead, using migration distance and neighbor retention rather than another factorization-state catalog.

Classical context: Stacks Project, Section 10.96 (tag 00M9), describes completion by compatible finite module residues. Natarajan-Hong-Viterbo, Lattice Index Coding, arXiv:1410.6569, and Kurkoski, Encoding and Indexing of Lattice Codes, arXiv:1607.03581, provide established quotient-lattice coding comparisons. No novelty claim is made for CRT, p-adic completion or ordinary change of coordinates; the explicit rotating-tower compatibility, rigidity and repair accounting are the present task-level synthesis.
