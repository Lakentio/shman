# ShMan - Shell Script Manager

ShMan is a shell script manager that allows you to create, edit, version, and execute scripts with ease.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Lakentio/shman.git
   cd shman
   ```

2. Install the package:
   ```bash
   pip install .
   ```

## Usage

### Initialize the environment
```bash
shman init
```

### Create a new script
```bash
shman new <script_name> --category <category> --tags <tag1> <tag2>
```

### Edit a script
```bash
shman edit <script_name>
```

### List script versions
```bash
shman versions <script_name>
```

### Restore a previous version
```bash
shman restore <script_name> <version_index>
```

### Save a new version
```bash
shman commit <script_name> <version> "<message>"
```

### Execute a script
```bash
shman run <script_name>
```

### List execution logs
```bash
shman log <script_name>
```

### View a specific log
```bash
shman view-log <script_name> <log_number>
```

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT license.
