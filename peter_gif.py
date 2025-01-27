import os

if __name__ == "__main__":
    # Check if the script is already running in a new terminal, not used anymore
    '''
    if os.environ.get("RUNNING_IN_TERMINAL") != "1":
        # Set the environment variable and run in a new terminal
        script_path = os.path.abspath(__file__)
        os.environ["RUNNING_IN_TERMINAL"] = "1"  # Mark the script as running in the terminal
        run_in_terminal(script_path)
        sys.exit()  # Exit the parent process after opening a new terminal
    '''

    current_path = os.getcwd()
    gif_name = input("Please enter the name of the gif stored in the 'in' folder: ")
    if not gif_name.lower().endswith('.gif'):
        gif_name += '.gif'
    gif_path = os.path.join(current_path, 'Gif', 'in', gif_name)
    print("Relative Path:", gif_path)

    from Codebase.video_to_asci import gif_to_ascii

    terminal_width = int(input("Enter the terminal width for ASCII art (default 100): ") or 100)
    save_path = os.path.join(current_path, 'Gif', 'out', 'output.gif')
    gif_to_ascii(gif_path, width=terminal_width, save_path=save_path)
