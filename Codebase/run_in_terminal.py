import subprocess
import sys


def run_in_terminal(script_path):
    """
    Opens a new terminal and runs the specified Python script.
    """
    python_executable = sys.executable  # Path to the current Python interpreter

    if sys.platform == "win32":
        # Windows: Use 'start' to open a terminal
        subprocess.run(["start", "cmd", "/k", f"{python_executable} {script_path}"], shell=True)
    elif sys.platform == "darwin":
        # macOS: Use 'osascript' to open Terminal and run the script
        apple_script = f"""
        tell application "Terminal"
            do script "{python_executable} {script_path}"
            activate
        end tell
        """
        subprocess.run(["osascript", "-e", apple_script])
    else:
        # Linux: Use 'x-terminal-emulator' or 'gnome-terminal'
        subprocess.run(["x-terminal-emulator", "-e", f"{python_executable} {script_path}"], stderr=subprocess.DEVNULL)

# Provide the path to your gif_to_ascii script
#script_path = "ascii_gif.py"
#run_in_terminal(script_path)