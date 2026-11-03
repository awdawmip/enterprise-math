# PREFIX-472 — Exact dictionary-free rank and unrank for normalized X6 BRC gate-support states

Date: 2026-11-04 (Asia/Shanghai). Scientific status: **AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED**. This is a mathematical/algorithmic result in the source-note lane, not a native Result or Foundation admission.

## Source, question and scope

Continue [PREFIX-471](2026-11-04_prefix471_mixed_sign_gate_universal_series.md) at immutable scientific input pin \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`, preserving P000's **six native signed-coordinate spatial axes plus separately typed time**. The problem is an exact codebook-free ranking of the *base support* of BRC positive-valuation observations, not compression of all ordered path provenance.

The signed native X6 step alphabet is \`x=+E_1\` plus the ten directions \`±E_2,...,±E_6\`. A fixed gate word \`w\` of length \`k>=1\` uses only the ten ordinary directions. An \`x\` is allowed initially and, subsequently, exactly after suffix \`w\`. The path length \`n>=0\` is fixed; all counts and outputs are exact integers.

For a path with \`s\` occurrences of \`x\` and five signed ordinary displacements \`y_i\`, take the PREFIX-471 normalized coordinates
\[
d_i=y_i-r(h_i^+-h_i^-),\quad r=\max(s-1,0),\quad
A'=A-(L_2+2L_4+L_5),\quad C'=C-(L_3+L_5),
\]
where \`h_i^±\` are signed-letter multiplicities in \`w\`,
\[
L_i=\max(0,rh_i^+-\max(y_i,0),rh_i^--\max(-y_i,0))
\]
and \`A=p_2+2p_4+p_5,\ C=p_3+p_5\` are the previously established two exact valuation coordinates, with \`p_i=min(c_i^+,c_i^-)\`.

PREFIX-471 proves that these map the reachable base-support states bijectively to
\[
\mathcal U_{n,k}=
\left\{(s,d,A',C'):\; s\ge0,\;
T={n-s-k\max(s-1,0)-\|d\|_1\over2}\in\mathbf Z_{\ge0},\
0\le C'\le T,\ 0\le A'\le2T-C'\right\}.
\tag{1}
\]
This paper constructs exact inverses \`rank : U_{n,k}->[0,B_n-1]\` and \`unrank\`, **without storing \`U_{n,k}\` or an enumeration dictionary**. Both are independent of the letters/signs of \`w\` once \`k\` and the normalized state are supplied; transforming to or from the raw observer retains the actual \`w\` and its signed counts.

## Theorem 1 — exact constant-degree block and shell prefix counters

Put
\[
R(T)={(T+1)(3T+2)\over2},\qquad
c_j(q)=[z^q]\left({1+z\over1-z}\right)^j\quad(q\ge0).
\]
Here \`c_j(q)\` counts integer vectors of length \`j\` with L1 norm \`q\`; \`c_0(q)=1_{\{q=0\}}\`.

Set
\[
P(m)=[z^m]{(1+2z^2)(1+z)^2\over(1-z)^8}
 =\sum_{h=0}^4 a_h\binom{m-h+7}{7},\
(a_0,\ldots,a_4)=(1,2,3,4,2).\tag{2}
\]
For every \`m>=0\`, \`P(m)=sum_{T=0}^{floor(m/2)} c_5(m-2T)R(T)\`. The binomial in (2) is its **integer polynomial continuation**, defined for all integers via the falling factorial divided by \`7!\`; the coefficient identity is used only for \`m>=0\`.

The possible number of special letters satisfies
\[
0\le s\le S:=\lfloor (n+k)/(k+1)\rfloor,\qquad
M_s=\begin{cases}n,&s=0,\\n-1-(s-1)(k+1),&s\ge1.\end{cases}
\]
The number of states in the fixed-\`s\` block is \`P(M_s)\`, and
\[
B_n(k)=P(n)+\sum_{j=0}^{S-1}P(n-1-j(k+1)).\tag{3}
\]

**Proof.** For fixed \`s\`, equation (1) partitions states into the shells
\`q=||d||_1=M_s-2T\`, with \`c_5(q)\` possible signed vectors and exactly \`R(T)\` possible pairs \`(A',C')\`. The product of generating series is
\[
\left({1+z\over1-z}\right)^5
\sum_{T\ge0}R(T)z^{2T}
={ (1+z)^5\over(1-z)^5}{1+2z^2\over(1-z^2)^3}
={ (1+2z^2)(1+z)^2\over(1-z)^8}.
\]
This proves (2)–(3) for all nonnegative integers.

For shell-prefix computation, for every positive integer \`q\`,
\[
c_5(q)=c_5^*(q):={4q^4+20q^2+6\over3},\qquad c_5(0)=1,\quad c_5^*(0)=2.
\tag{4}
\]
Consequently \`W_m^*(T)=R(T)c_5^*(m-2T)\` is a polynomial in \`T\` of degree at most six. If \`D_i=Delta^i W_m^*(0)\` are its first seven forward differences, the actual prefix through shells \`T=0,...,t-1\` (\`0<=t<=floor(m/2)+1\`) is
\[
Q_m(t)=\sum_{i=0}^6 D_i\binom t{i+1}
-1_{\{m\ {\rm even},\ t=\lfloor m/2\rfloor+1\}}\,R(m/2).
\tag{5}
\]
The correction accounts for the single \`q=0\` shell. Newton's finite-difference summation identity proves (5) exactly, including \`m=0\`.

Likewise \`g(j)=P(n-1-j(k+1))\`, understood using the polynomial continuation of (2), has degree at most seven in \`j\`. With \`E_i=Delta^i g(0)\`, the prefix of positive-\`s\` blocks is
\[
\sum_{j=0}^{u-1}g(j)=\sum_{i=0}^7E_i\binom u{i+1},\quad 0\le u\le S.\tag{6}
\]
Although the eight samples used to calculate differences may extend to negative \`m\`, (6) evaluates a polynomial identity and agrees with the physical counts for all sampled **valid** blocks \`0<=j<S\`, where \`M_{j+1}>=0\`. Hence the block and shell cumulative counts require only fixed-degree exact-integer formulas, rather than enumeration.

## Theorem 2 — explicit signed shell and triangle ranking

Order normalized states by \`s\` increasing, \`T\` increasing, signed five-vector \`d\` lexicographically in ordinary integer order, then \`C'\` increasing and \`A'\` increasing.

For \`j>=0\` define \`H_j(q)=sum_{h=0}^q c_j(h)\`, with \`H_j(q)=0\` for \`q<0\`. Exact finite binomial formula:
\[
H_j(q)=\sum_{a=0}^{\min(j,q)}\binom ja\binom{q-a+j}{j}.
\tag{7}
\]
At a recursive signed-vector step with remaining norm \`r>=0\` and \`j\` coordinates still to follow the candidate first coordinate, the cumulative number of vectors with candidate coordinate at most \`v\` (\`-r<=v<=r\`) equals
\[
K_{r,j}(v)=
\begin{cases}
H_j(r+v),&v<0,\\
2H_j(r-1)+c_j(r)-H_j(r-v-1),&v\ge0.
\end{cases}\tag{8}
\]
For the triangular pair field, the number preceding \`(A',C')\` is
\[
D_T(A',C')=C'(2T+1)-C'(C'-1)/2+A'.\tag{9}
\]

**Proof.** Each signed coordinate \`v\` leaves norm \`r-|v|\` for the \`j\` remaining coordinates; summing \`c_j(r-|v|)\` over \`-r<=v<=v_0\` yields (8) by splitting negative, zero and positive values. Formula (7) follows from \`(1+z)^j/(1-z)^{j+1}\`. The \`C'\` row of the triangle has \`2T-C'+1\` successive values of \`A'\`, giving (9).

**Exact rank construction.** Add (i) all preceding \`s\` blocks using (6), (ii) all preceding \`T\` shells using (5), (iii) the lexicographic signed-vector rank derived recursively from (8), multiplied by \`R(T)\`, and (iv) (9). The result is an integer in \`[0,B_n(k)-1]\`.

**Exact unrank construction.** Use monotone prefix binary search on (6) to select \`s\`, then on (5) to select \`T\`. Divide the remaining index by \`R(T)\` to separate signed-vector and triangular ranks. Invert (8) by five successive monotone binary searches, and invert (9) by one binary search on \`C'\`. The identities above partition the complete state set into nonoverlapping consecutive integer intervals, so both algorithms are inverse bijections for every \`n>=0,k>=1\`.

**Worked joint-normalization example.** For \`n=4,k=2\`, the last normalized state has rank 932 of 933 and is \`(s=2,d=(0,0,0,0,0),A'=0,C'=0)\`. For gate \`w=aa\`, its raw axis-2 displacement is \`+2\`; for \`w=aA\`, it is \`0\`. The *same* normalized rank is valid for each gate, with the raw state recovered using its own \`w\`. This makes the cross-gate cardinality equivalence constructive while retaining the raw distinctions.

## Complexity and bit optimality

For fixed five ordinary signed axes and any supplied integers \`n>=0,k>=1\`, a block or shell prefix requires at most eight or seven polynomial samples plus fixed-size binomial arithmetic. Binary searches for the two outer blocks, five signed coordinates and the triangle each use \`O(log(n+1))\` prefix evaluations. Thus **rank and unrank require \`O(log(n+1))\` arbitrary-precision arithmetic operations**, with \`O(1)\` scalar scratch cells; their intermediate integers use \`O(log(n+k+1))\` bits. With multiplication cost \`M(b)\`, the core costs \`O(log(n+1) M(log(n+k+1)))\` bit operations up to fixed-degree division overhead. The raw-to-normalized adapter additionally reads the known gate word (\`O(k)\` letters) or its already supplied signed-count profile.

The rank uses the *entire* interval \`0,...,B_n(k)-1\`. Therefore a fixed-width exact binary code at given \`n,k\` has the optimal width \`\lceil\log_2 B_n(k)\rceil\` (zero bits for the one-state case). This is a statement about **the declared base-support observer**. Full ordered-source multiplicities, suffix history and phase/signed amplitudes have separately declared carriers and would require their own observer-safe augmentation.

## Executed exact-integer certificate

- Source: [\`prefix472_rank_codec.py\`](prefix472_rank_codec.py), pure Python 3 standard library with arbitrary-precision integers, containing the full rank and inverse and an independent direct enumerator of the set (1).
- Actual execution log: [\`PREFIX472_EXACT_EXECUTION.log\`](PREFIX472_EXACT_EXECUTION.log).
- Local executed source Git blob: \`5eb89ee9bacbeba07970935d689a51f36bb073e3\`; local executed log Git blob: \`74588e575e4686e3c8331d5aab12bae7b8f07fc5\`. Connector readback of both published files matched these blob IDs.
- Exhaustively tested **107,125 distinct normalized states**: all \`n=0..7\`, \`k=1,2,3,4\`, every valid \`(s,d,A',C')\` independently enumerated and checked against both \`rank\` and \`unrank\` using its exact sequence index. Checked \`Q_m(floor(m/2)+1)=P(m)\` for every \`m=0..109\`, and independently enumerated signed shells of norm \`q=0..10\`.
- Additional nonexhaustive exact rank/unrank round trips at \`(n,k)=(64,1),(256,2),(1024,3),(65536,2),(10^9,2),(10^9,1000000001)\`, seven selected ranks in each domain. The fixed \`k=2,n=10^9\` base-support state count has 226 bits. Cross-checks reproduce \`B_8(2)=33797\`, \`B_8(3)=33295\` from the established series.
- All executed assertions passed: \`ALL_CHECKS_PASS\`. No GitHub Actions or native execution was claimed; high-length random/full enumeration was not performed. The universal result rests on the derivation above, with finite exact regression checks.

## Remaining scientific unit

PREFIX-473: extend this dictionary-free codec to the joint base-observer × KMP suffix-state set for a specified gate (start with \`aba\`), deriving exact nonproduct occupancy-conditioned suffix counts or prefix counts. Compare \`H=0,1,2,3\` finite-future minimal quotient widths at arbitrary \`n\`. Preserve ordered-path multiplicity and source distinctions when introducing new state quotients; compute an exact \`n\`-indexed counterexample if naive base × suffix ranking claims to preserve a future observation it does not.

The arbitrary-order X6 moment-rank problem remains a distinct authorized research direction.

## Control and provenance

Authenticated GitHub connector login \`awdawmip\`, with Enterprise Math repository \`admin/push\` permissions. At 2026-11-04 local research start, native Sites status \`0.6.11\`; task listing returned \`CONTROL_QUOTA\`, and native researcher session creation was denied with \`STATIC_READONLY_SCOPE_DENIED\` / \`operation_sent=false\`. Hence active owner, native Researcher-ID and CLAIM were not established. This submission is author-side portable Source research; it does not set native Task, Result, Review or admission state. Current normative policies were loaded independently of the frozen scientific pin. No change was made to P000 or the protected ACTIVE worldview.
