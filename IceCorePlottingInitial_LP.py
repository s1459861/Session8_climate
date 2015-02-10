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
    ice_age_deut = np.loadtxt(deut_file,skiprows=6,usecols=[1])    
    deut = np.loadtxt(deut_file,skiprows=6,usecols=[2])
    deltaTS = np.loadtxt(deut_file,skiprows=6,usecols=[3])
    
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
    
    ax1 = plt.subplot2grid((6,4),(0,0),colspan=4)
    ax1.plot(ice_age_deut/1000,deltaTS,'-',color="blue",linewidth=1)
    ax1.set_ylabel(u'$\Delta TS  (^{o}C)$',fontsize=10) # Note that the text held between the $ signs gets converted to "math" format
    ax1.set_title('420ka Climate Record from Vostok Ice Core (Petit et al., 1999)',fontsize=12) 
    ax1.set_xlim(0,420)
    ax1.grid(True)
    majorLocator = tk.MultipleLocator(20)
    ax1.xaxis.set_major_locator(majorLocator)
    ax1.annotate('a', xy=(0.05,0.9),  xycoords='axes fraction', backgroundcolor='none', horizontalalignment='left',  verticalalignment='top',  fontsize=10)
    
    ax2 = plt.subplot2grid((6,4),(1,0),colspan=4)
    ax2.plot(ice_age_deut/1000,deut,'-',color="green",linewidth=1)
    ax2.set_ylabel(u'$\delta D  (\u2030)$',fontsize=10)
    ax2.set_xlim(0,420)
    ax2.grid(True)
    majorLocator = tk.MultipleLocator(20)
    ax2.xaxis.set_major_locator(majorLocator)
    ax2.annotate('b', xy=(0.05,0.9),  xycoords='axes fraction', backgroundcolor='none', horizontalalignment='left',  verticalalignment='top',  fontsize=10)
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")

   
    ax3 = plt.subplot2grid((6,4),(2,0),colspan=4)
    ax3.plot(ice_age_CO2/1000,CO2,'-',color="green",linewidth=1)
    ax3.set_ylabel('$CO_2(ppmv)$',fontsize=10)
    ax3.set_xlim(0,420)
    ax3.grid(True)
    majorLocator = tk.MultipleLocator(20)
    ax3.xaxis.set_major_locator(majorLocator)
    ax3.annotate('c', xy=(0.05,0.9),  xycoords='axes fraction', backgroundcolor='none', horizontalalignment='left',  verticalalignment='top',  fontsize=10)
    
    ax4 = plt.subplot2grid((6,4),(3,0),colspan=4)
    ax4.plot(ice_age_o18/1000,o18,'-',color="green",linewidth=1)
    ax4.set_ylabel(u'$\delta ^{18}O_{atm}  (\u2030)$',fontsize=10)
    ax4.set_xlabel("$Age BP (ka)$",fontsize=10)
    ax4.set_xlim(0,420)
    ax4.grid(True)
    majorLocator = tk.MultipleLocator(20)
    ax4.xaxis.set_major_locator(majorLocator)
    ax4.annotate('d', xy=(0.05,0.9),  xycoords='axes fraction', backgroundcolor='none', horizontalalignment='left',  verticalalignment='top',  fontsize=10)
    ax4.yaxis.tick_right()
    ax4.yaxis.set_label_position("right") 
    xticklabels = ax1.get_xticklabels()+ax2.get_xticklabels()+ax3.get_xticklabels()
    plt.setp(xticklabels, visible=False)
    plt.subplots_adjust(hspace=0.001)
    
    ax5 = plt.subplot2grid((8,4),(6,0),colspan=3,rowspan=3)
    line1 = ax5.plot(ice_age_deut[ice_age_deut<130000]/1000,deltaTS[ice_age_deut<130000], '-', color="blue", linewidth=1, label=u'$\Delta TS$')
    ax5.plot(ice_age_deut[ice_age_deut<130000]/1000,deltaTS[ice_age_deut<130000], '-', color="blue", linewidth=1, label=u'$\Delta TS$')
    ax5.set_ylabel(u'$\delta ^{18}O_{atm}  (\u2030)$',fontsize=10)
    ax5.set_xlabel("$Age BP (ka)$",fontsize=10)
    ax5.grid(True)
    ax5.annotate('e', xy=(0.06125,0.9), xycoords='axes fraction',backgroundcolor='white',horizontalalignment='left', verticalalignment='top', fontsize=rcParams['font.size']+2) 
    ax5.set_xlim(xmax=130)

    ax6 = ax5.twinx()
    line2 = ax6.plot(ice_age_CO2[ice_age_CO2<130000]/1000,CO2[ice_age_CO2<130000], ':', color="green", linewidth=2, label='$CO_2$')
    ax6.plot(ice_age_CO2[ice_age_CO2<130000]/1000,CO2[ice_age_CO2<130000], ':', color="green", linewidth=2, label='$CO_2$')
    ax6.set_ylabel('$CO_2(ppmv)$',fontsize=10)
    ax6.set_ylim(ymin=150,ymax=300)
    ax5.set_ylim(ymin=-10,ymax=10)

    lines_for_legend=line1+line2
    labels=[l.get_label() for l in lines_for_legend]
    ax5.legend(lines_for_legend,labels,bbox_to_anchor=(1.36,0.66))
    
    ax5.axvspan(12, 115, alpha = 0.2, color='cyan')
    ax1.axvspan(0, 130, ymin=0, ymax=0.2, color = '0.0',alpha=0.7)
    ax1.annotate('Panel (e)', xy=(65,-9), xycoords='data', color='white', horizontalalignment='center',  verticalalignment='center',  fontsize=10)
    ax5.annotate('Last Glacial Maximum', xy=(26.5, -7), xycoords='data', xytext=(0.5, 0.7), textcoords='axes fraction', horizontalalignment='right', verticalalignment='top', fontsize = 10, arrowprops=dict(arrowstyle="fancy", facecolor="gold", edgecolor="black", linewidth=0.25, shrinkB=4, connectionstyle="arc3,rad=0.1",))
    
    ax1.fill_between(ice_age_deut/1000, 0, deltaTS, where=deltaTS<=0, color="blue", alpha = 0.5)
    ax1.fill_between(ice_age_deut/1000, 0, deltaTS, where=deltaTS>0, color="red", alpha = 0.5)



    
    # the tight_layout() function is a handy tool for automating the layout if
    # you are running into difficulties with seeing your axes labels properly       
    plt.savefig("PlottingExample.svg",format="svg")    
    plt.show()



# This bit at the bottom tells the python interpreter what to do if you run the
# script directly
if __name__ == "__main__":
    ice_age_deut, deut, deltaTS,ice_age_o18,o18,ice_age_CO2,CO2 = read_data_files()    
    ice_core_plot_simple(ice_age_deut, deut, deltaTS,ice_age_o18,o18,ice_age_CO2,CO2)
    ice_core_plot_final(ice_age_deut, deut, deltaTS,ice_age_o18,o18,ice_age_CO2,CO2)