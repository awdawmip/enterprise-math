import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location('repro506',str(Path(__file__).with_name('REPRO_STAGE506B.py')))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def brute(n,h,R):
    out=set()
    def recurse(tokens,depth):
        if depth==h: return
        L=len(tokens)
        cases=['pop','del2','ins2']+[f'set:{r}' for r in R]
        for case in cases:
            if case=='pop' and L>=1:
                hits=[tokens[-1]]; nxt=tokens[:-1]
            elif case=='del2' and L>=3:
                hits=[tokens[-3]]; nxt=tokens[:-3]+tokens[-2:]
            elif case=='ins2' and L>=2:
                hits=[tokens[-2]]+([tokens[-3]] if L>=3 else []);nxt=tokens[:-2]+(-1,)+tokens[-2:]
            elif case.startswith('set:') and L>int(case[4:]):
                hits=[tokens[-1-int(case[4:])]];nxt=tokens
            else: continue
            out.update(n-1-i for i in hits if i>=0)
            recurse(nxt,depth+1)
    recurse(tuple(range(n)),0)
    return sorted(out)

N=0
for n in range(11):
 for h in range(5):
  for R in ((),(2,),(0,3),(1,2,5)):
   a=m.exact_mask(n,h,R);b=brute(n,h,R)
   assert a==b,(n,h,R,a,b)
   N+=1
print('INDEPENDENT_EXHAUSTIVE_ORIGINAL_TOKEN_EXPOSURE_CASES',N,'PASS')

# Provenance gap counterexample: same F and even same count of P in gap.
word=(2,0,0,0,0); mask=m.exact_mask(len(word),1,())
print('mask',mask,'K gap initial indices',list(range(len(word)-len(mask))))
removed_index0=word[1:]
removed_index1=word[:1]+word[2:]
print('initial F equal',m.observe(word)==m.observe(word))
print('gap public count equal',1,'1')
print('after deleting single public at index 0 or 1', removed_index0,removed_index1)
print('after D',m.observe(removed_index0)[1], m.observe(removed_index1)[1]);assert m.observe(removed_index0)!=m.observe(removed_index1)
