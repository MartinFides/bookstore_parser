import subprocess
from pathlib import Path


def get_file_path(path_and_file_name: str) -> Path:
    """
    The function can be only run in a git repo or locally.
    """
    # Use git command to determine repo root.
    git_cmd_proc = subprocess.run(["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE)
    git_cmd_proc.check_returncode()
    repo_root = git_cmd_proc.stdout.decode().strip()

    return Path(f"{repo_root}/{path_and_file_name}")
