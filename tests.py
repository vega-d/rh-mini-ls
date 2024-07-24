import os
import subprocess
import pytest
import tempfile
import shutil


@pytest.fixture
def setup_directory_structure():
    # Create a temporary directory structure for testing
    base_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(base_dir, 'dir1'))
    os.mkdir(os.path.join(base_dir, 'dir2'))
    with open(os.path.join(base_dir, 'file1.txt'), 'w') as f:
        f.write('Hello, World!')
    with open(os.path.join(base_dir, 'dir1', 'file2.txt'), 'w') as f:
        f.write('Hello from dir1!')

    yield base_dir
    # shutil.rmtree(base_dir)  # Clean up after tests


def execute_script(script_path, args=""):
    try:
        command = ['python', script_path]
        if args:
            command.append(args)
        # Run the script and capture output
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True  # Raises an error if the command fails
        )
        return result.stdout  # Return the standard output
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"  # Return standard error if there's an error


def test_mini_ls_current_directory(setup_directory_structure):
    base_dir = setup_directory_structure
    shutil.copy("./mini-ls.py", base_dir)
    os.chdir(base_dir)

    result = execute_script("./mini-ls.py", "./")

    # Check if the output contains the expected files and directories
    assert ('file1.txt' in result)
    assert ('dir1' in result)
    assert ('dir2' in result)


def test_mini_ls_recursive(setup_directory_structure):
    base_dir = setup_directory_structure
    shutil.copy("./mini-ls.py", base_dir)
    os.chdir(base_dir)

    result = execute_script("./mini-ls.py", "-r")

    # Check if the output contains the expected file in dir1
    assert ('file2.txt' in result)


def test_mini_ls_with_file(setup_directory_structure):
    base_dir = setup_directory_structure
    shutil.copy("./mini-ls.py", base_dir)
    os.chdir(base_dir)

    result = execute_script("./mini-ls.py", "file1.txt")

    # Check if the output contains the expected file
    assert 'file1.txt' in result


def test_mini_ls_no_arguments(setup_directory_structure):
    base_dir = setup_directory_structure
    shutil.copy("./mini-ls.py", base_dir)
    os.chdir(base_dir)

    result = execute_script("./mini-ls.py")

    # Check if the output is not empty
    assert len(result) > 0
