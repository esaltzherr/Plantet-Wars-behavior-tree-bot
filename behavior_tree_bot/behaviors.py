import sys
sys.path.insert(0, '../')
from planet_wars import issue_order


def attack_weakest_enemy_planet(state):
    

    # (2) Find my strongest planet.
    strongest_planet = max(state.my_planets(), key=lambda t: t.num_ships, default=None)

    # (3) Find the weakest enemy planet.
    weakest_planet = min(state.enemy_planets(), key=lambda t: t.num_ships, default=None)

    if not strongest_planet or not weakest_planet:
        # No legal source or destination
        return False
    else:
        # (4) Send half the ships from my strongest planet to the weakest enemy planet.
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)


def spread_to_weakest_neutral_planet(state):
    # (1) If we currently have a fleet in flight, just do nothing.
    if len(state.my_fleets()) >= 1:
        return False

    # (2) Find my strongest planet.
    strongest_planet = max(state.my_planets(), key=lambda p: p.num_ships, default=None)

    # (3) Find the weakest neutral planet.
    weakest_planet = min(state.neutral_planets(), key=lambda p: p.num_ships, default=None)

    if not strongest_planet or not weakest_planet:
        # No legal source or destination
        return False
    else:
        # (4) Send half the ships from my strongest planet to the weakest enemy planet.
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)


def spread_to_closest_neutral_planet(state):


    my_planets = iter(sorted(state.my_planets(), key=lambda p: p.num_ships, reverse=True))


    target_planets = [planet for planet in state.neutral_planets()
                      if not any(fleet.destination_planet == planet.ID for fleet in state.my_fleets())]
    # target_planets = iter(sorted(target_planets, key=lambda p: p.num_ships, reverse=True))
    #target_planets = iter(sorted(target_planets, key=lambda p: p.num_ships, reverse=True))
    
    

    
    if not target_planets:
        return False
    for my_planet in my_planets:
        
        close_target_planets = sorted(target_planets, key=lambda p: state.distance(my_planet.ID, p.ID))
        closest_three_planets = close_target_planets[:3]

        sorted_closest_three_by_ships = sorted(closest_three_planets, key=lambda p: p.num_ships)
        target_planet = sorted_closest_three_by_ships[0]
        if target_planet.owner == 0:
            required_ships = target_planet.num_ships + 1
        else:
            required_ships = target_planet.num_ships + \
                                state.distance(my_planet.ID, target_planet.ID) * target_planet.growth_rate + 1
            
        if my_planet.num_ships > required_ships:
                issue_order(state, my_planet.ID, target_planet.ID, required_ships)
        
    return


def spread_to_closest_planet(state):


    my_planets = iter(sorted(state.my_planets(), key=lambda p: p.num_ships, reverse=True))


    target_planets = [planet for planet in state.not_my_planets()
                      if not any(fleet.destination_planet == planet.ID for fleet in state.my_fleets())]
    # target_planets = iter(sorted(target_planets, key=lambda p: p.num_ships, reverse=True))
    #target_planets = iter(sorted(target_planets, key=lambda p: p.num_ships, reverse=True))
    
    

    
    if not target_planets:
        return False
    for my_planet in my_planets:
        
        close_target_planets = sorted(target_planets, key=lambda p: state.distance(my_planet.ID, p.ID))
        closest_three_planets = close_target_planets[:3]

        sorted_closest_three_by_ships = sorted(closest_three_planets, key=lambda p: p.num_ships)
        target_planet = sorted_closest_three_by_ships[0]
        if target_planet.owner == 0:
            required_ships = target_planet.num_ships + 1
        else:
            required_ships = target_planet.num_ships + \
                                state.distance(my_planet.ID, target_planet.ID) * target_planet.growth_rate + 1
            
        if my_planet.num_ships > required_ships:
                issue_order(state, my_planet.ID, target_planet.ID, required_ships)
        
    return



def spread_to_closest_neutral_planet(state):


    my_planets = iter(sorted(state.my_planets(), key=lambda p: p.num_ships, reverse=True))


    target_planets = [planet for planet in state.neutral_planets()
                      if not any(fleet.destination_planet == planet.ID for fleet in state.my_fleets())]
    # target_planets = iter(sorted(target_planets, key=lambda p: p.num_ships, reverse=True))
    target_planets = iter(sorted(target_planets, key=lambda p: p.num_ships, reverse=True))

    if not target_planets:
        return False
    
    try:
        my_planet = next(my_planets)
        target_planet = next(target_planets)
        while True:
            if target_planet.owner == 0:
                required_ships = target_planet.num_ships + 1
            else:
                required_ships = target_planet.num_ships + \
                                 state.distance(my_planet.ID, target_planet.ID) * target_planet.growth_rate + 1
                
            if my_planet.num_ships > required_ships:
                issue_order(state, my_planet.ID, target_planet.ID, required_ships)
                my_planet = next(my_planets)

            target_planet = next(target_planets)


    except StopIteration:
        return
    



    for my_planet in my_planets:
        
        close_target_planets = sorted(target_planets, key=lambda p: state.distance(my_planet.ID, p.ID))
        closest_three_planets = close_target_planets[:3]

        sorted_closest_three_by_ships = sorted(closest_three_planets, key=lambda p: p.num_ships)
        target_planet = sorted_closest_three_by_ships[0]
        if target_planet.owner == 0:
            required_ships = target_planet.num_ships + 1
        else:
            required_ships = target_planet.num_ships + \
                                state.distance(my_planet.ID, target_planet.ID) * target_planet.growth_rate + 1
            
        if my_planet.num_ships > required_ships:
                issue_order(state, my_planet.ID, target_planet.ID, required_ships)
        
    return