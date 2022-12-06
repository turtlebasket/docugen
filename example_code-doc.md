# Documentation for `example_code.py`

## `remove_dirt(image)`
This function removes small dirt and noise from a binary image by closing small holes and removing small objects.

Here is an example of how to use the function:

```
import skimage.morphology as morphology
from skimage import data

# Load a binary image
image = data.coins() > 100

# Remove dirt from the image
cleaned_image = remove_dirt(image)
```

## `center_of_mass(X)`
This function calculates the center of mass of a 2D shape defined by a set of points.

Here is an example of how to use the function:

```
import numpy as np

# Define a set of points that define a shape
X = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])

# Calculate the center of mass of the shape
center_of_mass = center_of_mass(X)

# Print the center of mass
print(center_of_mass)
```

The output will be `[0.5, 0.5]`, which is the coordinates of the center of the square defined by the points `X`.

## `center_of_mass(X)`
This function calculates the center of mass of a 2D shape defined by a set of points.

Here is an example of how to use the function:

```
import numpy as np

# Define a set of points that define a shape
X = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])

# Calculate the center of mass of the shape
center_of_mass = center_of_mass(X)

# Print the center of mass
print(center_of_mass)
```

The output will be `[0.5, 0.5]`, which is the coordinates of the center of the square defined by the points `X`.

