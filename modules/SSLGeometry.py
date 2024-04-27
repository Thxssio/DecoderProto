class SSLGeometry:
    def __init__(self):
        self.field_size = []
        self.penalty_area = []
        self.geometry_frame = None
        self.goal_size = []

    def set_geometry_frame(self, geometry_frame):
        self.geometry_frame = geometry_frame

    def process_field_info(self, geometry_frame):
        self.set_geometry_frame(geometry_frame)
        self.get_penalty_info()
        self.get_field_size()
        self.get_goal_size()

    def get_penalty_info(self):
        area_depth, area_width = None, None
        if self.geometry_frame.field.HasField("penalty_area_depth"):
            area_depth = self.geometry_frame.field.penalty_area_depth
            print(area_depth)
        if self.geometry_frame.field.HasField("penalty_area_width"):
            area_width = self.geometry_frame.field.penalty_area_width
        if area_depth is not None and area_width is not None:
            self.penalty_area = [
                area_width,
                area_depth,
            ]
            # print(self.penalty_area)

    def get_field_size(self):
        self.field_size = [
            self.geometry_frame.field.field_length,
            self.geometry_frame.field.field_width,
        ]

    def get_goal_size(self):
        self.goal_size = [
            self.geometry_frame.field.goal_width,
            self.geometry_frame.field.goal_depth,
        ]
        # print(self.goal_size)