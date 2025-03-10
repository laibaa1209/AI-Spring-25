class Environment:
    def __init__(self, corridors, room, nurse_stations, p_id, med_time, med_type):
        self.corridors = corridors
        self.patient_room = {
            "room num": room,  # list of room numbers
            "patient id": p_id,  # list of patient IDs
            "patient med schedule": med_time  # list of medicine schedules
        }
        self.nurse_stations = nurse_stations
        self.medicine_storage_area = med_type  # list of medicines

    def get_room_num(self, pt_idx):
        return self.patient_room["room num"][pt_idx]
    
    def get_patient_schedule(self, pt_idx):
        return self.patient_room["patient med schedule"][pt_idx]

    def get_medicine(self, pt_idx):
        return self.medicine_storage_area[pt_idx]

    def get_patient_id(self, pt_idx):
        return self.patient_room["patient id"][pt_idx]

    def staff_availability(self):
        print("The staff is needed!!")


class Robot:
    def __init__(self):
        self.model = {
            "move_around": 0,
            "interact_with_patients": 0,
            "medicine_picking": 0,
            "delivered_medicine": 0,
            "alert": 0
        }

    def move_to_storage(self):
        self.model["move_around"] = 1
        print("Robot is moving to storage...")

    def pick_up_medicine(self, env, pt_idx):
        self.model["medicine_picking"] = 1
        medicine = env.get_medicine(pt_idx)
        print(f"Robot has picked up {medicine} from storage.")

    def move_to_room(self, env, pt_idx):
        self.model["move_around"] = 1
        room = env.get_room_num(pt_idx)
        print(f"Robot is moving to Patient Room {room}...")

    def scan_id(self, env, pt_idx):
        patient_id = env.get_patient_id(pt_idx)
        print(f"Scanning ID...Patient ID {patient_id} verified.")

    def medicine_delivery(self, env, pt_idx):
        self.model["delivered_medicine"] = 1
        schedule = env.get_patient_schedule(pt_idx)
        print(f"Medicine delivered as per schedule: {schedule}.")

    def complete_delivery(self, env, pt_idx):
        """ Full medicine delivery process for one patient """
        print("\n==== Medicine Delivery Process Started ====")
        self.move_to_storage()
        self.pick_up_medicine(env, pt_idx)
        self.move_to_room(env, pt_idx)
        self.scan_id(env, pt_idx)
        self.medicine_delivery(env, pt_idx)
        print("Delivery successfully completed!")
        print("========================================\n")

    def alert_staff(self):
        self.model["alert"] = 1
        print("Alert! There's an emergency situation!")



env = Environment(
    corridors=["A", "B", "C"],
    room=[101, 102, 103],
    nurse_stations=["Station 1", "Station 2"],
    p_id=[1111, 2222, 3333],
    med_time=["8 AM", "12 PM", "6 PM"],
    med_type=["Paracetamol", "Ibuprofen", "Amoxicillin"]
)

robot = Robot()

robot.complete_delivery(env, 1)
