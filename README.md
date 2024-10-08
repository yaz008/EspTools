![logo](assets/esptools-logo.png)

# EspTools

EspTools is an extensive toolset for [Espanso](https://espanso.org/)

## Prerequisites

-   [Espanso](https://espanso.org/): Version 2.2.1
-   [Python](https://www.python.org/): Version 3.12

## Installation

1. Clone the repository

```sh
git clone https://github.com/yaz008/EspTools.git
```

2. Create Python 3.12 virtualenv named `.venv`, activate it and run

```sh
pip install -r requirements.txt
```

3. Navigate to the Espanso `match` directory and copy `esptools` folder there

4. In `esptools/global.yml` file change `path-to-esptools-folder` to an actual path of the EspTools folder

**For example:** `C:\Users\Example\Desktop\EspTools`

### Check Installation

Open any text editor and type `:esptools`, it should be replaced with `Hello, EspTools!`

**Note:** Espanso must be enabled in the text editor you type in

## License

EspTools is a free, open-source software distributed under the [MIT License](LICENSE.txt)
