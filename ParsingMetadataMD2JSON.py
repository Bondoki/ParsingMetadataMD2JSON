#!/usr/bin/env python
# coding: utf-8

from pathlib import Path
import re
import json
import sys

"""
Usage:
    ./ParsingMetadataMD2JSON [options] <input file>...
Options:
    --help            Show this screen.
"""

def main() -> int:
    # Reads in a MarkDown M_datafile.md parsing every section
    # into a separate JSON M_datafile.json file

    # Get command line arguments for file
    args = sys.argv[1:]
    
    # Get the file to convert
    try:
        md_path = Path(args[0])
        if not md_path.exists():
            raise FileNotFoundError(f"{md_path} does not exist.")
    except IndexError:
        print("Usage:")
        print("./ParsingMetadataMD2JSON [options] <input file>...")
        print("Options:")
        print("--help            Show this screen.")
        print()
        #raise IndexError(f"Expected file name as first argument")
        print(f"Expected file name as first argument...EXITING...")
        sys.exit(1) # something went wrong
    
    with open(str(md_path), "r", encoding="utf-8") as f:
        contents = f.read()#.replace("\r", "") # Remove Windows style line breaks

    parsed_data = get_headings(contents)
    
    dictionaryJSON = getJSON(parsed_data)
    
    # Replace file extension from .md to .json and dump .json
    with open(Path(args[0][:-len(".md")] + ".json"), 'w', encoding='utf-8') as f:
        json.dump(dictionaryJSON, f, ensure_ascii=False, indent=4)
    
    print("SUCCESS: " + str(Path(args[0]))+" parsed to " + str(Path(args[0][:-len(".md")] + ".json")) )

    return 0 # success


def get_headings(content):
    # this fct split the input file in sections divided by empty lines
    # using regular expression with heading pound # in markdown
    pattern = r'(?:^|\t)*#+\s*([^#]+)\s*\r?'
    matches = re.findall(pattern, content)
    
    heading_values = []
    for match in matches:
        heading, value = match.split('\n', maxsplit=1)
        heading_values.append({heading: value})
        
    return heading_values


def getJSON(contentdictionary):
    # this fct converts the list to the appropriate JSON style
    # change, amend, or replace to your needs

    # Initialize variables to store the JSON data
    M_title = {}
    M_creators = [] # can be a list
    M_publisher = {}
    M_contributors = [] # can be a list
    M_description = {}
    M_subjects = [] # a list of keywords
    M_date = {}
    M_language = [] # a list of languages
    M_formats = [] # a list of file formats
    M_type = {}
    M_coverage = {}
    M_identifier = {}
    M_methods = []
    M_sources = []
    M_relations = []
    M_rights = []
    
    
    for index, entry in enumerate(contentdictionary):
            for heading, value in entry.items():
                # parse every heading
                if heading == "Title":
                    M_title["Title"] = value.strip()
                
                elif heading == "Creator":
                    name = value
                    creator = {}
                    creator["Name"] = name.strip()
                    M_creators.append(creator)
                
                elif heading == "Creator.ORCID":
                    creator = M_creators[-1]
                    creator["ORCID"] = value.strip()
                    
                elif heading == "Creator.Email":
                    creator = M_creators[-1]
                    creator["Email"] = value.strip()
                
                elif heading == "Publisher":
                    M_publisher["Name"] = "<p>" + value.strip().replace("  \n", "<br>") + "</p>"
                
                elif heading == "Contributor":
                    name = value
                    contributor = {}
                    contributor["Name"] = name.strip()
                    M_contributors.append(contributor)
                
                elif heading == "Contributor.ORCID":
                    contributor = M_contributors[-1]
                    contributor["ORCID"] = value.strip()
                
                elif heading == "Contributor.Email":
                    contributor = M_contributors[-1]
                    contributor["Email"] = value.strip()
                
                elif heading == "Description":
                    M_description["text"] = "<p>" + value.strip().replace("  \n", "<br>") + "</p>"
                
                elif heading == "Subject":
                    text = value
                    delimiters = ['*','']
                    words = [word.strip() for word in value.strip().split('*')]
                    result = [word for word in words if word not in ['*','']]
                    M_subjects.append(result)
                
                if heading == "Date":
                    M_date["Date"] = value.strip()
                    
                if heading == "Language":
                    text = value
                    delimiters = [';','']
                    words = [word.strip() for word in value.strip().split(';')]
                    result = [word for word in words if word not in [';','']]
                    M_language.append(result)
                
                if heading == "Format":
                    text = value
                    delimiters = ['*','']
                    words = [word.strip() for word in value.strip().split('*')]
                    result = [word for word in words if word not in ['*','']]
                    M_formats.append(result)
                
                if heading == "Type":
                    M_type["Type"] = value.strip()
                
                if heading == "Coverage":
                    M_coverage["Coverage"] = value.strip()
                
                if heading == "Identifier":
                    M_identifier["Identifier"] = value.strip()
                
                if heading == "Method":
                    text = value
                    lines = [word.strip() for word in text.strip().split('\n')]
                    for line in lines:
                        tokens = [word.strip() for word in line.strip().split()]
                        method = {}
                        method["identifier_source"]=tokens[0]
                        method["relation_type"]=tokens[1]
                        method["identifier_destination"]=tokens[2]
                        M_methods.append(method)
                
                if heading == "Source":
                    text = value
                    lines = [word.strip() for word in text.strip().split('\n')]
                    for line in lines:
                        tokens = [word.strip() for word in line.strip().split()]
                        source = {}
                        source["identifier_source"]=tokens[0]
                        source["relation_type"]=tokens[1]
                        source["identifier_destination"]=tokens[2]
                        M_sources.append(source)
                
                if heading == "Relation":
                    text = value
                    lines = [word.strip() for word in text.strip().split('\n')]
                    for line in lines:
                        tokens = [word.strip() for word in line.strip().split()]
                        relation = {}
                        relation["identifier_source"]=tokens[0]
                        relation["relation_type"]=tokens[1]
                        relation["identifier_destination"]=tokens[2]
                        M_relations.append(relation)
                        
                if heading == "Rights":
                    text = value
                    lines = [word.strip() for word in text.strip().split('\n')]
                    for line in lines:
                        tokens = [word.strip() for word in line.strip().split()]
                        right = {}
                        right["identifier_source"]=tokens[0]
                        right["relation_type"]=tokens[1]
                        right["identifier_destination"]=tokens[2]
                        M_rights.append(right)

    
    # Return the resulting JSON object
    json_object = { "metadata":
                   {
                    "title": M_title["Title"],
                    "creators": M_creators,
                    "publisher": M_publisher["Name"],
                    "contributor": M_contributors,
                    "description": M_description["text"],
                    "subject": M_subjects,
                    "date": M_date["Date"],
                    "language": M_language,
                    "format": M_formats,
                    "type": M_type["Type"],
                    "coverage": M_coverage["Coverage"],
                    "identifier": M_identifier["Identifier"],
                    "method": M_methods,
                    "source": M_sources,
                    "relation": M_relations,
                    "rights": M_rights,
                    }
    }
    
    #print(json.dumps(json_object))
    return json_object


if __name__ == "__main__":
    sys.exit(main())



