# Black-Scholes Option Pricing with Greeks
# Ramy Alsammarae

import numpy as np
from scipy.stats import norm

# Input values
r = 0.035          # Risk-free rate
S = 25             # Price of the underlying asset
K = 30             # Strike price
T = 240/365        # Time to expiration (years)
sigma = 0.25       # Volatility (stdev of log returns)
option_type = 'c'  # 'c' for Call or 'p' for Put

def black_scholes(r, S, K, T, sigma, option_type):
    """Calculates the Black-Scholes price of an option"""
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == "c":
        price = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    elif option_type == "p":
        price = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Please use 'c' for Call or 'p' for Put.")
    return price

def option_delta(r, S, K, T, sigma, option_type):
    """Calculates the delta of an option"""
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    if option_type == "c":
        delta_calc = norm.cdf(d1)
    elif option_type == "p":
        delta_calc = -norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Please use 'c' for Call or 'p' for Put.")
    return delta_calc

def option_gamma(r, S, K, T, sigma):
    """Calculates the gamma of an option"""
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    gamma_calc = norm.pdf(d1)/(S*sigma*np.sqrt(T))
    return gamma_calc

def option_vega(r, S, K, T, sigma):
    """Calculates the vega of an option"""
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    vega_calc = S*norm.pdf(d1)*np.sqrt(T)
    return vega_calc*0.01

def option_theta(r, S, K, T, sigma, option_type):
    """Calculates the theta of an option"""
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == "c":
        theta_calc = -S*norm.pdf(d1)*sigma/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2)
    elif option_type == "p":
        theta_calc = -S*norm.pdf(d1)*sigma/(2*np.sqrt(T)) + r*K*np.exp(-r*T)*norm.cdf(-d2)
    else:
        raise ValueError("Invalid option type. Please use 'c' for Call or 'p' for Put.")
    return theta_calc/365

def option_rho(r, S, K, T, sigma, option_type):
    """Calculates the rho of an option"""
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == "c":
        rho_calc = K*T*np.exp(-r*T)*norm.cdf(d2)
    elif option_type == "p":
        rho_calc = -K*T*np.exp(-r*T)*norm.cdf(-d2)
    else:
        raise ValueError("Invalid option type. Please use 'c' for Call or 'p' for Put.")
    return rho_calc*0.01

option_price = black_scholes(r, S, K, T, sigma, option_type)
delta = option_delta(r, S, K, T, sigma, option_type)
gamma = option_gamma(r, S, K, T, sigma)
vega = option_vega(r, S, K, T, sigma)
theta = option_theta(r, S, K, T, sigma, option_type)
rho = option_rho(r, S, K, T, sigma, option_type)

print("Option Price: ", round(option_price, 3))
print("       Delta: ", round(delta, 3))
print("       Gamma: ", round(gamma, 3))
print("       Vega : ", round(vega, 3))
print("       Theta: ", round(theta, 3))
print("       Rho  : ", round(rho, 3))