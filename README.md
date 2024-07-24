# mini-ls

`mini-ls` is a simple command-line utility that mimics the functionality of the Unix `ls` command. It provides information about files and directories, including their owner, permissions, and last modified time. This tool was designed because I was asked to. Looks professional though innit.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Testing](#testing)
- [License](#license)

## Features

- Lists file information: owner, permissions, and modified time.
- Supports recursive listing with the `-r` option.

## Installation

To install `mini-ls`, clone the repository and run the installation script:

```bash
git clone https://github.com/vega-d/rh-mini-ls.git
cd rh-mini-ls
./install.sh
```

This will set up `mini-ls` on your system.

## Usage

To use `mini-ls`, open your terminal and run the following command:

```bash
./mini-ls [OPTIONS] [FILE...]
```

### Examples

- List information about the current directory:

  ```bash
  ./mini-ls
  ```

- List information about specific files:

  ```bash
  ./mini-ls file1.txt file2.txt
  ```

- List information recursively in a directory:

  ```bash
  ./mini-ls -r /path/to/directory
  ```

## Options

- `-r`: Run recursively on any directory encountered.

## Testing

To ensure the functionality of `mini-ls`, you can run the provided tests. Execute the following command:

```bash
./run_tests.sh
```

This will run a series of automated tests to verify that `mini-ls` behaves as expected.

## License

This project is licensed under the Unlicense License.
Do whatever.
---
