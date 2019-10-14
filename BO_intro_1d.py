#Following tutorial for Bayesian Optimisation using GPyOPt: https://nbviewer.jupyter.org/github/SheffieldML/GPyOpt/blob/devel/manual/GPyOpt_reference_manual.ipynb 

import GPyOpt
from numpy.random import seed
import matplotlib


# function to minimise, minimum should be at (0,0)
def myf(x):
    return (2*x)**2

# constraints on the function, in this case we look only in the interval -1 -> 1, and we're looking at a continuous variable
bounds = [{'name': 'var_1', 'type' : 'continuous', 'domain' : (-1,1)}]

max_iter = 15

# create a GPyOpt object that stores the problem
myProblem = GPyOpt.methods.BayesianOptimization(myf, bounds)

# run the optimisation for the given max number of iterations
myProblem.run_optimization(max_iter)

print(myProblem.x_opt)

print(myProblem.fx_opt)


# now try with the Forrester function, the minimum should be at x=0.78
f_true = GPyOpt.objective_examples.experiments1d.forrester() #true forrester function
bounds = [{'name':'var_1', 'type':'continuous', 'domain':(0,1)}]

f_true.plot()

seed(123)
myBO = GPyOpt.methods.BayesianOptimization(f=f_true.f, domain=bounds, acquisition_type='EI', exact_feval=True)

max_iter = 15
max_time = 60
eps = 10e-6 #minimum allowed disatnce between the last two observations

myBO.run_optimization(max_iter, max_time, eps)

myBO.plot_acquisition()
myBO.plot_convergence()

print(myBO.x_opt)
