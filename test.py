import matplotlib.pyplot as plt

def plot_coordinates_with_lines(coordinates):
    # Create a new figure
    plt.figure()

    # Plot each point one by one
    for i, (y, x) in enumerate(coordinates):
        plt.scatter(x, y, color='blue', label=f'Point {i+1}')
        plt.pause(1)  # Pause for 1 second between points

    # Connect the points with lines
    y_values, x_values = zip(*coordinates)
    plt.plot(x_values + (x_values[0],), y_values + (y_values[0],), linestyle='-', color='red', label='Connecting Line')

    # Set labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plotting Coordinates with Connecting Lines')

    # Display legend
    plt.legend()

    # Show the plot
    plt.show()

# Example usage with a list of coordinates
#coordinates_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
#plot_coordinates_with_lines(coordinates_list)
if __name__ == "__main__":

    coordinates_list = [(7, 6), (6, 6), (7, 7), (5, 6), (7, 8), (7, 9), (5, 7), (6, 9), (5, 8), (5, 9), (4, 8), (4, 9), (3, 9), (3, 8), (2, 9), (2, 8), (1, 9), (2, 7), (1, 8), (1, 7), (2, 6), (1, 6), (1, 5), (2, 5), (1, 4), (1, 3), (2, 4), (1, 2), (1, 1), (2, 3), (2, 2), (2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (7, 1), (5, 3), (7, 2), (7, 3), (5, 4), (6, 4), (7, 4)]
    plot_coordinates_with_lines(coordinates_list)
