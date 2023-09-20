import math

# Function to calculate the surface area and volume of a cone
def cone_surface_area_volume(radius, height):
    # Calculate the slant height (l) of the cone
    l = math.sqrt(radius**2 + height**2)
    
    # Calculate the surface area of the cone
    surface_area = math.pi * radius * (radius + l)
    
    # Calculate the volume of the cone
    volume = (1/3) * math.pi * radius**2 * height
    
    return surface_area, volume

# Function to calculate the surface area and volume of a sphere
def sphere_surface_area_volume(radius):
    # Calculate the surface area of the sphere
    surface_area = 4 * math.pi * radius**2
    
    # Calculate the volume of the sphere
    volume = (4/3) * math.pi * radius**3
    
    return surface_area, volume

# Function to calculate the surface area and volume of a cuboid
def cuboid_surface_area_volume(length, width, height):
    # Calculate the surface area of the cuboid
    surface_area = 2 * (length * width + length * height + width * height)
    
    # Calculate the volume of the cuboid
    volume = length * width * height
    
    return surface_area, volume

# Input values
cone_radius = 5
cone_height = 10
sphere_radius = 4
cuboid_length = 6
cuboid_width = 7
cuboid_height = 8

# Calculate and display surface area and volume for each shape
cone_surface, cone_volume = cone_surface_area_volume(cone_radius, cone_height)
sphere_surface, sphere_volume = sphere_surface_area_volume(sphere_radius)
cuboid_surface, cuboid_volume = cuboid_surface_area_volume(cuboid_length, cuboid_width, cuboid_height)

print(f"Surface Area and Volume of Cone:")
print(f"Surface Area: {cone_surface:.2f} square units")
print(f"Volume: {cone_volume:.2f} cubic units\n")

print(f"Surface Area and Volume of Sphere:")
print(f"Surface Area: {sphere_surface:.2f} square units")
print(f"Volume: {sphere_volume:.2f} cubic units\n")

print(f"Surface Area and Volume of Cuboid:")
print(f"Surface Area: {cuboid_surface:.2f} square units")
print(f"Volume: {cuboid_volume:.2f} cubic units")
