#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Libraries
##############################################################################

import numpy as np 
import matplotlib.pyplot as plt
from lmfit.models import (GaussianModel, LorentzianModel, PseudoVoigtModel) # pip install lmfit

##############################################################################
# Base Models
##############################################################################

def gaussian(x, y):

	# Gaussian fit to a curve

    x_shifted = x - x.min() # Shifting to 0    
    y_shifted = y - y.min() # Shifting to 0    
    mod = GaussianModel() # Setting model type
    pars = mod.guess(y_shifted, x=x_shifted) # Estimating fit
    out = mod.fit(y_shifted, pars, x=x_shifted) # Fitting fit
    print(out.fit_report(min_correl=0.25)) # Outputting best fit results
    #print("Gaussian FWHM = ", out.params['fwhm'].value) # Outputting only FWHM
    out.plot() # Plotting fit
    
    
    std = np.std(x_shifted)
    mux = np.mean(x_shifted)
    h_y = np.max(out.best_fit)
    #print(std, mux, h_y)
    
    y_x = h_y/2
    
    x_i = mux - np.sqrt(2*(std**2)*
                    np.log((np.sqrt(2*np.pi)*y_x*std)/
                          (h_y)))
    
    x_f = mux + np.sqrt(2*(std**2)*
                    np.log((np.sqrt(2*np.pi)*y_x*std)/
                          (h_y)))  
    
    fwhm = x_f-x_i
    print(x_i, x_f, fwhm)
    
    #plt.plot(x_shifted, out.best_fit)
    #plt.show
    
def lorentzian(x, y):

	# Lorentzian fit to a curve

    x_shifted = x - x.min() # Shifting to 0  
    y_shifted = y - y.min() # Shifting to 0    
    mod = LorentzianModel() # Setting model type
    pars = mod.guess(y_shifted, x=x_shifted) # Estimating fit
    out = mod.fit(y_shifted, pars, x=x_shifted) # Fitting fit
    # print(out.fit_report(min_correl=0.25)) # Outputting best fit results
    print("Lorentzian FWHM = ", out.params['fwhm'].value) # Outputting only FWHM
    out.plot() # Plotting fit

def voigt(x, y):

	# Voigt fit to a curve

    x_shifted = x - x.min() # Shifting to 0
    y_shifted = y - y.min() # Shifting to 0    
    mod = PseudoVoigtModel() # Setting model type
    pars = mod.guess(y_shifted, x=x_shifted) # Estimating fit
    out = mod.fit(y_shifted, pars, x=x_shifted) # Fitting fit
    # print(out.fit_report(min_correl=0.25)) # Outputting best fit results
    print("Voigt FWHM = ", out.params['fwhm'].value) # Outputting only FWHM
    out.plot() # Plotting fit

##############################################################################
# Combined Model
##############################################################################

def GLVmodels(x, y, t=None):

	# Gaussian, Lorenzitian, and Voigt fit to a curve
    
    # x is an array of values for along the x axis
    # y is an array of values for along the y axis
    # t is the type of model to be used G, L, or V, if no input all are done
       
    print ("\n",'{:_^52}'.format('X Values Vs Y Values'),"\n")
    plt.plot(x,y)
    plt.show()
    
    print("X Axis off-set from origin is", x.min())
    print("Y Axis off-set from origin is", y.min(),"\n")

    if t is None:

        print ("\n",'{:_^52}'.format('Gaussian Model'),"\n")
        gaussian(x, y)
        
        print ("\n",'{:_^52}'.format('Lorentzian Model'),"\n")
        lorentzian(x, y)
        
        print ("\n",'{:_^52}'.format('Voigt Model'),"\n")
        voigt(x, y)
        
    if t == "G":

        print ("\n",'{:_^52}'.format('Gaussian Model'),"\n")
        gaussian(x, y)
        
    if t == "L":

        print ("\n",'{:_^52}'.format('Lorentzian Model'),"\n")
        lorentzian(x, y)
        
    if t == "V":
        
        print ("\n",'{:_^52}'.format('Voigt Model'),"\n")
        voigt(x, y)


##############################################################################
# Execution
##############################################################################

data = np.load('Data_Pathfile_Here') # Data location

GLVmodels(X_Data, Y_Data) # run model
