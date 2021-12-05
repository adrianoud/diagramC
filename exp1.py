from matplotlib import pyplot as plt
from celluloid import Camera
import numpy as np
fig = plt.figure()
camera = Camera(fig)


t = np.linspace(0, 2 * np.pi, 128, endpoint=False)

for i in t:
    plt.plot(t, np.sin(t + i), color='blue')
    camera.snap()

animation = camera.animate()
animation.save('celluloid_minimal.gif', writer = 'imagemagick')