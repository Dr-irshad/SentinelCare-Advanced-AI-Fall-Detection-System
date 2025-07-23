class DigitalTwin:
    def __init__(self):
        self.environment_state = "normal"

    def update_environment(self, fall_detected):
        if fall_detected:
            self.environment_state = "fall"
        else:
            self.environment_state = "normal"

    def simulate(self):
        # Add logic to simulate different scenarios
        print(f"Current Environment State: {self.environment_state}")

if __name__ == "__main__":
    twin = DigitalTwin()
    # Simulate a fall detection event
    twin.update_environment(fall_detected=True)
    twin.simulate()
