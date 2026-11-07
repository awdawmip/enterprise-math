#!/usr/bin/env python3
"""Three exact nonnegative 7x7 Q/P transports for negative-residual FULL corners."""
from VERIFY import F,R,m,t,check

def f(s): return F(str(s))

cases = [
 ("U_ONLY", (f('1'),f('1'),f('1'),f('27/80'),f('9/40'),f('0'),f('0')),
  (f('1'),f('1'),f('9/10'),f('5/16'),f('3/10'),f('0'),f('12/121')),
  {0:{0:'20443/72000',5:'7661/4356000'},1:{3:'23561/1089000',5:'9211/4356000'},
   3:{3:'189253/871200'},4:{3:'23561/544500',5:'916/136125'},
   5:{5:'249/800'},6:{5:'68161/4356000',6:'6943/72000'}}),
 ("W_ONLY",(f('1'),f('1'),f('1'),f('0'),f('9/40'),f('27/80'),f('0')),
  (f('1'),f('9/10'),f('1'),f('0'),f('3/10'),f('5/16'),f('3/35')),
  {0:{0:'6943/72000',1:'13381/756000'},1:{1:'61/200'},
   2:{1:'5729/483000',3:'18421/483000'},3:{3:'6823/30240'},
   5:{3:'7/400'},6:{1:'51103/17388000',3:'379/434700',6:'20443/72000'}}),
 ("BOTH",(f('1'),f('1'),f('1'),f('27/80'),f('9/40'),f('27/80'),f('0')),
  (f('1'),f('19/20'),f('19/20'),f('513/1600'),f('247/800'),f('513/1600'),f('19/200')),
  {0:{0:'10343/36000',3:'7517/720000'},2:{3:'1/40'},3:{3:'42541/120000'},
   4:{3:'1/40'},6:{3:'7517/720000',6:'10343/36000'}})
]

for label,x,y,sparse in cases:
 J=[[F(0) for j in range(7)] for i in range(7)]
 for i,row in sparse.items():
  for j,value in row.items(): J[i][j]=f(value)
 assert 9*x[2]*x[6]-4*x[1]*(x[4]-x[6]) < 0
 check(x,y,J)
 print('PASS_EXACT_SINGLE_SEEDLESS_CORNER_TRANSPORT',label,
       'TP',t(x)[0],'TQ',t(x)[1],
       'joint_nonzero',sum(v>0 for row in J for v in row))
print('PASS_THREE_REMAINING_FULL_NEGATIVE_RESIDUAL_CORNERS')
