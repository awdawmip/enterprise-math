"""Compare the integer prefix formulas to the original positive three-state recursion."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json
import sys
from stock_decoder import ends,edge,mul,ID,span,widths,SCALE,WIDTH

def run(prior):
 sys.path.insert(0,str(prior.resolve()))
 from mixed_kernel import responses
 known=[]
 def check(r,c,w):
  rows,_=responses(r,c,w)
  z=[(7*rows[0][j]+rows[1][j])/(7*rows[0][j]+rows[2][j]) for j in (3,4,5)]
  b=c;M=ID
  for i,m in enumerate(w[:-1]):
   M=mul(M,edge(r-i,b,m));b-=m
  a,p,h,d=M
  computed=sorted((a*t+p)/(h*t+d) for t in ends(b))
  assert computed==[min(z),max(z)]
  lo,hi=span(r,c);wl,wh=widths(r,c)
  assert lo<=min(z)*SCALE and hi>=max(z)*SCALE and wl<=(max(z)-min(z))*WIDTH<=wh
  return tuple(computed)
 def words(r,total):
  if r==0:
   yield (total,);return
  for j in range(total+1):
   for sub in words(r-1,total-j):yield (j,)+sub
 for r in range(1,5):
  for c in range(2,10):
   s={check(r,c,w) for w in words(r,c-2)}
   assert len(s)==comb(r+c-2,r)
   known.append(len(s))
 rows=[]
 for r,c in [(27,28),(31,32),(33,34),(50,28),(80,32)]:
  s=c-2
  for i in range(3):
   w=[0]*(r+1)
   for j in range(s):w[(j*7+i*13)%(r+1)]+=1
   x,y=check(r,c,tuple(w))
   rows.append(dict(r=r,c=c,sample=i,min_numerator_bits=x.numerator.bit_length(),max_denominator_bits=y.denominator.bit_length()))
 return dict(full_exact_small_words=sum(known),independent_samples=rows,observations_per_word=6)
if __name__=='__main__':
 p=ArgumentParser(description=__doc__)
 p.add_argument('--prior',type=Path,required=True)
 print(json.dumps(run(p.parse_args().prior),indent=2))
