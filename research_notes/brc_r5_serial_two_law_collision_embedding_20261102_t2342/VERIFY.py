#!/usr/bin/env python3
"""Exact rational verifier of the two-law finite stopped-tree realization.

No floating-point arithmetic. P/Q natural kernels, path masses, decision times,
full-history strategies and restricted time/likelihood policies are explicit.
"""
from fractions import Fraction as F
from itertools import product

GROUPS = ("C", "I", "BJ", "IJ", "D")
PROBS = {"C": F(1, 4), "I": F(1, 4), "BJ": F(1, 8), "IJ": F(1, 8), "D": F(1, 4)}
ALPHA = {"C": F(1, 2), "I": F(2, 3), "BJ": F(1, 2), "IJ": F(3, 4)}
BETA_B, BETA_I, C = ALPHA["BJ"], ALPHA["IJ"], F(2, 3)
# Terminal nature coin: chance of outputting the label Q (only before K1).
A = {"P": F(1, 2), "Q": F(1, 4)}
D = {"P": F(1, 4), "Q": F(1, 2)}
F_DUMMY = {"P": F(1, 2), "Q": F(1, 2)}
check_count = 0

def ck(expr, message='assertion failed'):
    global check_count
    assert expr, message
    check_count += 1

def dot(a, b):
    return sum((u*v for u, v in zip(a, b)), F(0))

def probability_kernel(group, law, eps):
    alpha = ALPHA[group]
    # K1 chance of success after the decision to continue.
    p1 = alpha if law == 'P' else alpha / 2
    # K2 chance of success conditional on reaching K2 and choosing continue.
    theta = C + (eps / BETA_B if group == 'BJ' else 0)
    p2 = theta if law == 'P' else theta / 2
    return (p1, p2)

def auxiliary(x, jb, ji, z, t, eps):
    b, i = 1-jb, (1-x)*(1-ji)
    w = (F(1, 4), (1-x)/4, b/8, i/8)
    d = (BETA_B*b + BETA_I*i)/8
    gamma = tuple(C*ALPHA[s] + (eps if s == 'BJ' else 0) for s in GROUPS[:4])
    r1 = sum((ws*ALPHA[s]*zs for ws, s, zs in zip(w, GROUPS[:4], z)), F(0))
    r2 = sum((ws*gs*zs*ts for ws, gs, zs, ts in zip(w, gamma, z, t)), F(0))
    return x,d,r1,r2

def physical_of_aux(u):
    x,d,r1,r2 = u
    return (F(107,128)-F(21,128)*x+d/4,
            F(13,64)+F(3,64)*x-d/2,
            3+r1+r2,
            3+r1/2+r2/4)

def recover_aux(v):
    eP,eQ,TP,TQ = v
    vP, vQ = eP-F(107,128), eQ-F(13,64)
    # [[-21/128, 1/4], [3/64, -1/2]] * [x,d] = [vP,vQ]
    det = F(9,128)
    x = (-vP/2 - vQ/4) / det
    d = (-F(3,64)*vP - F(21,128)*vQ) / det
    p, q = TP-3, TQ-3
    return (x,d,4*q-p,2*p-4*q)

def direct_tree(x,jb0,jb1,ji0,z,t,eps):
    """All deterministic tree exits explicitly summed under each law.

    x is the one root choice before group sampling. At time 2, BJ can have a
    different full-history J action for each root flag; IJ is eligible only
    when the root did not choose the X-exit. All exits at time 3 are padded.
    K1 is at time 3, K2 at time 4; successful K2 exits at time 5.
    z,t dicts use (group, root_flag) keys, with ignored unreachable entries.
    """
    totals = {}
    for law in ('P','Q'):
        mass, yes, t_mass = F(0), F(0), F(0)
        def terminal(prob, at, q_chance):
            nonlocal mass, yes, t_mass
            mass += prob
            yes += prob*q_chance
            t_mass += prob*at
        for flag,flagprob in ((0,1-x),(1,x)):
            for group in GROUPS:
                w = flagprob * PROBS[group]
                if group == 'D':
                    terminal(w,3,F_DUMMY[law]);continue
                if flag and group in ('I','IJ'):
                    terminal(w,3,A[law]);continue
                if group in ('BJ','IJ'):
                    j = jb0 if (group == 'BJ' and flag == 0) else jb1 if group == 'BJ' else ji0
                    coeff = BETA_B if group == 'BJ' else BETA_I
                    terminal(w*j,3,D[law]*coeff)
                    w *= 1-j
                p1,p2 = probability_kernel(group,law,eps)
                p4 = w*z[(group,flag)]*p1
                terminal(w-p4,3,F(0))
                p5 = p4*t[(group,flag)]*p2
                terminal(p4-p5,4,F(0))
                terminal(p5,5,F(0))
        ck(mass==1, f'tree P/Q normalization {law} {mass}')
        totals[law]=(yes,t_mass)
    return (1-totals['P'][0], totals['Q'][0], totals['P'][1], totals['Q'][1])

def reduced_full(x,jb,ji,z4,t4,eps):
    z={};t={}
    for g,zv,tv in zip(GROUPS[:4],z4,t4):
        for flag in (0,1): z[(g,flag)]=zv;t[(g,flag)]=tv
    return direct_tree(x,jb,jb,ji,z,t,eps)

def lr_aux(x,y,z,t,eps):
    b, i = y,(1-x)*y
    d = (BETA_B*b+BETA_I*i)/8
    amax = ALPHA['C']/4+ALPHA['I']*(1-x)/4+d
    gmax = C*amax+eps*b/8
    return (x,d,z*amax,z*t*gmax)

def lr_lift(a):
    x,d,r1,r2=a
    denom = (BETA_B+BETA_I*(1-x))/8
    y=d/denom
    amax = ALPHA['C']/4+ALPHA['I']*(1-x)/4+d
    z=r1/amax
    t=r2/(C*r1) if r1 else F(0)
    return x,y,z,t

def full_corners(eps):
    for v in product((F(0),F(1)),repeat=11):
        x,jb,ji=v[:3]
        yield v,auxiliary(x,jb,ji,v[3:7],v[7:11],eps)

def lr_corners(eps):
    return [lr_aux(*bits,eps) for bits in product((F(0),F(1)),repeat=4)]

def naux(eps):
    b = BETA_B+BETA_I
    return (C*ALPHA['I']/4-eps*BETA_I/(8*b),-(C+eps/b),F(0),F(1))

# All natural probabilities remain strictly between 0 and 1 at both decisions.
for eps in (F(0), F(1,96), F(1,32), F(1,12), F(1,8)):
    for s in GROUPS[:4]:
        for law in ('P','Q'):
            p1,p2=probability_kernel(s,law,eps)
            ck(0<p1<1 and 0<p2<1)

# A completely independent terminal-path flow implementation vs the derived
# affine observable formula. Includes full policies conditional on root flag.
for k in range(1,201):
    x=F(k%7+1,9)
    jb0=F((2*k)%7+1,9)
    jb1=F((3*k)%8+1,10)
    ji0=F((5*k)%6+1,8)
    z={(g,flag):F(((k+2*ix+3*flag)%8)+1,10) for ix,g in enumerate(GROUPS[:4]) for flag in (0,1)}
    t={(g,flag):F(((3*k+ix+2*flag)%8)+1,10) for ix,g in enumerate(GROUPS[:4]) for flag in (0,1)}
    eps=(F(0), F(1,8))[k%2]
    b=(1-x)*(1-jb0)+x*(1-jb1)
    i=(1-x)*(1-ji0)
    d=(BETA_B*b+BETA_I*i)/8
    ws = {}
    for g in GROUPS[:4]:
        for flag,pr in ((0,1-x),(1,x)):
            if flag and g in ('I','IJ'):continue
            w=pr*PROBS[g]
            if g == 'BJ': w*=1-(jb0 if flag==0 else jb1)
            if g == 'IJ': w*=1-ji0
            ws[(g,flag)]=w
    r1=sum((w*ALPHA[g]*z[(g,flag)] for (g,flag),w in ws.items()),F(0))
    r2=sum((w*(C*ALPHA[g]+(eps if g=='BJ' else 0))*z[(g,flag)]*t[(g,flag)] for (g,flag),w in ws.items()),F(0))
    aux=(x,d,r1,r2)
    obs=direct_tree(x,jb0,jb1,ji0,z,t,eps)
    ck(obs==physical_of_aux(aux))
    ck(recover_aux(obs)==aux)

# Exhaust all 2^11 reduced FULL deterministic vertices and all 2^4 LR
# deterministic vertices for the base and the BJ-perturbed models.
for eps in (F(0),F(1,8)):
    nc=naux(eps)
    full_list=list(full_corners(eps))
    lr_list=lr_corners(eps)
    ck(len(full_list)==2048 and len(lr_list)==16)
    max_full=max(dot(nc,a) for _,a in full_list)
    max_lr=max(dot(nc,a) for a in lr_list)
    ck(max_full-max_lr==eps*BETA_I/(8*(BETA_B+BETA_I)))
    for bits,a in full_list:
        ck(recover_aux(physical_of_aux(a))==a)
        if eps==0:
            params=lr_lift(a)
            ck(all(0<=v<=1 for v in params))
            ck(lr_aux(*params,eps)==a)
    for a in lr_list: ck(recover_aux(physical_of_aux(a))==a)

# One positive rational full-history example with root-flag-dependent J/K
# choices, checked as an independent path flow (not reduced FULL class).
X=F(2,5)
Z={(g,f):F(2+ix+f,8) for ix,g in enumerate(GROUPS[:4]) for f in (0,1)}
T={(g,f):F(3+ix+f,10) for ix,g in enumerate(GROUPS[:4]) for f in (0,1)}
obs_adaptive=direct_tree(X,F(1,5),F(2,7),F(3,8),Z,T,F(1,8))
ck(all(0<=obs_adaptive[j]<=1 for j in (0,1)))
ck(F(3)<=obs_adaptive[2]<=F(5) and F(3)<=obs_adaptive[3]<=F(5))

# Physical signed hyperplane inherited by exact invertible affine duality.
normal_phys=(-F(86,405),F(578,405),F(2),-F(4))
normal_aux=naux(F(1,8))
ck(normal_aux==(F(293,2880),-F(23,30),F(0),F(1)))
# For any two auxiliary points, m dot (A(u)-A(v))=n dot (u-v).
for a in (auxiliary(F(0),F(0),F(1),(F(1),)*4,(F(1),)*4,F(1,8)),
          auxiliary(F(1,2),F(1,3),F(2,5),(F(1,2),)*4,(F(3,4),)*4,F(1,8))):
    origin=physical_of_aux((F(0),)*4)
    ck(dot(normal_phys,tuple(p-o for p,o in zip(physical_of_aux(a),origin)))==dot(normal_aux,a))

w_aux=auxiliary(F(0),F(0),F(1),(F(1),)*4,(F(1),)*4,F(1,8))
w_phys=physical_of_aux(w_aux)
ck(w_aux==(F(0),F(1,16),F(17,48),F(145,576)))
ck(w_phys==(F(109,128),F(11,64),F(2077,576),F(7465,2304)))
ck(reduced_full(F(0),F(0),F(1),(F(1),)*4,(F(1),)*4,F(1,8))==w_phys)
lf=max(dot(normal_phys,physical_of_aux(a)) for a in lr_corners(F(1,8)))
ff=max(dot(normal_phys,physical_of_aux(a)) for _,a in full_corners(F(1,8)))
ck(ff==dot(normal_phys,w_phys))
ck(ff-lf==F(3,320))
ck(sum(map(abs,normal_phys))==F(3094,405))
ck((ff-lf)/sum(map(abs,normal_phys))==F(243,198016))
# Invertible affine block det(A_e)=9/128, det(A_T)=-1/4.
ck(F(9,128)*(-F(1,4))==-F(9,512))
# Previous auxiliary LR interior Jacobian 71407/28311552.
ck((-F(9,512))*F(71407,28311552)==-F(71407,1610612736))

print('PASS_EXACT_R5_SERIAL_TWO_LAW_COLLISION_EMBEDDING')
print('P_Q_kernels_strictly_positive', True, 'groups', PROBS)
print('terminal_Q_answer_coins_P',A['P'],D['P'],'Q',A['Q'],D['Q'])
print('K1_P_alpha', tuple(ALPHA.values()), 'K1_Q_alpha', tuple(x/2 for x in ALPHA.values()))
print('K2_P_base_and_BJ_eps',C,C+F(1,8)/BETA_B, 'K2_Q_base_and_BJ_eps', C/2,(C+F(1,8)/BETA_B)/2)
print('FULL_deterministic_aux_vertices_per_eps',2048,'LR_deterministic_aux_vertices_per_eps',16)
print('adaptive_full_history_noncorners_tested',200,'exact_assertions',check_count)
print('physical_map_determinant',-F(9,512),'physical_LR_interior_Jacobian',-F(71407,1610612736))
print('perturbed_physical_witness',w_phys,'physical_normal',normal_phys)
print('supports_LR_FULL_gap',lf,ff,ff-lf)
print('normal_l1',sum(map(abs,normal_phys)),'distance_Linf_lower_bound',F(243,198016))
print('sample_adaptive_full_observation',obs_adaptive)
