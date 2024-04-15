# mbpstester

mbpstester is a command-line tool for measuring the download and upload speeds of your internet connection. It performs multiple measurements and provides an average speed along with a connection quality assessment. The tool also offers options to display network information and save the results in JSON format.

## Features

- Measures download and upload speeds
- Calculates average speeds from multiple measurements
- Displays speeds in appropriate units (bps, Kbps, Mbps)
- Assesses connection quality based on the measured speeds
- Provides a simple and intuitive command-line interface
- Supports logging of speed test results
- Allows skipping download or upload tests individually
- Displays network information (hostname, global IP, provider)
- Outputs results in JSON format to a specified file
- Cross-platform compatibility (Windows, macOS, Linux)

## Requirements

- Python 3.x
- `colorama`
- `requests`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/flowernotfound/mbpstester
```

2. Navigate to the project directory:

```bash
cd mbpstester
```

3. Create a virtual environment (optional but recommended):

```bash
python3 -m venv env
source env/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the Speed Test CLI, use the following command:

```bash
python mbpstester.py [options]
```

Available options:

- `--log`: Enable logging of speed test results
- `--log-file LOG_FILE`: Specify the path to the log file (default: mbpstester.log)
- `--version`, `-v`: Show the version of the program and exit
- `--no-download`: Skip the download test and only perform the upload test
- `--no-upload`: Skip the upload test and only perform the download test
- `--network-info`: Display network information
- `--json JSON_FILE`: Output the results in JSON format to the specified file

Examples:

1. Run speed test with default settings:

```bash
python mbpstester.py
```

2. Run speed test with logging enabled:

```bash
python mbpstester.py --log
```

3. Run speed test without the download test:

```bash
python mbpstester.py --no-download
```

4. Run speed test and save the results in JSON format:

```bash
python mbpstester.py --json results.json
```

5. Run speed test, display network information, and save the results in JSON format:

```bash
python mbpstester.py --network-info --json results.json
```

## Configuration

The following constants in the `config.py` file can be adjusted according to your requirements:

- `DOWNLOAD_URL`: The URL of the dummy data file used for download speed measurement.
- `UPLOAD_URL`: The URL of the server endpoint for uploading dummy data.
- `SIZE`: The size of the dummy data in bytes. Default is 1 MB.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
