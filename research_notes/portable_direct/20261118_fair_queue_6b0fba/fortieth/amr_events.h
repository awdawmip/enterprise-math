/* Added instrumentation for the published, cell-centred vortex test.
   Program globals mode_id, max_level, and tau are inserted by amr_check.py.
   0 = uniform grid, 1 = upstream velocity indicator, 2 = kinetic-loss indicator. */
#include <time.h>
static long calls, pre_leaves, post_leaves, refinements, coarsenings;
static long p_cycles, pf_cycles, risk_parents, risk_leaf_clears;
static double adapt_cpu, observable_cpu;

static void predict_kinetic_loss (Point point, scalar score)
{
  const double area = sq(Delta);
  const double vx = u.x[], vy = u.y[];
  double variation = 0.;
  foreach_child()
    variation += sq(u.x[] - vx) + sq(u.y[] - vy);
  double loss = area*variation/8.;
  foreach_child()
    score[] = loss;
  risk_parents++;
}

event adapt (i++)
{
  // The uniform controls get the same instrumentation outside adaptation.
  calls++;
  pre_leaves += grid->n;
  p_cycles += mgp.i;
  pf_cycles += mgpf.i;
  astats st = {0};
  clock_t ts = clock();
  if (mode_id == 1)
    st = adapt_wavelet ((scalar *){u}, (double[]){tau,tau}, max_level);
  if (mode_id == 2) {
    scalar score[];
    foreach()
      score[] = 0.;
    risk_leaf_clears += grid->n;
    score.refine = refine_injection;
    score.prolongation = predict_kinetic_loss;
    restriction ((scalar *){u});
    st = adapt_wavelet ({score}, (double[]){tau}, max_level);
  }
  adapt_cpu += (double)(clock()-ts)/CLOCKS_PER_SEC;
  post_leaves += grid->n;
  refinements += st.nf;
  coarsenings += st.nc;
}

// The original movie triggers every 0.2 and therefore constrains the dt schedule.
event observation_clock (t += 0.2; t <= 1.) {}

// Same global observable and conservation diagnostics in all runs.
event finish (t = 1.)
{
  clock_t ts = clock();
  double energy=0., mx=0., my=0., area=0., face_div_max=0., face_div_integral=0.;
  foreach(reduction(+:energy) reduction(+:mx) reduction(+:my)
          reduction(+:area) reduction(max:face_div_max) reduction(+:face_div_integral)) {
    double da = sq(Delta);
    energy += 0.5*da*(sq(u.x[])+sq(u.y[]));
    mx += da*u.x[]; my += da*u.y[]; area += da;
    double div = (uf.x[1]-uf.x[] + uf.y[0,1]-uf.y[])/Delta;
    face_div_max = max(face_div_max,fabs(div));
    face_div_integral += div*da;
  }
  double maxwall = 0.;
  foreach_boundary(left,reduction(max:maxwall))
    maxwall = max(maxwall,fabs(uf.x[]));
  foreach_boundary(right,reduction(max:maxwall))
    maxwall = max(maxwall,fabs(uf.x[1]));
  foreach_boundary(bottom,reduction(max:maxwall))
    maxwall = max(maxwall,fabs(uf.y[]));
  foreach_boundary(top,reduction(max:maxwall))
    maxwall = max(maxwall,fabs(uf.y[0,1]));
  observable_cpu += (double)(clock()-ts)/CLOCKS_PER_SEC;
  fprintf (stdout,"RESULT %d %d %.17g %d %.17g %.17g %.17g %.17g %.17g %.17g %.17g %.17g %ld %ld %ld %ld %ld %ld %ld %ld %ld %ld %ld %.6f %.6f\n",
    mode_id,max_level,tau,i,t,energy,mx,my,area,face_div_max,face_div_integral,maxwall,
    calls,(long)grid->n,pre_leaves,post_leaves,refinements,coarsenings,p_cycles,pf_cycles,
    risk_parents,risk_leaf_clears,(long)depth(),adapt_cpu,observable_cpu);
  return 1;
}
