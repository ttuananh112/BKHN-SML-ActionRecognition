# Modify DATASET_FOLDER according to your path
DATASET_FOLDER = "/home/anhtt163/Documents/BKHN/materials/statistical_machine_learning/dataset/IneritialGaitActionDataset"

FREQ = 100  # 100Hz
DURATION = 0.5
NUM_SAMPLES = int(FREQ * DURATION)

# labels
MAPPING_LABELS = {
    -1: "invalid",
    0: "level_walk",
    1: "upstairs",
    2: "downstairs",
    3: "slope_up",
    4: "slope_down"
}

# sensors
GX = "Gx"
GY = "Gy"
GZ = "Gz"

AX = "Ax"
AY = "Ay"
AZ = "Az"

SENSORS = [GX, GY, GZ, AX, AY, AZ]

LABEL = "Label"
GROUP = "Group"

CENTER = "CenterSensor"
LEFT = "LeftSensor"
RIGHT = "RightSensor"
POS = [CENTER, LEFT, RIGHT]

TYPES = ["Gyro", "Accel"]
COLUMNS = [f"{pos}_{sen}" for pos in POS for sen in SENSORS]

# processing
WINDOW_SIZE = 50  # 0.5s
STEP = 50  # 0.5s
FREQ_THRESHOLD = 0.8

# extensions
CSV = ".csv"

# Save folder
WINDOWS_FOLDER = f"{DATASET_FOLDER}/windows_w{WINDOW_SIZE}_s{STEP}"
PREPROCESSED_FOLDER = f"{DATASET_FOLDER}/preprocessed_w{WINDOW_SIZE}_s{STEP}"
