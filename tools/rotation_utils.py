def rotate_positions(positions, center, degrees=90):
    states = [(0,1),(1,0),(0,-1),(-1,0)]
    rotations = degrees/90

    new_positions = []
    for position in positions:
        x_component = position[0]-center[0]
        y_component = position[1]-center[1]

        new_x = position[0]
        new_y = position[1]

        if(x_component != 0):

            current_state_x = None

            if(x_component > 0):
                current_state_x = 1

            elif(x_component < 0):
                current_state_x = 3

            final_state_x = int((current_state_x + rotations)%4)

            new_y += (states[final_state_x][1]-states[current_state_x][1])*abs(x_component)
            new_x += (states[final_state_x][0]-states[current_state_x][0])*abs(x_component)

        if(y_component != 0):

            current_state_y = None

            if(y_component > 0):
                current_state_y = 0
            elif(y_component < 0):
                current_state_y = 2


            final_state_y = int((current_state_y + rotations)%4)

            new_y += (states[final_state_y][1]-states[current_state_y][1])*abs(y_component)
            new_x += (states[final_state_y][0]-states[current_state_y][0])*abs(y_component)

        new_positions.append((new_x,new_y))

    return new_positions
