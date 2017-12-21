# http://adventofcode.com/2017/day/20
import re
from ast import literal_eval


# === Part 1 ====

class Particle(object):
    def __init__(self, id, p, v, a):
        self.id = id
        self.p = p
        self.v = v
        self.a = a

    def __str__(self):
        return "<Particle id=" + str(self.id) + ",p=" + str(self.p) + ",v=" + str(self.v) + ",a=" + str(self.a) + ">"


def parse(input):
    particles = []
    for idx, line in enumerate(input.splitlines()):
        p = re.compile('p=<(-?\d+,-?\d+,-?\d+)>, v=<(-?\d+,-?\d+,-?\d+)>, a=<(-?\d+,-?\d+,-?\d+)>')
        m = p.match(line)
        pos, vel, acc = m.groups()
        particles.append(Particle(idx, literal_eval(pos), literal_eval(vel), literal_eval(acc)))
    return particles


def particle_swarm(input, ticks):
    particles = parse(input)

    for tick in range(ticks):
        update_particles(particles)

    particles.sort(key=manhattan_distance)
    return particles[0]


def update_particles(particles):
    for particle in particles:
        update_velocity(particle)
        update_position(particle)


def update_position(particle):
    (x, y, z) = particle.p
    (vx, vy, vz) = particle.v
    particle.p = (x + vx, y + vy, z + vz)


def update_velocity(particle):
    (vx, vy, vz) = particle.v
    (ax, ay, az) = particle.a
    particle.v = (vx + ax, vy + ay, vz + az)


def manhattan_distance(particle):
    (x, y, z) = particle.p
    return abs(x) + abs(y) + abs(z)


# example_input = """p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
# p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>
# """

# puzzle_input = open('day20.txt').read()
# print particle_swarm(puzzle_input, 3000)


# ==== Part 2 ====

def particle_swarm_2(input, ticks):
    particles = parse(input)

    for tick in range(ticks):
        update_particles(particles)
        particles = remove_collisions(particles)

    return len(particles)


def remove_collisions(particles):
    collisions = set()
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            if particles[i].p == particles[j].p:
                collisions.add(particles[i])
                collisions.add(particles[j])

    return [p for p in particles if p not in collisions]


# example_input = """p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
# p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
# p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
# p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>
# """

puzzle_input = open('day20.txt').read()
print particle_swarm_2(puzzle_input, ticks=1000)
