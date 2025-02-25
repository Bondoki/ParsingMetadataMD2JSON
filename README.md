# ParsingMetadataMD2JSON
Simplistic parser to convert Markdown metadata file for a given [M_README.md](https://doi.org/10.5281/zenodo.14848834) with identifiers similar to [DublinCore terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) to a simplistic JSON file for further processing. The JSON file is inspired by the [ZENODO.json schema](https://github.com/zenodo/zenodo/blob/master/zenodo/modules/deposit/jsonschemas/deposits/records/legacyrecord.json), see also [ZENODO developers guide](https://developers.zenodo.org/#representation). Metadata information (data on data) are crucial to find and understand your data in your project tree and these JSON files can be used for further data processing, e.g. to create a database catalog for your files or to provide additional metadata in public repository. Feel free to adapt it to your needs.

## Getting Started

Follow these instructions to run the application `ParsingMetadataMD2JSON` with `Python`.

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
* alternatively, run and use the Jupyter notebook `ParsingMetadataMD2JSON.ipynb` with
    ``` bash
    jupyter-lab ParsingMetadataMD2JSON.ipynb
    ```

## Metadata fields

The following keywords will be parsed and converted:

| Keyword                                                                                                                      | Description                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Title](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/title)             | Descriptive name the Paper/Project/Thesis/Dataset                                                                                                                                                                                       |
| [Creator](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/creator)         | A consecutive list of names, who created the resource and is primarily responsible.                                                                                                                                                     |
| [Creator.ORCID](https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier)                  | Additional information: The ORCID identifier of the Creator.                                                                                                                                                                            |
| [Creator.Email](https://schema.org/email)                                                                                    | Additional information: The email identifier of the Creator.                                                                                                                                                                            |
| [Publisher](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/publisher)     | The department/institute responsible for making the resource available.                                                                                                                                                                 |
| [Contributor](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/contributor) | A consecutive list of names, contributed to the resource and is secondary to Creators.                                                                                                                                                  |
| [Contributor.ORCID](https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier)              | Additional information: The ORCID identifier of the Contributor.                                                                                                                                                                        |
| [Contributor.Email](https://schema.org/email)                                                                                | Additional information: The email identifier of the Contributor.                                                                                                                                                                        |
| [Description](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/description) | A textual description of the content of the resource.                                                                                                                                                                                   |
| [Subject](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/subject)         | Phrase\Keywords describing the content of the resource.                                                                                                                                                                                 |
| [Date](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/date)               | A date associated with the creation or availability of the resource. Recommended format: YYYY-MM-DD.                                                                                                                                    |
| [Language](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/language)       | The language of the resource recommended as [BCP 47 language tag](https://doi.org/10.17487/RFC5646).                                                                                                                                    |
| [Format](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/format)           | The data format to identify the software and possibly hardware that might be needed to display or operate the resource. For a list of MIME types see [here](https://www.iana.org/assignments/media-types/media-types.xhtml).            |
| [Type](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/type)               | The category of the resource e.g. Collection, Dataset, Event, Image, Experiment, Simulation, Report, Text, Draft, Image. See also [DCMI Type Vocabulary](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7/). |
| [Coverage](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/coverage)       | Temporal coverage is typically a period for acquiring the data.                                                                                                                                                                         |
| [Source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/source)           | Information about a second resource from which the present resource is derived - if applicable.                                                                                                                                         |
| [Relation](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/relation)       | Provide a relationship from source to the present resource, e.g. IsVersionOf, IsReplacedBy, IsPartOf, IsReferencedBy, see [Qualified Dublin Core Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/).             |
| [Identifier](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/identifier)   | An unique identifier of the resource, e.g. DOI, ISBN, Number                                                                                                                                                                            |
| [Method](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/terms/MethodOfAccrual)         | Refer to your (post-)processing tools/methods, e.g. URL or git hash, as relation.                                                                                                                                                       |
| [Rights](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/elements/1.1/rights)           | A rights management statement of the resource, e.g. license for publishing and sharing.                                                                                                                                                 |


## Authors

  - [Ron Dockhorn](https://github.com/Bondoki) (<a href="https://orcid.org/0000-0002-5268-5430"><img alt="ORCID logo" src="https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png" width="16" height="16" /> 0000-0002-5268-5430</a>)


## License

This project is licensed under the [Unlicense](LICENSE).
