import matplotlib.pyplot as plt
from random_walk import RandomWalk

#keep making new walks as long as the program is active
while True:
    # make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    ax = plt.subplot(figsize=((10,6)),dpi=300)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,
               c=point_numbers,cmap=plt.cm.Blues,
               edgecolors='none',s=1)
    ax.set_aspect('equal')
    # Emphasize the first and last points
    ax.scatter(0,0,c='black',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break