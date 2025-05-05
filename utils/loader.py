import itertools
import threading
import time
import sys

def loading_animation(message="Loading...", delay=0.1):
    done_flag = {"value": False}

    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done_flag["value"]:
                break
            sys.stdout.write(f'\r{message} {c}')
            sys.stdout.flush()
            time.sleep(delay)
        # Clear the line completely
        sys.stdout.write('\r' + ' ' * (len(message) + 4) + '\r')
        sys.stdout.flush()

    t = threading.Thread(target=animate)
    t.start()

    def stop():
        done_flag["value"] = True
        t.join()

    return stop

