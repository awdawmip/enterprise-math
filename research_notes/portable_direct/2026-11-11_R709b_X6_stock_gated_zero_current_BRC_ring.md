# R709b — Stock-gated X6 counterflow ring and exact BRC zero-current holonomy

Date: 2026-11-11 (Asia/Shanghai). Classification: author-side exact candidate-model theorem; fully enumerated finite checker; UNREVIEWED. Parent task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Immutable publication: TP2-8B7E13C5904A2D6F1142. The parent had another live CLAIM when checked; this research does not assume that claim or submit a native Result.

## Frozen foundation and actual source

Task science is pinned, not rebased: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md). All three files were actually fetched at this immutable commit. Current operating rules were read separately.

V17 supplies the active-triad slot replacement and S3 holonomy. V20 supplies the one-hot pure-triadic unique maximizer: K(T,T)=6>K(U,T) for U != T. V29 defines allowed typed TRANSFER occurrences and nonnegative cumulative M/Rin/Rout. V36 proves a synchronous ring copy map. V38 supplies two noncommuting three-step based native X6 packets. V39 defines the based future joint observer (j,h).

Prior exact work: R706@16fd003aaaa88d221db442c9e048f9af6878487d, R707@696c2e3d698105447b77c64ecee631b91e052dcc, and R708@08add1a31272738532deb96ff002caf3ea44ce77. R707 overlays a fixed V29 transfer schedule, whose net directed ring current is nonzero. R708 proves pointed S3 root information is absent from the complete unrooted cyclic spatial necklace. The following explicit conserved-inventory candidate scheduler removes the arbitrary overlay and realizes zero net physical current.

## 1. Native input and positive BRC branch carrier

The four oriented based packets in the native six-axis active-triad space J(6,3) are:

    A : 012 -> 013 -> 023 -> 012
    a : 012 -> 023 -> 013 -> 012
    B : 012 -> 023 -> 123 -> 012
    b : 012 -> 123 -> 023 -> 012.

They all replace exactly one active native axis at each step. The V17 frame transports are involutions s=(0,2,1) for A,a and t=(1,0,2) for B,b. For any k,l >= 0 with k+l>0, form all **distinct oriented packet words** with k copies each of A and a, and l copies each of B and b. Each word is a separate positive unit-count BRC branch retaining its orientation, ordered provenance and full initial field; enumeration is not a physical probabilistic ensemble.

Put q=2(k+l), m=3q=6(k+l). Concatenate the q three-step packets into a cyclic sequence W=(S_0,...,S_{m-1}) with S_0=012 and every consecutive pair Johnson-adjacent, including S_{m-1} to S_0.

## 2. Exact conservative inventory-gated scheduler

Use the **same** ring of m labeled X6 Cells for every word at a fixed k,l, and declare links in *both physical directions* between i and i+1 mod m. Give every Cell two matching typed interface ports p+ and p-, and distinct nonnegative integer token inventories n_i^+,n_i^-. These are an explicit *candidate extension* to V29; the baseline V29 schema has additive event counters but no token inventory or autonomous event selector.

At every synchronous relation layer t, calculate each edge i's local gate from OLD state:

    fire_i(t) :=
      [X_i(t) Johnson-adjacent to X_{i+1}(t)]
      AND [n_{i+1}^+(t)>=1]
      AND [n_i^-(t)>=1].

If fire_i is true, simultaneously post these two permitted, typed, matched V29 events:

    TRANSFER(i+1:p+ -> i:p+)
    TRANSFER(i:p- -> i+1:p-).

The first sends one + token and the second one - token; if the edge is disabled it posts neither. Each Cell sends at most one token per type per layer. Compute all outgoing decrements and all incoming increments on old inventories in one simultaneous conservative step. At each fired target Cell i, apply the V20 unique-max update with clockwise neighbor X_{i+1}(t), yielding X_i(t+1)=X_{i+1}(t); a nonfiring Cell holds X_i(t+1)=X_i(t). Thus current triad fields and finite stocks **deterministically select** all events. This is a total local-gated, synchronously committed map; no externally supplied transfer list is needed.

## 3. Theorem: autonomous full-speed zero-current orbit

For every such oriented word W, initialize

    X_i(0)=S_i, n_i^+(0)=n_i^-(0)=1.

Then for EVERY integer t>=0 and every i,

    fire_i(t)=true,
    n_i^+(t)=n_i^-(t)=1,
    X_i(t)=S_{i+t mod m}.

Each ring edge carries exactly one + transfer in one physical direction and one - transfer in the opposite direction *per layer*. Thus its signed **physical edge 1-chain** is zero on every layer, not merely at the endpoint. Over the first m layers, all Cell counters are

    M_i=0,
    Rin_i[p+]=Rout_i[p+]=m,
    Rin_i[p-]=Rout_i[p-]=m.

They are independent of packet ordering; each directed port-labelled edge has count m. After m layers the entire Cell triad field and both stocks return to their initial values, while the cumulative V29 counters retain their m-layer history. The Cell-0 path is W followed by its initial triad; its V17/V39 pointed h is exactly h(W) in S3.

**Proof.** For t=0, each initial neighbor pair differs by exactly one native axis by packet construction, and each required source token exists. Hence every gate fires. Each Cell sends one and receives one token of EACH type; thus both token stocks remain one. The V20 K unique-max premise forces the clockwise old-neighbor copy because that neighbor is an admissible candidate. Consequently X_i(1)=S_{i+1}. Repeating this argument inductively proves the three identities for all t. The two opposite TRANSFER events on any one physical edge cancel as **signed edge incidence**, not as positive BRC masses, and the exact matched positive V29 counter increments give the displayed arrays. The V17 transport is the exact ordered slot replacement along W. QED.

For arbitrary initial nonnegative stock fields, each old-stock gate authorizes at most one outgoing token of each type, so updates preserve nonnegativity and the separate total stocks sum_i n_i^+ and sum_i n_i^-. Every fired edge still produces an opposite physical-edge pair, hence its net physical edge-current contribution is zero, even during partial firing. These are unconditional conservation properties of the stated candidate map.

## 4. Theorem: exact inventory threshold

Every edge fires in a layer if and only if every Cell has n_i^+>=1 and n_i^->=1, **provided the declared cyclic triad field is Johnson-adjacent everywhere**. Necessity follows by reading the + source at each i+1 and the - source at each i. Therefore full simultaneous firing on m ring edges requires at least 2m total tokens, at least m of each type. The uniform one-per-type construction attains the threshold and repeats indefinitely. Removing any one token from either species blocks at least one edge immediately.

The threshold applies to this paired-event, two-species, synchronous local interface; it is a sharp candidate-model resource result rather than a universal optimum over conceivable X6 dynamics.

## 5. Corollary: three holonomy values under identical zero-current port ledgers

For any k,l>0, all oriented source words share a fixed ring, identical local rules and stock allocation, the same complete final port-typed V29 ledger, the same zero signed physical transfer 1-chain, and the same base Cell-0 endpoint triad 012. They nevertheless realize ALL THREE possible even S3 holonomies, by the constructive embedding above and the R706 exact histogram.

Define C=binom(2k+2l,2k), z=binom(2k,k)binom(2l,l), and

    D=sum_{r=0}^{min(k,l)}
          (k+l)! / ((k-r)!(l-r)!(2r)!).

The exact positive BRC branch histogram is

    H(e)=z*(C+2D)/3,
    H(st)=H(ts)=z*(C-D)/3.

With the fixed coarse observation (full V29 ledger, zero current, stock totals, Cell-0 endpoint) the pointed h-fiber therefore has three members and its worst-case fixed-length repair requires exactly ceil(log2 3)=2 bits.

On the more informative *unrooted complete spatial necklace* observer, rotating the packet word by one complete packet shifts the entire initial field by three Cells. The scheduler is translation-equivariant with uniform stocks and link types. A first-packet transposition conjugates nonidentity h to its inverse: h(rho W)=H(first)^-1 h(W) H(first), interchanging st and ts. Thus the complete unrooted spatial necklace, all cyclic window decks of any radius, both inventories and the V29 counters still need exactly one binary root/frame bit on each nonflat necklace. This uses R708's exact converse classification; the scheduler supplies a non-overlay coupled realization.

Concrete 12-Cell words AaBb, ABab, BAba have pointed native axis-to-slot tuples respectively (0,1,2), (1,2,0), (2,0,1). A nonflat one-packet necklace rotation is AbaB -> baBA, with pointed (1,2,0) versus (2,0,1). All have equal counters and zero net physical edge current.

## 6. Fully reproducible exact evidence

The accompanying Python standard-library script simulates every actual stock-gated layer, records per-type V29 counter increments, checks nonnegative stocks and conservation, Johnson adjacency, cyclic triad shifts, V17 slot transport, R706 histogram and R708 necklace fibers. Its independent negative gates remove one + or - token at a chosen Cell and confirm loss of all-edge firing.

Exact enumerated cases:

| k,l | m Cells | oriented BRC branches | full holonomy counts | flat/nonflat necklaces |
|---|---:|---:|---|---|
| 1,1 | 12 | 24 | 16,4,4 | 4 / 2 |
| 1,2 | 18 | 180 | 108,36,36 | 18 / 12 |
| 2,1 | 18 | 180 | 108,36,36 | 18 / 12 |
| 2,2 | 24 | 2520 | 1296,612,612 | 164 / 154 |

Total = 2,904 separate fully checked positive BRC source branches and 67,248 actual simulated relation layers. Every assertion passed with marker R709B_STOCK_COUPLED_ZERO_CURRENT_BRC_PASS. The Python program and JSON results are separate Git files at this same revision. The finite checks establish those enumerated cases; Theorems 3 and 4 give the arbitrary nonnegative k,l statement by induction and incidence algebra.

## 7. Actual scope and next mathematical unit

The inventory, local predicates and simultaneous commit rule are explicitly new semantically typed *candidate* dynamics. V29's original PASS/TRANSFER definitions do not themselves select events or define token stocks. This result constructs one exact source-labelled extension satisfying their additive event syntax, stock conservation, X6 triad adjacency, and V20 unique-max response. It establishes zero physical edge current, but the separate port-typed directional counts are intentionally nonzero and retained.

Next: derive a locality-certified prepare/commit event semantics for the paired opposite transfers, check conflicts with any active native Link/Port capacity or temporal dependency requirement, and determine whether nonuniform initial stocks can still support a closed nonflat necklace orbit. Intersect accepted input configurations with that scheduler, then compute its restricted positive BRC holonomy fibers. Existing formal task owner and native Result/Review state are preserved.
