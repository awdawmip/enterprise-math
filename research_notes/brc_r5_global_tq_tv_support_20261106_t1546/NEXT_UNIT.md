# R5 next scientific unit — interior-image discriminator

Frozen inputs: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`. Read [research proof](RESEARCH.md), then the previous [fixed two-stage hexagon](../brc_r5_two_stage_lr_hexagon_20261106_t1441/RESEARCH.md).

**Resolved:** every unrestricted FULL_HIST policy satisfies `|eP+eQ-1| <= (TQ-1)/8`. On `1<=TQ<=2` this is sharp and all equality faces are realized by seedless LR; at `TQ=15/8`, the two-stage hexagon already supplies both extreme supporting faces.

**Executable next unit:** choose rational `W=(eP,eQ,TP,15/8)` with `57/64<eP+eQ<71/64`, full-history legal via explicit (g,u_0,u_1,x_{ij},t_h) and either `TP != 15/8` or `TP=15/8` with errors outside the two-stage hexagon. Construct the *full* seven-variable LR fiber `K(W)`, preserving its quadratic residual `F=(A+B)J-X1(alpha*A+beta*B)`; certify globally `min F>0` or `max F<0`, or explicitly produce a legal LR strategy where `F=0`. Work with exact rational endpoints / certified algebraic signs.

**Return criterion:** one completely checked candidate with exact residual sign certificate or exact LR realization; otherwise a tighter derived subregion with proof. Do not promote fixed-family separation to full LR separation. Keep formal Owner/CLAIM and independent admission separate.
