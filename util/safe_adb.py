from time import sleep
from subprocess import check_output, CalledProcessError

CHANCES = 5
WAITSEC = 5
SUCCESS = 0

def adb(*cmd):
    cmd = " ".join(cmd)
    cmd = "adb " + cmd
    for _ in range(CHANCES):
        try:
            return check_output(cmd, shell=True)
        except CalledProcessError as e:
            print "ADB failed:", e
            print "Command:", cmd
            print "Return code:", e.returncode
            print "Output:", e.output
            sleep(WAITSEC)
        except Exception as e:
            print "Ran into exception", e
            print "Command:", cmd
            sleep(WAITSEC)
