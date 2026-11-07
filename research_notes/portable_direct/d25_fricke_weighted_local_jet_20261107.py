"""Symbolic exact D25 two-legged Fricke weighted jet gauge at t=+-6sqrt(2)."""
import sympy as s
t=s.symbols("t");r=s.sqrt(2)
z=108*t*t*(t+9)*(t+8)**2/(t+12)**6
w=256*t**3*(t+8)*(t+9)**3/(t*t+36*t+216)**4
dz=s.diff(z,t);dw=s.diff(w,t)
logg=(s.Rational(4,3)*dz+s.diff(dz,t)/dz+s.Rational(99,16)*dw-s.diff(dw,t)/dw)/2
for sign in (1,-1):
    u=sign*6*r
    expected={"z":s.Rational(1,2),"w":s.Rational(1,9),
      "dz":-1+sign*3*r/4,"dw":s.Rational(4,9)-sign*8*r/27,
      "J":sign*s.Rational(27,16)*r,
      "zdd_zd":-s.Rational(2,3)+sign*5*r/12,
      "wdd_wd":s.Rational(13,4)-sign*9*r/4,
      "logg":-s.Rational(5,4)+sign*11*r/12}
    actual={"z":z,"w":w,"dz":dz,"dw":dw,
      "J":dz/dw,"zdd_zd":s.diff(dz,t)/dz,
      "wdd_wd":s.diff(dw,t)/dw,"logg":logg}
    for name in actual:
        assert s.simplify(actual[name].subs(t,u)-expected[name])==0,(sign,name)
ellp=-s.Rational(5,4)+11*r/12
ellm=-s.Rational(5,4)-11*r/12
assert s.simplify(ellp+ellm+s.Rational(5,2))==0
assert s.simplify(ellp*ellm+s.Rational(17,144))==0
print("PASS: exact two signed Fricke local weighted two-jets; trace -5/2; norm -17/144")
