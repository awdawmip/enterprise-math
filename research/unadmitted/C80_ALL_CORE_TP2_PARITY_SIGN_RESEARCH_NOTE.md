# C80 — 全部48位核心的BRC双端口关联符号（作者未接纳草稿）
2026-10-15; auxiliary type only: 156 integer edges, 142 faces, 48 core bits, 76 correlated non-core factors. Frozen sources GLOBAL_KNOWLEDGE_V1 main@d61d60db8d0c5a22dc6caad9f6d0da5ac28e5c3b, enterprise-math main@7b9d8752d58b3bee838749028e522b5266838636. Evidence developed from preserved C68 get_graph() + C79 independent basis builder; not an independently generated graph.

For fixed noncore weights s_8=s_11=s_44=s_61=1/2 and s_f=1/4096 for all 70 other noncore faces except variable faces 86,111, set x=1/s86>1, y=1/s111>1. For any feasible 48-bit core c, write Z_c(x,y)=Axy+Bx+Cy+D as the full 45-free-bit joint positive partition (never split 76 factors into independent products).

NEW EXACT CONDITIONAL THEOREM:
  sign(A_c D_c-B_c C_c) = (-1)^(c18+c19), strictly nonzero, for EVERY c in F_2^48.
Thus a core with equal face 83/96 signs is strictly TP2, and an odd-parity core is strictly reverse TP2, for ALL x,y>1; no exhaustive 2^48 enumeration required.

Proof: original 156-edge masks verify m86 xor m111 xor m89 xor m118 = m83 xor m96. Expand the remaining 74 factors in F_2^45 Fourier characters. With 4 strong faces and 70 weak faces t=1/4096, low-subset exhaustive profiles (weak-count, strong-count : multiplicity) are
A: (0,0):1 (0,4):1 (3,1):8 (3,3):8.
B: (2,1):1 (2,3):1 (3,0):1 (3,2):4 (3,4):1.
C: (2,1):1 (2,3):1 (3,0):2 (3,2):4 (3,4):2.
D: (2,0):1 (2,4):1 (3,1):2 (3,3):2.
No unlisted term with <=3 weak factors exists. All q-zero weak-0 terms are empty and the 4-strong loop, core mask 0x300. Put h=1+(-1)^((0x300)·c)/16 in [15/16,17/16]. The leading two-weak D pair is exactly faces (89,118), with or without all four strong faces; D/kappa = (-1)^(c18+c19) h t² + error.

Rigorous uniform tails:
T3=(81/16)*C(70,3)*t^3/[1-(67/4)t]
T4=(81/16)*C(70,4)*t^4/[1-(66/5)t].
Let A*=15/16-T3, D*=(15/16)t²-(5/4)t³-T4, B*=(5/8)t²+(33/16)t³+T4, C*=(5/8)t²+(25/8)t³+T4.
Exact-rational checks show A*>0, D*>0, A*D*-B*C*>0 (margin approx 3.6859459371312136e-8). Therefore |AD|>|BC| and the determinant has D's parity-controlled sign. This is a uniform analytic bound for all cores. Direct mathematical objects A-D each have common positive normalization factor kappa.

Author checks: C80_ALL_CORE_PARITY_SIGN_THEOREM_PASS; independent weak-mask hash enumeration and exact 70-term binomial tail C80_INDEPENDENT_HASH_AND_EXACT_BINOMIAL_TAIL_PASS; inherited C79 27-core exact data C79_STRICT_POSITIVE_RESIDUAL_CORRELATION_PASS. Full script, exact JSON, proof and frozen graph retained in the local C80 portable research package; not uploaded as part of this note.

Research status: UNADMITTED / NO_CLAIM / NO_DRIVER_REVIEW / NOT_FORMAL_SOURCE_RESULT. Sites MCP static_machine_readonly cannot start execution session (STATIC_READONLY_SCOPE_DENIED). Active owner not authenticated. A non-main draft branch is NOT a canonical Research Result or acceptance. Do not promote to Working Truth, P000, C46 or native six-dimensional Cell theorem. Follow-up: vary common t and certify parity-stable region or actual sign transition, and independently reconstruct the 156-edge graph.