"""Integer checks for the limiting suffix law and a certified density floor."""
from math import comb
from fractions import Fraction as Q
from itertools import combinations
import json

def binary_words(n,s):
 for subset in combinations(range(n+s),n):
  b=set(subset)
  yield tuple(int(i not in b) for i in range(n+s))

def witness(q,n,s):
 return comb(2*q-1-n-s,q-n) if n<=q and s<q else 0

def main():
 # alpha gives a positive supermartingale for the walk +51 on a five, -52 on a block.
 a=Q(2654,2653)
 assert a**51+a**(-52)<2
 C=34
 m=C-1
 # Round every probability contribution down separately to avoid a large denominator.
 unit=10**10
 lower=0
 for j in range(150):
  slack=52*j-51*m-103
  if slack>0:
   mass=Q(comb(m+j-1,j),2**(m+j))
   lower+=int(mass*(1-a**(-slack))*unit)
 assert lower>unit*4//100
 # verify exact extension formula on actual reversed fixed-weight binary words.
 cases=0
 for q in range(2,9):
  words=list(binary_words(q,q-1))
  from collections import Counter
  for n in range(1,q+1):
   cnt=Counter()
   for w in words:
    j=0
    for k,symbol in enumerate(w):
     j+=symbol==0
     if j==n:break
    prefix=w[:k+1];cnt[prefix]+=1
   assert all(n==w.count(0) and a==witness(q,n,w.count(1)) for w,a in cnt.items())
   cases+=len(cnt)
 return dict(safe_five_inventory=C,supermartingale_base=str(a),
             numerator_of_density_floor=lower,denominator_of_density_floor=unit,
             largest_j_in_sum=149,checked_binary_prefix_counts=cases,
             distinct_aligned_witnesses_at_q33=comb(65,33))
if __name__=='__main__':print(json.dumps(main(),indent=2))
