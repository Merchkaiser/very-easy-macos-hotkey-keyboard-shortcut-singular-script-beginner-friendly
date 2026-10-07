# =============================================================================
# UNIVERSAL HOTKEY ACTION RUNNER FOR macOS
# =============================================================================
#
# !!! ATTENTION — READ THIS FIRST !!!
#
# These are the important parts.
# Read this section and you know what to do.
#
# 1. Make sure Python 3 is installed.
#
# 2. Run this once in Terminal:
#
#    python3 -m pip install pyobjc
#
# 3. Give Python permission to read keyboard shortcuts:
#
#    System Settings
#    → Privacy & Security
#    → Accessibility
#    → Enable Python / Terminal
#
# 4. Add your shortcuts in the sections below.
#
# 5. Run this Python file once.
#
# 6. Done. Your shortcuts now work anywhere on your Mac.
#
#
# EXAMPLE
# -------
#
# CTRL+CMD+D     ~/Downloads
#
# Press CTRL+CMD+D → Downloads opens.
#
#
# WHAT CAN A HOTKEY DO?
# ---------------------
#
# - Open folders
# - Open files
# - Open apps
# - Open websites
# - Run Python scripts
# - Run Shell scripts
# - Run JavaScript
# - Run AppleScript
# - Run JXA
# - Run Swift
# - Run Go
# - Run AWK
#
#
# HOW TO ADD ONE
# --------------
#
# Write:
#
# HOTKEY     THING_TO_OPEN_OR_RUN
#
# Example:
#
# CTRL+CMD+T     Terminal
#
# You can also use the same hotkey for multiple actions.
#
#
# RUNNING
# -------
#
# Run this file once → it keeps working in the background.
#
# Run it again → old copy is automatically replaced.
#
# Edit and save this file → it reloads automatically.
#
#
# OPTIONAL
# --------
#
# JavaScript actions need Node.js.
# Go actions need Go.
# Other action types only need their matching tools if you actually use them.
#
#
# AFTER RESTART
# -------------
#
# If you want this to start automatically every time your Mac starts
# add this script to your startup setup.
#
# =============================================================================


import os, queue, signal, subprocess, sys, tempfile, threading, time, traceback


### PS: DONT GET CONFUSED, THE STUFF U FIND DOWN HERE IS WHAT I PERSONALLY USED, U CAN OBVIOUSLY REPLACE IT & CREATE UR OWN STUFF, BUT I GUESS IT SERVES WELL AS EXAMPLE.
### PS: DONT GET CONFUSED, THE STUFF U FIND DOWN HERE IS WHAT I PERSONALLY USED, U CAN OBVIOUSLY REPLACE IT & CREATE UR OWN STUFF, BUT I GUESS IT SERVES WELL AS EXAMPLE.
### PS: DONT GET CONFUSED, THE STUFF U FIND DOWN HERE IS WHAT I PERSONALLY USED, U CAN OBVIOUSLY REPLACE IT & CREATE UR OWN STUFF, BUT I GUESS IT SERVES WELL AS EXAMPLE.
### PS: DONT GET CONFUSED, THE STUFF U FIND DOWN HERE IS WHAT I PERSONALLY USED, U CAN OBVIOUSLY REPLACE IT & CREATE UR OWN STUFF, BUT I GUESS IT SERVES WELL AS EXAMPLE.
### PS: DONT GET CONFUSED, THE STUFF U FIND DOWN HERE IS WHAT I PERSONALLY USED, U CAN OBVIOUSLY REPLACE IT & CREATE UR OWN STUFF, BUT I GUESS IT SERVES WELL AS EXAMPLE.


# <><><><><><><><><><><><><><><><><><>
#          ~~~ FOLDER < OPEN ~~~
# <><><><><><><><><><><><><><><><><><>

FOLDERS_OPEN = """
CTRL+CMD+Z     ~/
CTRL+CMD+D     ~/Downloads
CTRL+CMD+A      /Applications
CTRL+CMD+W     ~/Library/Mobile Documents/com~apple~CloudDocs
"""

# <><><><><><><><><><><><><><><><><><>
#          ~~~ FILE < OPEN ~~~
# <><><><><><><><><><><><><><><><><><>

FILES_OPEN = """

"""

# <><><><><><><><><><><><><><><><><><>
#          ~~~ APP < OPEN ~~~
# <><><><><><><><><><><><><><><><><><>

APPS_OPEN = """

CTRL+CMD+T     Terminal

CTRL+CMD+B     Safari

CTRL+CMD+G     TextEdit

CTRL+CMD+E     Mail

CTRL+CMD+S      DEVONthink

"""

# <><><><><><><><><><><><><><><><><><>
#          ~~~ URL < OPEN ~~~
# <><><><><><><><><><><><><><><><><><>

URLS_OPEN = """

CTRL+CMD+Y      https://www.youtube.com/feed/playlists

# ↓ KK FOR TESTING
CMD+ALT+CTRL+SHIFT+8

"""

# <><><><><><><><><><><><><><><><><><>
#          ~~~ SHELL < RUN ~~~
# <><><><><><><><><><><><><><><><><><>

SHELL_RUN = """

# (ROUT) COMMUNICATION-PLATFORMS -- OPENING
SHIFT+CTRL+ALT+L     /users/supersaiyan1/wachulookinat/COMMUNICATION-PLATFORMS < OPENING_sh.txt

# ↓ KK FOR TESTING
CMD+ALT+CTRL+SHIFT+8

"""

# <><><><><><><><><><><><><><><><><><>
#          ~~~ ASCRIPT < RUN ~~~
# <><><><><><><><><><><><><><><><><><>

ASCRIPT_RUN = """

# ↓ KK FOR TESTING
CMD+ALT+CTRL+SHIFT+8

"""

# <><><><><><><><><><><><><><><><><><>
#          ~~~ JS < RUN ~~~
# <><><><><><><><><><><><><><><><><><>

JAVASCRIPT_RUN = """

# ↓ KK FOR TESTING
CMD+ALT+CTRL+SHIFT+8

"""

# <><><><><><><><><><><><><><><><><><>
#          ~~~ JXA < RUN ~~~
# <><><><><><><><><><><><><><><><><><>

JXA_RUN = """

# ↓ KK FOR TESTING
CMD+ALT+CTRL+SHIFT+8

"""

# <><><><><><><><><><><><><><><><><><>
#          ~~~ PYT < RUN ~~~
# <><><><><><><><><><><><><><><><><><>

PYTHON_RUN = """

# ↓ PWL -- MACRO-FINDER MEGA-MACRO ↓
CTRL+A     /users/supersaiyan1/wachulookinat/(PWL) MACRO-FINDER -- SEM-SEARCH & MACRO-TAGS -- MINI-AI -- MUST SPECIFY FOLDER_py.txt

# ↓ PWL-PASTING ↓
CTRL+S      /users/supersaiyan1/wachulookinat/(NSS) PWL-PASTING_py.txt

# ↓ PWL -- LOCAL-LLM > SHORT C&P-CMDS ↓
CTRL+E      /users/supersaiyan1/wachulookinat/(NSS) (PWL) LOCAL-LLM > SHORT C&P-CMDS -- BASICALLY LIKE MACROS_py.txt

# MARK MSN > AS FINISHED > VIA REPLACING > BULLET-CHARS > WITH STAR-CHARS
SHIFT+CMD+L    /users/supersaiyan1/wachulookinat/(NSS) MARK MSN AS FINISHED VIA REPLACING BULLET-CHAR WITH STAR-CHAR_py.txt

# SINGLE + MULTI LINE > ADD CUSTOM-BULLETS -- SELECTED TEXT
CTRL+ALT+1      /users/supersaiyan1/wachulookinat/(SS) MULTI-LINE-BEGINNINGS > PASTE CUSTOM-BULLETS AT FRONT > OF SELECTED TEXTS_py.txt

# SINGLE-LINE PASTING > CUSTOM-BULLET-LAYER
CTRL+ALT+2      /users/supersaiyan1/wachulookinat/(SS) PASTE LAYER 2 CUSTOM-BULLET_py.txt
CTRL+ALT+3      /users/supersaiyan1/wachulookinat/(SS) PASTE LAYER 3 CUSTOM-BULLET_py.txt
CTRL+ALT+4      /users/supersaiyan1/wachulookinat/(SS) PASTE LAYER 4 CUSTOM-BULLET_py.txt
CTRL+ALT+5      /users/supersaiyan1/wachulookinat/(SS) PASTE LAYER 5 CUSTOM-BULLET_py.txt
CTRL+ALT+6      /users/supersaiyan1/wachulookinat/(SS) PASTE LAYER 6 CUSTOM-BULLET_py.txt
CTRL+ALT+7      /users/supersaiyan1/wachulookinat/(SS) PASTE LAYER 7 CUSTOM-BULLET_py.txt
CTRL+ALT+8      /users/supersaiyan1/wachulookinat/(SS) PASTE LAYER 8 CUSTOM-BULLET_py.txt
CTRL+ALT+9      /users/supersaiyan1/wachulookinat/(SS) PASTE LAYER 9 CUSTOM-BULLET_py.txt
CTRL+ALT+0      /users/supersaiyan1/wachulookinat/(SS) PASTE LAYER 10 CUSTOM-BULLET_py.txt

# DELETE > MULTI-LINE > CUSTOM-BULLETS > OF SELECTED TEXTS
CTRL+ALT+X      /users/supersaiyan1/wachulookinat/(SS) MULTI-LINE-BEGINNINGS > DELETE 1 CUSTOM-BULLET-LAYER_py.txt

# ↓ KK FOR TESTING
# CMD+ALT+CTRL+SHIFT+P

"""

# <><><><><><><><><><><><><><><><><><>
#          ~~~ SWIFT < RUN ~~~
# <><><><><><><><><><><><><><><><><><>

SWIFT_RUN = """

# ↓ KK FOR TESTING
CMD+ALT+CTRL+SHIFT+8 

"""

# <><><><><><><><><><><><><><><><><><>
#          ~~~ GO < RUN ~~~
# <><><><><><><><><><><><><><><><><><>

GO_RUN = """

# ↓ KK FOR TESTING
CMD+ALT+CTRL+SHIFT+8 

"""

# <><><><><><><><><><><><><><><><><><>
#          ~~~ GO < RUN ~~~
# <><><><><><><><><><><><><><><><><><>

AWK_RUN = """

# ↓ KK FOR TESTING
CMD+ALT+CTRL+SHIFT+8 

"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# NUTD:
# -- (** KEPT IN KM > CUZ AFTER-OPEN > NEEDED ALL-FOLDER-SELECTION) CTRL+CMD+M     "Keyboard Maestro"
# -- (** REPLACED WITH SEMANTIC MINI-AI) CTRL+A     /users/supersaiyan1/wachulookinat/MASTER-SHELL-OVERVIEW-RUNNER -- ODS-ONLY.txt

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ============================================================================
# SETUP / SINGLE INSTANCE
# ============================================================================

if sys.platform != "darwin":
    raise SystemExit("This script requires macOS.")

try:
    import AppKit
    import Quartz

except ImportError:
    traceback.print_exc()
    raise SystemExit("PyObjC Quartz/Cocoa is required.")


THIS_FILE = os.path.abspath(__file__)
PID_FILE = "/tmp/hotkeys.pid"
USER_SHELL = os.environ.get("SHELL") or "/bin/zsh"


def read_pid():
    try:
        with open(PID_FILE, "r", encoding="ascii") as file:
            return int(file.read().strip())

    except FileNotFoundError:
        return None


def write_pid(pid):
    temp = f"{PID_FILE}.{os.getpid()}.tmp"

    with open(temp, "w", encoding="ascii") as file:
        file.write(str(pid))
        file.flush()
        os.fsync(file.fileno())

    os.replace(temp, PID_FILE)


def pid_alive(pid):
    try:
        os.kill(pid, 0)
        return True

    except ProcessLookupError:
        return False

    except PermissionError:
        return True


def pid_is_this_script(pid):
    result = subprocess.run(
        [
            "ps",
            "-ww",
            "-p",
            str(pid),
            "-o",
            "command=",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )

    return (
        result.returncode == 0
        and THIS_FILE in result.stdout
    )


def stop_previous_instance():
    pid = read_pid()

    if not pid or pid == os.getpid():
        return

    if not pid_alive(pid):
        try:
            os.remove(PID_FILE)

        except FileNotFoundError:
            pass

        return

    if not pid_is_this_script(pid):
        print(
            f"PID {pid} does not belong to this script; "
            "not terminating it.",
            file=sys.stderr,
        )
        return

    os.kill(pid, signal.SIGTERM)

    for _ in range(30):
        if not pid_alive(pid):
            return

        time.sleep(0.05)

    if pid_is_this_script(pid):
        os.kill(pid, signal.SIGKILL)


def launch_daemon():
    stop_previous_instance()

    env = os.environ.copy()
    env["DAEMON_ACTIVE"] = "1"

    child = subprocess.Popen(
        [
            sys.executable,
            THIS_FILE,
        ],
        env=env,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
        close_fds=True,
    )

    write_pid(child.pid)


if os.environ.get("DAEMON_ACTIVE") != "1":
    try:
        launch_daemon()

    except Exception:
        traceback.print_exc()
        sys.exit(1)

    sys.exit(0)


# ============================================================================
# ACTION EXECUTION
# ============================================================================

ACTION_QUEUE = queue.SimpleQueue()


def cleanup_files(paths):
    for path in paths:
        try:
            os.remove(path)

        except FileNotFoundError:
            pass

        except Exception:
            traceback.print_exc()


def wait_process(
    proc,
    description,
    input_text,
    cleanup_paths,
):
    try:
        proc.communicate(input=input_text)

        if proc.returncode != 0:
            print(
                f"FAILED: {description} | exit={proc.returncode}",
                file=sys.stderr,
            )

    finally:
        cleanup_files(cleanup_paths)


def spawn_process(
    cmd,
    description,
    *,
    cwd=None,
    input_text=None,
    cleanup_paths=(),
):
    try:
        proc = subprocess.Popen(
            cmd,
            cwd=cwd,
            stdin=(
                subprocess.PIPE
                if input_text is not None
                else subprocess.DEVNULL
            ),
            text=True,
            encoding="utf-8",
            errors="replace",
            start_new_session=True,
            close_fds=True,
        )

    except Exception:
        cleanup_files(cleanup_paths)

        print(
            f"FAILED to start: {description}",
            file=sys.stderr,
        )

        traceback.print_exc()
        return

    threading.Thread(
        target=wait_process,
        args=(
            proc,
            description,
            input_text,
            tuple(cleanup_paths),
        ),
        daemon=True,
    ).start()


def existing_path(path, kind):
    target = os.path.abspath(
        os.path.expanduser(path)
    )

    valid = (
        os.path.isdir(target)
        if kind == "folder"
        else os.path.isfile(target)
    )

    if not valid:
        raise FileNotFoundError(
            f"{kind.title()} does not exist: {target}"
        )

    return target


def read_source(path):
    target = existing_path(
        path,
        "file",
    )

    with open(
        target,
        "r",
        encoding="utf-8",
    ) as file:
        return target, file.read()


def login_tool(
    args,
    description,
    *,
    cwd=None,
    input_text=None,
    cleanup_paths=(),
):
    spawn_process(
        [
            USER_SHELL,
            "-lic",
            'exec "$@"',
            "hotkeys",
            *args,
        ],
        description,
        cwd=cwd,
        input_text=input_text,
        cleanup_paths=cleanup_paths,
    )


def open_folder(path):
    target = existing_path(
        path,
        "folder",
    )

    spawn_process(
        [
            "open",
            target,
        ],
        f"open folder {target}",
    )


def open_file(path):
    target = existing_path(
        path,
        "file",
    )

    spawn_process(
        [
            "open",
            target,
        ],
        f"open file {target}",
    )


def open_app(app):
    spawn_process(
        [
            "open",
            "-n",
            "-a",
            app,
        ],
        f"open app {app}",
    )


def open_url(url):
    spawn_process(
        [
            "open",
            url,
        ],
        f"open URL {url}",
    )


def run_shell(path):
    target = existing_path(
        path,
        "file",
    )

    spawn_process(
        [
            USER_SHELL,
            "-lic",
            'source "$1"',
            "hotkeys",
            target,
        ],
        f"run Shell {target}",
    )


def run_applescript(path):
    target = existing_path(
        path,
        "file",
    )

    spawn_process(
        [
            "/usr/bin/osascript",
            target,
        ],
        f"run AppleScript {target}",
    )


def run_javascript(path):
    target, source = read_source(path)

    login_tool(
        [
            "node",
            "-",
        ],
        f"run JavaScript {target}",
        cwd=os.path.dirname(target),
        input_text=source,
    )


def run_jxa(path):
    target = existing_path(
        path,
        "file",
    )

    spawn_process(
        [
            "/usr/bin/osascript",
            "-l",
            "JavaScript",
            target,
        ],
        f"run JXA {target}",
    )


def run_python(path):
    target = existing_path(
        path,
        "file",
    )

    spawn_process(
        [
            sys.executable,
            target,
        ],
        f"run Python {target}",
    )


def run_swift(path):
    target, source = read_source(path)

    login_tool(
        [
            "swift",
            "-",
        ],
        f"run Swift {target}",
        cwd=os.path.dirname(target),
        input_text=source,
    )


def run_go(path):
    target, source = read_source(path)

    folder = os.path.dirname(target)

    fd, temp = tempfile.mkstemp(
        prefix="hotkeys_",
        suffix=".go",
        dir=folder,
        text=True,
    )

    try:
        with os.fdopen(
            fd,
            "w",
            encoding="utf-8",
        ) as file:
            file.write(source)
            file.flush()
            os.fsync(file.fileno())

    except Exception:
        try:
            os.close(fd)

        except OSError:
            pass

        cleanup_files(
            (temp,)
        )

        raise

    login_tool(
        [
            "go",
            "run",
            temp,
        ],
        f"run Go {target}",
        cwd=folder,
        cleanup_paths=(
            temp,
        ),
    )


def run_awk(path):
    target = existing_path(
        path,
        "file",
    )

    spawn_process(
        [
            "/usr/bin/awk",
            "-f",
            target,
        ],
        f"run AWK {target}",
    )


# ============================================================================
# SHORTCUT PARSING
# ============================================================================

def parse_entries(block):
    entries = []

    for raw in block.splitlines():
        line = raw.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split(
            None,
            1,
        )

        # Ignore incomplete entries without affecting valid shortcuts.
        if len(parts) != 2:
            print(
                f"Skipping incomplete shortcut: {line!r}",
                file=sys.stderr,
            )
            continue

        entries.append(
            (
                parts[0].lower(),
                parts[1],
            )
        )

    return entries


ACTION_MAP = {}

for block, runner in (
    (
        FOLDERS_OPEN,
        open_folder,
    ),
    (
        FILES_OPEN,
        open_file,
    ),
    (
        APPS_OPEN,
        open_app,
    ),
    (
        URLS_OPEN,
        open_url,
    ),
    (
        SHELL_RUN,
        run_shell,
    ),
    (
        ASCRIPT_RUN,
        run_applescript,
    ),
    (
        JAVASCRIPT_RUN,
        run_javascript,
    ),
    (
        JXA_RUN,
        run_jxa,
    ),
    (
        PYTHON_RUN,
        run_python,
    ),
    (
        SWIFT_RUN,
        run_swift,
    ),
    (
        GO_RUN,
        run_go,
    ),
    (
        AWK_RUN,
        run_awk,
    ),
):
    for combo, target in parse_entries(block):
        ACTION_MAP.setdefault(
            combo,
            [],
        ).append(
            (
                runner,
                target,
            )
        )


def action_worker():
    while True:
        combo, actions = ACTION_QUEUE.get()

        for runner, target in actions:
            try:
                runner(target)

            except Exception:
                print(
                    f"FAILED hotkey action: {combo} | "
                    f"target={target}",
                    file=sys.stderr,
                )

                traceback.print_exc()


# ============================================================================
# KEYBOARD MATCHING
# ============================================================================

MOD_FLAGS = {
    "cmd": Quartz.kCGEventFlagMaskCommand,
    "alt": Quartz.kCGEventFlagMaskAlternate,
    "option": Quartz.kCGEventFlagMaskAlternate,
    "ctrl": Quartz.kCGEventFlagMaskControl,
    "shift": Quartz.kCGEventFlagMaskShift,
}


FLAG_MASK = (
    Quartz.kCGEventFlagMaskCommand
    | Quartz.kCGEventFlagMaskAlternate
    | Quartz.kCGEventFlagMaskControl
    | Quartz.kCGEventFlagMaskShift
)


KEY_ALIASES = {
    "enter": "return",
    "backspace": "delete",
    "esc": "escape",
}


def appkit_character(value):
    if isinstance(
        value,
        str,
    ):
        return value

    return chr(value)


SPECIAL_KEYS = {
    "\r": "return",
    "\t": "tab",
    " ": "space",
    "\x7f": "delete",
    "\x1b": "escape",

    appkit_character(
        AppKit.NSDeleteFunctionKey
    ): "forwarddelete",

    appkit_character(
        AppKit.NSHomeFunctionKey
    ): "home",

    appkit_character(
        AppKit.NSEndFunctionKey
    ): "end",

    appkit_character(
        AppKit.NSPageUpFunctionKey
    ): "pageup",

    appkit_character(
        AppKit.NSPageDownFunctionKey
    ): "pagedown",

    appkit_character(
        AppKit.NSLeftArrowFunctionKey
    ): "left",

    appkit_character(
        AppKit.NSRightArrowFunctionKey
    ): "right",

    appkit_character(
        AppKit.NSDownArrowFunctionKey
    ): "down",

    appkit_character(
        AppKit.NSUpArrowFunctionKey
    ): "up",
}


for number in range(
    1,
    21,
):
    character = appkit_character(
        getattr(
            AppKit,
            f"NSF{number}FunctionKey",
        )
    )

    SPECIAL_KEYS[
        character
    ] = f"f{number}"


NUMPAD_KEYS = {
    "0": "num0",
    "1": "num1",
    "2": "num2",
    "3": "num3",
    "4": "num4",
    "5": "num5",
    "6": "num6",
    "7": "num7",
    "8": "num8",
    "9": "num9",

    "\r": "numenter",
    "=": "numequal",
    "/": "numdivide",
    "*": "nummultiply",
    "-": "numminus",
    "+": "numplus",
    ".": "numdecimal",
    ",": "numdecimal",

    appkit_character(
        AppKit.NSClearLineFunctionKey
    ): "numclear",
}


VALID_NAMED_KEYS = (
    set(
        SPECIAL_KEYS.values()
    )
    | set(
        NUMPAD_KEYS.values()
    )
    | set(
        KEY_ALIASES
    )
)


def compile_hotkeys():
    compiled = {}

    for combo, actions in ACTION_MAP.items():
        try:
            raw_parts = combo.split("+")

            if any(
                not part.strip()
                for part in raw_parts
            ):
                raise ValueError(
                    "contains an empty key/modifier"
                )

            parts = [
                part.strip().lower()
                for part in raw_parts
            ]

            flags = 0
            keys = []

            for part in parts:
                if part in MOD_FLAGS:
                    flags |= MOD_FLAGS[
                        part
                    ]

                else:
                    keys.append(
                        part
                    )

            if len(keys) != 1:
                raise ValueError(
                    "must contain exactly one non-modifier key"
                )

            key = KEY_ALIASES.get(
                keys[0],
                keys[0],
            )

            if (
                len(key) != 1
                and key not in VALID_NAMED_KEYS
            ):
                raise ValueError(
                    f"uses unknown key {key!r}"
                )

            signature = (
                key,
                flags,
            )

            if signature in compiled:
                compiled[
                    signature
                ][1].extend(
                    actions
                )

            else:
                compiled[
                    signature
                ] = [
                    combo,
                    list(actions),
                ]

        except Exception as error:
            print(
                f"Skipping invalid hotkey {combo!r}: {error}",
                file=sys.stderr,
            )

    return compiled


def event_key(event):
    ns_event = (
        AppKit.NSEvent.eventWithCGEvent_(
            event
        )
    )

    if ns_event is None:
        return None

    characters = (
        ns_event.charactersByApplyingModifiers_(
            0
        )
    )

    if not characters:
        return None

    key = str(
        characters
    ).lower()

    if (
        ns_event.modifierFlags()
        & AppKit.NSEventModifierFlagNumericPad
    ):
        numpad_key = NUMPAD_KEYS.get(
            key
        )

        if numpad_key:
            return numpad_key

    return SPECIAL_KEYS.get(
        key,
        key,
    )


COMPILED_HOTKEYS = compile_hotkeys()

TAP_REFERENCE = None
RUN_LOOP = None
SHUTTING_DOWN = False


# ============================================================================
# ACTIVE EVENT TAP
# ============================================================================

def event_tap_callback(
    proxy,
    event_type,
    event,
    refcon,
):
    if event_type in (
        Quartz.kCGEventTapDisabledByTimeout,
        Quartz.kCGEventTapDisabledByUserInput,
    ):
        if TAP_REFERENCE:
            Quartz.CGEventTapEnable(
                TAP_REFERENCE,
                True,
            )

        return event

    if event_type != Quartz.kCGEventKeyDown:
        return event

    key = event_key(
        event
    )

    if key is None:
        return event

    flags = (
        Quartz.CGEventGetFlags(
            event
        )
        & FLAG_MASK
    )

    match = COMPILED_HOTKEYS.get(
        (
            key,
            flags,
        )
    )

    if not match:
        return event

    ACTION_QUEUE.put(
        match
    )

    return None


# ============================================================================
# AUTO-RELOAD
# ============================================================================

def file_signature(path):
    stat = os.stat(
        path
    )

    return (
        stat.st_ino,
        stat.st_size,
        stat.st_mtime_ns,
    )


def valid_stable_script(path):
    before = file_signature(
        path
    )

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as file:
        content = file.read()

    if (
        not content
        or before != file_signature(path)
    ):
        return False

    compile(
        content,
        path,
        "exec",
    )

    return True


def watch_and_reload():
    last_signature = file_signature(
        THIS_FILE
    )

    while not SHUTTING_DOWN:
        time.sleep(
            0.5
        )

        try:
            current_signature = file_signature(
                THIS_FILE
            )

        except Exception:
            traceback.print_exc()
            continue

        if current_signature == last_signature:
            continue

        last_signature = current_signature

        time.sleep(
            0.15
        )

        try:
            if not valid_stable_script(
                THIS_FILE
            ):
                continue

        except Exception:
            traceback.print_exc()
            continue

        try:
            os.execv(
                sys.executable,
                [
                    sys.executable,
                    THIS_FILE,
                ],
            )

        except Exception:
            traceback.print_exc()


# ============================================================================
# ENGINE / CLEANUP
# ============================================================================

def remove_own_pid_file():
    try:
        if read_pid() == os.getpid():
            os.remove(
                PID_FILE
            )

    except FileNotFoundError:
        pass

    except Exception:
        traceback.print_exc()


def handle_shutdown(
    signum,
    frame,
):
    global SHUTTING_DOWN

    if SHUTTING_DOWN:
        return

    SHUTTING_DOWN = True

    if RUN_LOOP:
        Quartz.CFRunLoopStop(
            RUN_LOOP
        )


def main():
    global TAP_REFERENCE
    global RUN_LOOP

    write_pid(
        os.getpid()
    )

    signal.signal(
        signal.SIGTERM,
        handle_shutdown,
    )

    signal.signal(
        signal.SIGINT,
        handle_shutdown,
    )

    threading.Thread(
        target=action_worker,
        daemon=True,
    ).start()

    threading.Thread(
        target=watch_and_reload,
        daemon=True,
    ).start()

    TAP_REFERENCE = Quartz.CGEventTapCreate(
        Quartz.kCGSessionEventTap,
        Quartz.kCGHeadInsertEventTap,
        Quartz.kCGEventTapOptionDefault,
        1 << Quartz.kCGEventKeyDown,
        event_tap_callback,
        None,
    )

    if not TAP_REFERENCE:
        raise RuntimeError(
            "CGEventTapCreate returned NULL. "
            "Check macOS Accessibility permission for Python."
        )

    run_loop_source = (
        Quartz.CFMachPortCreateRunLoopSource(
            None,
            TAP_REFERENCE,
            0,
        )
    )

    if not run_loop_source:
        raise RuntimeError(
            "CFMachPortCreateRunLoopSource returned NULL."
        )

    RUN_LOOP = Quartz.CFRunLoopGetCurrent()

    Quartz.CFRunLoopAddSource(
        RUN_LOOP,
        run_loop_source,
        Quartz.kCFRunLoopCommonModes,
    )

    Quartz.CGEventTapEnable(
        TAP_REFERENCE,
        True,
    )

    Quartz.CFRunLoopRun()


if __name__ == "__main__":
    exit_code = 0

    try:
        main()

    except Exception:
        exit_code = 1
        traceback.print_exc()

    finally:
        remove_own_pid_file()

    sys.exit(
        exit_code
    )
