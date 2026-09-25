from pathlib import Path
import shutil
import tempfile

MAX_COPIES = 4


def replicate():
    source = Path(__file__).resolve()

    with tempfile.TemporaryDirectory(prefix="replication_demo_") as temp:
        temp_dir = Path(temp)

        current = source

        for i in range(1, MAX_COPIES + 1):
            copy_path = temp_dir / f"copy_{i}.py"
            shutil.copy2(current, copy_path)

            print(f"Created copy {i}: {copy_path.name}")
            current = copy_path

        print("\nStopped after 4 copies.")
        print("The temporary files will be deleted automatically.")


if __name__ == "__main__":
    replicate()
