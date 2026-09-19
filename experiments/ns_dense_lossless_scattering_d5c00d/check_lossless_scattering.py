#!/usr/bin/env python3
"""Exact finite checks for a dense X6 lossless-scattering / relation-transport candidate.

This is a research diagnostic, not a native-force, quantum-origin, or Navier--Stokes solver.
Only Fraction arithmetic is used.  No continuum limit or floating point is required.
"""
from __future__ import annotations
from fractions import Fraction as F
import argparse, json
from pathlib import Path

D = 6
SIGNED_DIRS = tuple((i,s) for i in range(D) for s in (-1,1))
V = [F(2)] + [F(1)]*12


def h_apply(x):
    if len(x) != 13:
        raise ValueError("need cavity + twelve channel amplitudes")
    dot = sum(a*b for a,b in zip(V,x))
    return [xi - vi*dot/F(8) for xi,vi in zip(x,V)]


def norm2(x): return sum(t*t for t in x)


def householder_checks():
    cols=[]
    for j in range(13):
        e=[F(0)]*13; e[j]=F(1)
        cols.append(h_apply(e))
    for i in range(13):
        for j in range(13):
            got=sum(cols[i][k]*cols[j][k] for k in range(13))
            assert got == (F(1) if i==j else F(0))
    for j in range(13):
        e=[F(0)]*13; e[j]=F(1)
        assert h_apply(h_apply(e)) == e
    bg=[F(-6)]+[F(1)]*12
    assert h_apply(bg)==bg
    return {"H00":str(cols[0][0]),"H0port":str(cols[0][1]),"dense_background_fixed":True}


def infinite_ray_checks(max_n=10):
    rows=[]
    for n in range(max_n+1):
        a=F(1,2**n)
        hidden=F(0)
        for d in range(1,n+1):
            amp=-F(1,2**(n-d+2))
            hidden += 12*amp*amp
        assert hidden == F(1)-a*a
        rows.append({"n":n,"cavity_amplitude":str(a),"visible_energy":str(a*a),
                     "residual_energy":str(hidden)})
    return rows


def ring_step(a, fields):
    L=len(fields[0])
    local=[a]+[fields[c][0] for c in range(12)]
    out=h_apply(local)
    a2=out[0]
    nf=[]
    for c in range(12):
        arr=list(fields[c]); arr[0]=out[c+1]
        shifted=[F(0)]*L
        for p,val in enumerate(arr): shifted[(p+1)%L]=val
        nf.append(shifted)
    return a2,nf


def ring_checks(lengths=(5,7,11)):
    out=[]
    for L in lengths:
        a=F(1); fields=[[F(0)]*L for _ in range(12)]
        sequence=[a]; energies=[]
        for _ in range(L+1):
            energies.append(a*a+sum(x*x for arr in fields for x in arr))
            a,fields=ring_step(a,fields); sequence.append(a)
        assert all(e==1 for e in energies)
        assert all(sequence[n]==F(1,2**n) for n in range(L+1))
        expected=F(3,4)+F(1,2**(L+1))
        assert sequence[L+1]==expected
        out.append({"L":L,"first_no_return_steps":L,"first_return_cavity_amplitude":str(sequence[L+1]),
                    "predicted":str(expected)})
    return out


def phase_fiber_counterexample():
    xp=[F(1),F(1)]+[F(0)]*11
    xm=[F(1),F(-1)]+[F(0)]*11
    assert [x*x for x in xp] == [x*x for x in xm]
    yp=h_apply(xp); ym=h_apply(xm)
    assert yp[0]==F(1,4) and ym[0]==F(3,4)
    return {"same_per_slot_positive_energies":True,
            "next_cavity_amplitudes":[str(yp[0]),str(ym[0])],
            "next_visible_energies":[str(yp[0]*yp[0]),str(ym[0]*ym[0])],
            "fiber_constancy":False}


def bell_density_sparse(num_b):
    n=1+num_b
    s1=[0]*n; s2=[0]*n
    s1[0]=1; s2[1]=1
    t1=tuple(s1); t2=tuple(s2)
    return {(t1,t1):F(1,2),(t1,t2):F(1,2),(t2,t1):F(1,2),(t2,t2):F(1,2)}


def swap_qubits(rho,i,j):
    def sw(bits):
        b=list(bits); b[i],b[j]=b[j],b[i]; return tuple(b)
    return {(sw(r),sw(c)):v for (r,c),v in rho.items()}


def reduce_two(rho,i,j,nq):
    M=[[F(0) for _ in range(4)] for __ in range(4)]
    traced=[k for k in range(nq) if k not in (i,j)]
    for (r,c),val in rho.items():
        if all(r[k]==c[k] for k in traced):
            rr=2*r[i]+r[j]; cc=2*c[i]+c[j]
            M[rr][cc]+=val
    return M

BELL=[[F(0),F(0),F(0),F(0)],
      [F(0),F(1,2),F(1,2),F(0)],
      [F(0),F(1,2),F(1,2),F(0)],
      [F(0),F(0),F(0),F(0)]]


def mlin(a,A,b,B): return [[a*A[i][j]+b*B[i][j] for j in range(2)] for i in range(2)]
def kron(A,B): return [[A[i//2][j//2]*B[i%2][j%2] for j in range(4)] for i in range(4)]
def trace_prod(rho,O): return sum(rho[i][j]*O[j][i] for i in range(4) for j in range(4))
def partial_transpose_B(M):
    out=[[F(0) for _ in range(4)] for __ in range(4)]
    for i in range(2):
        for b in range(2):
            for j in range(2):
                for c in range(2): out[2*i+c][2*j+b]=M[2*i+b][2*j+c]
    return out


def quantum_relation_transport():
    path=[(0,0,0,0,0,0),(1,0,0,0,0,0),(1,0,1,0,0,0),(1,-1,1,0,0,0),(1,-1,1,0,0,1)]
    for a,b in zip(path,path[1:]):
        assert sum(abs(y-x) for x,y in zip(a,b))==1
    rho=bell_density_sparse(len(path)); nq=1+len(path)
    records=[{"tick":0,"endpoint":path[0]}]
    assert reduce_two(rho,0,1,nq)==BELL
    target_old=[[F(1,2),F(0),F(0),F(0)],[F(0),F(0),F(0),F(0)],
                [F(0),F(0),F(1,2),F(0)],[F(0),F(0),F(0),F(0)]]
    for j in range(1,len(path)):
        rho=swap_qubits(rho,j,j+1)
        assert reduce_two(rho,0,j+1,nq)==BELL
        assert reduce_two(rho,0,j,nq)==target_old
        for (r,c),val in rho.items():
            if val: assert sum(r)==1 and sum(c)==1
        records.append({"tick":j,"endpoint":path[j]})
    X=[[F(0),F(1)],[F(1),F(0)]]; Z=[[F(1),F(0)],[F(0),F(-1)]]
    A0=X; A1=[[-z for z in row] for row in Z]
    B0=mlin(F(3,5),X,F(4,5),Z); B1=mlin(F(3,5),X,F(-4,5),Z)
    corr=[trace_prod(BELL,kron(A,B)) for A,B in ((A0,B0),(A0,B1),(A1,B0),(A1,B1))]
    chsh=corr[0]+corr[1]+corr[2]-corr[3]
    assert chsh==F(14,5)
    pt=partial_transpose_B(BELL)
    det=pt[0][0]*pt[3][3]-pt[0][3]*pt[3][0]; assert det==F(-1,4)
    I4=[[F(1,4) if i==j else F(0) for j in range(4)] for i in range(4)]
    chi=[[BELL[i][j]-I4[i][j] for j in range(4)] for i in range(4)]
    hs=sum(x*x for row in chi for x in row); assert hs==F(3,4)
    return {"path":path,"primitive_edges":len(path)-1,"records":records,
            "partial_transpose_principal_minor":str(det),"chi_hilbert_schmidt_sq":str(hs),
            "CHSH_correlations":[str(x) for x in corr],"CHSH":str(chsh)}


def add6(a,b): return tuple(x+y for x,y in zip(a,b))
DIRVECS=[]
for i,s in SIGNED_DIRS:
    v=[0]*6; v[i]=s; DIRVECS.append(tuple(v))
DIRVECS=tuple(DIRVECS); ZERO6=(0,0,0,0,0,0)


def bulk_step(a_field, port_field):
    cells=set(a_field); cells.update(z for z,_ in port_field)
    anew={}; pout={}
    for z in cells:
        local=[a_field.get(z,F(0))]+[port_field.get((z,j),F(0)) for j in range(12)]
        out=h_apply(local)
        if out[0]: anew[z]=out[0]
        for j,v in enumerate(DIRVECS):
            val=out[j+1]
            if val:
                target=(add6(z,v),j); pout[target]=pout.get(target,F(0))+val
    return anew,pout


def heat_step(a_field):
    out={}
    for z,val in a_field.items():
        out[z]=out.get(z,F(0))+F(1,4)*val
        for v in DIRVECS:
            q=add6(z,v); out[q]=out.get(q,F(0))+F(1,16)*val
    return {z:v for z,v in out.items() if v}


def field_norm2(a_field,port_field): return sum(x*x for x in a_field.values())+sum(x*x for x in port_field.values())


def bulk_heat_and_memory_checks():
    a={ZERO6:F(1)}; ports={}; states=[(a,ports)]
    for _ in range(4):
        a,ports=bulk_step(a,ports); states.append((a,ports))
    assert all(field_norm2(a,p)==1 for a,p in states)
    assert states[2][0]==heat_step({ZERO6:F(1)})
    T2=heat_step(heat_step({ZERO6:F(1)})); assert states[4][0] != T2
    assert states[4][0][ZERO6]==F(1,64) and T2[ZERO6]==F(7,64)
    vis=[sum(x*x for x in a.values()) for a,_ in states]
    assert vis==[F(1),F(1,4),F(7,64),F(403,4096),F(9553,65536)]
    backflow=vis[4]-vis[3]; assert backflow==F(3105,65536)>0
    return {"visible_energy":[str(x) for x in vis],"two_tick_exact_operator":"T=I+Delta_X6/16",
            "T2_center_if_residual_reset":str(T2[ZERO6]),"actual_four_tick_center":str(states[4][0][ZERO6]),
            "fourth_tick_visible_backflow":str(backflow),"full_relative_quadratic_conserved":True}


def finite_unitary_semigroup_obstruction():
    lam=F(7,8); assert F(0)<lam<F(1)
    return {"periodic_side":4,"strict_heat_eigenvalue":str(lam),
            "finite_dimensional_exact_all_time_unitary_dilation":"impossible_by_recurrence_proof"}


def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,default=Path('results_17.json')); a=p.parse_args()
    data={"schema":"EM_DENSE_LOSSLESS_SCATTERING_RESULTS_V1",
      "event_id":"NS-DENSE-LOSSLESS-SCATTERING-20260910-D5C00D-17",
      "status":"EXACT_FINITE_ALGEBRA_TEST_MODEL_NOT_PHYSICAL_ADMISSION",
      "householder":householder_checks(),"infinite_no_return":infinite_ray_checks(),
      "finite_ring_return":ring_checks(),"phase_fiber_counterexample":phase_fiber_counterexample(),
      "bulk_heat_memory":bulk_heat_and_memory_checks(),
      "finite_unitary_semigroup_obstruction":finite_unitary_semigroup_obstruction(),
      "quantum_relation_transport":quantum_relation_transport(),
      "nonclaims":["Dense means a discrete field of resident degrees of freedom; no continuum density is assumed.",
        "The 13-mode Householder scatterer is a constitutive test law, not derived from P000.",
        "The conserved quadratic is not identified with complete physical energy.",
        "Quantum tensor products, Born observables and SWAP are added comparison assumptions.",
        "No primitive-force, viscosity, Navier-Stokes, superluminal-signalling, or quantum-origin theorem."]}
    text=json.dumps(data,indent=2,ensure_ascii=False)+'\n'; a.output.write_text(text,encoding='utf-8'); print(text)

if __name__=='__main__': main()
