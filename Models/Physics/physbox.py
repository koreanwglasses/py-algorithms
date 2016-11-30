import numbers

class ParticleBox:
    def __init__(self, particles, force_func):
        self.particles = particles
        self.force_func = force_func

    def step(self, dt):
        for p1 in self.particles:
            for p2 in self.particles:
                if p1 != p2:
                    p1.force += self.force_func(p1, p2)
        for p in self.particles:
            p.step(dt)

    def state(self):
        return [p.to_tuple() for p in self.particles]

class Particle:
    def __init__(self, mass, radius, init_position, init_velocity):
        self.mass = mass
        self.radius = radius
        self.position = init_position
        self.velocity = init_velocity

        self.force = Vector3(0,0,0)
    
    def kinetic_energy(self):
        return 0.5 * self.mass * self.velocity.mag2()

    def step(self, dt):
        acceleration = self.force * self.mass
        self.velocity += acceleration * dt
        self.position += velocity * dt
        
        self.force = Vector3(0,0,0)

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_tuple():
        return (self.x, self.y, self.z)

    def __abs__(self):
        return Math.sqrt(x**2 + y**2 + z**2)
    def mag2(self):
        return x**2 + y**2 + z**2
    def mag(self):
        return Math.sqrt(mag2(self))

    def nor(self):
        return self / mag(self)

    def __iadd__(self, other):
        if isinstance(other, Vector3):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        elif isinstance(other, tuple):
            self.x += other[0]
            self.y += other[1]
            self.z + other[2]
            return self
        else:
            raise TypeError()
    def __radd__(self, other):
        if other == 0:
            return Vector3(self.x, self.y, self.z)
        else:
            return __add__(self, other)
    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, tuple):
            return Vector3(self.x + other[0], self.y + other[1], self.z + other[2])
        else:
            raise TypeError()

    def __rsub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(other.x - self.x, other.y - self.x, other.z - self.z)
        elif isinstance(other, tuple):
            return Vector3(other[0] - self.x, other[1] - self.y, other[2] - self.z)
        else:
            raise TypeError()    
    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, tuple):
            return Vector3(self.x - other[0], self.y - other[1], self.z - other[2])
        else:
            raise TypeError()

    def __rmul__(self, other):
        return __mul__(self, other)
    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Vector3(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3):
            raise TypeError('Ambiguous operation. Use v1.dot(v2) or v1.crs(v2) instead.')
        else:
            raise TypeError()

    def __div__(self, other):
        if isinstance(other, numbers.Number):
            return Vector3(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError()

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import mpl_toolkits.mplot3d.axes3d as p3
    import matplotlib.animation as animation

    def force_func(p1, p2):
        r2 = (p1 - p2).mag2()
        f = p1.mass * p2.mass / r2
        return (p2 - p1).nor() * f

    box = ParticleBox([
        Particle(1, .1, Vector3(1, 0, 0), Vector3(0, 0, 0)),
        Particle(1, .1, Vector3(-1, 0, 0), Vector3(0, 0, 0))
    ], force_func)
    dt = 1 / 60.0

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False)

    particles = ax.scatter([], [], [])

    def init():
        global particles
        particles = ax.scatter([], [], [])
        return particles,
    
    def animate(i):
        global particles
        box.step(dt)

        xs, ys, zs = zip(*box.state())
        particles = ax.scatter(xs, ys, zs)
        return particles,

    anim = animation.FuncAnimation(fig, animate, frames=600, interval=dt * 1000, blit=True, init_func=init)

    plt.show()