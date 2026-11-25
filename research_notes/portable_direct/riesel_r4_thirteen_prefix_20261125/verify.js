const c=(v,m)=>{if(!v)throw Error(m)};
const phi=new Map();
function C(d){if(!phi.has(d)){let n=(1n<<BigInt(d))-1n;for(let j=1;j<d;j++)if(d%j===0)n/=C(j);phi.set(d,n);}return phi.get(d);}
function prime(p){for(let j=2n;j*j<=p;j++)if(p%j===0n)return false;return p>=2n;}
const inv={11:[23,89],13:[8191],22:[683],26:[2731],33:[599479],44:[397,2113],52:[53,157,1613],66:[67,20857],80:[4278255361],132:[312709,4327489],240:[394783681,46908728641]};
for(const [d,p] of Object.entries(inv)){const q=p.map(BigInt);c(q.every(prime)&&q.reduce((a,b)=>a*b,1n)===C(+d),'factor '+d);}
const count=(...d)=>d.flatMap(x=>inv[x]).length;
c(count(11,22,44)===5&&count(13,26,52)===5&&count(11,22,33,44,66,132)===10&&count(80,240)===3,'counts');
const g=[1,3,5,7,15,21,35,105],K=[36,23,11,7,6,4,2,1],lim=[16,27,25,28,45,42,35,105];
c(lim.every((e,i)=>9*K[i]*g[i]<=23*e),'one-missing generic cap');
const l=143*396,L=11*572;
let single=0,allCommon=0,n1=0,n2=0;
for(let j=0;j<=5;j++)for(let k=0;k<=5;k++)for(let w=0;w<=2;w++)for(let r=0;r<=1;r++)for(let z=0;z<=1;z++){
 const rest=12-j-k-w-r-z;if(rest<0)continue;
 const u=(11-j)*(13-k);
 const a=36*(143-u)*(l/143)+u*(w*13*(l/(143*3))+r*23*(l/(143*6))+z*11*(l/(143*4)));
 const b=rest*Math.max(u*23*(l/(143*9)),23*(l/11));
 single=Math.max(single,a+b);n1++;
}
for(let j=0;j<=10;j++)for(let z=0;z<=3;z++){
 const rest=11-j-z;if(rest<0)continue;
 const u=11-j;
 const a=j*(L/11)+z*u*5*(L/(11*52));
 const b=rest*Math.max(u*(L/(11*13)),L/22);
 allCommon=Math.max(allCommon,a+b);n2++;
}
c(4207+4752/16===563*8,'both');
c(single===1285*(l/36)&&allCommon===21*(L/22),'maxima');
console.log({both:"563/594",one:"1285/36",common:"21/22",n1,n2});
