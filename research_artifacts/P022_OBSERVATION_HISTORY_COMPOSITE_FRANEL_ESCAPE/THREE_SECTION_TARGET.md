# Three-section next target

For `M=3m`, `q=6M-1=18m-1`, define

`w_j = C(2M,j) C(M+j,j) C(2M-1,j)`

and

`W_a = sum_{0<=j<2M, j=a mod 3} w_j`, `a=0,1,2`.

Then the exact live obstruction is `W_0+W_1+W_2 = 0 (mod q)`.

Over `F_(q^2)` choose `omega^2+omega+1=0`.  Root-of-unity filtering gives

`W_a = (1/3) sum_{t=0}^2 omega^(-a t) P_M(omega^t)`

for `P_M(z)=sum_{j=0}^{2M-1} w_j z^j`.

Since `q=5 mod 6`, Frobenius exchanges `omega` and `omega^2`.  The next exact
unit is to derive the Frobenius relation of `P_M(omega)` and `P_M(omega^2)` and
use it to forbid `P_M(1)=0` on the admissible twin-boundary line.

No nonvanishing conclusion is frozen here.
