import subprocess

def clone_blender_repo(repo_url, local_path):
    try:
        subprocess.run(['git', 'clone', repo_url, local_path], check=True)
        print(f"Successfully cloned the repository at {local_path}.")
    except subprocess.CalledProcessError as e:
        print(f"Error while cloning the repository: {e}")


def sync_blender_repo(local_path):
    try:
        subprocess.run(['git', '-C', local_path, 'pull'], check=True)
        print(f"Successfully synced the repository at {local_path}.")
    except subprocess.CalledProcessError as e:
        print(f"Error while syncing the repository: {e}")


repo_url = "https://github.com/blender/blender.git"
local_path = "G:\\ClayTree\\BlenderSource" # Put your own source here

try:
    clone_blender_repo(repo_url, local_path)
except Exception as e:
    print(f"Error while cloning the repository: {e}")

try:
    sync_blender_repo(local_path)
except Exception as e:
    print(f"Error while syncing the repository: {e}")
