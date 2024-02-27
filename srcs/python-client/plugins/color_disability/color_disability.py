import  cv2
import  numpy as np
from    PIL \
        import  Image, ImageDraw, ImageFont
from    typing \
        import List

from    plugins.plugin  \
        import  Plugin
from    plugins.color_disability.traffic_object \
        import  *

def draw_corner_rect(image, pt1, pt2, color, thickness, length, padding):
    x1, y1 = pt1
    x2, y2 = pt2
    cv2.line(image, (x1 - padding, y1 - padding), (x1 + length - padding, y1 - padding), color, thickness)
    cv2.line(image, (x1 - padding, y1 - padding), (x1 - padding, y1 + length - padding), color, thickness)
    cv2.line(image, (x2 + padding, y2 + padding), (x2 - length + padding, y2 + padding), color, thickness)
    cv2.line(image, (x2 + padding, y2 + padding), (x2 + padding, y2 - length + padding), color, thickness)

def put_text_with_background(image_pil, text, org, font, text_color, bg_color, padding=5, radius=4):
    draw = ImageDraw.Draw(image_pil)
    text_width, text_height = draw.textsize(text, font=font)
    x, y = org
    box_coords = (x - padding, y - padding, x + text_width + padding, y + text_height + padding)
    draw.rounded_rectangle(box_coords, radius, fill=bg_color)
    draw.text((x, y), text, fill=text_color, font=font)

    return image_pil

class   ColorDisability(Plugin):

    def __init__(self):
        self.traffic_light = self.TrafficLight()
        self.traffic_sign = self.TrafficSign()

    class   TrafficLight:
        def __init__(self):
            pass
        def get_traffic_light_color(self, frame):
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            red_lower = np.array([0, 50, 50])
            red_upper = np.array([10, 255, 255])
            green_lower = np.array([40, 40, 40])
            green_upper = np.array([90, 255, 255])
            yellow_lower = np.array([15, 150, 150])
            yellow_upper = np.array([35, 255, 255])

            red_mask = cv2.inRange(hsv, red_lower, red_upper)
            green_mask = cv2.inRange(hsv, green_lower, green_upper)
            yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)

            red_area = cv2.countNonZero(red_mask)
            green_area = cv2.countNonZero(green_mask)
            yellow_area = cv2.countNonZero(yellow_mask)

            if yellow_area > red_area and yellow_area > green_area:
                return "Yellow"
            elif red_area > green_area and red_area > yellow_area:
                return "Red"
            elif green_area > red_area and green_area > yellow_area:
                return "Green"
            else:
                return "Unknown"
        
        def process(self, frame, roi_bounds, font_path):
            roi = frame[roi_bounds[0]:roi_bounds[1], roi_bounds[2]:roi_bounds[3]]  # ROI 추출
            if roi.size == 0:
                raise ValueError(f"ROI {roi_bounds} results in an empty image. Check the coordinates.")

            color = self.get_traffic_light_color(roi)
            print("[Plugin] [ColorDisability] [TrafficLight] detected color: ", color)

            border_padding = 9
            corner_length = 20
            corner_padding = 4
            draw_corner_rect(frame, (roi_bounds[2], roi_bounds[0]), (roi_bounds[3], roi_bounds[1]), 
                            (0, 0, 0), 2, corner_length, corner_padding)

            font_size = 13
            padding = 0
            info_text = f" Traffic Light: {color} "
            frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(frame_pil)
            font = ImageFont.truetype(font_path, font_size)
            text_width, text_height = draw.textsize(info_text, font=font)
            text_x = roi_bounds[2] + corner_padding
            text_y = roi_bounds[1] + border_padding - padding
            
            if text_y + text_height + padding > frame.shape[0]:
                text_y = roi_bounds[0] - text_height - padding - border_padding
            
            text_bg_color = (0, 0, 0, 51)

            frame_pil = put_text_with_background(
                frame_pil,
                info_text,
                (text_x, text_y),
                font,
                (255, 255, 255),
                text_bg_color,
                padding,
                radius=4
            )

            return frame_pil

    class   TrafficSign:
        def __init__(self):
            pass
        def process(self, frame, roi_bounds, font_path):
            roi = frame[roi_bounds[0]:roi_bounds[1], roi_bounds[2]:roi_bounds[3]]  # ROI 추출
            if roi.size == 0:
                raise ValueError(f"ROI {roi_bounds} results in an empty image. Check the coordinates.")

            border_padding = 9
            corner_length = 20
            corner_padding = 4
            draw_corner_rect(frame, (roi_bounds[2], roi_bounds[0]), (roi_bounds[3], roi_bounds[1]), 
                            (0, 0, 0), 2, corner_length, corner_padding)

            font_size = 13
            padding = 0
            info_text = f" Traffic Sign "
            frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(frame_pil)
            font = ImageFont.truetype(font_path, font_size)
            text_width, text_height = draw.textsize(info_text, font=font)
            text_x = roi_bounds[2] + corner_padding
            text_y = roi_bounds[1] + border_padding - padding
            
            if text_y + text_height + padding > frame.shape[0]:
                text_y = roi_bounds[0] - text_height - padding - border_padding
            
            text_bg_color = (0, 0, 0, 51)

            frame_pil = put_text_with_background(
                frame_pil,
                info_text,
                (text_x, text_y),
                font,
                (255, 255, 255),
                text_bg_color,
                padding,
                radius=4
            )

            return frame_pil

    def opencv(self, frame, trafficObjects: List[TrafficObject]):
        frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        font_path = "assets/font/opensans.ttf"

        for trafficObject in trafficObjects:
            roi_bounds = trafficObject.getRoi()
            object_type = trafficObject.getType()

            if object_type is LIGHT:
                frame_pil = self.traffic_light.process(frame, roi_bounds, font_path)
            elif object_type is SIGN:
                frame_pil = self.traffic_sign.process(frame, roi_bounds, font_path)
            else:
                print("UNKNOWN DETECTED")

            frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
        return frame

    def predict(self, frame):
        model_path = " ./model/bestl.pt"
        model = torch.hub.load("./yolov5", "custom", path=model_path, source='local')

#        Preprocess Image
#        image = cv2.imread(image_path)
#        resized_image = cv2.resize(image, (640, 640)).astype('float32') / 255.0
#        img_tensor = torch.from_numpy(resized_image).permute(2, 0, 1).unsqueeze(0)
        
        with torch.no_grad():
            output = model(img_tensor)
        
        conf_minimum = 0.8

        tobjs: TrafficObject = []
        light_cnt = 0
        sign_cnt = 0

        for i in range(output.size(1)):
            detection = output[0, i]

            x_center = detection[0].item()
            y_center = detection[1].item()
            width = detection[2].item()
            height = detection[3].item()
            conf = detection[4].item()

            # [5] : traffic_light, [6] : traffic_sign
            light = detection[5].item()
            sign = detection[6].item()

#            if i == 0:
#                print(x_center, "\n", y_center, "\n", width, "\n", height)

            if (conf > conf_threshold):
                x1 = int(x_center - width / 2)
                y1 = int(y_center - height / 2)
                x2 = int(x_center + width / 2)
                y2 = int(y_center + height / 2)
                
                if(light > sign and light_cnt == 0):
                    tobjs.append(TrafficObject([y1, y2, x1, x2], LIGHT))
                    light_cnt += 1
                elif(light < sign and sign_cnt == 0):
                    tobjs.append(TrafficObject([y1, y2, x1, x2], SIGN))
                    sign_cnt += 1

        return (frame, tobjs)

    def start(self, frame):
        frame, tobjs = self.predict(frame)
        with torch.no_grad():
            output = model(img_tensor)
            frame = self.opencv(frame, tobjs)
        return frame
