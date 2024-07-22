# ParsingMetadataMD2JSON
Simplistic parser to convert Markdown Metadata File for a given [M_README.md](https://zenodo.org/doi/10.5281/zenodo.10648863) with identifiers similar to [DublinCore terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)  
to a simplisitic JSON file for further processing.

## Getting Started

Follow these instructions to run the application `ParsingMetadataMD2JSON`.

### Prerequisites

Requirements for the software:
- [Python3](https://www.python.org/) and Python modules `sys`, `pathlib`, `re`, and `json`
- Optional: [Jupyter](https://jupyter.org/) for interactivity

### Installing

* clone the repository
    ```bash
    git clone https://github.com/Bondoki/ParsingMetadataMD2JSON
    ```

### RUNNING
* run the application with sample file `M_Dataset_README_Example.md`
    ``` bash
    python3 ParsingMetadataMD2JSON.py M_PhD_README_Example.md
    ```
* this should generate a new file `M_Dataset_README_Example.json` and promted with success:
    ``` bash
    SUCCESS: M_Dataset_README_Example.md parsed to M_Dataset_README_Example.json
    ```
* alternatively, run and use the Jupyter notebook `ParsingMetadataMD2JSON.jpynb` with
    ``` bash
    jupyter-lab ParsingMetadataMD2JSON.ipynb
    ```

## Authors

  - [Ron Dockhorn](https://github.com/Bondoki)


## License

This project is licensed under the [Unlicense](LICENSE.md).
