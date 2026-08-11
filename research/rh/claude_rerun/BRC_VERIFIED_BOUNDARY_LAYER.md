# BRC_VERIFIED_BOUNDARY_LAYER — on-demand refinement beyond the verified-zero PF strip

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`

Status:

`VERIFIED_STRIP_BOUNDARY_LAYER_COMPRESSED / FIRST_UNCOVERED_RANK_SINGLE_PAIR_BRANCH / RH_NOT_CLOSED`

## 1. Setup

Assume all nontrivial zeta zeros through height `H` have been rigorously verified on the critical line. Put

`L=floor(pi H)`.

The standard sector certificate gives nonnegativity for Toeplitz/PF order

`r <= L-1`.

For an unverified off-line conjugate pair at ordinate `gamma>H`, the pair angle satisfies

`|theta| <= 1/gamma < 1/H`.

For a rank-r rectangular pair-router state `(a,b)`, put `m=a-b+1`. A negative pair factor requires

`m|theta|>pi`.

## 2. First uncovered rank

Take

`r=L`.

If `m<=L`, then

`m|theta| < L/H < pi`,

so the pair branch is nonnegative. The only remaining possibility is

`m=L+1=r+1`.

Since `0<=b<=a<=r`, the equality `a-b+1=r+1` forces uniquely

`(a,b)=(r,0)`.

Moreover that branch can be unsafe only if

`(r+1)|theta|>pi`.

Using `|theta|<=1/gamma` gives the necessary height condition

`H < gamma < (L+1)/pi`.

Because `L<=pi H<L+1`, this unresolved height interval has width

`(L+1)/pi - H = (1-{pi H})/pi < 1/pi`.

Therefore:

`boxed: at the first rank r=floor(pi H) beyond the verified-zero sector strip, every possible negative-support witness is localized to an off-line pair in a height window of width <1/pi, and each such pair has exactly one potentially negative router state, (a,b)=(r,0).`

For this unique extreme branch the rectangle-complement router coefficient is

`s_(r^(k-1))(X) * s_(r)(Y)`

with

`s_(r)(Y)=R^r sin((r+1)theta)/sin(theta)`.

Thus the first boundary-layer correction couples a single pair Chebyshev factor to the adjacent rectangular carrier, rather than to an uncontrolled LR family.

## 3. General h-th boundary layer

Take

`r=L+h`, `h>=0`.

Every potentially negative unverified pair still has `gamma>H`, hence any unsafe state must have

`m>pi H`,

so integer `m>=L+1` and therefore

`a-b=m-1>=L`.

Write

`x=r-a>=0`, `y=b>=0`.

Then

`x+y = r-(a-b) <= h`.

The complement shape in the exact pair router is

`mu_(x,y)=(r^(k-2), r-y, x)`.

So all potentially negative pair branches at excess rank `h` live in the finite triangular edge-carrier family

`{mu_(x,y): x>=0, y>=0, x+y<=h}`,

whose cardinality is

`binom(h+2,2)`.

The unsafe pair itself must satisfy the spectral causal cone

`H < gamma < (r+1)/pi = (L+h+1)/pi`,

so the active unresolved zero-height window has width less than

`(h+1)/pi`.

Hence the branch refinement required immediately above the gigantic verified strip is controlled by the **excess rank h**, not by the absolute rank `r~pi H`.

## 4. BRC interpretation

This is a genuine branch-on-demand compression:

- verified region: one terminal `NONNEGATIVE` token;
- rank `L+h`: inspect only conjugate pairs in a height window of width `<(h+1)/pi`;
- for each such pair, retain only the triangular edge-shape family `x+y<=h` as potentially negative;
- all higher pairs and all non-edge allocations recoalesce into safe sign-support branches.

The first uncovered rank `h=0` has one edge state per active pair. The next layer has three, then six, and so on.

## 5. What remains

This compression does not establish that the surviving edge branches are positive or dominated. It reduces `PAIR_CLUSTER_DOMINATION` to a microscopic spectral boundary layer and a finite near-rectangular edge-carrier family.

The strongest next target is to express/bound

`s_(r^(k-2),r-y,x)(X) / s_(r^k)(safe baseline)`

for `x+y<=h`, and compare it against the exact pair factor. At `h=0` this starts with the adjacent rectangle `s_(r^(k-1))(X)`, creating a direct interface with the Toda determinant-ratio carrier.
