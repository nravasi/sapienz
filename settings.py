DEBUG = False
# if False, "0" will be used
ENABLE_STRING_SEEDING = False
# use headless evaluator
HEADLESS = False


# === Emulator ===
DEVICE_NUM = 0
AVD_BOOT_DELAY = 5
AVD_SERIES = "api19_"
EVAL_TIMEOUT = 100
# if run on Mac OS, use "gtimeout"
TIMEOUT_CMD = "gtimeout"
TIME_LIMIT = 30


# === Env. Paths ===
# path should end with a '/'
ANDROID_HOME = '/Users/nmravasi/Library/Android/sdk/'
# the path of sapienz folder
WORKING_DIR = '/Users/nmravasi/dev/thesis/sapienz/'


# === GA parameters ===
SEQUENCE_LENGTH_MIN = 100
SEQUENCE_LENGTH_MAX = 1000
SUITE_SIZE = 5
POPULATION_SIZE = 10
OFFSPRING_SIZE = 10
GENERATION = 10
# Crossover probability
CXPB = 0.7
# Mutation probability
MUTPB = 0.3


# === Only for main_multi ===
# start from the ith apk
APK_OFFSET = 0
APK_DIR = ""
REPEATED_RESULTS_DIR = ""
REPEATED_RUNS = 20


# === MOTIFCORE script ===
# for initial population
MOTIFCORE_SCRIPT_PATH = '/mnt/sdcard/motifcore.script'
# header for evolved scripts
MOTIFCORE_SCRIPT_HEADER = 'type= raw events\ncount= -1\nspeed= 1.0\nstart data >>\n'
