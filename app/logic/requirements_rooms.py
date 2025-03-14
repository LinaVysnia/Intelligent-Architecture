#if a room smaller than this threshold will be skipped and considered an error
min_valid_room = 0.5

def living_room_area_check(room : dict):
    if room["label"] != "space_living_room" or room["area"] < min_valid_room:
        return

    print("Validating living room total area...")

    smallest_min_edge = 3.3

    #because we won't know all the edges but only the minimum width, 
    #we assume that smallest living room is square with each edge the minimum lengh
    min_area = smallest_min_edge**2

    try:
        area = room["area"]

        if area < min_area:
            status = "Fail"
            message = f"The living room area {area} sq.m. is smaller than the required minimum of {min_area} sq.m."
            print(status, "\n", message )
            return
        
        if area >= min_area:
            status = "Pass"
            message = f"There is enough space in the living room ({area})"
            print(status, "\n", message )
            return
        
        #if the code is still running here, something went wrong
        raise Exception("There was an unknown issue analysing the livig room space")

    except Exception as ex:
        print("Failure due to an error")
        print(ex)

def kitchen_room_area_check(room : dict):
    if room["label"] != "space_kitchen" or room["area"] < min_valid_room:
        return

    print("Validating kitchen area...")

    min_area = 7

    try:
        area = room["area"]

        if area < min_area:
            status = "Fail"
            message = f"The kitchen area of {area} sq.m. is smaller than the required minimum of {min_area} sq.m."
            print(status, "\n", message )
            return
        
        if area >= min_area:
            status = "Pass"
            message = f"There is enough space in the kitchen ({area})"
            print(status, "\n", message )
            return
        
        #if the code is still running here, something went wrong
        raise Exception("There was an unknown issue analysing the kitchen area")

    except Exception as ex:
        print("Failure due to an error")
        print(ex)

def bathroom_area_check(room : dict):
    if room["label"] != "space_toilet" or room["area"] < min_valid_room:
        return

    print("Validating bathroom total area...")

    smallest_min_edge = 1.7

    #because we won't know all the edges but only the minimum width, 
    #we assume that smallest bathroom is square with each edge the minimum lengh
    min_area = smallest_min_edge**2

    try:
        area = room["area"]

        if area < min_area:
            status = "Fail"
            message = f"The bathroom area {area} sq.m. is smaller than the required minimum of {min_area} sq.m."
            print(status, "\n", message )
            return
        
        if area >= min_area:
            status = "Pass"
            message = f"There is enough space in the bathroom ({area})"
            print(status, "\n", message )
            return
        
        #if the code is still running here, something went wrong
        raise Exception("There was an unknown issue analysing the bathroom space")

    except Exception as ex:
        print("Failure due to an error")
        print(ex)

def bedroom_area_check(room : dict):
    if room["label"] != "space_bedroom" or room["area"] < min_valid_room:
        return

    print("Validating bedroom total area...")

    min_area = 6.5

    try:
        area = room["area"]

        if area < min_area:
            status = "Fail"
            message = f"The bedroom area {area} sq.m. is smaller than the required minimum of {min_area} sq.m."
            print(status, "\n", message )
            return
        
        if area >= min_area:
            status = "Pass"
            message = f"There is enough space in the bedroom ({area})"
            print(status, "\n", message )
            return
        
        #if the code is still running here, something went wrong
        raise Exception("There was an unknown issue analysing the bedroom space")

    except Exception as ex:
        print("Failure due to an error")
        print(ex)

def corridor_area_check(room : dict):
    if room["label"] != "space_elevator_hall" or room["area"] < min_valid_room:
        return

    print("Validating corridor total area...")

    smallest_min_edge = 1.2

    #because we won't know all the edges but only the minimum width, 
    #we assume that smallest corridor is square with each edge the minimum lengh
    min_area = smallest_min_edge**2

    try:
        area = room["area"]

        if area < min_area:
            status = "Fail"
            message = f"The corridor area {area} sq.m. is smaller than the required minimum of {min_area} sq.m."
            print(status, "\n", message )
            return
        
        if area >= min_area:
            status = "Pass"
            message = f"There is enough space in the corridor ({area})"
            print(status, "\n", message )
            return
        
        #if the code is still running here, something went wrong
        raise Exception("There was an unknown issue analysing the corridor space")

    except Exception as ex:
        print("Failure due to an error")
        print(ex)
