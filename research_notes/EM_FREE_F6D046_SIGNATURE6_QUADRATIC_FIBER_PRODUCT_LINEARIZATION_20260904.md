# signature 6 的 quadratic fiber product、四-signature 最小严格线性化覆盖与 genus 57

Status: `FREE_RESEARCH / DERIVED_QUADRATIC_FIBER_PRODUCT / EXACT_FOUR_SIGNATURE_LINEARIZATION / CORRECTS_R5 / NOT_AXIOM / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`
Research unit: `EM-FREE-F6D046-R7-SIGNATURE6-QUADRATIC-FIBER-PRODUCT`

## 0. 正确的四-signature 结构

令 `Y=X0(12)`，`z=1728/j_Y`。R4 已在 Y 上统一 signatures 2/3/4 的 projective local system，并得到独立 linear characters chi2、chi4，其 branch blocks 在 Y 上分别有 2、4 点。

signature 6 不能只作为 Y 上第三个 linear character 加入。标准二次变换为

`2F1(1/6,5/6;1;w)=2F1(1/12,5/12;1;4w(1-w))`。

必须先定义

`C: s^2=1-z=1-1728/j_Y`, `w=(1-s)/2`。

Y 的 j-map degree 为 24 且 Y torsion-free：over j=0 有 8 points、各 local degree 3；over j=1728 有 12 points、各 local degree 2。函数 `(j-1728)/j` 在前八点 order -3，在后十二点 order +2，故 quadratic cover只在八个 j=0 preimages 分支。

Riemann--Hurwitz 给出 `2g(C)-2=2*(-2)+8=4`，故 `g(C)=3`。这是 signature 6 与 congruence signatures 的最小 projective fiber product。

## 1. signature 6 与 signature 3 的 linear difference

在 C 的 j=0 ramification point，以 u 为局部参数。Y 上 j~t^3，C 上 t=u^2，而 w~u^-3。signature 6 infinity exponents `{1/6,5/6}` 拉回为 `{1/2,5/2}`，local linear monodromy 是 -I。

signature 3 在 Y 的全部 j=0 preimages 上为 +I：其 order-3 elliptic preimages 经三重拉回给 `{1,2}`，其余来自 ordinary ramified j-points。再拉到 C 后仍为 +I。

所以 C 上存在 relative character lambda6，branch block R 恰是上述八个 ramification points。其 kernel double cover 满足 `2g-2=2*(2*3-2)+8=16`，故 genus 9。

这说明先前 genus 9 数字的正确位置是：C 上 signature 3/6 linear-character kernel cover，而不是 X0(12) 上全部四 signatures 的 common cover。

## 2. pullback 的 signature 2/4 characters

C->Y 只在 j=0 分支。R4 的 chi2 branch block B2 是两个 cusps；chi4 branch block B4 是四个内部 order-2 preimages，位于 j=1728 locus 的特定子集。因此 C 在 B2、B4 上均 unramified，各点有两个 preimages：

`|p^-1 B2|=4`, `|p^-1 B4|=8`。

它们与 R 及彼此均不交。围绕三个 branch blocks 的小环给出独立坐标，故 `<p*chi2,p*chi4,lambda6> ~= (Z/2)^3`。

## 3. 最小 strict linearization cover

在 C 上同时消去三个独立 characters 的共同 kernel cover `Ctilde->C` 次数为 8。任何实际四-signature strict common cover Z->Y 必须先承载 w，因而 factor through C；随后必须杀掉 joint character image，所以 `[Z:Y]>=2*8=16`。共同 kernel construction 达到下界。

C genus 3，三个不交 branch blocks 总点数 `4+8+8=20`。对 degree-8 `(Z/2)^3` cover，每个 branch point inertia order2，贡献4：

`2g(Ctilde)-2=8*(2*3-2)+20*4=32+80=112`，故 `g(Ctilde)=57`。

因此在当前明确类别中：

- projective quadratic fiber product: degree 2, genus 3；
- relative linear characters on C: rank 3；
- strict all-four linear cover over Y: degree 16, genus 57。

## 4. 三层阻碍

1. projective descent/base-change obstruction：由 `s^2=1-1728/j` 处理；
2. linear H1 character ambiguity：由 C 上 degree-8 kernel cover 处理；
3. common monodromy：前两层清除后仍不自动平凡。

R6 的 parity theorem只能抹去第二层的 quadratic characters，不能替代第一层 projective fiber product。

## 5. 最小性边界

最小性限于：保留标准 j-marking；signature 6 通过 `4w(1-w)=1728/j` 接入；strict equivalence 指 rank-2 linear local systems 的共同 pullback；covers connected 且允许 algebraic branching。改变 j-marking、采用非标准 correspondence 或只比较局部 branch 可能产生不同 span。

## 6. 审计

R5 unconditional four-signature claim: `SUPERSEDED_BY_CORRECTION`；仅保留条件模型与 parity theorem。T9: `REUSE_APPLIED`。T7: `COMPOSE_APPLIED`。quadratic hypergeometric transformation 是标准机制。Verdict: `DERIVED_QUADRATIC_FIBER_PRODUCT / EXACT_FOUR_SIGNATURE_LINEARIZATION / NOT_NEW_AXIOM / NOT_FOUNDATION`。
