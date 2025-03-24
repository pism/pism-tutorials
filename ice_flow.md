The flow of glaciers can be described as Stokes flow, obeying conservation equations for *mass*, *linear momentum*, and *energy* (*angular momentum* results in a symmetric stress tensor)

### Conservation Equations
$$
\begin{aligned}
\textrm{mass}:  &\nabla \cdot \mathbf{v} & = & 0 \\
\textrm{momentum}:  & \nabla \left( \eta \nabla \cdot \mathbf{v} \right) - \rho \mathbf{g} & = & 0 \\
\textrm{energ}: & \frac{\mathrm{d} E}{\mathrm{d} t}
\end{aligned}
$$

### Closure Equations (Material Equations)

The Stokes problem has more unknowns that equations, requiring additional equations called *closure equations* or *material equations*. These *closure equations* are not as fundamental as the *conservation equations* and are frequently determined by laboratory or field experiments.
The visosity of ice, $\eta = A(T) \left(v \right)$. Ice has a memory, which significantly complicates the simulation of glaciers.

To solve the system of PDEs we need initial and boundary conditions.
Unfortunately, the initial state cannot be described by observations alone (think of, e.g, temperature within the ice or the characteristics of the ice-bed interface).

mass: initial ice geometry $\Omega_0$
momentum:
energy: initial energy field $E_0$
$$
\begin{aligned}
\textrm{mass}:  & \textrm{ice geometry} \Omega_0 \\
\textrm{momentum}: & \textrm{}  \\
\textrm{energy}: & \textrm{energy} E_0
\end{aligned}
$$
