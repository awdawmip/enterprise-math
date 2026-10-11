# J1 neutral supporting research — mod-3 parity-steered Pell triple (2026-10-11)

Status: UNREVIEWED / NOT_ADMITTED. Author: ChatGPT scheduled researcher2, separate supporting research without a native claim. This is NOT the live owner's formal Result, research activity registration, Driver review, or an original six-dimensional Cell theorem.

GLOBAL_KNOWLEDGE_V1 snapshot: awdawmip/chatgpt-global-knowledge@49017179c37e3ca29ae78fccdce206a08d004574 (P000 ACTIVE, checked).
EM Source snapshot at proof construction: awdawmip/enterprise-math@410647cefb6872123fe829748aaa5224dbb23fca.
Formal task: RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT / TP2-0B9541A191FE5231A19B. Its 2026-10-11T09:17Z continuation reported LEASED/IN_PROGRESS with another active owner, EM-NATIVE-79EB13, and a six-row prior-art checkpoint pending formal Result freeze; no ownership was requested, taken, or displaced.

## New exact theorem

For k=2^r, r>=34 with r≡1 (mod 3), and any odd prime q>=2k+3, put N_j=(2j+1)^2+16k (0<=j<k), and U=69698, m(r)=max({0} union {m>=1:U^(2m)<2^r}). There are m(r) pairwise disjoint triples of indices, each having squarefree kernels d=17,41,697=17*41, with integer square product and with no N_j divisible by q. Thus for the previously established classical original-input count identity E(q,k)=2 sum_j(1+chi_q(N_j)), one gets E(q,2^r)>=4m(r), with chi_q(0)=0. In particular the new *even* r≡4 mod6 subfamily begins at r=34 and gives r=70 E>=8, r=100 E>=12, r=130 E>=16, r=196 E>=24 for all allowed primes. No all-r upgrade to the old theorem is claimed.

## Exact proof data

At r0=10 the three odd seed pairs (d,x,y)=(17,83,37),(41,529,85),(697,1923,73) satisfy x²-d*y²=-2^14. Their norm multipliers beta=(a+b sqrt(d))/2 are (5,1) at d17 of norm 2; (7,1) at d41 of norm 2; (27,1) at d697 of norm 8. For odd x,y,a,b,d≡1 mod4, among epsilon=+1,-1 exactly one makes both (a*x+epsilon*d*b*y)/2 and (epsilon*b*x+a*y)/2 odd integers; this follows because the two x numerators differ by 2 mod4, and the x/y numerators differ by (a-epsilon*b)(x-y)≡0 mod4. Taking absolute values gives positive odd norm solutions; after 3t steps in d17/d41 and t steps in d697 the norm equals -2^(14+3t).

The positive integral norm-one units u17=33+8sqrt(17), u41=2049+320sqrt(41), u697=34849+1320sqrt(697), all have odd A/even B and satisfy u_d<2A_d<=69698. An integral unit power normalizes each solution alpha=x+y sqrt(d) into sqrt(D)<alpha0<=u_d sqrt(D), D=2^(r+4). For h=0,...,m(r)-1, alpha_h=alpha0 u_d^h yields odd positive x,y with x< U^m*2^(r/2+1)<2^(r+1), so j=(x-1)/2 lies in [0,k). Different h give increasing x, different d give distinct squarefree kernels. Each triple product is (697*y17*y41*y697)^2. As N_j< (2k+3)^2<=q² and d<q, y<q, no selected factor vanishes mod q. The three ±1 Legendre symbols have product +1, hence at least one +1 per disjoint triple, giving E>=4m.

The initial legal r=10 seed indices are j=(41,264,961). One higher even case at r=34 has (d,x,j)=(17,2750717,1375358),(41,1784591,892295),(697,7134747291,3567373645). This proof does NOT assert the fixed unit orbits give legal j at every r=10+3t below 34.

## Executed reproducibility

The full local proof/checker/evidence package (artifact names to be transported separately) has checks: 3 exact seeds/norm multipliers/units, 16/16 parity-steering mod4 configurations, all 75 exponents r=34,37,...,256 and 300 mutually disjoint integer-square triples with exact j/x/y in decimal certificate, direct original finite-field mapping equal to E character formula for k=1024,q=2053 (E=2046) and q=2063 (E=2052). Source data digest SHA256=007fcc49cf894b5ed8977bf0492ed8be7209f92954a1152de39c0330dfcc3091. Full report digest SHA256=0502f97dfd16707dcea63392b3d63d18c40a47cf2ff6583a8548a9971c189eb8. The digests identify LOCAL scientific files; they are not claims that those files are separately committed in GitHub.

BRC application: original finite-field input labels, positive counted exterior branches, j/d/x/y provenance and valuation/squarefree-kernel distinction are retained. Legendre signs are detector states, NOT cancellations of positive branch mass. No native X6 transport is inferred.

Next smallest research question: construct low-height simultaneous odd Pell norm solutions for even r≡0,2 mod6, with parity-safe signed multipliers, or reduce U; then seek a quantitative E bound uniform across all dyadic exponents. Independent mathematical audit of parity steering, normalization, and uniform q-nonvanishing is required before promotion. Formal J1 six-row prior-art comparison is distinct and should not be repeated.