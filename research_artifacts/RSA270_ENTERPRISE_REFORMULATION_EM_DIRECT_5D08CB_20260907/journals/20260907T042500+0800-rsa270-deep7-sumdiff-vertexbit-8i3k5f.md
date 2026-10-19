# RSA-270：深入研究第 7 轮——证书的和/差线性结构与顶点侧位

Progress-Event-ID: `rsa270-deep7-sumdiff-vertexbit-8i3k5f`
At: `2026-09-07T04:25+08:00`
Scope: `enterprise-math / RSA-270 / deep research round 7`
Source: `ChatGPT TASK_RESEARCH conversation; exact integer Python; journal 7h2j4e; P000 assumed`
Kind: `PROGRESS / EXACT THEOREM`
Researcher-ID: `EM-DIRECT-5D08CB`

## Event

Deep-research round 7. No factor obtained.

### Sum/difference linear certificate (exact, verified)

For branch `l`: `x = l p + q`, `y = |l p - q|` satisfy

`{x+y, x-y} = {2 l p, 2 q}`

(one of the sum/difference equals `2 l p`, the other `2 q`, depending on the vertex side). Verified on 5 semiprimes x all primes <= 31.

### Vertex-side bit (exact, verified)

For `l = 2`: `x+y = 4p` (hence `x+y = 0 mod 4`) iff `2p > q` (`r < 2` side); `x+y = 2q` (`= 2 mod 4`) iff `2p < q` (`r > 2` side). Verified on 6 semiprimes covering both sides.

### RSA-270 x2 side split

- 8 of the 12 admissible classes lie on the `2p > q` side, 4 on the `2p < q` side;
- `4p mod 72 in {20, 44, 68}` (3 classes), `2q mod 72 in {10, 22, 34, 46, 58, 70}` (6 classes).

The x2 certificate therefore carries **one genuine vertex-side bit** (`r < 2` vs `r > 2`), readable as `x+y mod 4` from any claimed layer-2 observation `(x,y)`. Under the prior band `r in [1.765, 2.266]` both sides are admissible — the bit is real factor data, the finest bit of the layer-2 shadow identified so far.

## Artifacts

- Script: `rsa270_deep7.py` (conversation-local).
- Prior frontier: `journal/enterprise-math/2026-09-07/20260907T034000+0800-rsa270-deep6-root-gap-saturation-suite-7h2j4e.md`.

## Next

1. The vertex-side bit belongs to the certificate suite (extend `rsa270-certificate-suite-20260907.md`).
2. Multi-branch vertex-side bits (`l = 3, 5, ...` give analogous `r < l` vs `r > l` bits via `x+y mod 2l`-structure) — the vertex is sandwiched by consecutive primes; the finest sandwich for the prior band is `r in (2, 3)`-free -> only the l=2 bit is band-cutting. Record the general form.
