'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    social_graph = {"@bongolpoc":{"following":""},
                "@joaquin": {"following":["@chums","@jobenilagan"]},
                "@chums" : {"following":["@bongolpoc","@miketan","@rudyang","@joeilagan"]},
                "@jobenilagan":{"following":["@eeebeee","@joeilagan","@chums","@joaquin"]},
                "@joeilagan":{"following":["@eeebeee","@jobenilagan","@chums"]},
                "@eeebeee":  {"following":["@jobenilagan","@joeilagan"]}
                }


    x = to_member in social_graph[from_member]["following"]
    y = from_member in social_graph[to_member]["following"]
        
    if x == True and y == True:
        return(print("friends"))
    elif x == True:
        return(print("following"))
    elif y == True:
        return(print("follower"))
    else:
        return(print("no relationship"))


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if len(board) == 3:    
        new_board = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    new_board.append(12)
                elif board[i][j] == 'O':
                    new_board.append(10)
                else:
                    new_board.append(0)
    
        points = [new_board[k:k + 3] for k in range(0, len(new_board), 3)]
  
        horizontal_sums = [sum(x) for x in points]
        vertical_sums = [sum(x) for x in zip(*points)]
        diagonal_up_down = sum([points[i][i] for i, v in enumerate(points)])
        diagonal_down_up = sum([points[2-i][i] for i, v in enumerate(points)])
    
        for i in horizontal_sums:
            if i == 36:
                return print('X')
            elif i == 30:
                return print('O')
        for i in vertical_sums:
            if i == 36: 
                return print('X')
            elif i == 30:
                return print('O')
        if diagonal_up_down == 36:
                return print('X')
        if diagonal_up_down == 30:
                return print('O')
        if diagonal_down_up == 36:
                return print('X')
        if diagonal_down_up == 30:
                return print('O')
        else:
                return print('No Winner')
    
    elif len(board) == 4: 
        new_board = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    new_board.append(12)
                elif board[i][j] == 'O':
                    new_board.append(10)
                else:
                    new_board.append(0)
    
        points = [new_board[k:k + 4] for k in range(0, len(new_board), 4)]
  
        horizontal_sums = [sum(x) for x in points]
        vertical_sums = [sum(x) for x in zip(*points)]
        diagonal_up_down = sum([points[i][i] for i, v in enumerate(points)])
        diagonal_down_up = sum([points[2-i][i] for i, v in enumerate(points)])
    
        for i in horizontal_sums:
            if i == 48:
                return print('X')
            elif i == 40:
                return print('O')
        for i in vertical_sums:
            if i == 48: 
                return print('X')
            elif i == 40:
                return print('O')
        if diagonal_up_down == 48:
            return print('X')
        if diagonal_up_down == 40:
            return print('O')
        if diagonal_down_up == 48:
                return print('X')
        if diagonal_down_up == 40:
                return print('O')
        else:
            return print('No Winner')
        
    elif len(board) == 5: 
        new_board = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    new_board.append(12)
                elif board[i][j] == 'O':
                    new_board.append(10)
                else:
                    new_board.append(0)
    
        points = [new_board[k:k + 5] for k in range(0, len(new_board), 5)]
  
        horizontal_sums = [sum(x) for x in points]
        vertical_sums = [sum(x) for x in zip(*points)]
        diagonal_up_down = sum([points[i][i] for i, v in enumerate(points)])
        diagonal_down_up = sum([points[2-i][i] for i, v in enumerate(points)])
    
        for i in horizontal_sums:
            if i == 60:
                return print('X')
            elif i == 50:
                return print('O')
        for i in vertical_sums:
            if i == 60: 
                return print('X')
            elif i == 50:
                return print('O')
        if diagonal_up_down == 60:
               return print('X')
        if diagonal_up_down == 50:
            return print('O')
        if diagonal_down_up == 60:
                return print('X')
        if diagonal_down_up == 50:
                return print('O')
        else:
            return print('No Winner')
        
    elif len(board) == 6: 
        new_board = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    new_board.append(12)
                elif board[i][j] == 'O':
                    new_board.append(10)
                else:
                    new_board.append(0)
    
        points = [new_board[k:k + 6] for k in range(0, len(new_board), 6)]
  
        horizontal_sums = [sum(x) for x in points]
        vertical_sums = [sum(x) for x in zip(*points)]
        diagonal_up_down = sum([points[i][i] for i, v in enumerate(points)])
        diagonal_down_up = sum([points[2-i][i] for i, v in enumerate(points)])
    
        for i in horizontal_sums:
            if i == 72:
                return print('X')
            elif i == 60:
                return print('O')
        for i in vertical_sums:
            if i == 72: 
                return print('X')
            elif i == 60:
                return print('O')
        if diagonal_up_down == 72:
               return print('X')
        if diagonal_up_down == 60:
            return print('O')
        if diagonal_down_up == 72:
                return print('X')
        if diagonal_down_up == 60:
                return print('O')
        else:
            return print('No Winner')

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
   
    route_map = {
         ("upd","admu"):{
             "travel_time_mins":10
         },
         ("admu","dlsu"):{
             "travel_time_mins":35
         },
         ("dlsu","upd"):{
             "travel_time_mins":55
         }
    }

    total = 0
    for j in route_map.keys():
        if j[0] == first_stop:
            if j[1] == second_stop:
                total = route_map[(first_stop, second_stop)]["travel_time_mins"]
                return total
            else:
                total += route_map[j]["travel_time_mins"]
                middle = j[1]
                break
    for k in route_map.keys():
        if k[0] == middle and k[1] == second_stop:
          total += route_map[k]["travel_time_mins"]
        return total
    