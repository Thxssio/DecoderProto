from .Receiver import VisionReceiver


class SSLDetection(VisionReceiver):
    def process_positions(self, detection_frame):
        self.set_blue_robots(detection_frame)
        self.set_yellow_robots(detection_frame)
        self.set_ball_positions(detection_frame)

    def set_blue_robots(self, detection_frame):
        robots_blue = []

        # Processar posições dos robôs azuis
        for robot_info in detection_frame.robots_blue:
            robot_data = (
                robot_info.robot_id,
                (robot_info.x, robot_info.y, robot_info.orientation),
            )
            robots_blue.append(robot_data)

        # Atualizar informações dos robôs azuis existentes ou adicionar novos
        for robot_id, new_info in robots_blue:
            updated = False
            for i, (existing_id, existing_info) in enumerate(self.robots_blue):
                if existing_id == robot_id:
                    # Atualizar informações do robô existente com o mesmo ID
                    self.robots_blue[i] = (robot_id, new_info)
                    updated = True
                    break
            if not updated:
                # Adicionar novas informações de robô se não existir um com o mesmo ID
                self.robots_blue.append((robot_id, new_info))

    def set_yellow_robots(self, detection_frame):
        robots_yellow = []
        for robot_info in detection_frame.robots_yellow:
            robot_data = (
                robot_info.robot_id,
                (robot_info.x, robot_info.y, robot_info.orientation),
            )
            robots_yellow.append(robot_data)

            # Atualizar informações dos robôs amarelos existentes ou adicionar novos
        for robot_id, new_info in robots_yellow:
            updated = False
            for i, (existing_id, existing_info) in enumerate(
                self.robots_yellow
            ):
                if existing_id == robot_id:
                    # Atualizar informações do robô existente com o mesmo ID
                    self.robots_yellow[i] = (robot_id, new_info)
                    updated = True
                    break
            if not updated:
                # Adicionar novas informações de robô se não existir um com o mesmo ID
                self.robots_yellow.append((robot_id, new_info))

    def set_ball_positions(self, detection_frame):
        balls = detection_frame.balls
        if balls:
            max_confidence_ball = max(balls, key=lambda ball: ball.confidence)
            ball_position = (max_confidence_ball.x, max_confidence_ball.y)
            self.ball_position = ball_position