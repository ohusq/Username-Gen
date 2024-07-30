# Username Generator

Welcome to the Username Generator project! This Python-based tool helps you generate random usernames based on given parameters. Whether you need usernames for testing, fun, or creative purposes, this project has got you covered.

## Features

- Generate random usernames
- Save generated usernames to a file
- Ensure necessary folders and files exist before saving
- Easy-to-use command line interface

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- Basic understanding of how to run Python scripts

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ohusq/Username-Gen.git
    cd Username-Gen
    ```

2. Install required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

To generate usernames, run the `main.py` script:

```sh
python main.py
```

### Code Overview

#### main.py

This is the main script that drives the username generation process. It handles user inputs and coordinates the overall functionality.

[View main.py](https://github.com/ohusq/Username-Gen/blob/master/main.py)

#### saveToFile.py

This module contains functions for saving the generated usernames to a file. It ensures that the file operations are handled smoothly.

[View saveToFile.py](https://github.com/ohusq/Username-Gen/blob/master/modules/saveToFile.py)

#### folderChecks.py

This module checks for the existence of necessary folders and creates them if they do not exist. It helps in maintaining the required directory structure.

[View folderChecks.py](https://github.com/ohusq/Username-Gen/blob/master/modules/folderChecks.py)

## Contributing

Contributions are welcome! If you have ideas for improvements or have found bugs, please open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the Unlicense License

## Acknowledgements

Thanks to everyone who has contributed to this project. Your help and feedback are greatly appreciated!

---

For any questions or further information, feel free to contact the project maintainers through the GitHub issues page.

Happy username generating!

---

[GitHub Repository](https://github.com/ohusq/Username-Gen)
