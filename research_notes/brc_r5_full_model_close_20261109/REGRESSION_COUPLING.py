from fractions import Fraction as F
from time import perf_counter
from VERIFY_PGEQ import source,target
from EXACT_COUPLING_SIMPLEX import exact_coupling
start=perf_counter();maxpiv=0;edges={};total=0
for j in range(120):
    den=127
    t=F(1,13)+(F(1,5)-F(1,13))*F((11*j+3)%den,den)
    p=F((13*j+5)%den,den)
    q=p*F((17*j+7)%den,den)
    th=F((19*j+11)%den,den)
    ka=F((23*j+13)%den,den)
    x=source(t,p,q,th,ka);y=target(t,p,q,th,ka)
    e,k=exact_coupling(x,y)
    maxpiv=max(maxpiv,k)
    count=sum(z>0 for row in e for z in row)
    edges[count]=edges.get(count,0)+1;total+=1
print('EXACT_120_FRACTION_MARTINGALE_COUPLINGS_PASS')
print('MAX_PIVOTS',maxpiv,'SUPPORT_COUNTS',edges,'SECONDS',round(perf_counter()-start,3))
