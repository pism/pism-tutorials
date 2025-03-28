
# Introduction to Ice Flow

The flow of glaciers can be described as Stokes flow, obeying conservation equations for *mass*, *linear momentum*, and *energy* (*angular momentum* results in a symmetric stress tensor).

## Conservation Equations
```{math}
\begin{aligned}
\textrm{mass}:  &-\nabla \cdot \mathbf{v} & = &\, 0  & \textrm{in} \, \Omega\\
\textrm{momentum}:  & \nabla \left(-p \mathrm{1} + 2 \eta \mathrm{D} \right) & = &\, \rho \mathbf{g}  & \textrm{in} \, \Omega\\
\textrm{energy}: & \frac{\mathrm{d} E}{\mathrm{d} t}
\end{aligned}
```

## Closure Equations (Material Equations)

The Stokes problem has more unknowns that equations, requiring additional equations called *closure equations* or *material equations*. These *closure equations* are not as fundamental as the *conservation equations* and are frequently determined by laboratory or field experiments.
The visosity of ice, $\eta = A(T) \left(v \right)$. Ice has a memory, which significantly complicates the simulation of glaciers.

To solve the system of PDEs we need initial and boundary conditions.
Unfortunately, the initial state cannot be described by observations alone (think of, e.g, temperature within the ice or the characteristics of the ice-bed interface).

The most widely used flow relation for glacier ice is
{cite:t}`Glen1955,Steinemann1954`
```{math}
:label: eq:Glen
\dot{\varepsilon}_{ij} = A \tau^{n-1}\sigma^{(d)}_{ij},
```
where $\dot{\varepsilon}_{ij}$ and $\sigma^{(d)}_{ij}$ are the strain rate tensor and the deviatoric stress tensor, respectively. $n \in [1, 4]$ is the exponent of the flow, with $n=3$ the most commonly used value. The rate factor $A = A(T,\ldots)$ depends on temperature and other parameters
like water content, impurity content and crystal size.  The quantity
$\tau$ is the second invariant of the deviatoric stress tensor, $\tau = \frac{1}{2}\sigma^{(d)}_{ij}\sigma^{(d)}_{ji}$.

Several properties of Equation {eq}`eq:Glen` are noteworthy:

- Elastic effects are neglected.  This is reasonable if processes on the
  time scale of days and longer are considered. But elastic effects are relevant to understand tidal flexure of ice shelves.
- Stress and strain rate are collinear, i.e. a shear stress leads to
  shearing strain rate, a compressive stress to a compressive strain rate, and
  so on.
- Only deviatoric stresses lead to deformation rates, isotropic pressure
  alone cannot induce deformation. Ice is an *incompressible* material
  (no volume change, except for elastic compression).  This is expressed as
  $
  \dot{\varepsilon}_{ii} = 0 \qquad \Longleftrightarrow \qquad
  \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} +
  \frac{\partial v_z}{\partial z} = 0 $. Incompressibility is a pretty good assumptions anywhere in a glacier execpt for firn.
- A *Newtonian viscous fluid*, like water, is characterized by
  the *viscosity* $\eta$
  ```{math}
    :label: eq:viscosity-newtonian
  \dot{\varepsilon}_{ij} = \frac{1}{2\eta} \sigma^{(d)}_{ij}.
  ```
  By comparison with Equation {eq}`eq:Glen` we find that viscosity of
  glacier ice is $\eta=\frac{1}{2A\tau^{n-1}}$.
- Polycrystalline glacier ice is a *viscous fluid* with a
  *stress dependent viscosity* (or, equivalently, a strain rate
  dependent viscosity).  Such a material is called a *non-Newtonian
    fluid*, or more specifically a *power-law fluid*.
- Polycrystalline glacier ice is treated as an \emph{isotropic fluid}. No
  preferred direction (due to crystal orientation fabric) appears in the flow
  relation.  This is a crude approximation to reality, since glacier ice
  usually is anisotropic, although to varying degrees.


Many alternative flow relations have been proposed that take into account the
compressibility of firn at low density, {cite:t}`Gagliardini1997`,
the anisotropic nature of ice, microcracks and damaged ice, {cite:}`Pralong&al2006,
the water content, impurities and different grain sizes.  Glen's flow law is
still widely used because of its simplicity and ability to approximately
describe most processes relevant to glacier dynamics at large scale.

\subsection{Inversion of the flow relation}
\label{sec:invers-flow-relat}

The flow relation of Equation {eq}`eq:Glen` can be inverted so that stresses
are expressed in terms of strain rates.  Multiplying equation {eq}`eq:Glen`
with itself gives
%
```{math}
\begin{aligned}
  \qquad \qquad\dot{\varepsilon}_{ij}\dot{\varepsilon}_{ij} & = A^2 \tau^{2(n-1)}\sigma^{(d)}_{ij}\sigma^{(d)}_{ij}
  \qquad \qquad (\textrm{multiply by }\frac{1}{2}) \notag\\
  \underbrace{\frac{1}{2}\dot{\varepsilon}_{ij}\dot{\varepsilon}_{ij}}_{\dot{\epsilon}^2} &
  = A^2
  \tau^{2(n-1)}\underbrace{\frac{1}{2}\sigma^{(d)}_{ij}\sigma^{(d)}_{ij}}_{\tau^2}
  \notag
\end{aligned}
```
%
where we have used the definition for the *effective strain rate*
$\dot{\epsilon} = \dot{\varepsilon}_e$, in
analogy to the *effective shear stress* $\tau = \sigma_e$
%
```{math}
:label: eq:epsdot-e
  \dot{\epsilon} = \sqrt{\frac{1}{2}\dot{\varepsilon}_{ij}\dot{\varepsilon}_{ij}}\,.
```
%
This leads to a relation between tensor invariants
%
```{math}
:label: eq:Glen-invariants
  \dot{\epsilon}  =  A\tau^n\,.
```
%
Coincidentally this is also the equation to describe simple shear, the most
important part of ice deformation in glaciers
%
```{math}
:label: eq:Glen-simple-shear
  \dot{\epsilon}_{xz}  =  A\sigma^{(d)}_{xz} {}^n\,.
```
%
Now we can invert the flow relation Equation {eq}`eq:Glen`
%
```{math}
:label: eq:Glen-inverse
\begin{aligned}
  \sigma^{(d)}_{ij} &= A^{-1}\tau^{1-n} \,\dot{\varepsilon}_{ij} \notag\\
  \sigma^{(d)}_{ij} &= A^{-1} A^\frac{n-1}{n}\, \dot{\epsilon}^{-\frac{n-1}{n}} \,\dot{\varepsilon}_{ij} \notag\\
  \sigma^{(d)}_{ij} &= A^{-\frac{1}{n}} \,\dot{\epsilon}^{-\frac{n-1}{n}}\, \dot{\varepsilon}_{ij}\,.
\end{aligned}
```
%
The above relation allows us to calculate the stress state if the strain rates
are known (from measurements).  Notice that only deviatoric stresses can be
calculated. The mean stress (pressure) cannot be determined because of the
incompressibility of the ice.  Comparing Equation {eq}`eq:Glen-inverse` with
{eq}`eq:viscosity-newtonian` we see that the shear viscosity is
%
```{math}
  :label: eq:viscosity-strainrate
  \eta = \frac{1}{2}A^{-\frac{1}{n}} \,\dot{\epsilon}^{-\frac{n-1}{n}}.
```
%
Polycrystalline ice is a *strain rate softening*  material: viscosity
decreases as the strain rate increases.

Notice that the viscosity given in Equation {eq}`eq:viscosity-strainrate`
becomes infinite at very low strain rates, which of course is unphysical.  One
way to alleviate that problem is to add a small quantity $\eta_{o}$ to
obtain a \*finite viscosity*
%
```{math}
  :label: eq:viscosity-strainrate-finite
  \eta^{-1} = \left( \frac{1}{2}A^{-\frac{1}{n}} \,\dot{\epsilon}^{-\frac{n-1}{n}} \right)^{-1} + \eta_0^{-1}.
```
