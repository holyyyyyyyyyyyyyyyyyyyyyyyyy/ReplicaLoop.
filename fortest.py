from pathlib import Path 
import shutil 
import tempfile  
def replicate(): 
    source = Path(__file__).resolve() 
    with tempfile.TemporaryDirectory(prefix="replication_demo_") as temp:
        temp_dir = Path(temp)
        current = source  
        c=1
        while True: 
                copy_path = temp_dir / f"copy_{c}.py" 
                shutil.copy2(current, copy_path) 
                print(f"Created copy {c}: {copy_path.name}") 
                current = copy_path 
                c = c+1
if __name__ == "__main__": 
    replicate()

#An infinite self-replicating file-copy program that can exhaust disk space if left running


# Ctrl + C
# Stops the currently running Python script from the terminal.

# Windows:
# taskkill /F /IM python.exe
# Forcefully terminates running Python processes.
# WARNING: this can stop ALL running Python programs.
