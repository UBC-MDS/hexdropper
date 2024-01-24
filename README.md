# hexdropper

A Python package designed for graphic designers, developers, and color enthusiasts. It simplifies the process of obtaining hex color codes from images. Given a cropped image, hexdropper quickly identifies and outputs the corresponding hex color code, streamlining design and development workflows.

## Contributors

- [Julia Everitt](https://github.com/juliaeveritt)
- [Hancheng Qin](https://github.com/hchqin)
- [Joey Wu](https://github.com/joeywwwu)
- [Mona Zhu](https://github.com/monazhu)

## Features
The key functionalities include:

- `read_image`: This function reads image files, and converts the image into a numpy array of RGB values.

- `most_common_rgb`: This function identifies the most common RGB value within the given image. 

- `rgb_to_hex`: This function converts RGB values into their corresponding hex color codes. 

- `create_color_image`: This function generates an image displaying the hex code on a background of the color it represents. 

## Installation

The current package is still under development. We have provided below a set of developer installation instructions.

### Developer Installation

#### Getting Started

Clone a copy of [this repository](https://github.com/UBC-MDS/hexdropper) onto your local machine. See [this page](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) for details on how to clone a repository.

#### Setting up a Conda Environment

We recommend creating an isolated conda environment on your local machine to test and develop the package. To create a conda environment for this project, type in the below command in your terminal, replacing `[your_env_name]` with your desired environment name (e.g., hexdropper)

```
$ conda create --name [your_env_name] python=3.9 -y
```

#### Using Poetry for Package Management

Please follow the official poetry [documentation](https://python-poetry.org/docs/) to install poetry on your local machine. Note that poetry should **always be installed on a dedicated virtual environment.**

Navigate to the root directory of your project folder. Ensure that your virtual conda environment has been activated. Run the following line of code to install existing packages required for the `hexdropper` package:

```
$ poetry install
```

If you would like to add a new package or dependency, run the following code in your terminal, replacing `[name-of-dependency]` with the package you would like to install (e.g., numpy)

```
$ poetry add [name-of-dependency]
```

You can also pin the specific version of the package you would like to install like so: 

```
$ poetry add numpy=1.22.0 --dry-run
```

#### Running Tests

Ensure `pytest` and `pytest-cov` are installed via poetry. If not, run the following in your terminal: 

```
$ poetry add --group dev pytest
```
```
$ poetry add --group dev pytest-cov
```

Ensuring that your test scripts are completed, then run the following code in your terminal to run the tests for all functions in the package: 

```
$ pytest tests/
```

To run coverage tests, run the following command:

```
$ pytest tests/ --cov=pycounts
```


## Usage

- TODO

## Python Ecosystem Context
hexdropper fills a unique niche in the Python ecosystem. While there are packages like Pillow for image processing and Matplotlib for visualization, hexdropper specifically focuses on color extraction and conversion, a task not directly addressed by existing packages. Its ability to directly translate image colors into hex codes and visually represent them is distinctive, setting it apart from general-purpose image manipulation tools. Related packages include:

- [Pillow](https://python-pillow.org/): For comprehensive image processing capabilities.
- [Matplotlib](https://matplotlib.org/): For creating visualizations and figures.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`hexdropper` was created by Julia Everitt, Hancheng Qin, Joey Wu, Mona Zhu. It is licensed under the terms of the MIT license.

## Credits

`hexdropper` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

