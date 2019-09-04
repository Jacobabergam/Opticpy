# Custom Ray tracer for optical engineering and system design

"""
Note: I mention zemax here. It is important to state reason for
writting own code compared to using ray tracing in zemax.
Zemax cannot use GPU acceleration. Zemax also will not allow me to
scale up the computer using a cloud service to compute intensive
data sets.
Zemax will provide a valuable calibration for this toolset though.
"""

"""Goal: To write a ray tracer for wavelength specturm and implement
various light/surface interactions and different optical systems to 
be simulated on cloud computers. Current optical simulation tools 
do not allow for Cloud useage and are therfor bottle-necked. Zemax 
is unable to even use GPU acceleration, which is severlly limiting.

Goal is to accelearte ray sim as fast as possible, and allow option to 
use GPU in cloud system to calculate large data sets to be used when evaluating 
lens changes and system impact"""

# class Scene:
"""Here we will layout the whole optical scene. This will include
but not limited to: Camera, objects, sources, scene width, scene
height.
We will also include the following funcionts:

render: Render the scene
_Trace_ray: recursively trace ray through scene, set a max number of
reflections (perhaps or just simply use dispersion and BRDF models
to define scatter functions from bluk/atmospher and surface interaction.
    Scatter fuction impact would be defined in object properties.
    Scatter would act as new source with distribution of the ray energy
    being integrated over radiant profile. To save space we can decide to
    ignore rays that would be lower than some threshold energy/intensity.
    Trace_ray will work genericly with all objects, sources, bulk media
_get_intersection: should return which object in scene the ray intesected
and the distnace to it.

Note that we will want a ray to keep track of its total path length,
if from DC source we will want to turn this functionality off OR give generic
dc distance signal. Can model impact from other pulsed sources in future.

"""

# class Vector
""" Generic 3D vector for ray loation calculations. consider using
C++ wrapped function in python"""

# class objects:
""" Define shape and intersection algorithm for different objects.
Simples are spheres, boxes, triangles.  Here would
also benefit from being implemented as C++ wrapped in python.
Will call to Material for interaction properties.
Ideal in future to import STL objects from CAD models.

"""

# class Materials:
"""Here we will define scater profile, index of refraction,
coating over wavelength. These profiless/materials/coating profiles are
likely best stored as text files or in a database of functions.
Zemax has good data base, consider taking advantage of their data.
Data collected can get very large, ideal is to define scatter from surface
interaction as generic function if possible. Sertain surfaces may require
us to effectively match the data set.
"""

# class Sensor:
"""
Here we will define the Rx optical system.
Initially should define such that we have an opening aperture that
collects rays (defines collection aperture) then we apply generic
mapping that turns ray incidence angle on aperture surface to a location
on the detector.

Here we also define number of pixels on the detector, hx and hy.
We also should define material to restrict which waveleneghts we consider.
Data out will likely be in the form of intensity and time (or the ray path length)


Later we would like to define a full lens object including baffle system. This
is very in depth but may give us insight into stray light analysis and ghost images
of our system. Ideal would be to define lenses as specific element objects with their
own glass/coating/scatter and define lens barrel and stop as objects as well. Then we
define detector in physical space and allow any ray incident, regardless of angle,
to influence read-out.

ideally would like to model scater impact of lens elements. Would be ideal to model
a scratch on the outmost surfac, a specific dust pattern (could be randomized via a random
dust function. should match physical measurements and ISO standard cleanliness and
particle size/distirbution on surface).  Scratch profile also should fit
ISO standard scratch def and be a randomizes function. tool to visualize in x/y as a
specific plot. This in this system would be good to keep track of which dust/scratch in system
is producing the most noise to better learn system limits. Ray should keep track of
its incidence on each lens surface or if any incidence on scratch/dust/barrel. This would
allos us to turn off/on stray light and define what rays/ghost images are caused by which
surface interactions. Also want to keep trac of rays from double bounce in system and
object/use-cases that cause lots of stray light.

"""

# class Ray:
"""
A mathematical ray. Has location, direction, intensity, wavelength, and OPL.

functions:

point_at_dist location + (direction * distance)
"""

# class source:
"""
Define sources: Look to Zemax for typical sources. Consider allowing STL and CAD
model act as source with defined radiant profile function and emission profile (wavelength)

Here we define the generic source as a point source. This will act as starting point for
system. Define BW to be narrow for out Tx system.

Later define Pulse width as a function to get idea of what signal on detector may look like
for typical objects. (impact of environement on pulse width, i.e. scattering and uncertain
path length)

Later give broad spectrum (defined by detector bw so as to not needlessly over whelm
physic engine). Apply generic source function as txt file for wavelength. apply generic
radiance as txt file and weight based on energy or power in system.
"""

""" 
Future tools could include:
multiple shots: define a realistic/changing wavelength and pulse width
Thermal impact: change material R+T+A over wavelength as well as errors from
    improper athermaliszation. Use thermal model (or add in some thermal characterstics)
    to determin source wavelength dist shift over temp.
    
    For lens element, Consider! End all rays in a simulation at a flat plan of
    equal diameter (or a little later) than first element and ~1 inch in front (or other).
    Then save all ray location/intensities/angle/wavelength on that surface in bit format.
    This allows us to analyse the same scene with various lens configurations. Meaning
    we can change lens elements, barrel structure, AR coating, BP elements, Baffles, thermal expansion,
    defocus, missalignemnet and compare exactly the impact on the full scene previosly calculated. 

Detector ROIC architecture: SPAD vs PIN or other. exact system to turn photons to electrons
Moving targets/scenes: study many scenes and how they interact, new sources coming into view
    etc. 
Model Rain/snow: Model changing atmosphere shot to shot. Fixed scene that has game engine
    to define falling snow/rain (or simple physics engine). 
    ->This will explode complexity and number of calculations. Best is to add in rain/snow as volume
    scatter/absorbtion function at first, then as real rain drops of random size/distribution.
"""
