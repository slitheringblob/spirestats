from codecs import ignore_errors
from shutil import ignore_patterns
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from stats.event_handlers import on_moved, on_created, on_deleted, on_modified

def run_watchdog():
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True

    #create event handler
    eh = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    #map functions to events
    eh.on_created = on_created
    eh.on_deleted = on_deleted
    eh.on_modified = on_modified
    eh.on_moved = on_moved

    path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\SlayTheSpire\\runs\\IRONCLAD\\"
    go_recursively = True
    obs = Observer()
    obs.schedule(eh , path , recursive=go_recursively)
    obs.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        obs.stop()
        obs.join()

if __name__=='__main__':
    run_watchdog()