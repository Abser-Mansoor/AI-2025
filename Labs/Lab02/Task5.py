import random

class Room:
    def __init__(self, id, schedule: str):
        self.id = id
        self.schedule = schedule
        self.med_needed = str(random.choice(["1", "5"]))  # Medicine ID as string
        self.situation = random.choice([1, 0])  # 1 = Critical, 0 = Normal

class Storage:
    def __init__(self):
        self.medicines = {
            "1": "Paracetamol",
            "2": "Ibuprofen",
            "3": "Aspirin",
            "4": "Cetirizine",
            "5": "Doxycycline",
        }

class Station:
    def __init__(self):
        self.availability = True  # Whether nurses are available

class Environment:
    def __init__(self, corridors, pat_rooms, nurse_stations, storage):
        self.corridors = corridors
        self.pat_rooms = pat_rooms  # List of Room objects
        self.nurse_stations = nurse_stations  # List of Station objects
        self.storage = storage  # Storage object

class Goal_Agent:
    def __init__(self, ids, environment: Environment):
        self.goal = "Deliver Medicines"
        self.env = environment
        self.loc = environment.corridors[0]  # Start in the first corridor
        self.med_on_hand = None
        self.time = "0500"
        self.ids = ids

    def Move(self, to):
        self.loc = to
        print(f"Moving to {self.loc}\n")

    def Pick_Medicine(self, med_id):
        if med_id in self.env.storage.medicines:
            self.Move("Storage")
            self.med_on_hand = self.env.storage.medicines[med_id]
            print(f"Picked up {self.med_on_hand} (ID: {med_id})\n")
        else:
            print(f"Medicine ID {med_id} not found in storage!\n")

    def Deliver_Medicine(self, room):
        if self.med_on_hand:
            self.Move(f"Room {room.id}")
            print(f"Scanning Patient ID in Room {room.id}...\n")

            if room.id in self.ids:  # Check if the room ID is in the list
                if room.situation == 0:
                    print(f"Delivering {self.med_on_hand} to Room {room.id}\n")
                    room.med_needed = "0"  # Mark medicine as delivered
                    self.med_on_hand = None  # Medicine is now delivered
                else:
                    print(f"Critical situation in Room {room.id}! Alerting staff...\n")
                    self.Alert_Staff()
            else:
                print("Patient ID mismatch! Cannot deliver.\n")
        else:
            print("No medicine on hand to deliver!\n")

    def Alert_Staff(self):
        for station in self.env.nurse_stations:
            if station.availability:
                station.availability = False
                print("Staff dispatched to handle critical situation!\n")
                return
        print("No available staff at the moment!\n")

    def Act(self):
        for room in self.env.pat_rooms:
            if self.time == room.schedule and room.med_needed != "0":  # Check if it's time to deliver
                self.Pick_Medicine(room.med_needed)
                self.Deliver_Medicine(room)

corridors = ["Corridor A", "Corridor B"]
pat_rooms = [Room(101, "0500"), Room(102, "0600"), Room(103, "0500")]
nurse_stations = [Station(), Station()]
storage = Storage()
hospital_env = Environment(corridors, pat_rooms, nurse_stations, storage)
robot = Goal_Agent(ids=[101, 102, 103], environment=hospital_env)
robot.Act()
