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
To generate \begin{minted}{python main.py}
