# CM24 new complete-forcing endpoint transport and mandatory cost scope

Root: EM-DVR-FBF223 / CONTROL_PLANE. Original owner EM-DIRECT-18F24A retained. New pure-paper theorem and directed nonauthor review PASS; no numerical execution or new owner. Read the original transport paper together with the mandatory independent cost addendum below. The capsule preserves all eight new original files in full, including review and pins. Fixed C/tau/F_CM endpoint equality remains OPEN.

# CM24: complete forcing to carrier endpoint transport

Status: ONE NEW PURE-PAPER UNIT. A complete independently given compatible
forcing determines its unique enlarged carrier with B_N=0. Both the full
carrier endpoint B(1) and its actual outside scalar Omega are transported
explicitly from that forcing. The earlier preset source-to-forcing map gives
a preset linear source-to-endpoint response. None is a proof of the fixed
C/tau/F_CM target.

Provenance: UNKNOWN local Root-delegated nonauthor helper
/root/cm24_extension_paper_check; same directed NONBLIND continuation. Root
retains direction and all original owners. No new owner, Task, Claim, Run,
branch, Native acceptance, Source write, script, prime/sample, old checker,
Green run or numerical evaluation. All earlier proof/review originals remain
unchanged. This unit is formal paper transport, not new data generation.

## 1. Complete finite objects and the forcing premise

Keep the declared F_p, p=6m+1 prime in classes13/19mod24, m>=2,
N=3m=(p-1)/2, q=x(x-3)^2/4 and

    D*=z(1-z)d^2+(3/2-5z/2)d-5/9.

Input is the entire finite forcing F'=sum_(j=0)^(p-2) f_j z^j,
independently prescribed before any desired endpoint, together with the
carrier conditions degree B<=p-2 and B_N=0. Write

    A_j=(j+1)(j+3/2), D_j=(j+2/3)(j+5/6),
    f_j=A_j B_(j+1)-D_j B_j.                              (1)

The top degree boundary is B_(p-1)=0. This paper supplies the exact
compatibility test for existence; a claim F'=D*B must satisfy it. For an
immutable independently given forcing, incompatibility is not repaired
by silently changing that forcing. Source-preserving adjustment below
belongs only to the separately specified preset source-to-forcing map.

All coefficients above N, including the last forcing f_(p-2), remain in
the input and custody. B_N=0 is one coefficient condition, not degree<N.

## 2. Lower endpoint: the legal e window and no e_N

For 0<=j<N define only the legal finite kernel

    e_j=(2/3)_j(5/6)_j / ((3/2)_j j!), e_0=1,
    E_k(1)=sum_(j=0)^k e_j, 0<=k<N.

Every e_j and D_j here is a unit. The ratio

    e_(j+1)/e_j=D_j/A_j

is used only for 0<=j<=N-2, where A_j is also a unit. At the actual
last row j=N-1, A_(N-1)=0, so its separate equation is

    B_(N-1)=-f_(N-1)/D_(N-1).

No e_N is introduced and no A_(N-1) division is performed. For j<=N-2,
divide (1) only by the unit D_j e_j and descend from that actual last row.
This gives the complete lower coefficient response

    B_j=-e_j sum_(k=j)^(N-1) f_k/(D_k e_k), 0<=j<N.     (2)

The zero A_(N-1) disconnects this block from B_N and every higher row.
Summing all of it, with a finite legal interchange, yields

    L(F')=sum_(j=0)^(N-1)B_j
         =-sum_(k=0)^(N-1) f_k E_k(1)/(D_k e_k).        (3)

This uses every lower coefficient. The sum interchange is ordinary linear
algebra, not a novelty claim. No old frozen-forcing endpoint reflection is
reproved or rerun.

## 3. Upper endpoint: a direct upward transport from B_N=0

For the entire upper row range N<=j<=p-2, A_j is a unit. Its zeros as
finite positions in 0,...,p-1 are N-1 and p-1, both outside this range.
The zeros D_(4m)=D_(5m)=0 cause no problem when they are multiplied,
rather than divided. Set

    r_j=f_j/A_j, t_j=D_j/A_j, N<=j<=p-2.

Starting from the independently fixed B_N=0, (1) now gives

    B_(j+1)=r_j+t_j B_j.

Thus for every actual N<=j<=p-1, with an empty sum at j=N,

    U_j(F')=sum_(k=N)^(j-1) r_k
                       product_(t=k+1)^(j-1)(D_t/A_t),
    B_j=U_j(F').                                        (4)

All products are finite; an empty product is1. Zero D factors are
retained as actual zero factors. These formulas explicitly determine
B_(4m), B_(5m) and every other upper coefficient from the forcing and
B_N=0. They are the same unique response obtained by the earlier
descending resonance construction, without a free endpoint choice.

The complete top-degree compatibility is

    ell(F')=U_(p-1)(F')
      =sum_(k=N)^(p-2) f_k/A_k
                       product_(t=k+1)^(p-2)(D_t/A_t)=0. (5)

Every term with k<5m contains the zero factor D_(5m), hence equivalently
the sum in (5) starts at k=5m. Its f_(p-2) coefficient is1/A_(p-2),
a unit, so ell is a nonzero linear functional. This is exactly the
top forcing compatibility, not a second independently adjustable seed.

The actual entire upper endpoint block is

    H(F')=H_B=sum_(j=N+1)^(p-2) U_j(F')                 (6)

or, by finite interchange,

    H(F')=sum_(k=N)^(p-3) (f_k/A_k)
               sum_(j=k+1)^(p-2)
                    product_(t=k+1)^(j-1)(D_t/A_t).

The last forcing coefficient f_(p-2) is not omitted from the problem:
it is essential to (5), although it does not enter (6) directly. All
upper B coefficients and the top check are produced by the same upward
scan before any endpoint is read.

## 4. Existence, injectivity and the complete carrier endpoint

For every F' satisfying ell(F')=0, formulas (2) and (4), with B_N=0,
solve all rows0,...,p-2. The boundary B_(p-1)=0 is precisely (5), and
no coefficient beyond the stated degree is introduced. Conversely any
carrier of this degree and B_N=0 must follow the same upper recurrence
and therefore satisfy (5). The condition is necessary and sufficient.

For zero forcing the lower block in (2) is zero. Starting from B_N=0,
the unit-A upward rows force every upper coefficient to zero as well.
Consequently D* restricted to degree<=p-2 and B_N=0 is injective. Its
image is exactly ker ell, a codimension-one subspace of the entire
(p-1)-coefficient forcing space. The compatible carrier is unique.

Because the central coefficient B_N is zero, the complete endpoint is

    B(1)=L(F')+H(F').                                   (7)

This is an explicit transport from the full independently given forcing,
not an endpoint-defined seed, existence-only statement or free H_B
parameter. All lower and upper coefficients are represented.

When the same forcing has degree<N, its upper coefficients are zero;
the recurrence from B_N=0 makes every U_j above N zero. Then ell=0,
H=0 and (7) reduces to the legal lower formula. This is the consistency
scope with the old degree<N carrier. Its old reflection proof is not
repeated, and its full 2m<r<=N half-prefix tail is not deleted.

## 5. Explicit transport of the actual outside scalar

Define the complete W_B=x^(-N)(x-3)B(q)/24 and P_B=Pi_(0..N)W_B.
To make its central endpoint fully explicit, define preset coefficient
weights for actual j=0,...,p-2:

    alpha_j=(4^(-j)/24)
       sum_(r=max(0,N-j))^min(2j+1,2N-j)
           binom(2j+1,r)(-3)^(2j+1-r).                 (8)

An empty interval contributes zero. Within each interval the exponent
is nonnegative. These are actual finite integer binomial coefficients
reduced in F_p; the upper binomial entry may exceed p, so no factorial
division across p is permitted. Direct finite coefficient extraction of
x^j(x-3)^(2j+1)/4^j gives

    P_B(1)=sum_(j=0)^(p-2) alpha_j B_j.                 (9)

Both lower and upper B_j enter the same formula; B_N is retained as its
known zero. Let Omega_B be the actual combined evaluation at1 of the
negative and above-N outer blocks of W_B. The complete evaluation gives

    Omega_B=-(L(F')+H(F'))/12
                     -sum_(j=0)^(p-2)alpha_j B_j(F').  (10)

All terms on the right are explicitly prescribed by (2)-(9). Thus the
previously necessary outer scalar is now computed from the complete
compatible forcing, instead of set from a desired B(1). This does not
make Omega recoverable from central P alone: the earlier delta B=1
countervariation changes the forcing. Its ambient necessity remains valid.

The original signed identity B(1)=-12(P_B(1)+Omega_B) is respected, with
both outer blocks retained. No new evaluation, prime or sample is used.

## 6. The earlier preset strict-source map gives linear endpoint transport

Use the already proved source M, annihilators Gamma_s, old-image right
inverse R_old, high monomials H_s=z^(p-s-1), and fixed kernel polynomial

    K=z^(5m)-R_old(M z^(5m)), MK=0.

For an independently given strict source y, the earlier preset construction
first supplies

    a_s(y)=-Gamma_s(y)/(9*4^(s-1)),
    y_0=y-sum_s a_s(y) M H_s,
    F_*(y)=R_old(y_0)+sum_s a_s(y) H_s,
    M F_*(y)=y.

The lower R_old output has degree<N. Therefore

    ell(K)=(1/A_(5m))
                  product_(t=5m+1)^(p-2)D_t/A_t != 0.

Every factor in this final product is a unit. The fixed source-preserving
compatibility response is exactly

    lambda(y)=-ell(F_*(y))/ell(K),
    F'(y)=F_*(y)+lambda(y)K.                            (11)

Then MF'(y)=y and ell(F'(y))=0. This is the prior top/resonance correction
expressed by an explicit forcing functional, not a new endpoint-fit choice.
The unique B(y) follows from (2),(4), and its complete endpoint and outside
scalar follow from (7),(10). Every step is a preset linear map whose
denominators are parameter-only proved units. Hence

    y -> F'(y) -> B(y) -> (B(y)(1),Omega_(B(y)))

is a preset linear transport with full signed source and upper state.

This depends on the specified right inverse and source-preserving forcing
selection. It does NOT make B(1) a universal function of y over all source-
equivalent forcings, nor replace the original fixed forcing by this new
selection. Giving y from the actual half source is ordinary linear response,
not an independent proof that its carrier endpoint matches fixed C/tau/F_CM.

## 7. Paid construction and retained state

No implementation or timing was run. With the complete compatible forcing
already present, a unit-diagonal lower descending scan and the upper
unit-A upward scan compute all B coefficients, L, H and the actual top
residual in O(N) field operations after paid inverses/parameter preparation.
The closed double-sum upper expression is evaluated by that recurrence,
not by treating its preparation as free. All p-1 forcing entries and
carrier entries remain preserved, including f_(p-2) and the upper block.

The e/E/lower weights and upper inverse-A tables cost separately paid
O(N) field preparation and the required inversions. e_N is never needed.
The alpha table can be constructed by finite Pascal rows, with no illegal
factorial inversion, in O(N^2) field operations and O(N) retained table/
workspace elements. This is a conservative construction bound, not a run.
Once paid alpha is available, (9)-(10) cost O(N) field operations. Building
the actual pullback coefficients instead is another separately paid route.
The earlier R_old/source-to-forcing construction retains its own previously
declared setup and evaluation costs; (11) does not make them free.

Full coefficient state, parameter tables and output use O(N) field
elements, in addition to preserved proof/source records. Reads, additions,
multiplications, inversions, modular representation and serialization have
positive costs; field operations are not bit instructions, API blocks or
native physical steps. No acceleration, native cost parity or performance
claim is made.

## 8. Remaining mathematical interface and custody

This closes the generic complete-forcing-to-endpoint transport and resolves
the upper block as an actual prescribed response. It leaves the independent
fixed-target mechanism open. Original C, tau, F_CM, all beta components,
literal g, rho leading16, class-19 terminal, lower/upper signed blocks,
full half-prefix tail and any additional weighted-terminal requirement
remain in their actual ledger. No scalar target equality or completion of
the mathematical parent follows from this generic transport.

Proof dependencies are the unchanged local degree-extension, B_N-zero,
projection/top-source and generic ledger papers with their complete pinned
chain. Root's review-chain Source reference6152f02ed6420b243e812f39b55f013ffc502ce4
is prior custody, not a new helper Source read/write. This remains classical
finite-field auxiliary readout algebra, not a new native dimension,
Working Truth/Foundation or physical propagation promotion. No old frozen
reflection, Green/check sequence or sample was re-executed.


# Cost-scope addendum: complete-forcing endpoint transport

Status: ONE LOCAL PURE-PAPER SCOPE CLARIFICATION. This leaves the 12093-byte
transport paper and its 3881-byte pins unchanged. No mathematical formula,
object, owner, target or proof conclusion changes. The fixed CM24 target is
OPEN. Provenance remains UNKNOWN local Root-delegated directed NONBLIND helper
/root/cm24_extension_paper_check. No mathematical execution, Source write,
Native acceptance, new owner, Task, Claim, Run or branch is performed.

The transport paper's O(N) retained coefficient/parameter/workspace statement
is a bound only for the inner stage with the complete compatible F' already
given: F' -> B -> (B(1),Omega_B). Its full forcing/carrier vectors, inverse
and e/E tables, alpha table and streaming accumulators use O(N) field
elements. Alpha construction still pays its stated O(N^2) field operations;
the storage bound does not make this computation free. Input/output and
immutable evidence retention remain separately paid.

That bound is not a total storage or workspace bound for the composed
source pipeline y -> R_old -> F' -> B -> endpoint. The already prescribed
R_old construction has d=2m=Theta(N) and retains its original fixed inverse/
interpolation matrix with O(d^2)=O(N^2) field elements, or O(N^2 log p) bits.
Its original setup and evaluation costs remain in force. Any retained
source projection, high-column or other source-map tables also keep their
own actual charged storage and preparation scope; none is absorbed into
the inner O(N) claim.

For a composed implementation with that fixed matrix retained, the account
must therefore include at least

    state = original R_old/source-map state + inner O(N) field state
            + actual other caches and preserved evidence,
    cost  = original source-map setup/evaluation
            + inner parameter/inverse preparation
            + alpha construction + inner readout + actual I/O/custody.

In particular the retained original matrix contributes O(N^2) field elements
to the composed account, separately from inner O(N) state and preserved
records. A total bound must also include any other actual retained source-map
tables. No O(N) total-pipeline bound, new implementation, measured
memory result, acceleration or free preprocessing is asserted. This addendum
only disambiguates which stage the existing inner bound describes.
