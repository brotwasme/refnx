import unittest
import refnx.analysis.curvefitter as curvefitter
from refnx.analysis.curvefitter import CurveFitter
import numpy as np
from copy import deepcopy
from lmfit import Parameters
from lmfit.minimizer import MinimizerResult

from numpy.testing import (assert_almost_equal, assert_equal, assert_,
                           assert_allclose)
import os.path
SEED = 1


path = os.path.dirname(os.path.abspath(__file__))


def gauss(x, p0, *args):
    p = list(p0.valuesdict().values())

    return p[0] + p[1] * np.exp(-((x - p[2]) / p[3])**2)


class TestFitter(unittest.TestCase):

    def setUp(self):
        self.xdata = np.linspace(-4, 4, 100)
        self.p0 = np.array([0., 1., 0.0, 1.])
        self.bounds = [(-1, 1), (0, 2), (-1, 1.), (0.001, 2)]

        self.params = curvefitter.to_Parameters(self.p0 + 0.2, bounds=self.bounds)
        self.final_params = curvefitter.to_Parameters(self.p0, bounds=self.bounds)

        self.ydata = gauss(self.xdata, self.final_params)
        self.f = CurveFitter(gauss, self.xdata, self.ydata, self.params)

    def pvals(self, params):
        return np.asfarray(list(params.valuesdict().values()))

    def test_fitting(self):
        # the simplest test - a really simple gauss curve with perfect data
        res = self.f.fit()
        assert_almost_equal(self.pvals(res.params), self.p0)
        assert_almost_equal(res.chisqr, 0)

    def test_model_returns_function(self):
        ydata = gauss(self.xdata, self.final_params)
        model = self.f.model(self.final_params)
        assert_almost_equal(ydata, model)

    def test_residuals(self):
        resid = self.f.residuals(self.final_params)
        assert_almost_equal(np.sum(resid**2), 0)

    def test_cost(self):
        resid = self.f.residuals(self.final_params)
        assert_almost_equal(0, np.sum(resid**2))

    def test_leastsq(self):
        # test that a custom method can be used with scipy.optimize.minimize
        res = self.f.fit()
        assert_almost_equal(self.pvals(res.params), self.p0)
        
    def test_resid_length(self):
        # the residuals length should be equal to the data length
        resid = self.f.residuals(self.params)
        assert_equal(resid.size, self.f.ydata.size)

    def test_scalar_minimize(self):
        assert_equal(self.pvals(self.params), self.p0 + 0.2)
        res = self.f.fit(method='differential_evolution')
        assert_almost_equal(self.pvals(res.params), self.p0, 3)

    def test_holding_parameter(self):
        # holding parameters means that those parameters shouldn't change
        # during a fit
        self.params['p0'].vary = False
        res = self.f.fit()
        assert_almost_equal(self.p0[0] + 0.2, self.params['p0'].value)

    def test_fit_returns_MinimizerResult(self):
        self.params['p0'].vary = False
        res = self.f.fit()
        assert_(isinstance(res, MinimizerResult))


class TestFitterGauss(unittest.TestCase):
    # Test CurveFitter with a noisy gaussian, weighted and unweighted, to see
    # if the parameters and uncertainties come out correct

    def setUp(self):
        theoretical = np.loadtxt(os.path.join(path, 'gauss_data.txt'))
        xvals, yvals, evals = np.hsplit(theoretical, 3)
        self.xvals = xvals.flatten()
        self.yvals = yvals.flatten()
        self.evals = evals.flatten()

        self.best_weighted = [-0.00246095, 19.5299, -8.28446e-2, 1.24692]

        self.best_weighted_errors = [0.0220313708486, 1.12879436221,
                                     0.0447659158681, 0.0412022938883]

        self.best_weighted_chisqr = 77.6040960351

        self.best_unweighted = [-0.10584111872702096, 19.240347049328989,
                                0.0092623066070940396, 1.501362314145845]

        self.best_unweighted_errors = [0.34246565477, 0.689820935208,
                                       0.0411243173041, 0.0693429375282]

        self.best_unweighted_chisqr = 497.102084956

        self.p0 = np.array([0.1, 20., 0.1, 0.1])
        self.bounds = [(-1, 1), (0, 30), (-5., 5.), (0.001, 2)]

        self.params = curvefitter.to_Parameters(self.p0, bounds=self.bounds)

    def test_best_weighted(self):
        f = CurveFitter(gauss, self.xvals, self.yvals, self.params,
                        edata=self.evals)
        res = f.fit()

        output = list(res.params.valuesdict().values())
        assert_almost_equal(output, self.best_weighted, 4)
        assert_almost_equal(res.chisqr, self.best_weighted_chisqr)

        uncertainties = [res.params['p%d' % i].stderr for i in range(4)]
        assert_almost_equal(uncertainties, self.best_weighted_errors, 3)

    def test_best_unweighted(self):
        f = CurveFitter(gauss, self.xvals, self.yvals, self.params)
        res = f.fit()

        output = list(res.params.valuesdict().values())
        assert_almost_equal(output, self.best_unweighted, 5)
        assert_almost_equal(res.chisqr, self.best_unweighted_chisqr)

        uncertainties = [res.params['p%d' % i].stderr for i in range(4)]
        assert_almost_equal(uncertainties, self.best_unweighted_errors, 3)

    def test_parameter_names(self):
        # each instance of CurveFitter should be able to give a default set of
        # parameter names
        names = ['p%i' % i for i in range(10)]
        names2 = CurveFitter.parameter_names(nparams=10)
        assert_(names == names2)

    # def test_mcmc_vs_lm(self):
    #     # test mcmc output vs lm
    #     f = CurveFitter(gauss, self.xvals, self.yvals, self.params,
    #                     edata=self.evals)
    #     np.random.seed(123456)
    #     f.mcmc(samples=2000, burn=500, thin=20)
    #     output = list(f.params.valuesdict().values())
    #     assert_allclose(output, self.best_weighted, rtol=0.02, atol=0.01)

    def test_emcee_vs_lm(self):
        # test mcmc output vs lm
        f = CurveFitter(gauss, self.xvals, self.yvals, self.params,
                        edata=self.evals)
        np.random.seed(123456)
        f.emcee(nwalkers=20, steps=1500, burn=100, thin=20)
        output = list(f.result.params.valuesdict().values())
        assert_allclose(output, self.best_weighted, rtol=0.02, atol=0.01)

        # test mcmc output vs lm, some parameters not bounded
        self.params['p1'].max = None
        f = CurveFitter(gauss, self.xvals, self.yvals, self.params,
                        edata=self.evals)
        np.random.seed(123456)
        f.emcee(nwalkers=20, steps=1500, burn=100, thin=20)
        output = list(f.result.params.valuesdict().values())
        assert_allclose(output, self.best_weighted, rtol=0.02, atol=0.01)

        # test mcmc output vs lm, some parameters not bounded
        self.params['p1'].min = None
        f = CurveFitter(gauss, self.xvals, self.yvals, self.params,
                        edata=self.evals)
        f.emcee(nwalkers=20, steps=1500, burn=100, thin=20)
        output = list(f.result.params.valuesdict().values())
        assert_allclose(output, self.best_weighted, rtol=0.02, atol=0.01)


if __name__ == '__main__':
    unittest.main()
