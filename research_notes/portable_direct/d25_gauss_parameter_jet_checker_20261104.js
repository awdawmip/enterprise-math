// D25 independent exact modular checker: p-adic Gauss parameter jets.
// JavaScript BigInt; no floating-point arithmetic.
function mod(x,n){x%=n;return x<0n?x+n:x}
function inv(x,n){x=mod(x,n);let [a,b,u,v]=[x,n,1n,0n];while(b){const q=a/b;[a,b]=[b,a-q*b];[u,v]=[v,u-q*v]}if(a!==1n)throw Error("non-unit");return mod(u,n)}
function primes(N){const a=[];for(let p=5;p<=N;p++){let y=true;for(let d=2;d*d<=p;d++)if(p%d===0){y=false;break}if(y)a.push(p)}return a}
function check(pNum){
 const p=BigInt(pNum),q=p*p,inv8=inv(8n,p),inv9=inv(9n,p),iv9=inv(9n,q);
 const a=Number(mod(-inv8,p)),b=Number(mod(-3n*inv8,p)),m=(8*a+1)/pNum,n=(8*b+3)/pNum,L=Math.min(a,b),R=Math.max(a,b),rootCoefficient=L===a?m:n;
 const invs=Array(pNum).fill(0n),invsP=Array(pNum).fill(0n);for(let i=1;i<pNum;i++){invs[i]=inv(BigInt(i),q);invsP[i]=mod(invs[i],p)}
 let F=1n,G=1n,v=1n;
 const iv576=inv(576n,q);
 for(let i=1;i<pNum;i++){v=mod(v*BigInt(8*i-7)*BigInt(8*i-5)*iv576*invs[i]*invs[i],q);F=mod(F+v,q);G=mod(G+BigInt(1+16*i)*v,q)}
 let coef=1n,B=0n,BG=0n,C=0n,CG=0n,ha=0n,hb=0n;
 for(let i=0;i<=L;i++){
  if(i){coef=mod(coef*BigInt(a-i+1)*BigInt(b-i+1)*iv9*invs[i]*invs[i],q);ha=mod(ha+invsP[a-i+1],p);hb=mod(hb+invsP[b-i+1],p)}
  const j=mod(-inv8*(BigInt(m)*ha+BigInt(n)*hb)*mod(coef,p),p);
  B=mod(B+coef,q);BG=mod(BG+BigInt(1+16*i)*coef,q);
  C=mod(C+j,p);CG=mod(CG+BigInt(1+16*i)*j,p);
 }
 const fac=Array(R+1).fill(1n),ifac=Array(R+1).fill(1n);for(let i=1;i<=R;i++)fac[i]=mod(fac[i-1]*BigInt(i),p);
 ifac[R]=inv(fac[R],p);for(let i=R;i>0;i--)ifac[i-1]=mod(ifac[i]*BigInt(i),p);
 let power=1n;for(let i=0;i<L+1;i++)power=mod(power*inv9,p);
 let T=0n,TG=0n;
 for(let i=L+1;i<=R;i++){
  const sign=(L+i)%2?-1n:1n;
  const term=mod(BigInt(rootCoefficient)*inv8*sign*fac[L]*fac[i-L-1]*fac[R]*ifac[R-i]*ifac[i]*ifac[i]*power,p);
  T=mod(T+term,p);TG=mod(TG+BigInt(1+16*i)*term,p);power=mod(power*inv9,p)
 }
 const pred=mod(B+p*mod(C+T,p),q),predG=mod(BG+p*mod(CG+TG,p),q);
 if(pred!==F||predG!==G)throw Error("jet mismatch at p="+pNum);
 return {p:pNum,a,b,m,n,L,R,P:Number(B),J_low:Number(C),J_mid:Number(T),F:Number(F),Q:Number(BG),J_G_low:Number(CG),J_G_mid:Number(TG),G:Number(G)};
}
function run(){
 const records=primes(2000).filter(p=>p%8===5||p%8===7).map(check);
 const counts=records.reduce((o,x)=>(o[x.p%24]=(o[x.p%24]||0)+1,o),{});
 const factor_mismatches=records.filter(x=>(x.p%24===13||x.p%24===23)?x.F!==0:x.G!==0);
 if(factor_mismatches.length)throw Error("finite conjecture mismatch");
 return {checked:records.length,class_counts:counts,factor_mismatches:factor_mismatches.length,samples:records.filter(x=>[5,7,13,23,29,37,53,71,373].includes(x.p))};
}

const result=run();
console.log(JSON.stringify(result,null,2));
