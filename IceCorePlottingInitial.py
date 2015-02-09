"""
IceCorePlottingDemo
Created on Sat Jan 31 15:29:39 2015

@author: David Milodowski
"""
#import modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
from matplotlib import rcParams
from mpl_toolkits.axes_grid1.inset_locator import *

# Set up some basiic parameters for the plots
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['arial']
rcParams['font.size'] = 8
rcParams['legend.numpoints'] = 1

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# A FUNCTION TO READ IN THE DATA FILES
# This function returns a set of variables, which contain the data you've just
# read in from the data files
def read_data_files():
    deut_file = "deutnat_data_only.txt"
    o18_file = "o18nat.txt"
    co2_file = "co2nat.txt"
    
    # read in the deuterium data
    ice_age_deut = np.loadtxt(deut_file,skiprows=1,usecols=[1])    
    deut = np.loadtxt(deut_file,skiprows=1,usecols=[2])
    deltaTS = np.loadtxt(deut_file,skiprows=1,usecols=[3])
    
    # read in the o18 data
    ice_age_o18 = np.loadtxt(o18_file,skiprows=1,usecols=[0])    
    o18 = np.loadtxt(o18_file,skiprows=1,usecols=[1])
    
    # read in the CO2 data
    ice_age_CO2 = np.loadtxt(co2_file,skiprows=1,usecols=[0])    
    CO2 = np.loadtxt(co2_file,skiprows=1,usecols=[1])
    return ice_age_deut, deut, deltaTS,ice_age_o18,o18,ice_age_CO2,CO2

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# FUNCTIONS TO MAKE THE FIGURE
# These functions will take in a set of variables, which pass the data into the
# the function.
# 
# This sample program uses subplots, which you should have been introduced to
# at the start of the tutorial
def ice_core_plot_simple(ice_age_deut, deut, deltaTS,ice_age_o18,o18,ice_age_CO2,CO2):
    # First set up the plot dimensions etc.
    plt.figure(1, facecolor='White',figsize=[8,10])
    # We are going to use subplots here.  We are going to specify the axes used
    # in each.  This will give us a bit more flexibility later on
    ax1 = plt.subplot(411)
    ax1.plot(ice_age_deut/1000,deltaTS,'-',color="blue",linewidth=1)
    ax1.set_ylabel(u'$\Delta TS  (^{o}C)$',fontsize=10) # Note that the text held between the $ signs gets converted to "math" format
    ax1.set_title('420ka Climate Record from Vostok Ice Core (Petit et al., 1999)',fontsize=12) 
    ax1.set_xlabel("$Age BP (ka)$",fontsize=10) 
       
    ax2 = plt.subplot(412)
    ax2.plot(ice_age_deut/1000,deut,'-',color="green",linewidth=1)
    ax2.set_ylabel(u'$\delta D  (\u2030)$',fontsize=10)
    ax2.set_xlabel("$Age BP (ka)$",fontsize=10) 
       
    ax3 = plt.subplot(413)
    ax3.plot(ice_age_CO2/1000,CO2,'-',color="green",linewidth=1)
    ax3.set_ylabel('$CO_2(ppmv)$',fontsize=10)
    ax3.set_xlabel("$Age BP (ka)$",fontsize=10) 
   
    ax4 = plt.subplot(414)
    ax4.plot(ice_age_o18/1000,o18,'-',color="green",linewidth=1)
    ax4.set_ylabel(u'$\delta ^{18}O_{atm}  (\u2030)$',fontsize=10)
    ax4.set_xlabel("$Age BP (ka)$",fontsize=10) 
    
    # the tight_layout() function is a handy tool for automating the layout if
    # you are running into difficulties with seeing your axes labels properly
    plt.tight_layout()        
    plt.savefig("PlottingExample.svg",format="svg")    
    plt.show()



# This bit at the bottom tells the python interpreter what to do if you run the
# script directly
if __name__ == "__main__":
    ice_age_deut, deut, deltaTS,ice_age_o18,o18,ice_age_CO2,CO2 = read_data_files()    
    ice_core_plot_simple(ice_age_deut, deut, deltaTS,ice_age_o18,o18,ice_age_CO2,CO2)
    ice_core_plot_final(ice_age_deut, deut, deltaTS,ice_age_o18,o18,ice_age_CO2,CO2)