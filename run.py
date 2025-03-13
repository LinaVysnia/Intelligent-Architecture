from app.logic.model_logic import get_model_prediction
from app.logic.result_postprocessing import postprocess_result
from app.UI.line_drawing_ui import run_get_line_measurements_UI
from types import FunctionType
import app.logic.requirements_rooms as room_vals
import app.logic.requirements_whole_residency as resd_vals

print("This is Architectural Intelligence!")

#getting all the validation functions
room_validators = [obj for name, obj in vars(room_vals).items() 
                if isinstance(obj, FunctionType)]

residence_validators = [obj for name, obj in vars(resd_vals).items() 
                if isinstance(obj, FunctionType)]

model_link = "C:/Users/Linos/Documents/Coding_practice/Dirbtinis Intelektas ir Python/Intelligent-Architecture/runs/segment/train7/weights/best.pt"
image_loc = "app/data/my_custom/image (16).png"  

result = get_model_prediction(image_loc, model_link)
#result.show()

line_pixels, line_meters = run_get_line_measurements_UI()

result_configured = postprocess_result(result, line_pixels, line_meters)

for validation in residence_validators:
    validation(result_configured)

for validation in room_validators:
    for room in result_configured:
        validation(room)