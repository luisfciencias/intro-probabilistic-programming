# first skill: generate random numbers following particular distributions
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
plt.rcParams['mathtext.fontset'] = 'cm'

# Method 1: instance of the random state class
random_seed = 31416
random_state = np.random.RandomState(seed=random_seed)
number_samples = 1000
gaussian_sample = random_state.normal(loc=0, scale=2, size=number_samples)

# ground truth gaussian
x = np.linspace(-5, 5, 100)
y = norm(loc=0, scale=2)

plt.xkcd()
plt.figure(figsize=(8, 6))
plt.hist(gaussian_sample, bins=10, histtype='step', density=True)
plt.plot(x, y.pdf(x))
plt.title(r'$\mu = {} \quad \sigma = {}$'.format(0, 2))
plt.xlabel(r'$X$')
plt.ylabel(r'$P(X)$')
plt.savefig('random_samples.png', dpi=128)
plt.close()


# Method 2: Inverse transform method
# set up functions to measure pdf, cdf and icdf
def exponential_pdf(x_array, lambda_parameter=1):
    """PDF of exponential distribution"""
    return lambda_parameter*np.exp(-lambda_parameter * x_array)


def exponential_cdf(x_array, lambda_parameter=1):
    """CDF of exponential distribution."""
    return 1 - np.exp(-lambda_parameter * x_array)


def exponential_icdf(p, lambda_parameter=1):
    """Inverse CDF of exponential distribution: quantile estimation"""
    return -np.log(1-p)/lambda_parameter


# generate instance of the distribution with default lambda parameter
# auxiliar arrays to manipulate
xi = np.linspace(0, 4, 100)
yi = np.linspace(0, 1, 100)

# visual inspection
with plt.xkcd():
    plt.figure(figsize=(12, 6))
    # left panel
    plt.subplot(121)
    # plot the cumulative distribution
    plt.plot(xi, exponential_cdf(xi))
    plt.axis([0, 4, 0, 1])
    # highlight values at cdf points of 50% and 80% (say)
    for q in [0.5, 0.8]:
        plt.arrow(0, q, exponential_icdf(q) - 0.1, 0, head_width=0.05, head_length=0.1, fc='b', ec='b')
        plt.arrow(exponential_icdf(q), q, 0, -q + 0.1, head_width=0.1, head_length=0.05, fc='b', ec='b')
    # labels
    plt.ylabel('1: Generate a (0,1) uniform PRNG')
    plt.xlabel('2: Find the inverse CDF')
    plt.title('Inverse transform method')
    # right panel
    plt.subplot(122)
    # samples from the uniform distribution
    number_uniform_samples = 10000
    u = np.random.random(number_uniform_samples)
    # get the inverse cumulative distribution
    v = exponential_icdf(u)
    # visualise the distribution from the samples
    plt.hist(v, histtype='step', bins=100, density=True, linewidth=2)
    # compare with real pdf
    plt.plot(x, exponential_pdf(x), linewidth=2)
    plt.axis([0, 4, 0, 1])
    plt.title('Histogram of exponential PRNGs')
plt.savefig('random_inverse_transform.png', dpi=128)
plt.close()
