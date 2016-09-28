#piv calculations
#steve brust
import numpy as np

#camera type that I use regularly; future option would be to have a dropdown menu to access different camera types
#Imperx B1610M Bobcat
#http://www.imperx.com/wp-content/uploads/B1610_2MP_CCDCamera_Specs.pdf

#inputs
focal_length=72. #[mm]
obj_dist= 800.#[mm]
f_stop = 5.6#[-]
wavelength= 532.#[nm]
dt= 2.5#[us]
vel= 250.#[m/s]

#d_particle = 1. #[um] 

#camera inputs
#res_x = 1620. #[pix] #standard values
res_x = 1628 #for Bobcat; the max. values
#res_y = 1220. #[pix]
res_y = 1236
pix_size = 4.4 #[um]

#Desired outputs
#magnification, 0.07758 check 
#image distance, 77.586 check
#resolution [pix/mm], 17.633228 check
#FOV x [mm], 92.325688 check
#FOV y [mm], 70.094933 check
#Focal depth [mm], 15.705165 check
#Diffr. spot size [pix], 1.7802821 check
#dx [mm], 0.64 check
#dx [pix], 11.285266 check

#per thin lens formula
D = focal_length/f_stop #lens aperature diameter

img_dist = 1./((1./focal_length) - (1./obj_dist))
print "img_dist = ", img_dist #done
M = img_dist/obj_dist
print "Magnification, M = ", M #done

fov_x = (pix_size/1e3)*res_x/M
fov_y = (pix_size/1e3)*res_y/M
print "FOV x = ", fov_x #done
print "FOV y = ", fov_y #done

resolution = res_x/fov_x #Same for y-dr
print "Resolution = ", resolution 

dx_mm = vel*(dt*10**(-6))*1000
print "dx [mm] = ", dx_mm #done

dx_pix = dx_mm*resolution
print "dx [pix] = ", dx_pix #[pix] done

focal_depth = 1000*4.88*(wavelength*1e-9)*(f_stop**2)*((M+1)/M)**2
print "Focal depth = ", focal_depth #[mm] done

d_diff = 2.44*(wavelength*1e-9)*(1+M)*f_stop
print "Diff. spot size [pix] = ", d_diff*(1e6)/pix_size

###
#finished computations above
###

#focal_depth = 4.88*(532e-9)*(f_stop**2)*((M+1)/M)**2
#print "focal_depth = ", focal_depth

#d_geom = M*1e-9
#print "d_geom = ", d_geom
#d_diff = 2.44*wavelength*(1+M)*f_stop
#d_geom = M*d_particle
#d_tau = np.sqrt((M*d_particle)**2 + d_diff**2)
#print "d_diff = ", d_diff
#print "d_tau = ", d_tau
