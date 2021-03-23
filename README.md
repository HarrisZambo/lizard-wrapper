# Lizard Wrapper

Lizard Wrapper is a tool used to analyse the complexity of projects by looking at function/method lengths and number of functions/methods in code files.

This tool comes in handy when trying to identify the monster functions and files in your code. This is very useful when you want to learn where to cut and what to split.

## Dependencies

- Docker
- An environment where you can run Bash commands (like Linux or MacOS terminals, or Git Bash on Windows)

## Installation

Download and unzip the archive found at https://github.com/HarrisZambo/lizard-wrapper.

## Usage

Run the script called `main.sh`.

This script takes one argument that represents the path to the local repository/file that you want to analyse. Starting with that location, the tool goes recursively in all subdirectories and analyses all supported code files.

```bash
./main.sh "path_to_repo_to_be_analysed"
```

### Expected output

The script will generate a folder called `results` right next to `main.sh`. Inside that folder you will find a *JSON* file containing the results. That file is compatible with DX-Platform.

## Original authors

This tool was originaly developed as a project for Computer Science faculty by:
- Robert Mîrza
- Harris Zambo

## Credits

Thanks to the developers that work on Lizard. More information here: http://www.lizard.ws.

## Contributing

Pull requests are welcome.

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct.md)

## License
[MIT](https://choosealicense.com/licenses/mit/)