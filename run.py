# import os
# import subprocess

# # Change directory to where your virtual environment is located
# venv_scripts_dir = r"C:\Users\arthur.medeiros\Desktop\SAP GUI\venv\Scripts"
# os.chdir(venv_scripts_dir)

# # Activate the virtual environment
# activate_venv_command = "call activate"
# subprocess.call(activate_venv_command, shell=True)

# # Change directory to where your Python script is located
# project_dir = r"C:\Users\arthur.medeiros\Desktop\SAP GUI"
# os.chdir(project_dir)

# # Run the Python script
# subprocess.call("python project.py", shell=True)

# # Keep the command prompt open (equivalent to cmd /K)
# subprocess.call("cmd /K", shell=True)


# THE CODE WAS THIS .BAT SCRIPT BELLOW

# REM SCRIPT TO ACTVATE PYTHON VENV TO EXECUTE STREAMLIT DASHBOARD THROUGH GUI

# REM Change directory to where your virtual environment is located
# cd C:\Users\arthur.medeiros\Desktop\SAP GUI\venv\Scripts

# REM Activate the virtual environment
# call activate

# REM Optionally, you can run a Python script or start an interactive Python session
# cd C:\Users\arthur.medeiros\Desktop\SAP GUI\

# python project.py


# cmd /K

import os
import subprocess
import sys


def create_and_activate_venv(venv_name):
    # Check if venv already exists
    if not os.path.exists(venv_name):
        print(f"Creating virtual environment '{venv_name}'...")
        subprocess.check_call([sys.executable, '-m', 'venv', venv_name])
    else:
        print(f"Virtual environment '{venv_name}' already exists.")
    
    # Activate the virtual environment

    activate_script = os.path.join(venv_name, 'Scripts', 'activate.bat')
    command = f'cmd /k "{activate_script}"'


    print(f"Activating virtual environment '{venv_name}'...")
    os.system(command)



# Replace 'myenv' with your desired virtual environment name
create_and_activate_venv('venv')



def run_script():
    # Define the path to the script
    script_path = "project.py"
    
    # Check if the script exists
    if not os.path.isfile(script_path):
        print(f"Error: {script_path} does not exist.")
        return

    # Run the script using Python
    try:
        result = subprocess.run(["python", script_path], capture_output=True, text=True)
        print("Script output:\n", result.stdout)
        if result.stderr:
            print("Script errors:\n", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

run_script()




