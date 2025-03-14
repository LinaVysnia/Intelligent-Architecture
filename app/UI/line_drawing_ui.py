def run_get_line_measurements_UI():
    input("Let's pretend you're a user drawing a line on the plan to calculate the scale of the plan")
    line_pixels = None
    line_meters = None
    while True:
        user_input = input("Choose how long the line would be in pixels: ").strip()
        try:
            user_input = float(user_input)
            if user_input <= 0:
                raise Exception(f"{user_input} isn't a valid length measurement")
            line_pixels = user_input
            break
        except Exception as ex:
            print(ex)
            print("Please enter the measurement as a number")

    while True:
        user_input = input("Choose what the real workd scale of the line would be in meters: ").strip()
        try:
            user_input = float(user_input)
            if user_input <= 0:
                raise Exception(f"{user_input} isn't a valid length measurement")
            line_meters = user_input
            break
        except Exception as ex:
            print(ex)
            print("Please enter the measurement as a number")

    print(f"The line drawn on the plan is {line_pixels} pixels long")
    print(f"The line from the plan is {line_meters} meters long in real life")

    return line_pixels, line_meters