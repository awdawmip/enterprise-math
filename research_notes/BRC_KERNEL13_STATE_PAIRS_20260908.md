# BRC kernel-13: paired D/U constructions and a frozen public-puzzle check

Researcher-ID: EM-HME-0CE4FD / TASK_RESEARCH  
Global-Knowledge-Sync: main@b2d9cef / GLOBAL_KNOWLEDGE_V1  
Canonical snapshot: b2d9ceff961c70ecb356721aafcb03d31396daeb  
Project parent: bd5251aae5669bf570180dc8e44128eb1c1e169b

The state-separated study retains a D family on the strip \(R=J-c\) and a matched U family with completion gap \(A=1\). All 52 assigned constructive witnesses passed, including 12 small examples whose two factors are prime. A separate fixed kernel-13 prefix check added 246 positions on the same three published mathematical puzzles. Their witness calls totaled 1.9552 ms and produced no square witness. This records one inexpensive experiment, with no claim about the success rate outside its declared positions.

## State convention

For a positive nonsquare target \(mN\), write

\[
J=\lfloor\sqrt{mN}\rfloor,\quad R=mN-J^2,\quad
a=J+1,\quad A=a^2-mN=2J+1-R.
\]

D means \(1\le R\le J\); U means \(J<R\le2J\). Z is the separate exact-square state. These are the established remainder/cost labels, not a claim that the floor-root BRC map moves upward in U. A multiplier's label belongs to \(mN\); the certificate separately records the original \(N\)'s label.

## Paired constructive families

For each squarefree kernel \(d\), choose:

| Kernel parity | \(c\) | Assigned multiplier \(m\) | \(\lambda\) |
| --- | ---: | ---: | ---: |
| Odd | \(d\) | \(d\) | 2 |
| Even | \(2d\) | \(4d\) | 1 |

Thus \(c^2=md\) and \(2c=m\lambda\). For any even integer \(h\ge2\), let

\[
b=ch+1,\qquad t=bh-1.
\]

The two members of each pair share \(t,m,h\).

**U member.**

\[
N_U=t(dt+\lambda),\qquad a_U=ct+1,
\]
\[
mN_U=a_U^2-1,\qquad A_U=1,\qquad R_U=2J_U.
\]

The target is immediately below a square, so its assigned state is U.

**D member.**

\[
N_D=t(dt+\lambda b),\qquad a_D=ct+b=b^2-c,
\]
\[
mN_D=a_D^2-b^2,\qquad A_D=b^2=a_D+c,\qquad R_D=J_D-c.
\]

Since \(b^2>2c+1\),

\[
0<R_D=b^2-2c-1\le J_D=b^2-c-1.
\]

Consequently \(J_D\) is the actual floor root and \(a_D\) the immediate ceiling. This is a positive D construction for every allowed \(h\), not an inference from a mixed D/U sample.

For either member write \(N=tq\), and let the gap root be \(g=1\) or \(b\). Then

\[
a-g=ct,\qquad \gcd(N,a-g)=t\gcd(q,c)=t.
\]

For odd \(d\), \(q\equiv2\pmod d\), so \(q\) and \(c=d\) are coprime. For even \(d\), \(q\) is odd and \(q\equiv1\pmod d\), so it is coprime to \(c=2d\). Also \(t\) is odd and \(\gcd(t,b)=1\); hence \(\gcd(t,q)=1\). Both factors exceed one.

This parameterizes familiar difference-of-squares identities by BRC state. It does not establish a new general factoring algorithm or an infinite family of prime pairs.

### Constructive checks actually executed

The source kernel list is

\[
(1,13,14,3,15,2,5,6,30,22,105,33,7).
\]

Each kernel received \(h=2\) and \(h=2^{511}+2\), with both D and U members: 52 prescribed source calls, 26 per state. Exact products, proper factors, gcd identities, ceiling inequalities and state relations all passed. The 26 large constructed inputs have 2045–2065 bits; their factors were not asserted prime.

The \(h=2\) factors are below 50,000 and received bounded exact primality checks. Twelve pairs passed, seven D and five U:

| \(d\) | \(m\) | Assigned state | Constructed product |
| ---: | ---: | :---: | --- |
| 1 | 1 | D | \(55=5\cdot11\) |
| 1 | 1 | U | \(35=5\cdot7\) |
| 13 | 13 | D | \(39379=53\cdot743\) |
| 13 | 13 | U | \(36623=53\cdot691\) |
| 14 | 56 | U | \(178879=113\cdot1583\) |
| 3 | 3 | D | \(689=13\cdot53\) |
| 3 | 3 | U | \(533=13\cdot41\) |
| 15 | 15 | D | \(59597=61\cdot977\) |
| 2 | 8 | D | \(731=17\cdot43\) |
| 30 | 120 | D | \(1771591=241\cdot7351\) |
| 105 | 105 | U | \(18611147=421\cdot44207\) |
| 7 | 7 | D | \(6757=29\cdot233\) |

For example, \(8\cdot731=77^2-9^2\). Here \(J=76,R=72=J-4,A=81=a+4\), giving the D witness and \(\gcd(731,77-9)=17\).

Every assigned multiplier occurs by slot 30 of the frozen prefix. This is an upper bound supplied by the assigned witness. Earlier prefix candidates were not executed on these controls, so neither actual first-hit rank nor first-hit direction is claimed. The controls are deliberately constructed positive examples, not independent samples of public-input success probability.

## Positive window for transporting one square witness

Suppose an already valid immediate-ceiling witness satisfies

\[
mN=a^2-b^2,\qquad b>0,\qquad (a-1)^2<mN<a^2.
\]

At integer scale \(v\ge1\), the same algebraic identity becomes

\[
v^2mN=(va)^2-(vb)^2.
\]

The proposed upper square remains the immediate ceiling exactly when

\[
v^2b^2<2va-1
\iff
1\le v\le\left\lfloor\frac{2a-1}{b^2}\right\rfloor.
\]

For \(v\ge2\), the strict inequality is equivalent to the integer condition \(vb^2\le2a-1\). For \(v=1\), the stated immediate-ceiling premise supplies the stronger strict inequality needed at that endpoint.

Within this window,

\[
R_v-J_v=v(a-vb^2).
\]

Thus U holds for \(vb^2<a\), and D for \(vb^2\ge a\). In particular, a U witness with \(b=1\) persists through \(v=2a-1\): U for \(1\le v\le a-1\), then D for \(a\le v\le2a-1\). For the constructed D members \(b^2=a+c\), the same witness has maximum preserving scale one.

The 98 selected multipliers partition into 13 sets of the form \(m_dv^2\), where \(m_d=d\) for odd \(d\), and \(m_d=4d\) for even \(d\). Applying the identity-window check to the 52 saved controls gives:

- 392 proposed scaled identities, all satisfying their exact difference-of-squares equality.
- 207 remain immediate-ceiling identities: 177 U and 30 D.
- 185 lie outside the window of that particular proposed witness.
- Zero additional public queries and zero source witness calls.

Outside a witness's window, a different witness may exist. This audit does not claim that a specific gcd factor survives every scale, nor that checking only 13 bases replaces all 98 candidate checks. It uses integer inequalities on known constructive identities; its only square roots concern the small multiplier quotients.

## Frozen source-prefix experiment

The experiment uses the existing kernel13_prefix(1000), checked against a literal 98-entry tuple before any new public query. Its actual largest member is 968. It does not call the companion full-fallback ordering function.

The declared list, in execution order, is:

~~~~text
1,3,5,7,8,9,13,15,16,24,25,27,32,33,45,48,49,56,63,64,72,75,80,81,88,96,
105,112,117,120,121,125,128,135,144,147,169,175,192,200,208,216,224,225,
240,243,245,256,288,289,297,320,325,343,352,361,363,375,384,392,400,405,
432,441,448,480,504,507,512,528,529,567,576,600,605,625,637,648,675,720,
729,735,768,784,792,800,825,832,841,845,847,864,867,896,945,960,961,968
~~~~

The three input integers are copied from the pinned RSA Inc-attributed MysteryTwister mathematical puzzle PDFs: [RSA-270](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-09-en.pdf), [RSA-896](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-10-en.pdf), and [RSA-2048](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-38-en.pdf). Their decimal digests and full values are preserved in the input certificates. The PDF provenance is not evidence of present-day unresolved status.

Each input had 22 saved positions, 16 of which intersect this prefix. Exactly 82 new positions per input were evaluated once. There were 48 reused prefix records and 246 new records, giving 294 prefix records. The full accumulated set grows from 66 to 312 unique positions; the 18 earlier positions outside this prefix remain historical observations.

| Published input | Bits | Original state | New D / U | New calls | Sum of API times, ms | Evaluation loop, ms | New square witnesses |
| --- | ---: | :---: | ---: | ---: | ---: | ---: | ---: |
| RSA-270 | 895 | U | 37 / 45 | 82 | 0.4029 | 0.9765 | 0 |
| RSA-896 | 896 | U | 44 / 38 | 82 | 0.3893 | 0.9505 | 0 |
| RSA-2048 | 2048 | D | 36 / 46 | 82 | 1.1630 | 3.3732 | 0 |
| Total | — | — | 117 / 129 | 246 | 1.9552 | 5.3002 | 0 |

No exact-square Z target occurred. There were no advancing ceilings, fallback candidates, timing repetitions on public inputs, or additions based on intermediate results.

Each new observation checks the exact floor-root interval, exact completion gap, and square-root interval of that gap, then compares the expected witness to the unchanged source API. The reference reconstruction and candidate core both use math.isqrt. The explicit integer inequalities verify their returned values; this is not a comparison of independent square-root algorithms.

The API timer includes target-root preparation, the existing default 4032 filter and its witness check. The loop timer also includes record creation and exact audits. Source-prefix generation took 0.8228 ms separately. Imports, input/source verification, parsing, constructive controls and serialization are outside those public timers. These are single-pass descriptive measurements, not a stable speedup benchmark or a throughput prediction. The one-time 52-control timing includes the prescribed API call and gcd/product verification, with fixture generation and primality annotation outside.

## Source and artifact authority

The public experiment uses the previously verified native-square-root core. This checkpoint changes only the three research artifacts, not production code or tests.

| Source relative to src/enterprise_math | Git blob |
| --- | --- |
| core.py | 2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07 |
| brc_opportunistic_shortcuts.py | 1214aa09770893fb3de7f85b994d1994ff56bffe |
| brc_square_gap_prefilter.py | 42d4e9a397b56d9d371f034780ffc736d43e6d96 |

The checker also pins all four consumed input-certificate blobs: the original public inputs, prior frozen prefix, materialized-gap order and native-square-root audit. Historical source/timing certificates retain their own provenance.

Companions:

- [Executable fixed-input checker](../experiments/brc_kernel13_state_pairs_20260908.py)
- [Exact observations and raw measurements](../experiments/brc_kernel13_state_pairs_20260908.json)
- [Native-root implementation and cost audit](BRC_NATIVE_SQUARE_ROOT_AUDIT_20260908.md)

The lift-window helper was added after the public run and executed separately on its saved constructive records. The final checker includes that helper for reproduction. Adding the algebraic audit did not rerun the public positions.

## Derived follow-up: a specific D-strip signature

For fixed integers \(m>0,c\ge0\) with \(mN>c^2\),

\[
R=J-c
\quad\Longleftrightarrow\quad
H_{m,c}(N)=4mN+4c+1\text{ is an integer square}.
\]

Forward, \(H=(2J+1)^2\). Reverse, an odd square root \(y\) gives \(J=(y-1)/2>c\), and \(mN=J^2+J-c\) has the valid D remainder \(0<J-c\le J\). This supplies an N-only signature for the particular strip. A square signature alone does not say its completion gap is square. In the constructed family, the second property is supplied by \(A=J+c+1=b^2\).

This is a derived candidate criterion, not an implemented or publicly tested new gate in this checkpoint. Any future cost comparison must charge for evaluating it; it does not by itself extract the hidden factor sum.

Reuse disposition: REUSE_EXECUTED for the existing kernel-13 prefix and witness API; COMPOSE_APPLIED for the paired state construction and its positive transport window. The active research objective remains open. This experiment retains its occasional positive cases and its exact fixed-budget public result.
