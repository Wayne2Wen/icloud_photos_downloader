"""Constants"""

# For retrying connection after timeouts and errors
MAX_RETRIES = 5
WAIT_SECONDS = 5

CAMERA_RE = "^IMG_\d+(\.HEIC|_HEVC\.MOV|\.JPG|\.PNG|\.MOV)$"
RECORD_RE = "^RPReplay_Final\d+.mp4$"
MATCH_RE = f"{CAMERA_RE}|{RECORD_RE}"
