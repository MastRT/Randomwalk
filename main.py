import matplotlib.pyplot as plt
from random_walk import RandomWalk

#keep making new walks as long as the program is active
while True:
    # make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    ax = plt.subplot()
    ax.scatter(rw.x_values,rw.y_values,s=10)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break