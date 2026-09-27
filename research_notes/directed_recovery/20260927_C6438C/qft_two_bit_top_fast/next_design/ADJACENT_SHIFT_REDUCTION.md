# Adjacent selected bits as a shifted single-bit correlation

Status: SYMBOLIC / AUTHOR / NOT_EXECUTED / NOT_ADMITTED. This is a new exact
reduction, not a measured implementation or a novelty claim. No scientific
module, numerical reference or provider query was run for this derivation.

## Contract and source

Let g>=2, 0<=ell, k=ell+1<g, V=2^ell, U=2V, P=4V, L=2^g=HP.
R is any supplied positive integer and 0<=r<R. Define the scalar sign

    s(x)=(-1)^(bit_ell(x)+bit_k(x)),  0<=x<L,
    A_s(d)=sum_(0<=x<L-d) s(x)s(x+d), 0<=d<L.

The ordinary single-bit periodic sign f(x) is +1 on residues [0,U) modulo P,
and -1 on [U,P). Its periodic definition includes all integer x, including
negative x in the symbolic boundary identity below. The implementation need
not construct negative bit indices or evaluate f at negative integers.

The frozen one-bit reduction read in full is
`../sep27-qft-gap-direct/DIFFERENCE_AUTOCORRELATION.md`, SHA256
`c0c3765fce7d07f383f1ebfcb514dd8483485944bfeb202d024dd21e69205cbf`.
Its source publication is EM `0e4c64d1b71aaa7db96594cd66b52de3e0b96ca6`,
`research_notes/directed_recovery/20260927_C6438C/qft_gap_direct/`, matching
the existing source-publication metadata read during preparation.
It gives sum A_f over a displacement progression using two degree-three
single-floor tables. The present proof adds only a finite-window correction.

## 1. Exact sign identity and finite-window endpoints

Adding V preserves the lower ell bits and carries into bit k precisely when
bit ell was one. Therefore, including carry past k,

    s(x)=f(x+V).

Carry past k has no effect on this periodic sign. For F_d(y)=f(y)f(y+d),
translation of a finite sum by V gives

    A_s(d)-A_f(d)
      =sum_(0<=t<V) [F_d(L-d+t)-F_d(t)]
      =sum_(0<=t<V) [f(t-d)-f(t+d)] =: C(d).       (1)

The second equality uses f(L+t)=f(t)=1 for 0<=t<V, and P divides L.
The finite-interval translation identity remains true when L-d<V: overlapping
terms in the two boundary sums cancel. Thus (1) does not assume the overlap
window is at least V. It also extends to d=L with both correlations empty.
This is scalar multiplication symmetry only, with no matrix reordering claim.

## 2. Three affine pieces for the correction

Write d=qP+z, 0<=z<P. Count positive and negative parts of the length-V
integer intervals in (1). The result is

    C(d) = -2z,             0<=z<=V,
           2z-4V,          V<=z<=3V,
           8V-2z,          3V<=z<P.                (2)

For explicit verification, the forward window sum h(z)=sum_(0<=t<V) f(t+z)
has four pieces V, 3V-2z, -V, 2z-7V on [0,V], [V,2V], [2V,3V], [3V,4V],
respectively. The backward window is h((-z) mod P), yielding (2), including
z=0 via h(0)=h(P)=V. Every junction agrees exactly. In particular C(0)=0,
C(V)=-2V, C(2V)=0, C(3V)=2V and C(P)=0 are symbolic endpoint identities.
This is not a new numeric fixture run.

Equivalently on one period,

    C(d)=-2z+4(z-V)_+-4(z-3V)_+.                   (3)

## 3. Two ordinary degree-two floor tables

Define

    Q_a=floor((d+3V)/P), Q_b=floor((d+V)/P).

Subtracting q=floor(d/P) gives the two threshold indicators in (3).
For an indicator e in {0,1}, 2qe=(q+e)^2-q^2-e. Substitute in (3) and
collect terms: the q and q^2 terms cancel. This proves the particularly
short identity

    C(d)=-2d+(4d+4V)Q_a+(4V-4d)Q_b
                    +8V(Q_b^2-Q_a^2).             (4)

Although d is unreduced in (4), the cancellation makes it P-periodic, so no
enumeration of periods or residues is involved. Formula (4) holds at the
junctions in (2) with the ordinary floor convention.

For d_j=b+Rj, 0<=j<n, all d_j in [0,L), let

    T_a[p,e]=sum_j j^p floor((Rj+b+3V)/P)^e,
    T_b[p,e]=sum_j j^p floor((Rj+b+V)/P)^e,
    S_d=nb+R*n(n-1)/2,
    S_da=b*T_a[0,1]+R*T_a[1,1],
    S_db=b*T_b[0,1]+R*T_b[1,1].

Then

    sum_j C(d_j)=-2S_d+4(S_da-S_db)
       +4V(T_a[0,1]+T_b[0,1])
       +8V(T_b[0,2]-T_a[0,2]).                    (5)

Only total degree <=2 is used in these two ordinary floor tables. The
existing fixed degree-three runner already contains all required entries;
the new degree-five extension is not a dependency of this reduction.

Add (5) to the frozen two-table expression for sum A_f(d_j). Thus one
progression uses at most four ordinary degree-three tables, and the full
supplied-modulus scalar query uses at most eight. These are top-level table
counts, not counts of primitive arithmetic operations or free oracle calls.
Typed construction of scales, counts, coefficients, exact halves, arithmetic
and floor recursion all remain paid. Using the established fixed-degree
Euclidean recurrence gives a polynomial-bit symbolic algorithm in the binary
input size; the bound is not logarithmic in g and is not a new general
mixed-floor closure result.

## 4. Query orientations and extension of the domain

Use the two heads b=r and b=R-r, step R; the latter is strictly positive when
r=0. A head b>=L gives an empty progression. Otherwise

    n=1+floor((L-1-b)/R).

For each head return sum A_f plus (5), then add both orientations. Preserve
both copies when R is even and r=R/2: they encode opposite displacements.
The zero displacement appears only once at r=0. Retain raw normalization
4^-g. The supplied R, residue and any external group address remain external
information; neither this identity nor its backend discovers an order.

Unlike the earlier highest-selected-bit implementation, the identity permits
k=ell+1 strictly below g-1, with arbitrary R and arbitrarily large ell. The
bit gap is fixed at one, not arbitrary. It also covers the overlapping
highest-bit subfamily without implying a cost improvement there.

## 5. Next actual check

Independent proof review must check the bit-shift identity, the short-window
telescoping case, all periodic junctions, the cancellation in (4), and both
orientations. A separately frozen observer/checker can then validate a
bounded non-top grid with actual typed ordered-pair evidence, plus existing
highest-bit saved fixtures as historical evidence where useful. No host
numerical reference is authorized by this mathematical note. Preserve all
failed/replay work and source bindings; do not claim timings or arithmetic
savings until a declared actual run and full-record review exist.

General separated-bit masks, growing masks, matrix chronology, many-gap
sampling, unknown-order recovery and complete Shor dequantization remain open.

Global-Knowledge-Sync: main@52978d9 / GLOBAL_KNOWLEDGE_V1
