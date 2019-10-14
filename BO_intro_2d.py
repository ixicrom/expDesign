#Following final section of tutorial for Bayesian Optimisation using GPyOPt: https://nbviewer.jupyter.org/github/SheffieldML/GPyOpt/blob/devel/manual/GPyOpt_reference_manual.ipynb
import GPy
import GPyOpt
from numpy.random import seed
import matplotlib

# six-hump camel function
f_true = GPyOpt.objective_examples.experiments2d.sixhumpcamel()
f_sim = GPyOpt.objective_examples.experiments2d.sixhumpcamel(sd=0.1)
bounds = [{'name':'var_1', 'type':'continuous', 'domain':f_true.bounds[0]},
            {'name':'var_2', 'type':'continuous','domain':f_true.bounds[1]}]

f_true.plot()

myBOpt2d = GPyOpt.methods.BayesianOptimization(f_sim.f, domain=bounds,
                                    model_type = 'GP', acquisition_type='EI',
                                    normalize_Y = True, acquisition_weight = 2)

max_iter = 40
max_time = 60

myBOpt2d.run_optimization(max_iter, max_time, verbosity=False)

myBOpt2d.plot_acquisition()
myBOpt2d.plot_convergence()
