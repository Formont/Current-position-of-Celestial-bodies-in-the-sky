import ephem, matplotlib.pyplot as plt
import numpy as np

#Convert into decimal system
def convert_to_decimal(angle):
    parts = str(angle).split(':')
    deg, min, sec = float(parts[0]), float(parts[1]), float(parts[2])
    res = deg + (min / 60) + (sec/3600)
    return res
 
time = ephem.now()

obs = ephem.Observer()

obs.lat, obs.lon, obs.date = '12', '41', time
#Create planets
J = ephem.Jupiter()
S = ephem.Saturn()
U = ephem.Uranus()
N = ephem.Neptune()
M = ephem.Mars()
V = ephem.Venus()
Me = ephem.Mercury()
Sun = ephem.Sun()
Moon = ephem.Moon()
pl = ephem.Pluto()


J.compute(obs)

S.compute(obs)

U.compute(obs)

N.compute(obs)

M.compute(obs)

V.compute(obs)

Me.compute(obs)

Sun.compute(obs)

Moon.compute(obs)

pl.compute(obs)
#Create cooordinates
alt =np.arange(-90, 90)
az = np.arange(0, 360, 2)

#Settings of the plot 
plt.title("Position of Celestial Bodies")
plt.xlabel("azimuth")
plt.ylabel("altitude")
plt.ylim(-90, 90)
plt.xlim(0, 360)
plt.yticks(range(-90, 91, 10))
plt.plot([0,360], [0, 0], color='red', label="horizon")
plt.get_current_fig_manager().set_window_title('Position of Celestial Bodies')


#planets on the plot
plt.scatter(convert_to_decimal(J.az), convert_to_decimal(J.alt), color=(255/255, 165/255, 0), label='Jupiter', s=6)

plt.scatter(convert_to_decimal(S.az), convert_to_decimal(S.alt), color='orange', label='Saturn', s=6)

plt.scatter(convert_to_decimal(U.az), convert_to_decimal(U.alt), color='lightblue', label='Uranus', s=6)

plt.scatter(convert_to_decimal(N.az), convert_to_decimal(N.alt), color='blue', label='Neptune', s=6)

plt.scatter(convert_to_decimal(M.az), convert_to_decimal(M.alt), color='red', label='Mars', s=6)

plt.scatter(convert_to_decimal(V.az), convert_to_decimal(V.alt), color='#FFE8CE', label='Venus', s=6)

plt.scatter(convert_to_decimal(Me.az), convert_to_decimal(Me.alt), color='lightgrey', label='Mercury', s=6)

plt.scatter(convert_to_decimal(Moon.az), convert_to_decimal(Moon.alt), color='grey', label='Moon', s=30)

plt.scatter(convert_to_decimal(pl.az), convert_to_decimal(pl.alt), color='brown', label='Pluto', s=4)

plt.scatter(convert_to_decimal(Sun.az), convert_to_decimal(Sun.alt), color='yellow', label='Sun', s=30)

plt.legend(loc=4)
plt.show()