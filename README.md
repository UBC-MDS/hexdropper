# hexdropper

A Python package designed for graphic designers, developers, and color enthusiasts. It simplifies the process of obtaining hex color codes from images. Given a cropped image, hexdropper quickly identifies and outputs the corresponding hex color code, streamlining design and development workflows.

## Features
The key functionalities include:

- `read_image`: This function reads image files, and converts the image into a numpy array of RGB values.

- `most_common_rgb`: This function identifies the most common RGB value within the given image. 

- `rgb_to_hex`: This function converts RGB values into their corresponding hex color codes. 

- `create_color_image`: This function generates an image displaying the hex code on a background of the color it represents. 

## Installation

```bash
$ pip install hexdropper
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

