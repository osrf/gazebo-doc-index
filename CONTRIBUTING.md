## Contribution guidelines

This document contains guidelines for contributing to Gazebo's [documentation
index](https://osrf.github.io/gazebo-doc-index/).

### Table of contents

- [About](https://github.com/osrf/gazebo-doc-index/blob/master/CONTRIBUTING.md#about)
- [Repository structure](https://github.com/osrf/gazebo-doc-index/blob/master/CONTRIBUTING.md#repository-structure)
- [How to contribute](https://github.com/osrf/gazebo-doc-index/blob/master/CONTRIBUTING.md#how-to-contribute)
  - [Index structure](https://github.com/osrf/gazebo-doc-index/blob/master/CONTRIBUTING.md#index-structure)
  - [Preview changes](https://github.com/osrf/gazebo-doc-index/blob/master/CONTRIBUTING.md#preview-changes)
  - [Test the changes](https://github.com/osrf/gazebo-doc-index/blob/master/CONTRIBUTING.md#test-the-changes)

### About

The documentation index intends to brings together all of Gazebo's learning
resources in one place, in an organised fashion. This will help beginners as
well as professionals in finding the best sources of information by just a 
browser quicksearch.

### Repository structure

```
.
├── _includes
├── _layouts
│   ├── category.html
│   ├── home.html
│   └── wrapper.html
├── _categories
│   ├── installing_gazebo.md
│   ├── models_import.md
│   ├── models_joints.md
│   ├── models_links.md
│   └── sensors.md
├── assets
│   └── css
│       └── style.css
├── .gitignore
├── README.md
├── _config.yml
├── Gemfile
├── 404.html
└── index.html
```

### How to contribute

Contributions can be made by opening a pull request for updating the index
items, their descriptions, categories or subcategories. For contributions
or question related to the structure or other parts not related to the
content please use the github issue tracker.

The items of documentation index has been divided into categories and
sub-categories.

Changes can be suggested to files in the ```_categories``` directory. This is
where the index items are stored in markdown files with yml-based frontmatter.
Each file in this directory represents a category and contains information
about sub-categories and corresponding items.

#### Index structure

- category 1
    - subcategory 1
        - item 1
        - item 2

    - subcategory 2
        - item 1
        - item 2

- category 2
- category 3
---

Each **category** file has the following variables -

```title```: Title of category

```desc```: Description of category

```subcategories```: Array of subcategories

---

Each **subcategory** can be defined using -

```title```: Title of subcategory

```items```: Array of index items corresponding to the subcategory.

---

Each **index item** can be defined using -

```title```: Title of index item

```url```: URL of resource

```desc```: Description of index item

```star```: Whether it is an important resource

---

This is an example category file -

```_categories/models_import.md```
```
---
title: "Models: import your existing models"
desc: "How to import previously existing models created with Gazebo or other external tools (Solidworks, Google Sketchup etc)."
subcategories:
  - title: "Importing models in Gazebo"
    items:
      - title: 'Model database structure'
        url: 'http://gazebosim.org/tutorials?tut=model_structure&cat=build_robot'
        desc: 'The gazebo model database description.'
        star: true

      - title: 'Nested models in gazebo: using SDFormat'
        url: 'http://gazebosim.org/tutorials?tut=nested_model&cat=build_robot'
        desc: 'How to compose a model in sdformat composed by different models.'
        star: false

  - title: "Creating models from code"
    items:
      - title: 'Import SolidWorks models to Gazebo'
        url: 'http://blogs.solidworks.com/teacher/2014/05/solidworks-to-gazebo-robot-simulation.html'
        desc: 'How to import the SolidWorks models into the Gazebo simulator.'
        star: true

      - title: 'Generate URDF with SolidWorks'
        url: 'http://answers.gazebosim.org/question/3258/is-there-and-visualization-software-to-create-a-sdf-file-eg-can-we-create-a-sdf-file-from-a-cad-model-etc/'
        desc: 'Generate URDF (superset of SDFormat) and use it in Gazebo'
        star: false

  - title: "Importing models from Google SketchUp"
    items:
    - title: 'Importing Google 3D Warehouse model'
      url: 'http://projects.csail.mit.edu/pr2/wiki/index.php?title=Importing_a_Google_3D_Warehouse_Model_%28.skp%29_into_Gazebo'
      desc: 'Importing a .skp (Google warehouse format) into Gazebo'
      star: true
---
```

Rendering of the above category data can be seen [here](https://osrf.github.io/gazebo-doc-index/categories/models_import.html).

#### Preview changes

Before opening a pull request, proposed changes to the documentation index can
be previewed by serving the jekyll project on a local server.

```
cd gazebo-doc-index
jekyll serve
```

For instructions to set up the jekyll project on your machine, refer to the
repository's [README](https://github.com/osrf/gazebo-doc-index#getting-started).

####  Test the changes

Automated tests for validating index structure integrity and external links can be run locally by using the following commands - 

```bundle install``` (first time)
```bundle exec rspec --format doc``` (index integrity tests)
```jekyll build && htmlproofer ./_site --url-ignore "/gazebo-doc-index/*/"``` ([html-proofer](https://github.com/gjtorikian/html-proofer) tests)

Note: Pull requests can't be merged if they don't pass the automated tests.