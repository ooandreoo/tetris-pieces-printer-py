# The logic behind this figures is that, when working in a 2D matrix or cartesian plane
# if you want to rotate the points drawn within the matrix or plane by having as center a specific
# (x,y) coordenate, then you must find the vector between each point and the center.
# Then, you separate the components of the vector: if its (vx, vy) then you will separate it
# in (vx, 0) and (0, vy). After that, you want to work with 1,0,-1 values, in order to calculate the
# variations between the states, and then multiply it their respective magnitude
#
# Example:
#   center = (2,2)   point_to_rotate = (1,1)    rotation=90 degrees clockwise
#   states = [(0,1),(1,0),(0,-1),(-1,0)]
#
#   vector = (1,1) - (2,2) = (-1,-1)
#
#   component_x = (-1,0)
#   component_y = (0,-1)
#
#   since magnitude is 1, we don't need to divide the values
#
#   90 degrees clockwise means we go to the immediate next state to the right in the states list
#   component_x_next_state = (0,1)
#   component_y_next_state = (-1,0)
#
#   variations_due_to_x = (+1,+1)
#   variations_due_to_y = (-1,+1)
#
#   new_position = (1,1) + (1,1) + (-1,1) = (1,3)
#
#       START
#
#       4
#       3
#       2     C
#       1   P
#       0
#         0 1 2 3 4
#
#       FINAL
#
#       4
#       3   P
#       2     C
#       1
#       0
#         0 1 2 3 4


def rotate_positions(positions, center, degrees=90, direction="right"):
    if(direction not in ["right","left"]):
        raise ValueError("Direction of rotation must be 'right' or 'left'")
    if(degrees%90 != 0):
        raise ValueError("Degrees of rotation must be multiple of 90")

    # this value represents the amount of jumps to the right across a list with 4 states
    rotations = degrees/90

    if(direction=="left"):
        # if rotations will be made to the left, we simply go from right to left
        rotations *= -1

    new_positions = []

    for position in positions:
        new_positions.append(get_new_position_after_rotation(position, center ,rotations))

    return new_positions

def get_new_position_after_rotation(position, center, rotations):
    # new positions are the result of moving from the current position ...
    new_x = position[0]
    new_y = position[1]

    changes_component_x = get_position_changes_for_component(0,position, center, rotations)
    changes_component_y = get_position_changes_for_component(1,position, center, rotations)

    # in addition to modifications needed by rotating each component (x and y)
    new_x += changes_component_x[0] + changes_component_y[0]
    new_y += changes_component_x[1] + changes_component_y[1]

    return (new_x,new_y)

def get_position_changes_for_component(axis, position, center, rotations):
    # the modification of the state of axis x or axis y can have an impact on both coordinates
    component = position[axis] - center[axis]

    changes_x = 0
    changes_y = 0

    if(component != 0):
        # states are the values of sinus (for x axis) and cosinus(for y axis) functions at 90 degrees multiples
        states = [(0,1),(1,0),(0,-1),(-1,0)]

        # we will convert this aux state into a tuple representing the current state of the component
        aux_state = [0,0]
        aux_state[axis] = component/abs(component)
        aux_state = tuple(aux_state)

        # we find the current state of the component
        current_state = states.index(aux_state)

        # now, we get the final state of the component after the rotations
        # we take the modulus by 4 because sinus and cosinus functions are periodic
        # meaning they repeat their values after 4 multiple of 90 degrees states
        final_state = int((current_state + rotations)%4)

        # now we add the modifications needed by changing values
        changes_y += (states[final_state][1]-states[current_state][1])*abs(component)
        changes_x += (states[final_state][0]-states[current_state][0])*abs(component)


    return (changes_x, changes_y)



