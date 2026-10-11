# U24: transported reserve, timely repair and lifetime order

Event: EM-20261011-CELL-U24-TRANSPORT-REPAIR-8C4D71
Status: CONDITIONAL_MODEL_THEOREMS / EXECUTED_TYPED_BRC / UNREVIEWED
Global read:46de0b0d4865d9e7410df30d96b07ee4167d1fbe
Source intake:670859d463cca9cd4d8f5e9f1d36f47792f8faa5
Predecessor: U23 REPAIR-RESERVE-74C2A9; all22 uploaded manifest entries verified.
Activity registration remains unresolved; no historical identity, Task/CLAIM or native admission is borrowed. This is new research, not retransmission of the previously rejected U22 report.

## Actual moving-path obstruction

Start the original four bodies at0,E1,E1+E2,E2, with AB,BC,CD,AD and four identified records. Release eligible BC, leaving its record1 free at B. The remaining AB,AD,CD graph is connected with total path length3. Execute unchanged U9 material() to grow B along a vacant transverse native edge. B now has degree1: the SAME released record supplies the new prefix on AB. Length becomes4, all four records are bound, and missing BC endpoints are no longer adjacent. The fixed-geometry repair proposal is not currently eligible, even though total resource inventory is unchanged. The actual inverse restores B, its source path and the free record, after which original BC capture succeeds. All eight signed transverse directions and per-stage free/held/bound identities are checked. This is an immediate repair obstruction, not a permanent-trap theorem.

If the sole free record is at y+nE3 and can move one native edge per stage, a repair requiring it at y cannot occur before n stages. The bound is attained by the inward route. Arbitrarily large finite distances are attainable by positive outward courier histories without adding another bound record. Thus no uniform finite delivery window holds across all such states. This does not imply that the mean repair time under the actual first-loss distribution is infinite.

## Exact repair-time criterion in a declared benchmark

The following is a NEW regenerative diagnostic, not a quotient, time rescaling or proof about U23's complete625-state modes or its moving-body extension. At a connected reference C, a first loss occurs with probability a*epsilon per stage. After that loss a spanning tree remains, with a released source record. Without another loss, repairing it would take sigma>=1 stages, possibly infinite. Include transport and binding work in sigma. Independently, a second critical loss occurs with probability b*epsilon BEFORE each repair stage and causes disconnection. Successful repair returns this benchmark to C with the same episode law. Record history is retained but passive for this stated observation; geometry/reference regeneration is an assumption needing proof in a full mobile model.

Put s=1-b*epsilon, h=E[s^sigma; sigma<infinity], q=1-h. The mean actual damaged interval is the positive survival sum

 u=SUM_(t>=0) s^t P(sigma>t)=q/(b*epsilon).

Renewing at successful repair gives the exact all-time formula

 E[T]=[1/(a*epsilon)+u]/q
     =1/[a*epsilon*q]+1/(b*epsilon).                       (1)

This uses the original probability space, including failure and nonreturn. For each positive epsilon, q>=b*epsilon and eventual first disconnection has probability1 with finite mean.

If sigma has finite mean mu, q/(b*epsilon)->mu and E[T]~epsilon^-2/(a*b*mu). If P(sigma=infinity)=theta>0, E[T]~[1/(a*theta)+1/b]epsilon^-1. If sigma is finite almost surely but its mean is infinite, q->0 while q/epsilon->infinity: lifetime grows faster than epsilon^-1 but slower than epsilon^-2. These statements follow from monotone convergence of the survival sum, not a fitted parameter sweep.

A useful sufficient condition is a conditional repair chance at least gamma>0 within K stages from every reachable unfinished state. Its geometric block bound gives E[sigma]<=K/gamma. The condition must include transport, occupancy, record availability and work. A finite mean under the actual episode-start law can also hold without such a uniform worst-state bound.

## A source-record courier with three regimes

Use the same four-record inventory. After BC releases at its actual head y=B, record1 takes one explicitly declared outward native step. At positive distance it steps toward y with probability p and away with probability1-p. It stops on FIRST return and completes two binding stages. Other losses remain possible during flight and binding. No new record identity is supplied. This courier is a controlled routing law along one native ray inside full X6, not a new one-dimensional world, unbiased six-dimensional diffusion, or a derived force law. Body positions are fixed during this delivery diagnostic; actual material motion was separately exercised above.

If tau_n is the courier's return time from distance n and d is additional work, sigma=tau_n+d. The literal benchmark uses n1,d3: outward transport plus two binding stages. First-step decomposition into positive ordered first-passage paths gives

 R(s)=s[p+(1-p)R(s)^2],
 h=s^d R(s)^n.                                           (2)

R is the least nonnegative solution, uniquely in(0,1) for0<s<1. The other root exceeds1. For p>=1/2 no-loss return is certain; its mean is n/(2p-1) for p>1/2 and infinite at p1/2. For p<1/2 the return probability is[p/(1-p)]^n.

Set R=1-delta. The exact quadratic is

 b*epsilon=(2p-1+2(1-p)b*epsilon)delta
                    +(1-p)(1-b*epsilon)delta^2.

Consequently, with all parameters and n,d fixed,

 p>1/2: E[T]~epsilon^-2/[a*b*(d+n/(2p-1))];
 p=1/2: E[T]~epsilon^-3/2/[a*n*sqrt(2b)];
 p<1/2: E[T]~{1/[a*(1-(p/(1-p))^n)]+1/b}epsilon^-1.       (3)

The fractional order is the critical first-return tail, not a prime/square-shell law. Even almost-sure record return does not ensure quadratic protection. With a=b=1,n1,d3, leading coefficients at p3/4,1/2,1/4 are respectively1/5,1/sqrt2,5/2. No physical probability or time calibration is claimed.

## Actual positive BRC calculation and finite-boundary warning

Positive height recursion F(x)=(s*p)*(s*(1-p)*x)^* uses unchanged recurrent BRC closure. Iterating from0 gives a killed-height lower bound; iterating from1 gives the reflected-height upper bound. Finite first-return prefixes separately preserve count,total,dominant and unresolved mass. For15 rational witnesses choose r<min(1,p/(1-p)), set s=r/[p+(1-p)r^2], and certify that r is the unique subunit root of(2). This is a proved all-time TOTAL observer, not a finite count of infinitely many histories. No numerical square-root, pi, classical propagator or ordinary matrix inverse is used.

Thirty complete finite reflected benchmarks are independently evaluated by unchanged pointed BRC state elimination and agree exactly with(1) and the height recurrence. At epsilon1/1024,128-level closures give outward-rounded UNBOUNDED mean bounds:

 p1/4:2556.26<E[T]<2556.27;
 p1/2:23260.56<E[T]<23261.54;
 p3/4:211271.71<E[T]<211271.72.

These are the new diagnostic's stage counts, not the U23 lifetime table or measured material lifetimes. Exact rational interval endpoints are retained in the package.

At zero loss a symmetric courier reflected at height K has mean return2K, verified by all-time BRC for K1..16. Including three work stages, every FIXED finite K has E[T_K]~epsilon^-2/(2K+3), while the unbounded courier has epsilon^-3/2. A reflective computation cutoff can therefore change the inferred lifetime power. The approximation boundary is not an unreported wall in the target model; limits in K and epsilon must not be exchanged without proof.

## Resource traces, verification and next target

All23 first-return words of length<=9 are executed in eight transverse signed directions:184 source traces and2136 checked phases. ContactInventory.toggle binds/releases the same original record. A selected trace actually releases another edge during transport, leaving the still-free courier at its remote Cell and a disconnected graph; no failure branch is suppressed. Another20 cycles execute release, native transport and recapture on ONE inventory object with the same four IDs. A carried record and a bound path-edge record are different roles and are never counted twice.

5303 new assertions;8 material-growth/inverse/capture cases;30 exact finite comparisons and234 full rows;15 certified rational all-time points;16 reflected zero-loss means;20 actual resource-reuse cycles. Calls:edge13701,alternative13428,serial25357,recurrent3988. Separate-process same-author replay reproduces results and compressed trace bytes exactly. No independent review or old full-suite rerun is claimed.

Unchanged eight-code chain: repair_reserve95426d4c2b3b0060c3f166696cf950eb7c0bb83f; residual_contact6160eb24cda9ef576d2972ef45df8e16e9fe67a4; contact_network5f89fe162f230c5ce31c317bda17089935f1c7fc; mobile_junction37931d40d7a2edc36889366d4766c83319eef0e7; local_latent67408af5b977bed7295f7225cdd3f550c41b9729; connected_retention569e6171d0052fbfd41cf007b09a8327b339228b; packet_router7465f5aa16cbb8fba61ba4be80f8a6884b879c53; brc_weighted3f205696709e847909958a153f8fe10d3f6b70f0. Original scientific bodies are unchanged; the inherited two-unused-import adapter is retained.

Results SHA256:5867810e749074ea06c230a358467ebf08f509ccf324be7eab60a4010fda9284.
Trace SHA256:5089e5a3204eddbbc9287f0504ec245c6145d42f8bbb75a43122332719718dd4.
Compressed trace SHA256:fa65c9e16cd41e071406de98f48589fce727f083b877d2ce4a53099474e3b615.

Full proofs, new code, dependencies and exact intervals are in cell_closure_u24_evidence.zip. This Source report is scientific preservation, not a standalone full-suite installation. General first-passage/renewal methods are attributed to Karl Sigman, Gambler's Ruin Problem(Columbia,2009), and Aldous/Fill chapter2 section2, read from primary author sources. They do not supply this native constitutive law.

Next: start from the actual moving four-body/path kernel's own first-release ensemble, suppress only NEW deletions for the repair test, and establish the required repair-time moment or its own heavy-tail/nonreturn obstruction. Neither the independent loss clocks nor the selected ray are automatically that kernel. Native material/field/support incidence, mechanical reaction and the original prime criterion remain open targets.
