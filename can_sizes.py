import math

def compute_storage_efficiency(name, radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{name} {storage_efficiency:.2f}")

def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    compute_storage_efficiency(name, radius, height)
    
    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    compute_storage_efficiency(name, radius, height)
    
    name = "#2"
    radius = 8.73
    height = 11.59
    compute_storage_efficiency(name, radius, height)
    
    name = "#2.5"
    radius = 10.32
    height = 11.91
    compute_storage_efficiency(name, radius, height)
    
    name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    compute_storage_efficiency(name, radius, height)
    
    name = "#5"
    radius = 13.02
    height = 14.29
    compute_storage_efficiency(name, radius, height)
    
    name = "#6Z"
    radius = 5.40
    height = 8.89
    compute_storage_efficiency(name, radius, height)
    
    name = "#8Z short"
    radius = 6.83
    height = 7.62
    compute_storage_efficiency(name, radius, height)
    
    name = "#10"
    radius = 15.72
    height = 17.78
    compute_storage_efficiency(name, radius, height)
    
    name = "#211"
    radius = 6.83
    height = 12.38
    compute_storage_efficiency(name, radius, height)
    
    name = "#300"
    radius = 7.62
    height = 11.27
    compute_storage_efficiency(name, radius, height)
    
    name = "#303"
    radius = 8.10
    height = 11.11
    compute_storage_efficiency(name, radius, height)

def compute_volume(radius, height):
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius**2 + 2 * math.pi * radius * height

main()