#include <bits/stdc++.h>
using namespace std;using u64=uint64_t;using i64=int64_t;
const u64 N=1ULL<<32,T=33*N;
const int LO=262145,HI=524287;
const int S[16]={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285};
u64 gcd_(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
u64 inv_(u64 a,u64 m){i64 r0=a,r1=m,s0=1,s1=0;while(r1){i64 q=r0/r1;tie(r0,r1)=make_pair(r1,r0-q*r1);tie(s0,s1)=make_pair(s1,s0-q*s1);}if(r0!=1)abort();return (s0%(i64)m+(i64)m)%(i64)m;}
bool U(int q){for(int s:S)if(s==q)return true;if((400011<=q&&q<=400521)||(480011<=q&&q<=480521))return true;for(int h=1;h<32;h++)if(((1ULL<<h)-1)%q==0||((1ULL<<h)+1)%q==0)return true;return false;}
bool OLD(u64 a,u64 b){return a*b<T || U(a)||U(b)|| (a/gcd_(a,b))*b<N ||33*((N+a-1)/a)>b ||33*((N+b-1)/b)>a;}
struct Witness{u64 x,y;int i,j;};
bool ZF(u64 a,u64 b){if(gcd_(a,b)>1)return false;u64 inv=inv_(a%b,b),r=inv,bit=1;for(int i=0;i<32;i++,bit<<=1){if(r*a<N || (b-r)*a+bit<N)return true;r=(r*2)%b;}return false;}
bool FFanchored(u64 a,u64 b,Witness &w){u64 g=gcd_(a,b),m=b/g,K=(N-1)/a;if(m<=K)abort();u64 inv=inv_((a/g)%m,m);
 for(int i=0;i<32;i++)for(int j=0;j<32;j++)for(int s:{1,-1}){
 i64 delta=(1LL<<i)-s*(1LL<<j);if(delta%(i64)g)continue;
 i64 d=delta/(i64)g;u64 rem=((d%(i64)m)+(i64)m)%(i64)m;
 u64 k=(rem*inv)%m;if(k==0||k>K)continue;
 u64 z=k*a;bool zero=((z>>j)&1)==0;if(zero!=(s==1))continue;
 u64 dest=z^(1ULL<<j);if(z>=N||dest>=N)abort();
 if(0%a!=z%a ||(1ULL<<i)%b!=dest%b)abort();
 w={0,z,i,j};return true;}return false;}
u64 bitones(u64 t,int i){u64 h=1ULL<<i,p=2*h;return (t/p)*h+(t%p>h?t%p-h:0);}
u64 lowcount(u64 l,u64 r,int bit,int target,u64 off){if(l>r)return 0;u64 n=bitones(r+1+off,bit)-bitones(l+off,bit);return target?n:r-l+1-n;}
struct BitIntersection{
 int i,bi,j,bj;u64 d,P,H,per;vector<pair<u64,u64>> highs;int lowbit,lowtarget;u64 off;
 BitIntersection(int i_,int bi_,int j_,int bj_,u64 d_):i(i_),bi(bi_),j(j_),bj(bj_),d(d_){
 int hi=max(i,j);H=1ULL<<hi;P=2*H;
 auto addRing=[&](u64 start,u64 len,vector<pair<u64,u64>>&v){u64 end=start+len;if(end<=P)v.push_back({start,end-1});else{v.push_back({start,P-1});v.push_back({0,end-P-1});}};
 if(i>=j)highs.push_back({bi*H,(bi+1)*H-1});
 else{u64 start=((bj*H+P)-(d%P))%P;addRing(start,H,highs);}
 if(i==j){vector<pair<u64,u64>> other;u64 start=((bj*H+P)-(d%P))%P;addRing(start,H,other);
 vector<pair<u64,u64>> is;for(auto a:highs)for(auto b:other){u64 l=max(a.first,b.first),r=min(a.second,b.second);if(l<=r)is.push_back({l,r});}highs=is;}
 if(i!=j){lowbit=min(i,j);lowtarget=(i<j?bi:bj);u64 lp=1ULL<<(lowbit+1);off=(i<j?0:d%lp);}
 else{lowbit=-1;off=0;lowtarget=0;}
 per=0;for(auto z:highs)per+=lowbit<0?z.second-z.first+1:lowcount(z.first,z.second,lowbit,lowtarget,off);
 }
 u64 prefix(u64 t)const{u64 ans=(t/P)*per,z=t%P;if(z==0)return ans;
 for(auto a:highs){if(a.first>=z)continue;u64 r=min(a.second,z-1);ans+=lowbit<0?r-a.first+1:lowcount(a.first,r,lowbit,lowtarget,off);}return ans;}
 u64 count(u64 L,u64 R)const{return L>R?0:prefix(R+1)-prefix(L);}
};
bool FFgeneral(u64 a,u64 b,Witness &w){
 u64 g=gcd_(a,b),m=b/g,inv=inv_((a/g)%m,m),K=(N-1)/a;
 for(int i=0;i<32;i++)for(int j=0;j<32;j++)for(int si:{1,-1})for(int sj:{1,-1}){
 i64 delta=si*(1LL<<i)-sj*(1LL<<j);if(delta%(i64)g)continue;
 i64 tmp=delta/(i64)g;u64 k0=(((tmp%(i64)m+(i64)m)%(i64)m)*inv)%m;
 for(i64 k=(i64)k0-((i64)K/m+2)*(i64)m;k<=(i64)K;k+=(i64)m){
 if(k<-(i64)K)continue;if(k==0&&i==j)continue;
 i64 d=k*(i64)a,L=max<i64>(0,-d),R=min<i64>((i64)N-1,(i64)N-1-d);if(L>R)continue;
 BitIntersection I(i,si==1?0:1,j,sj==1?0:1,(u64)((d%(i64)N+(i64)N)%(i64)N));
 if(!I.count(L,R))continue;
 u64 low=L,high=R;while(low<high){u64 mid=(low+high)/2;if(I.count(L,mid))high=mid;else low=mid+1;}
 u64 x=low,y=(i64)x+d;
 if(x>=N||y>=N||((x>>i)&1)!=(si==-1)||((y>>j)&1)!=(sj==-1)
 || x%a!=y%a||(x^(1ULL<<i))%b!=(y^(1ULL<<j))%b)abort();
 w={x,y,i,j};return true;
 }}return false;}
int main(int argc,char**argv){
 int a=argc>1?stoi(argv[1]):510389;if(a<LO||a>HI||a%2==0||U(a))abort();
 u64 old=0,zf=0,anchor=0,general=0,unresolved=0;
 vector<pair<int,Witness>> general_witnesses,anchor_witnesses;
 for(int b=LO;b<=HI;b+=2){
 if(OLD(a,b)){old++;continue;}
 if(ZF(a,b)){zf++;continue;}
 Witness w;if(FFanchored(a,b,w)){anchor++;if(anchor_witnesses.size()<3)anchor_witnesses.push_back({b,w});continue;}
 if(FFgeneral(a,b,w)){general++;general_witnesses.push_back({b,w});}
 else{unresolved++;cerr<<"UNRESOLVED "<<a<<" "<<b<<"\n";}}
 cout<<"{\"q1\":"<<a<<",\"q_count\":131072,\"old_four_family\":"<<old
 <<",\"zf_new\":"<<zf<<",\"anchored_ff_new\":"<<anchor
 <<",\"general_ff_new\":"<<general<<",\"unresolved\":"<<unresolved<<",\"general_witnesses\":[";
 for(int z=0;z<(int)general_witnesses.size();z++){auto [b,w]=general_witnesses[z];
 cout<<(z?",":"")<<"{\"q2\":"<<b<<",\"x\":"<<w.x<<",\"y\":"<<w.y<<",\"i\":"<<w.i<<",\"j\":"<<w.j<<"}";}
 cout<<"],\"anchored_examples\":[";
 for(int z=0;z<(int)anchor_witnesses.size();z++){auto[b,w]=anchor_witnesses[z];
 cout<<(z?",":"")<<"{\"q2\":"<<b<<",\"x\":"<<w.x<<",\"y\":"<<w.y<<",\"i\":"<<w.i<<",\"j\":"<<w.j<<"}";}
 cout<<"]}\n";
}