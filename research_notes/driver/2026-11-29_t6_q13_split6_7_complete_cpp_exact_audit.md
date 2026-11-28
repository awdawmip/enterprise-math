# T6 q13 final split(6,7): 165 exact alternate-solver exclusions

Driver EM-DVR-DEBB5E, frozen science d84bd940cfb093cdc60e569f15cad58772a51dca, shared nonblind informed context. Same saturated U, high atom domain, six mixed congruences and both budgets 2331 as previous exact C++ audit a11eb6e5b39657817ad4e5a4568276f63bddc714:research_notes/driver/2026-11-29_t6_q13_split5_8_len6to8_cpp_exact_audit.md. The Driver authors the alternate method and is not a clean independent decisive reviewer of that method. No new mathematical acceptance.

## Executed result
All 11 partitions of 6 crossed with all 15 partitions of 7. Exact Python rational precomputation and compiled C++17 enumeration completed. Independent Python postcheck verified set equality of all 165 pattern pairs, no duplicates, each raw count independently via product of binomial coefficients, all twelve rejection counters sum plus survivors equals search, and first index passes equal search minus first rejection counter. All 24,872 recovered vectors checked integer divisibility, original six congruences and signed budgets. No valid vector. Raw stdout CSV SHA256 a436b40d08af488ffac0a8d80a32d61b565817edd38b550f8f8874a540be9bc7 (local execution digest; full CSV reproducible, not separately stored at this path). Aggregate actual execution by negative length (min excess only among recovered box survivors):
```csv
negative_length,patterns,raw,search,index_pass,box_survivors,valid,min_max_budget_excess
1,11,511368,511368,158597,24,0,2291
2,33,18409248,18409248,5474542,316,0,917
3,44,193297104,193297104,54946290,2240,0,955
4,33,850916352,850916352,230694005,6159,0,650
5,22,1907914008,1907914008,492191618,8075,0,760
6,11,2233655424,2233655424,546865738,5795,0,671
7,11,1356147936,1356147936,314231971,2263,0,880
TOTAL,165,6560851440,6560851440,1644562761,24872,0,650
```
Every row has raw=search, so no high-budget candidate removal. The minimum excess 650 among box survivors is not a lower bound on arbitrary solutions outside the tested box. All exclusions use the necessary box for the fixed budget, not an enlarged budget.

## Reproduction
Use the exact C++ source in a11eb6e5b39657817ad4e5a4568276f63bddc714, replace `for(auto pp:parts(5))` with `for(auto pp:parts(6))` and `for(auto np:parts(8)){if(np.size()<6)continue;` with `for(auto np:parts(7)){`. No other C++ modification. The following exact Python setup is the one used (also works for the previous split if ms and ns are changed as indicated). Run python setup67.py, g++ -O3 -std=c++17 audit67.cpp -o audit67, ./audit67 < input.txt > results67.csv. No floating-point bound or approximate coordinate test. All integer values within the C++ signed-width bounds established in the previous note.
```python
import sympy as s
from fractions import Fraction as F
U=s.Matrix([[52,-163,-2,27,-16,7,16,-1,-4,2,-6,-4],[-112,-87,-29,38,29,5,-31,25,-16,15,5,-2],[55,-58,-9,47,-59,9,-9,24,-4,5,31,0],[-344,41,64,-38,-44,-15,8,-3,-7,-14,-13,-12],[-105,-39,-34,-67,-33,10,-65,-5,-13,-18,17,-8],[356,73,-4,-30,45,-39,38,34,-22,-14,-22,12],[-62,27,67,60,54,65,11,-15,-13,23,-1,1],[278,-68,114,32,-39,-9,-16,2,11,-6,6,-7],[-73,103,9,-39,2,-24,28,-15,-45,0,9,-9],[-233,17,43,-2,-15,-24,-7,7,-33,5,2,18],[-102,136,-14,84,-7,6,-7,-12,-27,-25,5,-16],[-210,-62,-9,-44,3,-30,13,-11,-22,-55,23,3]])
P=13;B=P**6; W=[13*r-1 for r in range(1,13)]; H=[[pow(r,-(k+1),P**(k+1)) for r in range(1,13)] for k in range(6)]
assert abs(U.det())==P**21 and all(sum(H[k][j]*int(U[i,j]) for j in range(12))%P**(k+1)==0 for i in range(12) for k in range(6))
UI=U.inv(); D=UI*B; assert all(x.q==1 for x in D)
bounds=[]
for i in range(12):
 g=[F(UI[j,i])/W[j] for j in range(12)]+[F(0)]; bounds.append((min(g),max(g),i))
bounds.sort(key=lambda x:x[1]-x[0]); assert max((h-l)*2453 for l,h,i in bounds)==F(498515831,736645312)
def lift(t):
 x=[0]*12
 for j in range(6):
  q=P**j;m=6-j;a=[]
  for k in range(j,6):
   d=t[k]-sum(h*v for h,v in zip(H[k],x));assert d%q==0;a.append([v%P for v in H[k][:m]]+[d//q%P])
  for k in range(m):
   l=next(l for l in range(k,m) if a[l][k]);a[k],a[l]=a[l],a[k];v=pow(a[k][k],-1,P);a[k]=[z*v%P for z in a[k]]
   for i in range(m):
    if i!=k:
     v=a[i][k];a[i]=[(z-v*y)%P for z,y in zip(a[i],a[k])]
  for i in range(m): x[i]+=q*a[i][-1]
 assert all((sum(h*v for h,v in zip(H[k],x))-t[k])%P**(k+1)==0 for k in range(6));return x
with open('input.txt','w') as o:
 def emit(a): print(*a,file=o)
 emit([B]);emit(W);emit([i for l,h,i in bounds])
 for row in U.tolist():emit(row)
 for row in H:emit(row)
 for q in range(1,9):
  for r in range(1,13):
   t=[pow(13*q+r,-(k+1),P**(k+1)) for k in range(6)];x=lift(t); emit([sum(x[j]*int(D[j,i]) for j in range(12))%B for l,h,i in bounds]+t)
 def masses(qsum,lens): return sorted({169*qsum+13*r-l for l in lens for r in range(l,12*l+1) if 169*qsum+13*r-l<=2331})
 ms=masses(6,range(1,7));ns=masses(7,range(1,8));emit([len(ms),len(ns)]);emit(ms);emit(ns)
 for mp in ms:
  for mn in ns:
   lo=[];hi=[]
   for l,h,i in bounds:
    a=B*((2331-mp)*l-(2331-mn)*h);b=B*((2331-mp)*h-(2331-mn)*l);lo.append(-((-a.numerator)//a.denominator));hi.append(b.numerator//b.denominator)
   assert all(l<=0<=h and h-l<B for l,h in zip(lo,hi));emit(lo+hi)
```
For split(5,8) previous remaining lengths, use ms=masses(5,range(1,6));ns=masses(8,range(6,9)). Its local full stdout CSV digest ce1d74972143b1f24638b279dec0d46516f54b69fb024335cc167607ecd3d18e; 28 rows independently checked by the same Python postcheck.

## q13 closure at exact model scope
Coverage across seven splits 101+77+112+126+150+154+165=885/885. Previously 692; this turn adds 28+165=193 distinct pairs, all executed. All relaxations at the same six mixed congruences and signed budgets; not an assertion of observation-envelope implication, H0, lower-prime completion, or global T6=2332. Prior native association 566; current full scope awaits fresh association under original Driver authority. No new formal Review, Result acceptance, Task completion, Working Truth or mother closure. Next: consolidate q13 exact model evidence into original Result, then focus on observation-envelope implication and existing follow-up rather than repeating finite q13 enumeration.
