# X6 unit 54 — finite Helly S12 chart to signed X6 Cell/BRC lift

Date 2026-11-16. Parent Task RS-X6-LEGACY-PLANE-RECONCILIATION / publication TP2-B4A441B23DA3159232C2. Original Research lane chatgpt-research-onhour-enterprise-math-20260923; researcher EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034. AUTHOR EXACT PROOF / FINITE INTEGER CHECK / UNREVIEWED / NOT_ADMITTED.

## Original source and scope

Current main producer is scripts/tool_discovery_helly_radon_certificate_calculus.py, immutable Git blob 6118b3bd04010e05355586d353c9cf0ec38b1070. Its check_enterprise_demos fixed-sector S12 chart uses three pairs of integer intervals: [2,7]x[1,6], [5,9]x[0,4], [4,8]x[3,9]. Their intersection is A={5,6,7}, B={3,4}, hence six ordered nonnegative S12 chart triples (a,b,0). The producer itself labels these FIXED_POSITIVE_S12_LOCAL_CHART and leaves the native Cell address unspecified pending explicit anchor and signed axes.

Native model: frozen P000 V5 at 59538f585d037d09ef687b28715c4bc1a3f9fe03, six signed axes, affine Cell torsor Z^6, component norm sum of six signed component squares. Preserve the joint observer relation: ordered steps, signs, axes, branch multiplicity and provenance.

## New exact bridge theorem

Fix any native Cell anchor x in Z^6. Choose an axis pair i<j among C(6,2)=15, signs (eps_i,eps_j) in {−1,+1}² and (a,b) in A×B. The labelled signed lift has displacement

 d = a eps_i e_i + b eps_j e_j,  endpoint y=x+d,

component-norm value G(d)=a²+b², natural shortest path length a+b and BRC multiplicity N_BRC(d)=binom(a+b,a).

THEOREM. Since a and b are strictly positive, support(d)={i,j}. Support uniquely recovers the axes; nonzero component signs recover the polarities; absolute values recover a and b. Thus at fixed anchor, all 6×15×4=360 labelled lifts map injectively to exactly 360 distinct native displacements/endpoints. The six chart-root path multiplicities are 56,126,84,210,120,330; their sum is 926. The complete all-axis-pair signed union has BRC mass 60×926=55,560. The six different squared norms are 34,41,45,52,58,65; this Helly chart is not a fixed-radius R063 shell.

PROOF. Direct interval intersection gives the exact two finite sets. Strict positivity gives a two-element support, which makes axis/sign/magnitude decoding unique. Native shortest step words consist of all shuffles of a signed i-axis steps and b signed j-axis steps, counted by (a+b)!/(a!b!). Sum the positive integer counts over six roots and 60 labelled charts. No positive-path cancellation is used. This is an internal P000 component-coordinate calculation, not a Euclidean-angle reinterpretation.

NONFACTOR WITNESS. The same local chart (5,3,0) can lift to distinct signed X6 displacements (5,3,0,0,0,0) and (5,0,3,0,0,0). Different choices of anchor give different native Cell endpoints. A consumer requiring native direction, origin, endpoint or trace must retain (x,i,j,eps_i,eps_j,a,b). The original unlabelled three-coordinate chart by itself has no uniquely determined native X6 address.

## Actually performed check and scientific boundary

The separately executed exact Python verifier copied the source's three finite interval pairs, iterated all 360 signed axis-pair/root labels, rejected duplicate displacements and checked square norms, step lengths and integer binomial weights. Standard Python and python -O both passed with zero failed checks on 2026-11-16. Exact checker: research_checks/X6_HELLY_S12_SIGNED_X6_BRC_LIFT_UNIT54_20261116.py; fixed expected results: research_checks/X6_HELLY_S12_SIGNED_X6_BRC_UNIT54_RESULTS_20261116.json. The published checker is a source-equivalent implementation of the same finite enumeration. The original Helly producer was read and pinned; its full program was not executed in this check.

This is a typed consumer bridge and exact nonfactor certificate, not a new Helly theorem or a complete full-six-axis shell result. It requires no source edit to the existing properly typed producer. Prior R063 six-blob 17/17 plus 512/512 author run (#50) was reused, not redone. Historical alleged wrong LP011 native argmax and LP019 positive natural BRC signed cancellation remain UNRESOLVED_PROVENANCE; full 28-LP current consumer closure and independent Driver REQUEST_REVISION remain open.

## Next

Consume successful original native #51 request onhour-20261116-0805-x6-lp011-valuation-unit51-native-progress-v1. Preserve GitHub/Activity #52/#53, authenticate own original winning run, then publish #52/#53/#54 semantic checkpoint without reuploading earlier GitHub artifacts. Inspect actual downstream Helly imports, and patch only a verified wrong native-address use; continue historical LP011/LP019 caller attribution. No scheduler or frozen scientific source change.
