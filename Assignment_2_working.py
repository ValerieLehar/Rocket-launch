# Valerie Lehar
#261205467
#Program designed to gain info about a rocket and
#apply computations to output to the user helpful
#information.
'''
Add doc strings
'''
import math

FT_M_CONVERSION = 3.28 # Feet to meter conversion
APPROX_DENSITY = 1.225 #kg/m^3 Density used to calculate mass
TAX = 1.15 #15% tax in quebec added to price
WEIGHT_MIN = 20 #kg, min weight of boxes storable in the rocket
WEIGHT_MAX = 500 #kg, max weight of boxes storable in the rocket
VOLUME_MIN = 0.125 #m^3, min volume of boxes storable in the rocket
INITIAL_STORAGE_USED = 0 #m^3, initial storage in use
INITIAL_WEIGHT = 0 #initial weight added through storage boxes
DONE_INITIAL = 0 #place holder value before boolean is assigned
GRAVITY = -9.81 #m/s^s acceleration due to gravity
INITIAL_TIME = 0 #Inicial time when simulation starts

def feet_to_meter(length_in_feet):
    '''
    Converts measurements in feet to meters and rounds
    the answer to 2 decimal places.
    
    Args:
        length_in_feet (float): measurement in feet
    
    Returns:
        float: measurement in meters rounded to 2 decimals
    
    Examples:
    
    >>> feet_to_meter(100.0)
    30.49
    
    >>> feet_to_meter(5.0)
    1.52
    
    >>> feet_to_meter(253.0)
    77.13
    '''
    length_in_meters = length_in_feet / FT_M_CONVERSION
    length_in_meters = round(length_in_meters, 2)
    return length_in_meters

#length_in_meters = feet_to_meter(253)
#print (length_in_meters)
    
def rocket_volume(radius, height_cone, height_cyl):
    '''
    Calculates the volume (to 2 decimal places) of the rocket under
    the assumption that the rocket is a cylinder with a cone on top.
    
    Args:
        radius (float): radius of the rocket in meters
        height_cone (float): height of the cone in meters
        height_cyl (float): height of the cylinder in meters
    
    Returns:
        float: volume of the rocket in m^3, rounded
        to 2 decimal places
    
    Examples:
    
    >>> rocket_volume(100.0, 10.0, 20.0)
    733038.29
    
    >>> rocket_volume(33.0, 300.0, 123.0)
    762926.35
    
    >>> rocket_volume(10.0, 30.0, 40.0)
    15707.96
    '''
    v_cone = math.pi * radius**2 * (height_cone/3)  #formula for volume of cone
    v_cyl = math.pi * radius**2 * height_cyl        #formula foe cylinder volume 
    v_rocket = v_cone + v_cyl
    v_rocket = round (v_rocket, 2)
    return v_rocket

#v_rocket = rocket_volume(10, 30, 40)
#print (v_rocket)

def rocket_area(radius, height_cone, height_cyl):
    '''
    Calculates the surface area of the rocket
    (rounded to 2 decimals) under the assumption that the
    rocket is a cylinder with a cone on top.
    
    Args:
        radius (float): radius of the rocket in meters
        height_cone (float): height of the cone in meters
        height_cyl (float): height of the cylinder in meters
        
    Returns:
        float: the suface area of the rocket in m^2 and
        rounded to 2 decimal places
    
    Examples:
    
    >>> rocket_area(10.0, 20.0, 30.0)
    2901.6
    
    >>> rocket_area(33.0, 120.0, 45.0)
    25654.27
    
    >>> rocket_area(78.0, 31.0 100.0)
    88689.96
    '''
    area_cone = math.pi * radius * (radius + math.sqrt
                                    (height_cone**2 + radius**2)) #forumla of are of cone
    area_cyl = 2 * math.pi * radius * (height_cyl + radius)
    area_circle = math.pi * radius**2 #Needed as to not count the circle's between cone and cyl.
    area_rocket = area_cone + area_cyl - 2 * area_circle
    area_rocket = round(area_rocket, 2)
    return area_rocket

#area_rocket = rocket_area(78, 31, 100)
#print(area_rocket)

def rocket_mass(radius, height_cone, height_cyl):
    '''
    Calculates the mass of the rocket (rounded to 2 decimals)
    under the assumption that the rocket is a cylinder with a
    cone on top and using an aproximation for density.
    
    Args:
        radius (float): radius of the rocket in meters
        height_cone (float): height of the cone in meters
        height_cyl (float): height of the cylinder in meters
        
    Returns:
        float: the mass of the rocket in kg and
        rounded to 2 decimal places
    
    Examples:
    
    >>> mass_rocket(39.0, 25.0, 12.0)
    119021.05
    
    >>> mass_rocket(100.0, 133.0, 4.0)
    1860084.65
    
    >>> mass_rocket(7.0, 81.0 22.0)
    9240.13
    '''
    mass_rocket = rocket_volume(radius, height_cone, height_cyl) * APPROX_DENSITY #line can not be split
    mass_rocket = round(mass_rocket, 2)
    return mass_rocket

#mass_rocket = rocket_mass(7, 81, 22)
#print (mass_rocket)

def rocket_fuel(radius, height_cone, height_cyl, velocity_e, velocity_i, time):
    '''
    Calculates the fuel required (rounded to 2 decimal places)
    in kg, based on the mass of the rocket
    
    Args:
        radius (float): radius of the rocket in meters
        height_cone (float): height of the cone in meters
        height_cyl (float): height of the cylinder in meters
        velocity_e (float): exhaust velocity in m/s
        velocity_i (float): initial velocity in m/s
        time (float): time of trip in seconds
    
    Returns:
        float: fuel required for the trip rounded to 2 decimals
    
    Examples:
    
    >>> rocket_fuel(10.0, 20.0, 30.0, 40.0, 50.0, 60.0)
    116741.18
    
    >>> rocket_fuel(33.0, 48.0, 100.0, 34.0, 76.0, 99.0)
    4328372.12
    
    >>> rocket_fuel(23.0, 34.0, 45.0, 56.0, 56.0, 67.0)
    331061.36
    '''
    rocket_mass1 = rocket_mass(radius, height_cone, height_cyl)
    fuel_rocket_1 = rocket_mass1 * (math.e**
                                    (velocity_i/velocity_e) - 1) #rocket fuel formula
    if rocket_mass1 < 100000:    #Approximations for simplicity sake
        fuel_rocket_spent = 1360
    elif rocket_mass1 < 400000:
        fuel_rocket_spent = 2000
    else:
        fuel_rocket_spent = 2721
    fuel_required = fuel_rocket_1 + fuel_rocket_spent * time
    fuel_required = round(fuel_required, 2)
    return fuel_required

#fuel_required = rocket_fuel(23.0, 34.0, 45.0, 56.0, 56.0, 67.0)
#print (fuel_required) 
    
def calculate_cost(radius, height_cone, height_cyl, velocity_e, velocity_i, time, tax): #can not be split
    '''
    Calculates the cost of the space trip (rounded to 2 decimals)
    based on the fuel price, materials and tax inclusion
    
    Args:
        radius (float): radius of the rocket in meters
        height_cone (float): height of the cone in meters
        height_cyl (float): height of the cylinder in meters
        velocity_e (float): exhaust velocity in m/s
        velocity_i (float): initial velocity in m/s
        time (float): time of trip in seconds
        tax (boolean): decides if tax is considered
    
    Returns:
        float: total price of the trip rounded to 2 decimals
    
    Examples:
    
    >>> calculate_cost(10.0, 20.0, 30.0, 40.0, 50.0, 60.0, True)
    835623.58
    
    >>> calculate_cost(33.0, 48.0, 100.0, 34.0, 76.0, 99.0, False)
    26554042.83
    
    >>> calculate_cost(23.0, 34.0, 45.0, 56.0, 56.0, 67.0, True)
    2386398.92
        
    '''
    cost_of_materials = 5 * rocket_area(radius, height_cone, height_cyl) #5$ per m^2 area
    cost_of_fuel = 6.1 * rocket_fuel(radius, height_cone, height_cyl, velocity_e, velocity_i, time) #Can not be split #6.1$ per kg fuel
    if tax == True:
        cost = (cost_of_materials + cost_of_fuel) * TAX
    else:
        cost = cost_of_materials + cost_of_fuel
    cost = round(cost, 2)
    return cost

#price = calculate_cost(23.0, 34.0, 45.0, 56.0, 56.0, 67.0, True)
#print(price)

def compute_storage_space(radius, height_cyl):
    '''
    Calculates storage space of rocket in m^3 rounded to
    two decimal places
    
    Args:
        radius (float): radius of the rocket in meters
        height_cyl (float): height of the cylinder in meters
        
    Returns:
        float: storage width in m and 2 decimal places
        float: storage length in m and 2 decimal places
        float: storage height in m and 2 decimal places
    
    Examples:
    
    >>> compute_storage_space(39.0, 41.0)
    55.15
    55.15
    20.5
    
    >>> compute_storage_space(23.0, 99.0)
    32.53
    32.53
    49.5
    
    >>> compute_storage_space(100.0, 12.0)
    141.42
    141.42
    6.0
    '''
    storage_width = math.sqrt(2) * radius
    storage_width = round(storage_width, 2)
    storage_length = storage_width
    storage_height = height_cyl / 2
    storage_height = round(storage_height, 2)
    return storage_width, storage_length, storage_height

#storage_width, storage_length, storage_height = compute_storage_space(100, 12)
#print(storage_width, storage_length, storage_height)
    
def load_rocket(mass_rocket, radius, height_cyl): 
    '''
    Interacts with the user in order to fill the rocket storage
    as efficently as possible given certain peramaters and retunrs
    the final weight of the rocket (kg) to 2 decimal places
    
    Args:
        mass_rocket (float): The mass of the rocket in kg
        radius (float): radius of the rocket in meters
        height_cyl (float): height of the cylinder in meters
    
    User inputs (str):
        item_weight (float): weight of the item in kg
        item_width (float): width of the item in meters
        item_length (float): length of the item in meters
        item_height (float): height of the item in meters
        "Done" (str): used as a boolean to end function
    
    Returns:
        float: weight of the rocket after having loaded items
        (if possible)
    
    Examples:
    >>> load_rocket(1000.0, 200.0, 300.0)
    Please enter the weight of the next item(type "Done" when
            you are done filling the rocket):5
    Enter the width:1
    Enter the length:1
    Enter the height:1
    Item could not be added... please try again...
    Please enter the weight of the next item(type "Done" when
            you are done filling the rocket):35
    Enter the width:20
    Enter the length:30
    Enter the height:10
    No more items can be added
    1035.0
        
    >>> load_rocket(10000.0, 1000.0, 500.0)
    Please enter the weight of the next item(type "Done" when
            you are done filling the rocket):25
    Enter the width:30
    Enter the length:30
    Enter the height:30
    Please enter the weight of the next item(type "Done" when
            you are done filling the rocket):Done
    10025.0
        
    >>> load_rocket(399.0, 100.0, 400.0)
    No more items can be added
    399.0
    
    '''
    storage_width, storage_length, storage_height = compute_storage_space(radius, height_cyl) #Can not be split
    storage_volume = storage_width * storage_height * storage_length
    weight_max = mass_rocket * 0.05  # parameter so to not add item of 5% rocket weight
    space_limit = storage_volume * 0.40  # parameter as to only fill up to 40% of rocket space
    space_occupied = INITIAL_STORAGE_USED
    final_weight = INITIAL_WEIGHT
    done_status = DONE_INITIAL
    
    if weight_max < WEIGHT_MIN or space_limit < VOLUME_MIN: #checks if rocket is so small/light that not even minimum weight/size fits
        print("No more items can be added")
        final_weight = round(mass_rocket, 2)
    else:
        while space_occupied + VOLUME_MIN <= space_limit and final_weight + WEIGHT_MIN <= weight_max and done_status == 0: #Can not be split #checks for parameters
            item_weight = input("Please enter the weight of the \
next item(type \"Done\" when you are done filling the rocket):")
            
            if item_weight == "Done": # To simplify input gathering, I decided to make boolean check to detect "Done"
                done_status +=1
                final_weight = final_weight + mass_rocket
                final_weight = round(final_weight, 2)
                return final_weight
            else:
                item_weight = float(item_weight)
                item_width = float(input("Enter the width:"))
                item_length = float(input("Enter the length:"))
                item_height = float(input("Enter the height:"))
                item_volume = item_height * item_width * item_length
                if WEIGHT_MAX < item_weight or item_weight < WEIGHT_MIN or item_volume < VOLUME_MIN or (final_weight + item_weight) > weight_max or (space_occupied + item_volume) > space_limit: #line can not be split
                    print("Item could not be added... please try again...")
                else:
                    space_occupied = space_occupied + item_volume
                    final_weight = final_weight + item_weight
        print("No more items can be added")
        final_weight = final_weight + mass_rocket
        final_weight = round(final_weight, 2)            
    return final_weight   
       
#x = load_rocket(10000.0, 1000.0, 500.0)
#print(x)

def projectile_sim(simulation_time, interval, velocity_i, angle):
    '''
    Calculates the height of the rocket in the simulation at
    certaint given intervals (rounded to 2 decimals) (meters)
    
    Args:
        simulation_time (int): time for which the simulation wil run
            in seconds
        interval (int): intervals at which height will be displayed
            in seconds
        velocity_e (float): exhaust velocity in m/s
        angle (float): angle of rocket launch in radians
    
    Returns:
        float: height of rocket at given intervals untill simulation
        time ends
    
    Exampes:
    
    >>> projectile_sim(10, 1, 50.0, 0.7)
    0.0
    27.31
    44.8
    52.49
    50.36
    38.43
    16.69
    
    >>> projectile_sim(50, 1, 33.0, 0.5)
    0.0
    10.92
    12.02
    3.32
    
    >>> projectile_sim(60, 1, 80.0, 0.33)
    0.0
    21.02
    32.23
    33.63
    25.21
    6.99        
    '''
    time = INITIAL_TIME
    for time in range(0, simulation_time + 1, interval):
      height = (0.5 * GRAVITY * (time ** 2) + velocity_i *
                math.sin(angle) * time)
      if height < 0:  #Ensures that rocket doesnt go undergound in simuation
        time = time + simulation_time + 1
      else:
        time = time + interval
        height = round(height, 2)
        print(height)      

#projectile_sim(60, 1, 80.0, 0.33)

def rocket_main():
    '''
    Runs a user interactive rocket simulation that informs the user
    of the price, storage loading and simulation of the rocket
    given the user's input of rocket dimensions and launch
    parameters.
    
    Args:
        None
    
    User inputs (str):
        radius (float): radius of the rocket in feet
        height_cone (float): height of the cone in feet
        height_cyl (float): height of the cylinder in feet
        velocity_e (float): exhaust velocity in m/s
        velocity_i (float): initial velocity in m/s
        angle (float): angle of rocket launch in radians
        time (float): time of trip in seconds
        tax (int): decides if tax is considered
        simulation_time (int): time for which the simulation wil run
            in seconds
        interval (int): intervals at which height will be displayed
        
    Returns:
        None
        
    Outputs:
        float: total price of the trip rounded to 2 decimals ($)
        float: mass of the rocket after loading items (kg)
    
    Example:
    >>> rocket_main()
    Welcome to the Rocket Simulation!
    Enter the rocket radius in feet:100
    Enter the rocket cone height in feet:450
    Enter the rocket cylinder height in feet:388
    Enter the exhaust velocity for the upcoming trip:80
    Enter the initial velocity for the upcoming trip:90
    Enter the angle of launch for the upcoming trip:0.7
    Enter the length of the upcoming trip:40
    Would you like to factor in tax? 1 for yes, 0 for no:0
    This trip will cost $8305521.2
    Now loading the rocket:
    Please enter the weight of the next item(type "Done" when you are done filling the rocket):35
    Enter the width:2
    Enter the length:4
    Enter the height:7
    Please enter the weight of the next item(type "Done" when you are done filling the rocket):15
    Enter the width:2
    Enter the length:5
    Enter the height:8
    Item could not be added... please try again...
    Please enter the weight of the next item(type "Done" when you are done filling the rocket):Done
    The rocket and its equipment will weigh 586857.08 kg
    Enter the simulation total time:50
    Enter the simulation interval:5
    Now simulating the rocket trajectory:
    0.0
    167.27
    89.3

    '''
    print("Welcome to the Rocket Simulation!")
    
    radius_ft = float(input("Enter the rocket radius in feet:"))
    radius = feet_to_meter(radius_ft)
    cone_height_ft = float(input("Enter the rocket cone height \
in feet:"))
    height_cone = feet_to_meter(cone_height_ft)
    cyl_height_ft = float(input("Enter the rocket cylinder height \
in feet:"))
    height_cyl = feet_to_meter(cyl_height_ft)
    velocity_e = float(input("Enter the exhaust velocity for the \
upcoming trip:"))
    velocity_i = float(input("Enter the initial velocity for the \
upcoming trip:"))
    angle = float(input("Enter the angle of launch for the upcoming \
trip:"))
    time = float(input("Enter the length of the upcoming trip:"))
    tax_determinant = int(input("Would you like to factor in tax? 1 \
for yes, 0 for no:"))
    
    cost = calculate_cost(radius, height_cone, height_cyl, velocity_e, velocity_i, time, bool(tax_determinant)) #can not be split
    print("This trip will cost $" + str(cost))
    
    mass_rocket = rocket_mass(radius, height_cone, height_cyl)
    print("Now loading the rocket:")
    
    final_weight = load_rocket(mass_rocket, radius, height_cyl)
    print("The rocket and its equipment will weigh", final_weight,
          "kg")
    
    simulation_time = int(input("Enter the simulation total time:"))
    interval = int(input("Enter the simulation interval:"))
    print("Now simulating the rocket trajectory:")
    
    projectile_sim(simulation_time, interval, velocity_i, angle)





