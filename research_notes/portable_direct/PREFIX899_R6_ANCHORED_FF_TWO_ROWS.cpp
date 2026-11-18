#include <bits/stdc++.h>
using namespace std;using ull=uint64_t;using ll=int64_t;
static const ull N=1ULL<<32,T=33*N;const int lo=262145,hi=524287;
const int S[16]={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285};
ull gcd_(ull a,ull b){while(b){ull t=a%b;a=b;b=t;}return a;}
ull inv_(ull a,ull m){ll r0=a,r1=m,s0=1,s1=0;while(r1){ll q=r0/r1;tie(r0,r1)=make_pair(r1,r0-q*r1);tie(s0,s1)=make_pair(s1,s0-q*s1);}assert(r0==1);return (s0%(ll)m+(ll)m)%(ll)m;}
bool U(int q){for(int s:S)if(s==q)return true;if((400011<=q&&q<=400521)||(480011<=q&&q<=480521))return true;for(int h=1;h<32;h++)if(((1ULL<<h)-1)%q==0||((1ULL<<h)+1)%q==0)return true;return false;}
bool OLD(ull a,ull b){return a*b<T || U(a) || U(b) || (a/gcd_(a,b))*b<N || 33*((N+a-1)/a)>b || 33*((N+b-1)/b)>a;}
bool ZF(ull a,ull b){ull g=gcd_(a,b);if(g>1)return false;ull inv=inv_(a%b,b),r=inv,bit=1;for(int i=0;i<32;i++,bit<<=1){if(r*a<N || (b-r)*a+bit<N)return true;r=(r*2)%b;}return false;}
bool FFanchored(ull a,ull b,ull &start,int &iout,int &jout){ull g=gcd_(a,b),m=b/g,K=(N-1)/a;if(m<=K){cerr<<"unexpected lcm positive";abort();}ull inv=inv_((a/g)%m,m);
for(int i=0;i<32;i++)for(int j=0;j<32;j++)for(int s:{1,-1}){
 ll delta=(1LL<<i)-s*(1LL<<j);if(delta%ll(g))continue;
 ll d=delta/ll(g);ll reduced=((d%ll(m))+ll(m))%ll(m);ull k=(ull(reduced)*inv)%m; if(!k||k>K)continue;
 ull z=k*a;bool zero=((z>>j)&1)==0;if(zero!=(s==1))continue;
 ull dest=z^(1ULL<<j);assert(z<N && dest<N);assert(0%a==z%a && ((1ULL<<i)%b)==dest%b);
 start=z;iout=i;jout=j;return true;
 }return false;}
int main(){for(int a:{510001,510195}){unsigned long long old=0,zf=0,ff=0,remain=0;vector<int> residual;int first_i=-1,first_j=-1;ull first_z=0;int first_b=0;
 for(int b=lo;b<=hi;b+=2){if(OLD(a,b)){old++;continue;}if(ZF(a,b)){zf++;continue;}ull z;int i,j;if(FFanchored(a,b,z,i,j)){ff++;if(first_i<0){first_i=i;first_j=j;first_z=z;first_b=b;}}else {remain++;if(residual.size()<16)residual.push_back(b);}}
 cout<<"q1="<<a<<" old="<<old<<" ZF_new="<<zf<<" FF_anchor_new="<<ff<<" remaining="<<remain<<" example_b="<<first_b<<" example_start="<<first_z<<" i="<<first_i<<" j="<<first_j<<" residuals=";for(int z:residual)cout<<z<<",";cout<<"\n";}
}
