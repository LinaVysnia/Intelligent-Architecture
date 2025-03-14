def minimum_habitable_area(all_rooms : list[dict]):
    """
    Checks if the sum of all habitable rooms is greater than minimum. 
    Works in square meters.
    Args: 
        A list of configured results that have been returned from the model 
        and postprocessed into a more usable list
    Not all rooms are habitable areas. Based on the current building 
    regulations habitable areas:
    "4.7. useful area of housing - the total floor area of living rooms 
    and other housing spaces (kitchens, sanitary facilities, corridors, 
    built-in closets, heated loggias and other heated auxiliary spaces). 
    The useful area of housing does not include the floor area of balconies, 
    terraces, basements, and unheated lodges;"
    """
    print("Validating the minimum habitable space...")

    min_area = 14
    full_area = 0
    ambigious_area = 0

    not_habitable_areas = ["background", "space_balconi", "space_front", 
                           "space_outdoor_room", "space_elevator", ]
    ambigious_areas = ["space_multipurpose_space", "space_other"]

    try:
        for room in all_rooms:
            if room["label"] in not_habitable_areas:
                continue
            full_area += room["area"]
            if room["label"] in ambigious_areas:
                ambigious_area += room["area"]

        if full_area < min_area:
            status = "Fail"
            message = f"The habitable area of {full_area} sq.m. is smaller than the required minimum of 14 sq.m."
            print(status, "\n", message )
            return
        
        if (full_area - ambigious_area) < min_area:
            status = "Warning"
            message = f"If the ambigious purpose rooms don't fall in the habitable category, the total habitable area could be smaller than the required minimum of 14 sq.m."
            print(status, "\n", message )
            return
        
        if (full_area - ambigious_area) >= min_area:
            status = "Pass"
            message = f"There is enough habitable space in the residence ({full_area})"
            print(status, "\n", message )
            return
        
        #if the code is still running here, something went wrong
        raise Exception("There was an unknown issue analysing the habitable space")

    except Exception as ex:
        print("Failure due to an error")
        print(ex)
