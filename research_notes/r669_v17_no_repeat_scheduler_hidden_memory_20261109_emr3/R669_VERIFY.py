#!/usr/bin/env python3
"""Exact two-letter no-repeat V17 block-schedule check."""
import itertools,json
from pathlib import Path
A=(0,2,1);B=(2,1,0);E=(0,1,2);R=(2,0,1)
def mul(p,q):return tuple(p[q[i]] for i in range(3))
def pw(p,n):
 z=E
 for _ in range(n):z=mul(z,p)
 return z
def legal_words(m,n):
 result=[]
 for w in itertools.product('AB', repeat=m+n):
  if w.count('A')!=m or w.count('B')!=n: continue
  if any(w[i]==w[i+1] for i in range(len(w)-1)):continue
  result.append(''.join(w))
 return result
def frame(w):
 g=E
 for v in w:g=mul(g, A if v=='A' else B)
 return g
def expected(m,n):
 if abs(m-n)>1:return []
 if m==n==0:return ['']
 if m==n:return ['AB'*m,'BA'*m]
 if m==n+1:return ['AB'*n+'A']
 if n==m+1:return ['BA'*m+'B']
 raise AssertionError

def main():
 assert mul(A,B)==pw(R,2) and mul(B,A)==R
 vectors=0; words=0; twin_equal=[]; twin_unequal=[]
 for m in range(11):
  for n in range(11):
   w=legal_words(m,n)
   assert w==sorted(expected(m,n)),(m,n,w,expected(m,n))
   vectors+=1;words+=len(w)
   if m==n and m>0:
    frames=[frame(z) for z in w]
    assert frames==[pw(R,(2*m)%3),pw(R,m%3)]
    if m%3==0:
     assert frames==[E,E]
     twin_equal.append(m)
     assert w==['AB'*m,'BA'*m]
     assert w[0][-1]=='B' and w[1][-1]=='A'
     # A is legal next only after the first schedule.
     assert (w[0][-1]!='A') and not(w[1][-1]!='A')
    else:
     assert frames[0]!=frames[1]
     twin_unequal.append(m)
 summary={"marker":"R669_NO_REPEAT_TWO_REFLECTION_FUTURE_LANGUAGE_MEMORY_PASS","model":"V17 legal closed blocks A,B; declared no-identical-consecutive-block scheduler","tested_count_vectors_m_n_0_to_10":vectors,"total_legal_words_tested":words,"balanced_same_frame_m":twin_equal,"balanced_distinct_frame_m":twin_unequal,"frozen_science":"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f","review":"AUTHOR_SIDE_UNREVIEWED"}
 Path(__file__).with_name('R669_EVIDENCE.json').write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n',encoding='utf-8')
 print(summary)
if __name__=='__main__':main()
