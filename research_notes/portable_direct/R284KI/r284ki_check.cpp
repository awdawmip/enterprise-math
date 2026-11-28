#define main old_main
#include "r284ki_sieve.cpp"
#undef main
int main(){for(int d:{81,120,3001})for(int q:{0,1,17,100,10000})for(int p:{2,3,5}){int s=p==2?54:p==3?33:23;Eval e(d,p,s);std::cout<<d<<' '<<q<<' '<<p<<' '<<s<<' '<<e.g<<' '<<e(q)<<'\n';}}
