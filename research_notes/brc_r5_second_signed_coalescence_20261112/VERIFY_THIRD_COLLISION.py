from fractions import Fraction as F
import runpy,contextlib,io
with contextlib.redirect_stdout(io.StringIO()): z=runpy.run_path(str(__import__('pathlib').Path(__file__).with_name('VERIFY_SECOND_COLLISION.py')))
x=z['x'];spectrum=z['spectrum'];count=z['count'];T0=z['T0'];epsmax=z['max_eps']
for sg in (1,-1):
 a2=sg*x/(23*(432+sg))
 # third: q=15, k=540+2*sign
 a3=sg*2*x/(23*(540+2*sg))
 assert abs(a2)<abs(a3)
 mid=(a2+a3)/2; boundary=a3; extra=a3+(a3-a2)/100
 for title,eta in [('inside-second-to-third',mid),('third-edge',boundary),('just-beyond',extra)]:
  vals,th=spectrum(eta)
  interior={v for v in vals if v<epsmax}
  expect=T0 | {(x-23*eta)/q for q in (15,12,3)}
  print('SIGN',sg,title,'ETA',eta,'NUM_INTERIOR',len(interior),'EXPECTED_EQUAL',interior==expect)
 t=(x-23*a3)/15; assert t==36*x/(540+2*sg)
 values,th=spectrum(a3);phase=sorted(values);i=phase.index(t)
 b=(phase[i-1]+t)/2;c=(t+phase[i+1])/2
 before=count(a3,b);after=count(a3,c)
 print('THIRD_EDGE',sg,'ETA',a3,'EPS',t,'MASKS',sum(q==t for q,_ in th.values()),'BEFORE',before,'AFTER',after,'DROP',before-after)
 assert before>after
 # exact neighboring two-cut attribution
 eta_inside=(999*a3+a2)/1000
 moving=(x-23*eta_inside)/15;fixed=36*x/(540+2*sg)
 vals,th=spectrum(eta_inside);phase=sorted(vals);i=phase.index(min(moving,fixed));assert phase[i+1]==max(moving,fixed)
 three=[count(eta_inside,(phase[i-1]+phase[i])/2), count(eta_inside,(phase[i]+phase[i+1])/2),count(eta_inside,(phase[i+1]+phase[i+2])/2)]
 masks=[sum(zv==p for zv,_ in th.values()) for p in (phase[i],phase[i+1])]
 print('THIRD_INSIDE_SIGN',sg,'ETA',eta_inside,'ORDER',['MOVING' if p==moving else 'FIXED' for p in (phase[i],phase[i+1])],'MASKS',masks,'WAYS',three,'DROPS',[three[0]-three[1],three[1]-three[2]])
 assert three[0]-three[2]==before-after
print('PASS_R5_THIRD_SIGNED_COALESCENCE')
