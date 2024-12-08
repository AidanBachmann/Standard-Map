<p align="center">
<img width="500" alt="CB" src="https://github.com/user-attachments/assets/bf421467-3190-4d65-abfd-e6672065044b">
</p>

# Overview
This code generates the stadard map for a specific value of the parameter $K$. Usually taken on the interal $p,\phi\in [0,2\pi ]$, the map is given by the equations

$p_{n+1} = p_{n} + K\sin{\theta_{n}}$

and

$\theta_{n+1} = \theta_{n} + p_{n+1},$

which can be derived form the unitless form of the kicked rotor Hamiltonian:

$H(p,\theta ) = \frac{p^2}{2} + K\sin{\theta}\displaystyle\sum_{n=-\infty}^{\infty}\delta (t - n).$

For smaller values of $K$ ($K\sim 0.1$), the map is mostly stable. However, as $K$ increases, the map exhibits chaotic behavior (i.e., some orbits are area filling). The figure at the top was generated using $K = 0.971635$, which exhibits large regions of choas with several basins of stability.

# Usage
To generate a map, clone the repository using
```sh
git clone https://github.com/AidanBachmann/Standard-Map.git
```
and cd into the directory. Then, simply run
```sh
python3 main.py
```
This will generate a map with the default value $K = 0.971635$. This repository depends on numba, matplotlib, and numpy, so be sure to install these dependencies before running. To change the $K$ value, density of orbits, and number of iterations plotted per orbit, open the main function in your preferred editor and alter the parameters at the bottom of the file. Each parameter that the user can change has a comment with an explanation of the variable.

# Features to Come
At some point, I will add command line arguments so you can change parameters from the terminal. Additionally, there is another version of the code that can generate gifs showing how the standard map changes as a funciton of $K$. Once this code is cleaned up, I will also add it to this repository. Below, you can find an example of one such gif. Note that the resolution has been reduced (github does not allow files larger than 10MB) and an older color map is used.

<p align="center">
<img width="500" alt="CB" src="https://github.com/user-attachments/assets/45c2c5c3-dc98-404b-b76d-0514c8b00792">
</p>
