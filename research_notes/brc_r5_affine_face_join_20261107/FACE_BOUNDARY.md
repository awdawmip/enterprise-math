# R5 — Exact stopping-time extremal boundary forces a second seedless face

2026-11-07 author-side mathematical theorem; same frozen scientific pins, seven-key model and definitions as `RESEARCH.md` and predecessor `194f81437a86b5fa24947d3dedd3e0f9bfed03be`.

For every legal **real** flow `x=(g,a,b,u,v,w,z)`, the stopping-time difference satisfies
```
T_Q - T_P = (a-b)/8 + (u-w)/2 <= 23/80.
```
The exact **nonnegative coefficient identity** is
```
23/80 - (T_Q-T_P)
  = 23*(1-a)/80 + 19*b/160
    + (13*a/40+b/80-u)/2 + w/2.
```
All four summands are nonnegative by the legal constraints `0<=a<=g<=1`, `b>=0`, `u<=13a/40+b/80`, `w>=0`. **Equality holds exactly on the real one-parameter family**
```
g=1, a=1, b=0, u=13/40, w=0;
0<=z<=1/10, v=z.
```
(The displayed equality also forces `g=1` because `a=1<=g<=1`, and `v=z` because `0<=v-z<=9b/40=0`.) Every flow on this extremal family is **seedless LR**, as `9*b*z=4*a*(v-z)=0`. Its stopping times are
```
T_P=203/80+z,     T_Q=113/40+z.
```

Take the legal seedless endpoint `x_*=(1,1,0,13/40,0,0,0)`, with `(T_P,T_Q)=(203/80,113/40)`. It has an exact identity Blackwell lift (itself). Nevertheless **no flow in the particular seedless affine face** `F={z=a/10,v-z=9b/40}` **can match its two stopping times**. Indeed, time-difference equality forces `a=1`; `F` then forces `z=1/10`, hence `T_P=211/80 != 203/80`. The obstruction already holds at the two stop-time observations, independently of declarations and transport matrices.

This precisely separates a limitation of the **single affine target face** `F` from any claim of impossibility over all seedless strategies: `x_*` itself is seedless. A multiple-face lifting construction can use the distinct seedless extremal edge `b=0,v=z`, but its nonlinear seedless equality must be checked after any mixed-face interpolation.

**Verification:** `VERIFY_FACE_BOUNDARY.py` checks the coefficient identity and endpoint legality, seedless constraint and exact times using standard-library `Fraction`; `FACE_BOUNDARY_OUTPUT.txt` contains the output. The entire-real equality characterization follows from the displayed nonnegative identity, not finite sampling.

**Next unit:** search exact calibrated cross-face lifts on `H={legal: v-z=9b/40}` outside the certified join `conv(C union F)`, starting at `z=0,a>b,u,w>0`. Preserve all seven P/Q stopping masses and both times. Find a new explicit affine seedless face or a stronger feasibility classification; failure of `F` alone is not failure of the full seedless family.
