# BRC root endpoints: exact residual identities and one fixed candidate

Researcher-ID: EM-HME-0CE4FD / TASK_RESEARCH  
Global-Knowledge-Sync: main@91cd38d / GLOBAL_KNOWLEDGE_V1  
Canonical snapshot: 91cd38de772d892c0707ba356d7bbcecb44996bb  
Project parent: ecf1ee1347804cb2fc2bec1f9d56fe96a21e2623

The root and residual directions now have an exact algebraic connection. Two root-endpoint gcds combine into one gcd with a signed center difference. A sufficient subcase tests that difference itself as a factor with one short remainder. The complete candidate check, including its root preparation, takes 3.275–6.900 microseconds on the three published puzzle inputs; none admits a factor.

The experiment retains 16 prescribed positive fixtures, including four verified small semiprimes and twelve larger constructed composites. All remain positive under the sufficient candidate test. Twelve additional small constructions verify the formula at ratio parameters 3, 5 and 8. No factor enumeration, multiplier expansion or public-input search fallback occurs.

## Input coordinates and separated states

For an odd nonsquare \(N>2\), let

\[
J=\lfloor\sqrt N\rfloor,\qquad
R=N-J^2,\qquad A=(J+1)^2-N.
\]

Then \(1\le R\le2J\), \(A>0\), and \(R+A=2J+1\). D means \(R\le J\); U means \(R>J\).

Define the center difference

\[
\Delta=J-R=J(J+1)-N=\frac{A-R-1}{2}.
\]

It satisfies \(-J\le\Delta\le J-1\). Because \(N\) is odd, \(J\) and \(R\) have opposite parity: \(\Delta\) is odd and nonzero. Consequently D has \(\Delta>0\), while U has \(\Delta<0\).

A prepared positive pair \(R,A\) encodes an odd nonsquare state exactly when \(A-R\equiv3\pmod4\). Indeed \(J=(R+A-1)/2\) is integral, \(R\le2J\) follows from \(A\ge1\), and the congruence gives odd \(J^2+R\). The two residuals retain the root coordinate in their sum; the computational representation is explicit.

The fixed-gap U criterion from the preceding direction also remains useful: if \(a^2=mN+b^2\), \(b\ge1\), and \(a>b^2\), then \(a\) is the immediate ceiling and the state is U. Its complete ceiling gaps were already available at the saved positions, so this checkpoint counts no new fixed-gap public witness query.

## Root-only and residual-only gcd identities

The root-only observations are

\[
g_-=\gcd(N,J),\qquad g_+=\gcd(N,J+1).
\]

They require the root coordinate and \(N\), with no input residual.

For a single residual and \(N\),

\[
\gcd(N,R)=\gcd(N,J^2),\qquad
\gcd(N,A)=\gcd(N,(J+1)^2).
\]

Their shared-prime supports equal those of the respective root gcds. For squarefree \(N\), the gcd values themselves agree. The initial numerical comparison verifies value agreement only on its fixed corpus; it does not assume that value equality for all composites.

There is a stronger exact form using both residuals:

\[
\boxed{g_-=\gcd(R,\Delta),\qquad g_+=\gcd(R+1,\Delta).}
\]

For the first identity, reduce \(N\) modulo \(J\), then replace \(J\) by \(J-R\). For the second, \(N\equiv R+1\pmod{J+1}\), and \(J+1-(R+1)=\Delta\). Neither identity needs a squarefree premise.

The equivalent parity-corrected expressions are

\[
g_-=\frac{\gcd(R,A-1)}{\gcd(R,2)},\qquad
g_+=\frac{\gcd(A,R+1)}{\gcd(A,2)}.
\]

To see the factor of two, \(2J=R+A-1\), and \(J,R\) have opposite parity. Thus \(\gcd(2J,R)=\gcd(J,R)\gcd(R,2)\). Apply the same argument to \(J+1,A\). This form was independently timed in the first residual-pair extension.

## One gcd for the union of both endpoints

Since \(J,J+1\) are coprime,

\[
\gcd(N,J)\gcd(N,J+1)=\gcd(N,J(J+1)).
\]

Subtracting \(N\) from the second argument gives

\[
\boxed{g_\cup=\gcd(N,\Delta)=g_-g_+.}
\]

For the stated domain, \(0<|\Delta|\le J<N\). Therefore any \(g_\cup>1\) is automatically a proper factor. This is exact for odd nonsquare composites, including those with repeated prime factors. The scalar union drops the endpoint label but preserves the existence of an endpoint factor.

The union audit compares six equivalent scalar outputs: complete/prepared endpoint gcds, complete/prepared center gcd, and complete/prepared residual-pair products. Each complete route pays for its native root and the coordinates it constructs. All nineteen fixed inputs agree.

In that paired run, complete public endpoint costs of 12.0875, 12.3875 and 30.5500 microseconds change to 8.0625, 7.9875 and 19.3125 microseconds using the center gcd. These are exact rewrites of the same endpoint information. They add no independent public factor observation.

## One sufficient candidate with no gcd in its query path

Set

\[
h=|\Delta|=|J(J+1)-N|.
\]

The following is a sufficient test:

\[
\boxed{h>1,\qquad J\bmod h\in\{0,h-1\}\quad\Longrightarrow\quad h\mid N.}
\]

The remainder condition makes \(h\) divide \(J\) or \(J+1\), hence their product. By its definition, \(h\) also divides \(J(J+1)-N\). Thus \(h\mid N\), and \(h\le J<N\) proves properness.

The query takes \(N\) alone, computes its native integer root, forms \(h\), and evaluates one short remainder. On admission it verifies the factor by exact divmod and product. It performs no gcd or factor search.

The residual form computes

\[
h=\frac{|A-R-1|}{2},\qquad R\bmod h=J\bmod h.
\]

Accordingly, prepared candidate calculation can read \(R,A\) alone. \(N\) is used when checking the resulting factor certificate. The prepared root form instead receives \(J\) and constructs \(h\) inside its timer.

This is a sufficient subset of the full center-gcd route. A miss means that this candidate was not admitted. It does not assert \(\gcd(N,h)=1\) for an arbitrary input, and the existing full gcd branch remains a distinct calculation. Outcomes coincide on the fixed measured corpus; that coincidence is not generalized.

## Positive families separated by state and endpoint

Let \(N=pq\), \(p>1\), and use integer ratio parameter \(a\). The following sufficient families explain root-endpoint successes.

For \(q=a^2p+\delta\), \(1\le\delta\le2a\),

\[
J=ap,\qquad R=\delta p.
\]

The state is D for \(\delta\le a\), and U for \(\delta>a\). For \(q=a^2p-\delta\), \(1\le\delta\le2a-1\),

\[
J+1=ap,\qquad A=\delta p.
\]

The state is U for \(\delta<a\), and D for \(\delta\ge a\). These follow directly by comparing \(N\) with the two neighboring squares.

Whenever \(q>a\),

\[
\gcd(N,ap)=p\gcd(q,a),\qquad 1<\gcd(N,ap)<N.
\]

For prime \(q>a\), this gcd equals \(p\). The two D branches and two U branches are recorded separately.

The short-remainder candidate has four positive subfamilies. For any odd \(p>1\) and integer \(a\ge2\):

| Cofactor \(q\) | State | Root endpoint | \(\Delta\) | Passing residue form |
| --- | :---: | --- | ---: | --- |
| \(a^2p+(a-1)\) | D | \(J=ap\) | \(p\) | \(R\equiv0\pmod p\) |
| \(a^2p+(a+1)\) | U | \(J=ap\) | \(-p\) | \(R\equiv0\pmod p\) |
| \(a^2p-(a-1)\) | U | \(J+1=ap\) | \(-p\) | \(R\equiv-1\pmod p\) |
| \(a^2p-(a+1)\) | D | \(J+1=ap\) | \(p\) | \(R\equiv-1\pmod p\) |

Here \(h=p\), so the candidate always returns the prescribed proper factor. All four cofactors are positive and odd under these conditions. This proves constructive positive families; no infinite prime-pair claim is made.

The original measured controls use \(a=2\). Four prescribed small cases received exact primality checks using the earlier bounded checker:

| Branch | \(N\) | Verified prime pair | \(J\) | \(R\) | \(A\) | \(\Delta\) |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| lower_D | 64643 | 127 × 509 | 254 | 127 | 382 | 127 |
| lower_U | 46117 | 107 × 431 | 214 | 321 | 108 | -107 |
| upper_U | 68513 | 131 × 523 | 261 | 392 | 131 | -131 |
| upper_D | 40501 | 101 × 401 | 201 | 100 | 303 | 101 |

For example, \(N=46117\) has \(J=214\), \(\Delta=214\cdot215-46117=-107\), and \(214\bmod107=0\). The candidate is \(107\), and \(46117=107\cdot431\). This is a U positive.

Each branch also has one prescribed 896-, 2048- and 8192-bit composite, for sixteen primary positive fixtures altogether. For target bit size \(B\), the fixture uses \(p=2^{B/2-1}-19\), except the negative-one branch uses offset 21, then \(q=4p+\delta\). Their large factors are not asserted prime.

Twelve additional small controls use \(p=127\), \(a\in\{3,5,8\}\), and all four subfamilies. They pass complete and prepared candidate checks. No new primality check or prime-pair claim is attached to those twelve cases. Full N-only queries receive \(N\); fixture parameters supply the expected answer for verification.

## Fixed public observations and timings

The pinned mathematical puzzles are [RSA-270](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-09-en.pdf), [RSA-896](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-10-en.pdf), and [RSA-2048](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-38-en.pdf), using the existing RSA Inc-attributed MysteryTwister input certificate. Its decimal digests and saved exact states are checked. No present-day unresolved status is inferred from the PDFs.

Exactly six primary endpoint gcd observations were added: \(J\) and \(J+1\) for each original \(N\). All six are 1. Their individual call times sum to 53.7 microseconds, using already saved roots; root preparation is excluded from that initial observation total.

All later representation, union and sufficient-candidate checks reuse these observations. Public unique multiplier positions remain 312. There are no new multiplier positions or square-completion witness calls.

The final candidate audit uses nine rotated-order paired rounds with eight repetitions per round. All times below are microseconds per complete or prepared call:

| Input | Complete center gcd | Complete candidate | Prepared root candidate | Prepared residual candidate | Complete ratio |
| --- | ---: | ---: | ---: | ---: | ---: |
| RSA-270 | 7.7000 | 3.3000 | 1.1250 | 1.0000 | 2.33x |
| RSA-896 | 7.6375 | 3.2750 | 1.1500 | 1.0000 | 2.33x |
| RSA-2048 | 18.5000 | 6.9000 | 2.3625 | 1.3000 | 2.68x |

The complete candidate includes root preparation. It is faster in all nine paired public rounds per input, while returning no admitted factor. Prepared costs require the stated existing root or residual input and must not be presented as full N-only costs.

The same paired candidate audit retains every positive fixture. Representative large cases are:

| Positive fixture | Complete center gcd | Complete candidate | Prepared residual candidate | Complete ratio |
| --- | ---: | ---: | ---: | ---: |
| lower_D_2048 | 13.8750 | 11.2875 | 5.6875 | 1.23x |
| lower_D_8192 | 147.1375 | 109.4625 | 57.7875 | 1.34x |
| lower_U_2048 | 14.3875 | 11.6625 | 5.8750 | 1.23x |
| lower_U_8192 | 147.3625 | 108.6750 | 57.4250 | 1.36x |
| upper_U_2048 | 13.6250 | 11.2375 | 5.7000 | 1.21x |
| upper_U_8192 | 142.9000 | 106.8875 | 56.3750 | 1.34x |
| upper_D_2048 | 13.8625 | 11.4250 | 5.8125 | 1.21x |
| upper_D_8192 | 146.3875 | 109.5250 | 58.2250 | 1.34x |

The 896-bit positive candidates take 4.3750–4.5125 microseconds from \(N\). The four very small cases take 0.9750–1.0750 microseconds and have no speed gain over the complete center-gcd baseline. These measurements retain the occasional larger-case gains without assigning a universal route preference.

Every timed admitted factor is checked with divmod and an exact product. Imports, input/source/domain checks, case restoration, warmups and serialization are excluded. The full routes include all root and coordinate preparation required by their named method. These are same-process cost replays on prescribed inputs, not independent success-rate observations. Compare each variant with its own paired baseline; do not multiply ratios across the separately timed stages.

The primary root/residual audit, parity-corrected residual-pair extension, scalar-union extension and sufficient-candidate extension retain separate raw timing series and explicit call counts. New extensions were executed on saved records; the original endpoint observations and timings were not rerun or replaced.

## Evidence and reuse boundary

Companions:

- [Fixed-input checker and all three extensions](../experiments/brc_root_endpoint_gcd_audit_20260908.py)
- [Exact controls, observations and raw measurements](../experiments/brc_root_endpoint_gcd_audit_20260908.json)
- [Preceding affine-mask and D residue-class audit](BRC_AFFINE_STATE_GATE_AUDIT_20260908.md)

The checker pins the native-root core, original public-input certificate, and earlier small-prime helper. It reads saved states with exact integer interval checks and consumes the standard-library gcd. This is COMPOSE_APPLIED reuse of existing arithmetic and BRC coordinates. No new general-purpose production API or adaptive routing policy is introduced.

Executed assertions and AST parsing pass. Production core and the 46 previously passing selected tests are unchanged. The previous goal turn is PROGRESS from its verified affine/CRT artifacts; this turn adds a different primitive, exact representation identities, bounded new public observations and additional positive families. No public challenge has been factored, and the parent objective remains active.
