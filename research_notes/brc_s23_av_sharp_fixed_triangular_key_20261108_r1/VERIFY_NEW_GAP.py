#!/usr/bin/env python3
"""Exact check of new H=N+510 threshold gap and its first prefix witness."""
from VERIFY_TRIANGULAR_KEY import P,D,N,LO,HI,Q,count_below
from VERIFY_LEX_ORDER import fibers,rank_lex,select_lex
u=(79,431)
w=(D,P)
H=N+510
q=(u[0]+w[0],u[1]+w[1])
prefix=(u[0]+2*w[0],u[1]+2*w[1]) # (ell,k)
# r=ln(7)/ln(10/7); eps=79r-431; eta=P-rD.
assert (79+D)*LO>(431+P)*Q # eps>eta, so T(q)>0
assert (2*P+431)*Q>(2*D+79)*HI # eps<2eta, so witness E>0
assert (158+3*D)*LO>(862+3*P)*Q # 2eps>3eta, so E<eps-eta
# In T_H key 0 fiber is [w,0]; key 1 fiber is [q,u].
assert fibers(H,0)==[w,(0,0)]
assert fibers(H,1)==[q,u]
assert rank_lex(H,*q)==rank_lex(H,0,0)+1
assert select_lex(H,rank_lex(H,0,0)+1)[1]==q
assert sum(q)==H
assert sum(prefix)==2*N+510
# Exact minimality: for prefix (ell,k)=A*u+B*w, E=B*eta-A*eps.
# E in (0,eps-eta) implies B>=1 and A>=0; B=1 impossible;
# B=2 forces A=1, B>=3 forces length >=3N>2N+510.
assert 3*N>sum(prefix)
print('NEW_THRESHOLD_GAP: H',H,'left=(0,0)','right',q,'rank',rank_lex(H,0,0))
print('SHARP_PREFIX_WITNESS: (ell,k)',prefix,'minimum_length',sum(prefix))
print('PROOF_CERT: 0<eta<eps<2eta and 2eps>3eta, first cell adjacency PASS')
print('PASS_S23_AV_FIRST_NEW_W_PLUS_U_GAP_MINIMAL_PREFIX')
