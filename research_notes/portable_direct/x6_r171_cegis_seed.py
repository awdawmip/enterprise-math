# First exact depth-six sample tree, with deterministic reconstruction of the next sample.
# The first tree is known to fail on the full enlarged arrangement. Do not claim global depth six.
# Run x6_r171_exact_arrangement.py first in the same directory.
import numpy as np, random, collections
z=np.load('r171_states.npz'); P=z['P']; L=z['L']; labs=z['labs']; Q=np.concatenate([L,-L],axis=0)
tree=[140,[35,[539,[497,[32,[99,["o",[4,693]],["o",[12,693]]],[98,["o",[6,693]],["o",[6,561]]]],[4,[268,["o",[4,692]],["o",[4,693]]],[9,["o",[2,132]],["o",[4,132]]]]],[10,[4,[11,["o",[5,132]],["o",[4,132]]],["o",[2,132]]],[509,[460,["o",[4,676]],["o",[4,164]]],[8,["o",[5,132]],["o",[4,132]]]]]],[89,[327,[5,[576,["o",[2,693]],["o",[2,132]]],[17,["o",[7,693]],["o",[12,693]]]],[9,[56,["o",[2,695]],["o",[2,951]]],["o",[4,693]]]],[551,[5,[119,["o",[12,689]],["o",[1,561]]],[17,["o",[12,561]],["o",[14,561]]]],[244,[99,["o",[12,951]],["o",[12,693]]],[32,["o",[12,561]],["o",[6,561]]]]]]],[251,[225,[90,[32,[171,["o",[11,561]],["o",[14,561]]],[143,["o",[6,561]],["o",[3,561]]]],[359,[660,["o",[1,561]],["o",[12,561]]],[17,["o",[7,561]],["o",[3,561]]]]],[252,[185,["o",[3,561]],[205,["o",[3,569]],["o",[3,633]]]],[419,[352,["o",[2,633]],["o",[8,633]]],["o",[8,72]]]]],[370,[265,[73,[184,["o",[10,49]],["o",[10,121]]],[306,["o",[3,633]],["o",[13,633]]]],[293,["o",[13,121]],[349,["o",[13,89]],["o",[13,72]]]]],[374,[352,[870,["o",[0,72]],["o",[13,72]]],["o",[8,72]]],[32,["o",[13,64]],[393,["o",[9,72]],["o",[9,64]]]]]]]]
rng=random.Random(171); groups=collections.defaultdict(list)
for i,(mask,near) in enumerate(labs):groups[(int(mask),int(near))].append(i)
S={i for g in groups.values() for i in rng.sample(g,min(4,len(g)))}
assert len(S)==505
bad=[]; leaves=0
def visit(n,I):
 global leaves
 if n[0]=='o':
  leaves+=1;a,b=n[1];ll=labs[I];fail=I[((ll[:,0]>>a&1)==0)|(ll[:,1]!=b)]
  if len(fail):bad.append(fail)
 else:
  a=P[I]@Q[n[0]]>0;visit(n[1],I[a]);visit(n[2],I[~a])
visit(tree,np.arange(len(P)))
assert leaves==57 and sum(map(len,bad))==18142 and len(bad)==41
assert not S.intersection(int(i) for b in bad for i in b)
for b in bad:
 gs=collections.defaultdict(list)
 for i in b:gs[tuple(labs[i])].append(int(i))
 for g in gs.values():S.update(rng.sample(g,min(3,len(g))))
assert len(S)==799
np.save('r171_refined_sample.npy',P[sorted(S)])
print('R171 first tree replay; 799-state refined sample saved; full-domain depth unresolved')
