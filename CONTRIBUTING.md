## Contribution guidelines

This document contains guidelines for contributing to Gazebo's [documentation index](https://osrf.github.io/gz-bigindex/). 

### About

The documentation index intends to brings together all of Gazebo's learning resources in one place. This will help beginners as well as professionals in finding the best sources of information by just a browser quicksearch.

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

Contributions can be made by updating the index items, their descriptions, categories or subcategories, using pull requests.

The items of documentation index has been divided into categories and sub-categories.

Changes can be suggested to files in the ```_categories``` directory. This is where the index items are stored in markdown files with yml-based frontmatter. Each file in this directory represents a category and contains information about sub-categories and corresponding items.

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

Each category file has the following variables -

```title```: Title of category

```desc```: Description of category

```subcategories```: Array of subcategories

---

Each subcategory can be defined using -

```title```: Title of subcategory

```items```: Array of index items corresponding to the subcategory.

---

Each item can be defined using -

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

Rendering of the above category data can be seen [here](https://osrf.github.io/gz-bigindex/categories/models_import.html).

