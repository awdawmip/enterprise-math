function check(){
 function mod(a,p){let r=a%p;return r<0?r+p:r}
 function pow(a,n,p){let v=1,b=mod(a,p);for(;n;n=Math.floor(n/2),b=b*b%p)if(n%2)v=v*b%p;return v}
 const N=10000,prime=new Uint8Array(N).fill(1);prime[0]=prime[1]=0;
 for(let d=2;d*d<N;d++)if(prime[d])for(let q=d*d;q<N;q+=d)prime[q]=0;
 let checked=0,powers=0;
 for(let p=11;p<N;p+=8)if(prime[p]){
  const m=(p-3)/8,inv=new Int32Array(3*m+2);inv[1]=1;
  for(let i=2;i<inv.length;i++)inv[i]=p-Math.floor(p/i)*inv[p%i]%p;
  let D=1;
  for(let r=1;r<=m;r++)D=D*(2*m+1+r)%p*inv[r]%p;
  let a=1;const b=[];
  for(let r=0;r<=m;r++){
   b.push((16*r+5)*a%p);
   if(r<m)a=a*(m-r)%p*(m-r)%p*inv[r+1]%p*inv[2*m+2+r]%p;
  }
  for(let n=0;n<=m+1;n++){
   const bp=n<m?b[n+1]:0,bn=n<=m?b[n]:0,bprev=n>0&&n-1<=m?b[n-1]:0;
   const q=mod(80*(n+1)*(4*n+5)*bp-(384*n*n+512*n+189)*bn+(8*n-5)**2*bprev,p);
   if(q)throw Error("GH66 coefficient failure p="+p+" n="+n+" q="+q);
  }
  let v=5,previous=0;
  for(let n=0;n<m;n++){
   const rhs=mod((384*n*n+512*n+189)*v-(8*n-5)**2*previous,p);
   const den=mod(80*(n+1)*(4*n+5),p);
   const nxt=rhs*pow(den,p-2,p)%p;
   if(nxt!==b[n+1])throw Error("G-only reconstruction failure "+p);
   previous=v;v=nxt;
  }
  if(p<800)for(const z of [2,5,9]){
   let value=0,fieldsum=0;
   for(let r=0;r<=m;r++)value=(value+b[r]*pow(z,r,p))%p;
   for(let x=1;x<p;x++)
    fieldsum=mod(fieldsum+
      pow(x,p-1-m,p)*pow(1+x,3*m+1,p)%p*
      pow(1+z*x,m-1,p)%p*(5-z*x),p);
   if(mod(D*value+fieldsum,p))throw Error("GH65 power sum failure p="+p+" z="+z);
   powers++;
  }
  checked++;
 }
 return {primes:checked,power_sum_charts:powers,pass:true};
}
const result=check();
console.log(result);
