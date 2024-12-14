# Description: Generate the standard map for some value of the parameter K.

# ---------- Imports ---------- 

import numpy as np
import matplotlib.pyplot as plt
import random
import sys
from numba import jit

# ---------- Functions ----------

@jit(nopython=True)
def computeTrajectory(p,phi,K,N): # Compute trajectory to plot with random IC
    for i in np.linspace(1,N-1,N-1).astype('int'):
        p[i] = (p[i-1] + K*np.sin(phi[i-1]))%(2*np.pi) # Update state according to standard map
        phi[i] = (phi[i-1] + p[i])%(2*np.pi)

@jit(nopython=True)
def burn(p0,phi0,K,Nburn): # Burn in
    p_ = (p0 + K*np.sin(phi0))%(2*np.pi) # Set initial value
    phi_ = (phi0 + p_)%(2*np.pi)
    for i in np.linspace(0,Nburn-1,Nburn).astype('int'): # Iterate map for Nburn time steps
        p_ = (p_ + K*np.sin(phi_))%(2*np.pi)
        phi_ = (phi_ + p_)%(2*np.pi)
    return p_,phi_ # Return final values, to be used as initial conditions for the trajectory that will be plotted

def generateMap(num_orbits,K,N,Nburn,save): # Generate standard map for certain K
    fig = plt.figure(figsize=(12,10))
    colors = plt.cm.hsv(np.linspace(0,1,num_orbits)) # Set color map
    #random.shuffle(colors) # Randomize ordering of colors
    p = np.zeros([N]) # Initialize arrays for p and phi
    phi = np.zeros([N])
    for i in np.linspace(0,num_orbits-1,num_orbits): # Generate num_orbits trajectories to build up the map
        p0 = np.random.uniform(low=0,high=2*np.pi) # Set random initial conditions in domain
        phi0 = np.random.uniform(low=0,high=2*np.pi)
        p[0],phi[0] = burn(p0,phi0,K,Nburn) # Burn in
        computeTrajectory(p,phi,K,N) # Compute trajectory after burn in
        plt.scatter(phi,p,s=1,color=colors[int(num_orbits-1)-int(i),:]) # Plot trajectory
    plt.title(f'K = {K}')
    if save:
        plt.savefig(f'Standard Map for K = {K}.png',dpi=fig.dpi)
    else:
        plt.show()

# ---------- Main ----------

seed = 358348583
np.random.seed(seed) # Set random number generator seed

if len(sys.argv) == 1:  
    K = 0.971635 # K value
elif len(sys.argv) == 2:
    K = float(sys.argv[1])
N = 400 # Number of points to plot for each orbit
Nburn = 500 # Number of burn in steps
num_orbits = 1500 # Number of orbits to plot

save = False # Save figure

generateMap(num_orbits,K,N,Nburn,save)