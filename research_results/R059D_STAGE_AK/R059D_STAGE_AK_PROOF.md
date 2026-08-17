# R059D Stage AK — Target fixed-length native turn-orbit proof

Researcher-ID: `EM-R059D-AK-3C7E52`

## 1. Target state and length class

For each integer `r>=1` and fixed endpoint `O`, define the anchor segment state

`A_r(O)=(O,r,0,L,r,0,-4)`.

The free endpoint projection is

`endpoint(O,r,k,phase,a,b,z)=O+R^k(a,b)`,

where `R(a,b)=(-b,a+b)` and `R^6=id`.

The anchor free endpoint is `O+(r,0)`. The integer `r` is therefore first defined operationally as the number of primitive Enterprise axis steps in the anchor segment, not as a Euclidean norm.

Let `SEG_E(r)` be the translates of all legal `tau` iterates of `A_r(0)`. Two target segment states are `ENTERPRISE_EQUAL_LENGTH` iff, after translating their fixed endpoints to a common origin, they belong to the same `SEG_E(r)` orbit class. Define `L_E(S)=r`.

Every branch of `tau` preserves `O` and `r`, so the fixed endpoint and length class are invariant under every legal turn.

## 2. Left-half one-step law

Stage AH already proved the first-sector N boundary can be generated on the left half by the integer state `(a,b,rho)` with initial

`(a,b,rho)=(r,0,-4)`.

While `a-b>1`:

- if `rho>=0`, emit `1`, set `b<-b+1` and
  `rho<-rho-3(a+2b_old+3)`;
- if `rho<0`, emit `2`, set `(a,b)<-(a-1,b+1)` and
  `rho<-rho+3(a_old-b_old-3)`.

The difference `d=a-b` decreases by one on `1` and by two on `2`, so the left phase reaches `d in {0,1}` in finitely many turns.

If `d=1`, the unique center move is symbol `2`. If an ordinary left move lands at `d=0`, there is no center move.

No phase normalization is counted as a turn: every invocation of `tau` emits exactly one boundary edge.

## 3. Direct forward right-half law

The nontrivial AK step is to eliminate AH's stored `reverse(left)` construction.

By reflection of the accepted AH support theorem, in the right half `a<=b` use the proof-only polynomial

`L_R(a,b)=3(a^2+ab+b^2)-3b+1`.

At a right-half boundary point `(a,b)`, define the proof residual for the next diagonal candidate by

`sigma=3r^2-L_R(a-1,b+1)`.

This polynomial is used only to derive the recurrence. Runtime never evaluates it.

The horizontal candidate satisfies

`L_R(a-1,b)-L_R(a,b)=3-6a-3b<0`

for every right-phase state `0<a<=b`. Hence the horizontal successor remains legal whenever the current point is legal.

The diagonal candidate is legal exactly when `sigma>=0`. Therefore the forward right-half rule is exact:

- if `sigma>=0`, emit `2` and move `(a,b)->(a-1,b+1)`;
- if `sigma<0`, emit `3` and move `(a,b)->(a-1,b)`.

Finite differences give the runtime recurrence without support evaluation:

- after symbol `2`,
  `sigma'<-sigma+3(a-b-2)`;
- after symbol `3`,
  `sigma'<-sigma+3(2a+b-2)`.

At the midline, direct algebra gives the same conversion in both parity cases:

`sigma=rho+9b+3`,

where `b` is the terminal left-half lower coordinate before a possible center move.

Thus the right half is a genuine forward local dynamics and does not store or reconstruct an unbounded word prefix.

## 4. Sector completion

Every right-half move decreases `a` by exactly one. Hence the phase reaches local endpoint `(0,r)`.

For sector index `k`,

`R^k(0,r)=R^(k+1)(r,0)`.

Therefore the state reached by the final edge of sector `k` can be normalized immediately to the next-sector anchor registers

`(k+1 mod 6,L,r,0,-4)`

without moving the free endpoint and without consuming an extra turn.

All six sectors use the identical local law. Since `R^6=id`, six sector completions return to the original chart and anchor endpoint.

## 5. Equality with the accepted AH boundary

On the left half, AK is exactly the frozen AH residual recurrence.

At the midline, the AK conversion gives the reflected residual with no history.

On the right half, the `sigma` sign test is exactly the reflected boundary-successor test, so the emitted sequence is the AH reflected right half edge for edge.

Consequently one AK sector is exactly the accepted AH first-sector word and vertex path. Applying the same `R^k` transport for `k=0,...,5` proves the complete endpoint orbit is exactly the accepted AH D6 boundary.

This is an equality theorem between two autonomous target descriptions; source-circle membership is not a runtime definition of either side.

## 6. Simple cycle and minimal period

Inside one sector, every edge is one of

`(0,1), (-1,1), (-1,0)`.

Thus `a` never increases, `b` never decreases, and every turn changes the endpoint. Apart from the two axis endpoints, sector vertices satisfy `a>0,b>0`. Hence a sector path has no repeated vertex.

The six rotated open-sector interiors are disjoint. Adjacent sectors meet only at their shared axis endpoint. Therefore the full D6 endpoint cycle has no repeated endpoint before the final return to `O+(r,0)`.

Stage AH gives one-sector edge count

`|W_N(r)|=r+J_N(r)`.

Sector normalization costs zero turns. Hence after exactly

`T_r=6(r+J_N(r))=C_N(r)`

applications of `tau`, the anchor state returns.

No smaller positive state period is possible because a repeated segment state would repeat its endpoint, contradicting the simple-cycle result.

Therefore

`TURN_PERIOD = BOUNDARY_EDGE_COUNT = CIRCUMFERENCE_COUNT`.

With Stage AG,

`T_r=6(r+floor(alpha*r+1/3))`.

With Stage AI,

`lim T_r/(2r)=kappa_E`, `kappa_E^2=12`, `kappa_E>0`.

Also `T_r-T_(r-1) in {6,12}`, so `T_r` is strictly increasing. The closed target orbit period itself therefore distinguishes different radius/length classes; the `r` label is not an arbitrary cosmetic annotation.

## 7. Translation and D6 covariance

Translation acts by changing `O` to `O+t` while leaving all local registers fixed. Because `tau` never reads `O`,

`tau(T_t S)=T_t(tau(S))`.

A rotation by `j` sectors around the fixed endpoint acts by

`k<-k+j mod 6`

with all canonical local registers unchanged. The update law is sector-independent, so

`tau(Rot_j S)=Rot_j(tau(S))`.

`R^3` gives sign inversion of the relative endpoint and is included automatically.

A D6 reflection maps the proved simple cycle to itself with reversed orientation. On the closed orbit this yields

`F tau F^{-1}=tau^{-1}`.

Thus the six sectors are transported copies of one turn law, not six fitted machines.

## 8. Runtime firewall

The canonical `tau` implementation uses only integer addition, subtraction, multiplication by fixed small integers, comparisons, finite phase control, and the D6 integer rotation map.

It does not call or store:

- a source-circle membership oracle;
- source `Q` occupancy;
- Euclidean distance/equidistance;
- standard `pi`;
- square root;
- trigonometry;
- floating-point arithmetic;
- occupancy, word, or boundary lookup tables;
- radius-specific tuned parameters.

The proof-only support polynomials explain why the residual recurrence is correct; they are not part of the runtime target definition.

## 9. State-minimality boundary

The online state uses a constant number of integers: `r`, local `(a,b)`, one signed residual, plus finite sector/phase control. No radius-growing history is stored.

True information-theoretic minimality is not claimed. On reachable states the residual can be reconstructed from `r,a,b,phase` by evaluating the frozen proof polynomial, but that route reintroduces the support calculation excluded by the target runtime firewall. The proved status is therefore

`SMALLEST_CURRENTLY_PROVED_SUFFICIENT_ONLINE_STATE_UNDER_RUNTIME_FIREWALL`.

## 10. C_s compatibility boundary

Stage AJ proves every inherited `C_s` uses the same anchor radius and differs from N by at most one shell, with circumference difference at most six. This supports a bounded finite-precision phase/readout interpretation at the same anchor label.

AK does not prove that a `C_s` endpoint boundary is the identical N `tau` orbit, and it does not construct a full autonomous C turn machine. Those statements remain open and are not needed for the N target fixed-length theorem.

## Conclusion

For every integer `r>=1` and every center `O`, the accepted autonomous N Enterprise circle is exactly the complete closed orbit of the free endpoint of a target Enterprise segment state of fixed Enterprise length class `r` under a radius-uniform local integer turn operator. The minimal positive turn period is exactly the native circumference count.

`TARGET_FIXED_LENGTH_NATIVE_TURN_ORBIT_THEOREM_PROVED`.
