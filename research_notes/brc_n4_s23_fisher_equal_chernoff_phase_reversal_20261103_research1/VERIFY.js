function runVerification(){
 const gcd=(a,b)=>{while(b){const r=a%b;a=b;b=r}return a<0n?-a:a};
 const F=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d};const g=gcd(n<0n?-n:n,d);return [n/g,d/g]};
 const plus=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const sub=(a,b)=>plus(a,[-b[0],b[1]]);
 const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
 const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
 const pow=(a,n)=>F(a[0]**BigInt(n),a[1]**BigInt(n));
 const eql=(a,b)=>a[0]===b[0]&&a[1]===b[1];
 const one=F(1),two=F(2),nine=F(9),forty=F(40),four=F(4);
 const D4=s=>div(mul(F(-2),mul(s,mul(sub(one,s),plus(sub(mul(nine,pow(s,2)),mul(forty,s)),four)))),mul(nine,pow(sub(two,s),3)));
 const v16=D4(F(1,16));const v4=D4(F(1,4));
 if(!eql(v16,F(-655,238328))||!eql(v4,F(29,686)))throw Error("quartic exact coefficient mismatch");
 function floorRootScaled(a,n,Q){
  let lo=0n,hi=Q*512n;const goal=a*(Q**n);
  while(lo+1n<hi){let m=(lo+hi)/2n;if(m**n<=goal)lo=m;else hi=m}
  if(!(lo**n<=goal&&(lo+1n)**n>goal))throw Error("root interval invalid");
  return lo
 }
 const Q=10n**17n,n=125n,k=63n;
 const r1=floorRootScaled(11n**k*10n**(n-k),n,Q);
 const r2=floorRootScaled(325n**k*326n**(n-k),n,Q);
 let rt=0n;const goal=110n*Q*Q;let lo=0n,hi=11n*Q;
 while(lo+1n<hi){let m=(lo+hi)/2n;if(m*m<=goal)lo=m;else hi=m}rt=lo;
 if(!(rt*rt<=goal&&(rt+1n)*(rt+1n)>goal))throw Error("sqrt interval invalid");
 const NB=r1+r2+2n,NT=315n*Q+2n*rt,den=336n*Q;
 const left=NB**31n,right=NT**16n*den**15n;
 if(!(left<right))throw Error("finite lawful s=1/16 h=1/42 certificate failed");
 return ["PASS_BRC_S23_CHERNOFF_FISHER_EQUALITY_REVERSAL_20261103",
         "quartic_D4_s_1_16="+v16.join("/"),"quartic_D4_s_1_4="+v4.join("/"),
         "root_floor_11_63_10_62="+r1,"root_floor_325_63_326_62="+r2,
         "sqrt110_scaled_floor="+rt,
         "finite_rational_comparison_ZB_upper_pow31_lt_ZT_lower_pow16=true",
         "exact_root_bound_checks=3","exact_sign_checks=2","arithmetic=BigInt_integer_and_rational",
         "s=1/16 h=1/42 beta_E=3/4 t=63/125 cost_T=31/16 cost_B=1"].join("\n")
}
console.log(runVerification());
