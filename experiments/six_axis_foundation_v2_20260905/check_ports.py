"""Independent formal-matrix, branch-prefix and boundary-port comparisons."""
from pathlib import Path
from fractions import Fraction as F
import json,time
from itertools import product
import sympy as s
from vendor import atlas_brc as old
from ports import schur_ports,same_labeled_ports,FormalPortSignature,specialize_ports

counts={}
def require(x,msg='exact port check failed'):
    if not x: raise AssertionError(msg)
def equal(A,B):
    require(A.shape==B.shape)
    for x in A-B:require(s.cancel(x)==0)
def bump(k,n=1):counts[k]=counts.get(k,0)+n

def unit(e):return tuple(int(j==e) for j in range(6))

def setup():
    z=s.Symbol('z');x=s.symbols('x0:6')
    h=(0,2,3,1);G=(old.IDENTITY,h,old.compose(h,h))
    edges=((0,1,old.BranchKey(F(1,2),unit(0),old.IDENTITY,1),1),
           (1,1,old.BranchKey(F(1,3),unit(1),h,1),2),
           (1,0,old.BranchKey(F(2,5),unit(2),old.IDENTITY,2),1),
           (0,0,old.BranchKey(F(1,7),unit(5),old.IDENTITY,1),1))
    T,index=old.frame_lift(2,edges,x,z,frames=G)
    labels=tuple(index)
    sig=schur_ports(T,labels,[p for p in labels if p[0]==1],z)
    return z,x,G,edges,T,index,sig


def matrix_coefficients(T,z,N):
    return [T.applyfunc(lambda q:s.expand(q).coeff(z,k)) for k in range(N+1)]


def inverse_prefix(coeff,N):
    require(coeff[0]==s.zeros(coeff[0].rows))
    R=[s.eye(coeff[0].rows)]
    for k in range(1,N+1):
        R.append(sum((coeff[j]*R[k-j] for j in range(1,k+1)),s.zeros(R[0].rows)))
    return R


def test_symbolic(z,x,G,edges,T,index,sig):
    I=[index[p] for p in index if p[0]==1]
    B=[index[p] for p in index if p[0]==0]
    A=T.extract(I,I);X=T.extract(I,B);Y=T.extract(B,I);D=T.extract(B,B)
    H=s.eye(3)-A;S=s.eye(3)-sig.effective
    # Independent block Gaussian factorization in [hidden,boundary] order.
    L=s.eye(6);L[3:6,0:3]=-Y*H.inv()
    U=s.zeros(6);U[0:3,0:3]=H;U[0:3,3:6]=-X;U[3:6,3:6]=S
    equal(L*U,(s.eye(6)-T).extract(I+B,I+B))
    require(s.cancel((s.eye(6)-T).det()-sig.hidden_determinant*S.det())==0)
    require(s.cancel(sig.hidden_determinant-(1-F(8,27)*z**3*x[0]*x[1]*x[2]))==0)
    bump('symbolic_block_factorization_entries',36)
    bump('symbolic_full_determinant_identity')
    # These 3 transpositions generate S4; full group tested separately below.
    generators=((1,0,2,3),(0,2,1,3),(0,1,3,2))
    for t in generators:
        conjugate=lambda g:old.compose(old.compose(t,g),old.inverse(t))
        Gt=tuple(conjugate(g) for g in G)
        Et=[(i,j,key.relabel(t),c) for i,j,key,c in edges]
        Tt,idxt=old.frame_lift(2,Et,x,z,frames=Gt)
        st=schur_ports(Tt,tuple(idxt),[p for p in idxt if p[0]==1],z)
        substitution={x[i]:x[j] for i,j in enumerate(old.edge_action(t))}
        transformed=T.applyfunc(lambda q:q.xreplace(substitution))
        p=[idxt[i,conjugate(g)] for i,g in index]
        equal(Tt.extract(p,p),transformed)
        bt=[st.boundary_labels.index((i,conjugate(g))) for i,g in sig.boundary_labels]
        equal(st.effective.extract(bt,bt),sig.effective.applyfunc(lambda q:q.xreplace(substitution)))
        require(s.cancel(st.hidden_determinant-sig.hidden_determinant.xreplace(substitution))==0)
        bump('symbolic_generator_schur_covariance_entries',9)
    # Complete 24-element variable/frame covariance, 36 entries per action.
    for t in old.GROUP:
        conjugate=lambda g:old.compose(old.compose(t,g),old.inverse(t))
        Tt,idxt=old.frame_lift(2,[(i,j,key.relabel(t),c) for i,j,key,c in edges],x,z,
                              frames=tuple(conjugate(g) for g in G))
        p=[idxt[i,conjugate(g)] for i,g in index]
        sub={x[i]:x[j] for i,j in enumerate(old.edge_action(t))}
        equal(Tt.extract(p,p),T.applyfunc(lambda q:q.xreplace(sub)))
        bump('all_group_transfer_covariance_entries',36)


def test_prefixes(z,x,G,edges,T,index,sig):
    N=10
    vals={x[i]:s.Rational(i+1,i+7) for i in range(6)}
    TT=T.subs(vals)
    coeff=matrix_coefficients(TT,z,N)
    direct=inverse_prefix(coeff,N)
    # Independent raw-branch dynamic program: visit state/frame, grade in
    # current global frame; do not call frame_lift or Schur inside this loop.
    labels=tuple(index)
    for start in labels:
        D=[{} for _ in range(N+1)];D[0][start]=s.Rational(1)
        for length in range(N+1):
            for (i,g),mass in list(D[length].items()):
                for source,target,key,c in edges:
                    end=length+key.length
                    if source!=i or end>N:continue
                    grade=old.rotate_axes(key.axes,g)
                    weight=c*s.Rational(key.weight.numerator,key.weight.denominator)
                    for e,power in enumerate(grade):weight*=vals[x[e]]**power
                    dest=(target,old.compose(g,key.frame))
                    D[end][dest]=D[end].get(dest,0)+mass*weight
        for length in range(N+1):
            for dest in labels:
                require(D[length].get(dest,0)==direct[length][index[start],index[dest]])
                bump('raw_branch_vs_matrix_prefix_entries')
    # Taylor coefficients of actual returned rational port transfer.
    W=s.Matrix(sig.effective).subs(vals)
    Wcoeff=[s.zeros(3) for _ in range(N+1)]
    for i,j in product(range(3),repeat=2):
        polynomial=s.series(W[i,j],z,0,N+1).removeO().expand()
        for k in range(N+1):Wcoeff[k][i,j]=polynomial.coeff(z,k)
    reduced=inverse_prefix(Wcoeff,N)
    B=[index[label] for label in sig.boundary_labels]
    for k in range(N+1):
        equal(reduced[k],direct[k].extract(B,B))
        bump('port_vs_direct_prefix_entries',9)
    # Allowed new boundary context: first frame -> second frame, one step.
    # This can mix boundary frames. It does not touch hidden states.
    CT=s.zeros(6);CW=s.zeros(3)
    CT[B[0],B[1]]=z/11;CW[0,1]=z/11
    composite=inverse_prefix(matrix_coefficients(TT+CT,z,N),N)
    W2=[q.copy() for q in Wcoeff];W2[1]+=CW/z
    reduced2=inverse_prefix(W2,N)
    for k in range(N+1):
        equal(reduced2[k],composite[k].extract(B,B))
        bump('boundary_context_prefix_entries',9)
    # A full-24-frame example is executed unchanged; no subgroup-only API.
    full,full_index=old.frame_lift(2,edges,x,z)
    require(full.shape==(48,48) and len(full_index)==48)
    bump('full_frame_lift_states',48)


def test_rejections(z,x,G,edges,T,index,sig):
    def reject(fn,*args,**kwargs):
        try:fn(*args,**kwargs)
        except (ValueError,TypeError):bump('negative_port_checks');return
        raise AssertionError('unsafe symbolic port input accepted')
    reject(schur_ports,s.eye(2),(0,1),(1,),z)
    reject(schur_ports,s.Matrix([[0,z],[z,s.sqrt(2)*z]]),(0,1),(1,),z)
    reject(schur_ports,s.Matrix([[0,0.1*z],[z,0]]),(0,1),(1,),z)
    reject(schur_ports,s.Matrix([[0,1/z],[z,0]]),(0,1),(1,),z)
    reject(schur_ports,T,tuple(index),tuple(index),z)
    reject(schur_ports,T,tuple(index),('not-a-label',),z)
    require(same_labeled_ports(sig,sig,absolute_determinant=True))
    reordered=FormalPortSignature(tuple(reversed(sig.boundary_labels)),
                   s.ImmutableMatrix(sig.effective.extract((2,1,0),(2,1,0))),sig.hidden_determinant,z)
    require(same_labeled_ports(sig,reordered,absolute_determinant=True))
    renamed=FormalPortSignature(tuple(('other',i) for i in range(3)),sig.effective,sig.hidden_determinant,z)
    require(not same_labeled_ports(sig,renamed))
    lostfactor=FormalPortSignature(sig.boundary_labels,sig.effective,s.Integer(1),z)
    require(same_labeled_ports(sig,lostfactor))
    require(not same_labeled_ports(sig,lostfactor,absolute_determinant=True))
    bump('observer_boundary_negative_controls',2)
    # The reduced W=z^2 is regular at t=0, but the source edge z/t is not.
    t=s.Symbol('t')
    guarded=schur_ports(s.Matrix([[0,z/t],[t*z,0]]),(0,1),(1,),z)
    require(s.cancel(guarded.effective[0,0]-z**2)==0)
    require(guarded.specialization_guards==(t,))
    reject(specialize_ports,guarded,{t:0})
    require(specialize_ports(guarded,{t:2}).effective[0,0]==z**2)
    require(specialize_ports(guarded,{t:s.Rational(1,2)}).effective[0,0]==z**2)
    reject(specialize_ports,guarded,{z:1})
    reject(specialize_ports,guarded,{t:0.5})
    dropped=FormalPortSignature(guarded.boundary_labels,guarded.effective,guarded.hidden_determinant,z)
    require(not same_labeled_ports(guarded,dropped))
    bump('source_pole_guard_controls',4)


def main():
    start=time.time();args=setup()
    for fn in (test_symbolic,test_prefixes,test_rejections):
        fn(*args);print(fn.__name__,'PASS',flush=True)
    out={'status':'PASS_EXACT_SELF_CHECKS_NOT_REPOSITORY_CI',
         'counts':counts,'seconds':round(time.time()-start,3),
         'hidden_determinant':str(args[-1].hidden_determinant),
         'specialization_guard':'Rational parameter denominators must remain nonzero on specialization; formal identities are over Q(parameters)((z)).'}
    Path(__file__).with_name('verification_ports.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
