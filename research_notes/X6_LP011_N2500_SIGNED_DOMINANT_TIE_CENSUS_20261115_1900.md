# X6 / LP011 — exact signed native dominant-axis ties on the N=2500 shell

Date: 2026-11-15 19:00 Asia/Hong_Kong. Parent `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Author-side Researcher `EM-X6-FB6990`; status **AUTHOR-EXECUTED / EXACT FINITE / NONBLIND / UNREVIEWED / NOT_ADMITTED**.

## Frozen ontology and observer

Freeze `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json`. For each genuine signed native displacement `z in Z^6` with `G(z)=sum z_i^2=2500`, define shortest-axis length `L(z)=sum |z_i|` and positive natural free-shortest-word mass `B(z)=L(z)!/prod |z_i|!`. The named signed dominant-axis **set**, not an arbitrary canonical axis, is

`Dom(z)={(i,sign(z_i)):|z_i|=max_j |z_j|}`; let `m(z)=|Dom(z)|`.

This is an LP011 native-argmax population calculation on all six signed axes. It does not infer which historical caller was erroneous, and the original R063 C3/C4 benchmark remains an independent execution object.

## Exact N=2500 theorem

| m(z), number of tied signed native dominant axes | signed endpoints | natural shortest-word mass |
|---:|---:|---:|
| 1 | 99,200,892 | 35475223480934449276968789614961077811398352519117351449193109599974530182415341882442005421332 |
| 2 | 3,275,520 | 8110893186798064638027688698967289983674264472806249147897587041553729333322631577221695358080 |
| 3 | 61,440 | 2677814761198139674727581468527950118702144444354117740270567960348335461723017382023533363200 |
| 4 | 1,200 | 1180206073344738821666738381471760663663866636929863218899499116432258805760 |
| **Total** | **102,539,052** | **46263931428930653590904265855801056735441499817749479001025131238806458196360489958119492948372** |

There are exactly **3,338,160** endpoints with `m>1` (3.255501% of endpoints). They carry **10788707947996204313935476240839978924043147298632127551832021638831928013945148075677487527040** shortest words (23.319912% of total free BRC mass).

If a downstream consumer counts a displacement `z` once **for each** member of `Dom(z)`, rather than once per Cell, it obtains **105,941,052** signed-axis memberships, exceeding the actual endpoint count by **3,402,000**. For BRC-weighted membership the uncorrected total is **59730454138124997581927735711858463421520268323679245620455454111846448109827653648685031450132**, exceeding the true natural BRC total by **13466522709194343991023469856057406686078768505929766619430322873039989913467163690565538501760** (29.108038% of the true mass). By symmetry each of the 12 signed primitive-axis labels has exactly **8,828,421** endpoint memberships.

The maximal possible tie on this shell is four: `(25,25,25,25,0,0)`. Examples for two and three ties are `(35,35,7,1,0,0)` and `(28,28,28,12,2,0)`. For five equal maximal magnitudes `M` and a residual magnitude `b<M`, `5M^2+b^2=2500` implies `M=5d,b=5c,c^2+5d^2=100`. Since `d=1..4`, the only putative squares would be 95,80,55,20, all nonsquares. Six equal magnitudes would require `6M^2=2500`. Hence no ties of size five or six occur.

## Exact constructive proof and separate check

Each endpoint corresponds uniquely to a sorted absolute tuple `a_1>=...>=a_6>=0` with `sum a_i^2=2500`, a permutation and signs of nonzero entries. If value `u` appears `c_u` times and `s` coordinates are nonzero, the sorted tuple contributes precisely `(6!/prod c_u!) 2^s` endpoints of tie multiplicity `c_{a_1}`. Each endpoint in that orbit carries exact free-shortest BRC `(sum a_i)!/prod a_i!`. Exhaustive recursive square decomposition with an exact last-coordinate `isqrt` test yields **3,356 sorted tuples** and the table.

An independently implemented **ordered-coordinate** coefficient calculation verifies each possible maximum `M=1..50` and every `m=1..6` against the sorted enumeration:

`C(M,m)=binom(6,m) 2^m [x^(2500-m M^2)](1+2 sum_(a=1)^(M-1) x^(a^2))^(6-m).`

The selected maximal positions/signs account for the first factors. The polynomial counts every remaining labeled signed coordinate smaller than `M`; the two constructions agree at every `(M,m)`. The BRC path totals also match the previously saved complete signed-X6 N=2500 result, including every support-stratum endpoint and BRC subtotal, and maximum shortest length 122.

## Executed checker and precise use

The self-contained stdlib checker is [`X6_LP011_N2500_SIGNED_DOMINANT_TIE_CENSUS_20261115_1900.py`](https://github.com/awdawmip/enterprise-math/blob/68cd1d3fa0e9fdca6f1094f8d1cc127669565242/research_checks/X6_LP011_N2500_SIGNED_DOMINANT_TIE_CENSUS_20261115_1900.py), Git blob `396038051e4c02aa4208977a32dd7f34fe178485`, SHA256 `d1478fc2813739cd654c006a6030296b07f0dff5c0915019afc947e4ad019c78`. The byte-identical local executable exited 0, reported `PASS_X6_LP011_N2500_SIGNED_DOMINANCE_TIES` and independently agreed with the saved 18:00 full-X6 JSON at every support/weighted subtotal; output body digest `872a904df983ba86e21bc3c00a055f2a2cec78b615b868becf9b246f42f47257`.

A current LP011 consumer needing an exclusive dominant axis must either supply a native signed-axis tie rule or distribute the path mass across the full tied set with an explicitly justified aggregation semantics. The exact new membership overcount is a finite acceptance oracle for such a caller. Its historical wrong-call provenance is still `UNRESOLVED_PROVENANCE`; LP019 positive natural signed-cancellation caller and complete 28-LP current consumers remain open. Original R063 Stage0 17-gate, 512-row native run remains at [execution-support #2416](https://github.com/awdawmip/enterprise-math/issues/2416); no substitute test is counted as that replay. Independent Driver review remains outstanding.

Native Source: #1–36 previously verified; author-side #37 GitHub saved; this new #38 is author-side saved pending live own-run authorization/semantic publication. Do not repeat old Source PROGRESS or reissue earlier denied 17:00 prose write.
