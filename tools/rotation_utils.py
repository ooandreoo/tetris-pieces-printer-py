def rotate_positions(positions, center, degrees=90):
    states = [(0,1),(1,0),(0,-1),(-1,0)]
    rotations = degrees/90
    state_changes = rotations % 4

    new_positions = []
    for position in positions:
        x_component = position[0]-center[0]
        y_component = position[1]-center[1]

        new_x = position[0]
        new_y = position[1]

        # conditions help identify the current state
        if(x_component > 0):
            #what is inside the condition should state what to do depending on the amount of rotations, at the moment is 90 degrees rotation logic hardcoded
            new_y -= x_component
            new_x -= x_component
        elif(x_component < 0):
            new_y += abs(x_component)
            new_x += abs(x_component)

        if(y_component > 0):
            new_x += y_component
            new_y -= y_component
        elif(y_component < 0):
            new_x -= abs(y_component)
            new_y += abs(y_component)

        new_positions.append((new_x,new_y))

    return new_positions
