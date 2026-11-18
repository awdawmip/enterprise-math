// R749SUE exact-integer certificate; standalone: node R749SUE_UNIMODULAR_LATE_TAIL_CERT.js

// Declared finite test domain M=1..32; no float approximations to the real BRC data are used.

'use strict';

function gcd(x,y){while(y){const t=x%y;x=y;y=t}return x}

function phi(n){let r=n;for(let p=2;p*p<=n;p++)if(n%p===0){while(n%p===0)n/=p;r-=r/p}if(n>1)r-=r/n;return r}

function base(m){return (2*m+1)*(2*m*m+2*m+1)}

function plateau(m){let e=m*m;for(let h=2;h<=m;h++)e+=2*phi(h)*(Math.floor(m/h)**2);return base(m)+(m**4-e)/2}

function gridCount(m,k){let v=base(m);for(let u=1;u<=m;u++)for(let w=1;w<=m;w++)for(let a=1;a<=m;a++)v+=Math.max(0,m-Math.floor(k*u*w/(a*(k-Math.max(u,w)))));return v}

function detScan(m,k){let total=0,miss=0;for(let a=1;a<=m;a++)for(let u=1;u<=m;u++){if(gcd(a,u)!==1)continue;for(let d=1;d<=m;d++){let q=a*d-1;if(q<=0||q%u!==0)continue;let v=q/u;if(v<1||v>m)continue;total++;if(k<=Math.max(u,v)*a*d)miss++}}return {total,miss}}

function verify(){let cases=0,recurrence=0,terminal=0,samples=[];let h=0;for(let m=1;m<=32;m++){h+=m===1?0:4*phi(m)-2;const check=detScan(m,Math.floor(m**3/2)+1);if(check.total!==h)throw Error(`Totient H_${m} mismatch`);recurrence++;const sat=m===1?2:m===2?5:m*(m-1)**2+1;const pool=[Math.floor(m**3/2)+1,Math.floor((Math.floor(m**3/2)+1+sat)/2),sat-1,sat,sat+5].filter(k=>k>m);for(const k of [...new Set(pool)]){const missing=plateau(m)-gridCount(m,k),det=detScan(m,k).miss;if(k>m**3/2&&missing!==det)throw Error(`late-count mismatch M=${m},K=${k}`);cases++;if(m>=2&&k===sat-1){if(missing!==2)throw Error(`terminal jump mismatch M=${m}`);terminal++}if([4,8,10,16,24,32].includes(m)&&[Math.floor(m**3/2)+1,sat-1,sat].includes(k))samples.push({M:m,K:k,plateau:plateau(m),missing,unit_determinant_total:check.total})}}return {status:"PASS",checked_M:"1..32",totient_identity_cases:recurrence,grid_vs_det_cases:cases,terminal_step_cases:terminal,samples}}

console.log(JSON.stringify(verify(),null,2));
