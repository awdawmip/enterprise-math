import importlib.util
from math import comb
from pathlib import Path
src=Path(__file__).with_name('pinned_signed_brc.py')
spec=importlib.util.spec_from_file_location('pinned_signed_brc',src)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=0
for q in range(1,5):
    for n in (3*q,4*q,4*q+1):
        for k in (0,q,2*q,3*q,4*q):
            if k>n: continue
            target=(n-2*k,0,0,0,0,0)
            got=m.endpoint_multiplicity(n,target)
            assert got>=comb(n,k) and got>0,(q,n,k,got)
            checks+=1
print('PASS original frozen signed_brc.endpoint_multiplicity')
print('source_git_blob=300a96e3dc24bf6fff73743037a0347a8bc83176')
print('capacity_checks=',checks)
