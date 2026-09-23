# very-easy-macos-hotkey-keyboard-shortcut-singular-script-beginner-friendly
Global macOS hotkey automation from one Python file. Open files, folders, apps and URLs or run Shell, Python, JavaScript, AppleScript, JXA, Swift, Go and AWK without learning a complex automation suite.

===========================================================================================================================================================================================================

# macOS Universal Hotkey Runner

A lightweight global hotkey automation engine contained in one Python script.

Instead of learning a complex automation tool you define shortcuts at the top of the file and run the script once.

Use hotkeys to:

* Open folders
* Open files
* Open apps
* Open URLs
* Run Shell scripts
* Run Python
* Run JavaScript
* Run AppleScript or JXA
* Run Swift
* Run Go
* Run AWK

The script runs in the background and automatically reloads when you edit and save it.

## Requirements

* macOS
* Python 3
* PyObjC with AppKit and Quartz
* Accessibility permission for Python

Optional runtimes such as Node.js or Go are only required if you use those action types. But not necessary if u just use open actions, shell, python, applescript,..

## Usage

Edit the shortcut blocks near the top (sequence of ALT, CMD, CTRL > irrelevant):

```text
CTRL+CMD+D     ~/Downloads
CTRL+CMD+T     Terminal
CTRL+ALT+1     ~/Scripts/example.py
```

Run:

```bash
python3 hotkeys.py
```

omg, thats actually it, no weird complexity. Enjoy.

Run the file again at any time to replace the currently running instance.
