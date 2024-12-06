import csv
import sys

if __name__ == "__main__":
    # read in the input file name and the input string
    args = sys.argv 
    filename = args[1]
    input_string = args[2].strip("'")

    # process the input string if it is the empty string
    if len(input_string) == 0:
        input_string = '_'
    
    # arbitrary max depth so that it doesn't loop forever
    max_depth = 100

    # open the input file 
    with open(filename, "r") as input_file:
        # empty array to store the data
        data = []
        for line in input_file:
            # append all data to the array
            data.append(line.strip())
        # read in and assign the header information to variables
        machine_name = data[0]
        start_state = data[4]
        accept_state = data[5]
        # append everything after the header to the transitions array
        transitions = []
        for i in range(7, len(data)):
            transitions.append(data[i].split(','))

    # print machine name and initial string
    print(f"Machine Name: {machine_name}")
    print(f"Initial String: {input_string}")

    # start stores what the machine looks like at the beginning
    start = []
    # append the start state and the input string
    start.append("")
    start.append(start_state)
    start.append(input_string)
    # create the final results array and put the starting configuration as the first element
    final = [[start]]

    # initialize depth of tree, number of transitions, and whether or not the tree should end
    depth = 0
    num_transitions = 0
    done = False

    # keep looping
    while depth < len(final):
        # pick the level of the tree that we are on
        level = final[depth]
        # add one to the depth
        depth += 1
        # list for all of the possible new configurations we can go to
        new_options = []
        # bool and check to see if all of the states in the level are in the reject state (in which case we would want to stop)
        rejected = True
        for config in level:
            if config[1] != 'qrej':
                rejected = False
        # stop if we reach max depth
        if depth > max_depth:
            print(f"Execution stopped after {max_depth}")
            break
        for config in level:
            # stop if all states are in reject state
            if rejected == True:
                print(f"String rejected in {depth - 1}")
                done = True
                break
            # bool to see if any of the transitions work or if we are going to a trap state
            transition_bool = False
            state = config[1]
            # if in the reject state, end the branch of the tree and go on to the next
            if state == 'qrej':
                continue
            # get the input character
            input = config[2][0]
            # loop through the transitions
            for transition in transitions:
                # see if we can find the transition that matches our current state and input character
                if transition[0] == state and transition[1] == input:
                    num_transitions += 1
                    transition_bool = True
                    # find the new state, char and which direction to move
                    new_state = transition[2]
                    new_char = transition[3]
                    direction = transition[4]
                    new_state_config = []
                    # if we are supposed to move right
                    if direction == 'R':
                        new_state_config.append(config[0]+new_char)
                        new_state_config.append(new_state)
                        # add blank if we are at the last character on the input string
                        if len(config[2]) > 1:
                            new_state_config.append(config[2][1:])
                        else:
                            new_state_config.append('_')
                    # if moving left
                    elif direction == 'L':
                        if len(config[0]) > 1:
                            new_state_config.append(config[0][:-1])
                        else: 
                            new_state_config.append('')
                        new_state_config.append(new_state)
                        if config[2] == '_':
                            new_state_config.append(config[0][-1]+new_char)
                        else:
                            new_state_config.append(config[0][-1]+new_char+config[2][1:])
                    # if we haven't moved to that transition in this level yet, add it to the possible new configurations
                    if new_state_config not in new_options:
                        new_options.append(new_state_config)
                    # stop and accept if in the accept state
                    if new_state == accept_state:
                        done = True
                        print(f"String accepted in {depth}")
                        break
            # move to q reject if none of the transitions match
            if transition_bool == False:
                num_transitions += 1
                new_state_config = []
                new_state_config.append(config[0])
                new_state_config.append("qrej")
                new_state_config.append(config[2])
                if new_state_config not in new_options:
                    new_options.append(new_state_config)
        if len(new_options) > 0:
            final.append(new_options)
        # if we have either accepted or rejected, break out of the while loop
        if done == True:
            break
    # print information at the end
    print(f"Number of Transitions Simulated: {num_transitions}")
    nondeterm = num_transitions/depth
    print(f"Average Nondeterminism: {nondeterm:.2f}")
    print("Tree:")
    for level in final:
        print(level)


    


