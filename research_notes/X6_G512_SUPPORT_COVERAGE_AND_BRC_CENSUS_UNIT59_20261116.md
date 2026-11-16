# X6 / LP019 / R063 — exact native six-axis quadratic-shell support coverage, g=0..512 (research unit 59)

Date: 2026-11-16. Parent task: RS-X6-LEGACY-PLANE-RECONCILIATION; publication: TP2-B4A441B23DA3159232C2. Research lane: chatgpt-research-onhour-enterprise-math-20260923. Prior author-side Researcher EM-X6-FB6990 and SID MCP-082892eb480e45dea6d4b9fcc0491034 are provenance only until current owner/claim and native write receipt are independently confirmed. Classification: AUTHOR-PROVED / AUTHOR-EXECUTED EXACT INTEGER CENSUS / UNREVIEWED / NOT_ADMITTED. This note does not itself assert formal Result or independent Driver approval.

## Actual objective and frozen science

Continue unit 58 (G=25) by measuring how much *native signed six-axis* quadratic-shell endpoint and positive N-BRC mass is missed by a restriction to at most two active signed axes, at every exact integer radius g=1..512. This is a mathematically distinct observer/support-completeness test, **not** an alternate performance run of the original fixed two-generator R063 Stage0 experiment or a substitute for its frozen 17-gate/512-radius execution (previously author-executed as unit 50). No frozen scientific file was modified.

Immutable baseline: P000 V5 and centered signed X6 Cell torsor at enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03; pre-rebase comparison corpus at fd2bcff10ca6e147348b6c1236027fc0d2877df3. Native object: signed displacement z in Z^6, with primitive signed unit-axis steps, G(z)=sum z_i^2, T(z)=sum |z_i|, support s(z)=#{i:z_i != 0}. Positive shortest-path multiplicity N(z)=T(z)!/prod_i |z_i|!. The component quadratic is the stipulated Enterprise 120-degree orthogonality readout, not a silent Euclidean-angle replacement. Endpoint and path identities have distinct types; the observer retaining only support <=2 loses higher-support composite paths.

## Exact partition theorem (all g)

For a multiset lambda=(a_1<=...<=a_s) of positive integer magnitudes with 0<=s<=6, sum_j a_j^2=g, and multiplicities m_b=#{j:a_j=b}, the exact number of **named signed six-axis** endpoints in the corresponding orbit is

  E(lambda) = [6!/(6-s)!] * [2^s / prod_b m_b!].

All endpoints in that orbit have the same natural shortest-path count

  N(lambda) = (sum_j a_j)! / prod_j a_j!.

Therefore the exact endpoint census and N-BRC shell mass are

  C_6(g,s) = sum_{lambda: |lambda|=s, sum a^2=g} E(lambda),
  M_6(g,s) = sum_{lambda: |lambda|=s, sum a^2=g} E(lambda)*N(lambda).

An empty multiset occurs only at g=0, contributing one zero endpoint and one empty path. All coefficients and the support restriction are exact nonnegative integers. There is no signed-path cancellation in N-BRC.

An independently formulated coordinate-state recurrence starts from c(0,0,0)=m(0,0,0)=1, and for each of six axes appends signed magnitude a>=0:

  c'(g+a^2,t+a,s+[a>0]) += q(a)*c(g,t,s),
  m'(g+a^2,t+a,s+[a>0]) += q(a)*m(g,t,s)*binom(t+a,a),

where q(0)=1 and q(a>0)=2, with g<=512. The recurrence sums over labeled axes and shortest-word interleavings, whereas the partition method enumerates nondecreasing positive-square multisets and their labeled-axis embeddings. Equality of these two independently implemented finite integer algorithms is the numerical cross-check.

## Executed finite certificate and distinguishing witnesses

Both algorithms were run locally over every g=0..512, and their (g,s) endpoint and BRC mass tables agreed exactly. All 512 positive g have a nonempty six-axis signed shell in this finite range. Among them, 510 contain at least one endpoint with support >=3, and **332 of the 512 have zero endpoints at support <=2**. The first such shell is already g=3:

  g=3: 160 signed endpoints, all support 3, each with three primitive steps and BRC=3!=6; total positive N-BRC mass=960. A support<=2 model has 0 endpoints and 0 mass.

These are exact model-relative facts; they do not imply the original two-generator R063 program is malfunctioning.

| g | All signed endpoints | All natural N-BRC mass | Support<=2 endpoints | Support<=2 natural mass |
|---:|---:|---:|---:|---:|
| 1 | 12 | 12 | 12 | 12 |
| 2 | 60 | 120 | 60 | 120 |
| 3 | 160 | 960 | 0 | 0 |
| 4 | 252 | 5,772 | 12 | 12 |
| 5 | 312 | 23,400 | 120 | 360 |
| 25 | 7,812 | 2,538,954,612 | 132 | 4,212 |
| 512 | 4,194,300 | 2,545,987,322,677,489,518,895,281,083,395,586,219,409,000 | 60 | 36,064,823,400 |

For g=25 the old two-axis complement is 7,680 endpoints and 2,538,950,400 natural paths, precisely reproducing unit 46/58 independently. For g=512, support<=2 covers only 60 of 4,194,300 endpoints and a very small positive fraction of the path mass. No approximation was used to establish these counts.

A universal minimal-support witness is the g=3 signed displacement z=(1,1,1,0,0,0). It is an ordinary signed six-axis coordinate displacement, not a newly asserted primitive diagonal. The missing support-3 shell therefore cannot be recovered by changing weights on existing two-axis endpoints alone. The support projection is demonstrably not fiber-complete for native quadratic-shell/BRC aggregation.

## Verification and limitations

Local executable: X6_NATIVE_G_SHELL_SUPPORT_MASS_UNIT59_20261116.py, SHA256 7a8a0dbe2d676a2f95e3ccc4c570e1054b58730ee09c64d872133edb328c670e. It exited 0 with UNIT59_PASS. Full 513-row JSON: X6_NATIVE_G_SHELL_SUPPORT_MASS_UNIT59_RESULTS_20261116.json (local raw SHA256 1ba692c0feea5b40aaa5d3812f10ea2205ee101d1027deaf4f28137f192e8c11; compact canonical SHA256 fd7740f0659a7f4ab4d5ec7c7f01c46d3935a775727f57abe8aa82f5ba1562f8). The internal canonical pre-digest JSON SHA256 is 8d0d120ac6857faddd2958ed19783e75e30e74487706598ca25307ec42b890f3. Evidence covers exact finite g=0..512 only, not an unbounded radius experiment.

The universal partition identity is proved algebraically by permutation-orbit counting of labeled axes and signed choices. The 512 exact values are computational checks, not a formally checked theorem nor independently reviewed result. The current P022 L1-only shell function remains correct in its own type and is not patched here.

## Mother task and next action

For the 28-LP reconciliation, this establishes an exact observer-completeness obstruction: a full X6 quadratic/BRC consumer cannot replace all native signed-axis support with pair-only output. Retain the original R063 two-generator experiment as the already executed *different object*. Continue the actual frozen/historical consumer callsite search for LP011 erroneous native singleton argmax and LP019 alleged subtraction of positive N-BRC counts; both are currently UNRESOLVED_PROVENANCE, not established bugs. Driver REQUEST_REVISION, full dependency ledger closure and Source semantic publication of this author evidence remain independent responsibilities. Do not infer admission or task completion from GitHub persistence.