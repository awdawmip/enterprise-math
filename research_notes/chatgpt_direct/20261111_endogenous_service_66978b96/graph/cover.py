"""Construct exact 2- and 3-fold C5 service codes, and an exact 6-fold bit count."""
import argparse,json,sys
from pathlib import Path
from itertools import product
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from adaptive.graph.feedback_graph import rectangles,E
def run():
    rect2,_=rectangles()
    bases=[(0,0,0),(0,0,1),(0,1,0),(0,4,4)]
    rect3=[tuple(tuple((x+t+s)%5 for s in (0,2)) for x in base) for base in bases for t in range(5)]
    def cover(rect):
        d=len(rect[0]);encoder={};counts=[]
        for i,r in enumerate(rect):
            assert all(len(b)==2 and ((b[0]-b[1])%5) in (2,3) for b in r)
            for w in product(*r):encoder.setdefault(w,i)
        assert len(encoder)==5**d
        for w,i in encoder.items():
            for a, pair in zip(w,rect[i]):
                for edge in E:
                    if a in edge:assert set(edge)&set(pair)=={a}
        for i in range(len(rect)):counts.append(sum(1 for v in encoder.values() if v==i))
        return [len(encoder),counts]
    t2=cover(rect2);t3=cover(rect3)
    r6=[a+b for a,b in product(rect3,repeat=2)]
    t6=cover(r6)
    lower=[1]
    for _ in range(6):lower.append((5*lower[-1]+1)//2)
    assert lower==[1,3,8,20,50,125,313]
    assert (lower[6]-1).bit_length()==(len(r6)-1).bit_length()==9
    return {'status':'PASS','three_fold_starts':bases,'three_fold_rectangles':rect3,
            'slice_lower_0_to_6':lower,'cover_counts':[t2[0],t3[0],t6[0]],'code_sizes':[len(rect2),len(rect3),len(r6)],
            'two_fold_bits':3,'three_fold_bits':5,'six_fold_message_interval':[313,400],'six_fold_bits':9,
            'scope':'625 pairs checked separately via original components; 125 and 15625 history tuples checked as abstract cover/decoder, not as larger kernels'}
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--out',type=Path,default=Path(__file__).with_name('cover_results.json'));opt=a.parse_args()
    v=run();opt.out.write_text(json.dumps(v,indent=2,sort_keys=True)+'\n');print('covers',v['cover_counts'],v['six_fold_bits'])
