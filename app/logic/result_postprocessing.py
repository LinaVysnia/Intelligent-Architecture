import numpy as np
import cv2

def calculate_sq_m(line_px, line_m, mask_matrix):
    sq_m = np.sum(mask_matrix) * ((line_m/line_px)**2)
    return sq_m

def postprocess_result(result, line_pixels, line_meters) -> list[dict]:

    img = np.copy(result.orig_img)

    result_configured = []

    # Iterating over each objects contour 
    for i, contour in enumerate(result):
        label = contour.names[contour.boxes.cls.tolist().pop()]

        b_mask = np.zeros(img.shape[:2], np.uint8)

        # Create contour mask 
        contour = contour.masks.xy.pop().astype(np.int32).reshape(-1, 1, 2)
        _ = cv2.drawContours(b_mask, [contour], -1, 255, cv2.FILLED)

        #display(mask_pil)

        binary_matrix = (b_mask > 0).astype(np.uint8)   

        result_configured.append(dict(label = label, mask = binary_matrix))

        for result in result_configured:
            print("Room recognised")
            print("Room name: ", result["label"])
            area = round(calculate_sq_m(line_pixels, line_meters, result["mask"]), 3)
            result["area"] = area
            print(f"Room size: {result["area"] } m^2.")

    return result_configured