#isentropic flow
#steve brust

#input
M = 2.
gamma = 1.4
print M

#want to output: p0p rho0rho t0t aa_crit
t0t = (1+((gamma-1)/2)*(M**2))
print t0t
rho0rho = t0t**(1/(gamma - 1))
p0p = rho0rho**gamma
print rho0rho
print p0p
aa_crit = ((1/M**2)*(2/(gamma+1)*t0t)**((gamma+1)/(gamma-1)))**0.5
print aa_crit