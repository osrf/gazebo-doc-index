# Design Specification Document: Gazebo Documentation Index

## Table of contents
- [Introduction](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md#1-introduction)
- [Background](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md#2-background)
- [Purpose](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md#3-purpose)
- [Implementation](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md#4-implementation)
  - [Technology stack](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md#41-technology-stack)
  - [Index structure](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md#42-index-structure)
  - [Collaboration and Maintenance](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md#43-collaboration-and-maintenance)
  - [User interface](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md#44-user-interface)
  - [Repository structure](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md#45-repository-structure)
  - [Hosting](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md#46-hosting)
- [Progress](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md#5-progress)


## 1. Introduction

The Gazebo project has a vast set of learning resources in the form of a
documentation section, Gazebo tutorials, the Q&A website, ROS answers and other
blogs that developers can refer to for any assistance. All of this information
is distributed across the internet with some links joining each other. 

The aim of this project is to bring all the learning material under one webpage
in the form of a documentation index that contains links to the content where
the respective information is hosted. 

## 2. Background
At present, the learning resources for Gazebo are distributed over the internet - 
the official documentation, the Q&A website and ROS-Answers. Some noteworthy
help can also be found through examples and explanations in the comments of Bitbucket
issues and Gazebo’s API. There are also third-party sources that provide video
tutorials and blog posts that are helpful in learning Gazebo. It can be a bit
overwhelming to keep track of one’s learning when the content is distributed
as in this case.

A documentation index is a platform where links to relevant learning resources
for a software system are indexed to allow users to find any help at one place.

#### Some common documentation indexes by - 

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Index)
- [Intel](https://www.intel.com/content/www/us/en/programmable/documentation/lit-index.html)
- [Oracle](https://www.oracle.com/technetwork/indexes/documentation/index-100966.html)

## 3. Purpose

A documentation index is a neat way to accommodate links to all the relevant
learning content into one webpage. It is very convenient since almost any help
is just a page quicksearch away. The user can think of related keywords or
categories and then look through the index to find the relevant information.
Such a platform can act as a one-stop place to get all pertinent information about Gazebo.


1. Compilation of best learning resources from across the internet, including 
tutorials, third-party blog posts, Github issues' comments and the Gazebo answers website,

2. All relevant content under one roof.

## 4. Implementation

### 4.1 Technology stack:

[Jekyll](https://jekyllrb.com/): 
- Static site generation
- Easy maintenance and collaboration with yml-based data for index items
- Reusable HTML templates

[Travis CI](https://travis-ci.org/): 
- Index integrity tests
- Continuous integration

### 4.2 Index structure

The documentation index is two levels deep. The first level of abstraction is
the **category** level and the second level is the **subcategory** level.

```Category >> Subcategory >> Index entries```

- Each category comprises of subcategories and each subcategory comprises of 
the corresponding index items. 
- Each category and index item also contain a brief description of the same.
- More important index items can be shown starred.

This hierarchical classification, as shown below has complied well with the
requirements of the project.

```
- category 1
    - subcategory 1
        - item 1 
        - item 2

    - subcategory 2
        - item 1 
        - item 2

- category 2 
- category 3
```


#### All links page

To allow for the user to be able to find all relevant content on one webpage,
an 'All links' page has been added. This can help in finding any help using a
browser quicksearch.

### 4.3 Collaboration and maintenance
Index entries are being saved using yml-based files for easy open-source
maintenance and collaboration.

Contributions can be made by updating the index items, their descriptions,
categories or subcategories, using pull requests. 

For information about how to contribute to the project, contribution guidelines
can be referred to [here](https://github.com/osrf/gazebo-doc-index/blob/master/CONTRIBUTING.md).

### 4.4 User interface

A simple, clean and responsive user interface has been developed as can be seen
in the images below.

![Screenshot 2019-06-10 at 9 15 54 PM](https://user-images.githubusercontent.com/24846546/59219032-0e7c2500-8bb1-11e9-88e9-2de2ed3bf3c7.png)

![Screenshot 2019-06-10 at 9 17 13 PM](https://user-images.githubusercontent.com/24846546/59219041-1340d900-8bb1-11e9-8604-c0fb612f1a63.png)

### 4.5 Repository structure

```
.
├── _includes
├── _layouts
│   ├── all.html
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
└── index.html
```

```_layout/```

This folder stores the HTML layouts of the home page and the category page
along with a wrapper layout that is the parent layout which includes the navbar
and footer components.


```_categories```

This folder is where information about all the categories is stored. Each file
represents a category and contains information about sub-categories and items.

This is an example category file -

```_categories/models_import.md```
```
---
title: "Models: import your existing models"
desc: "How to import previously existing models created with Gazebo or other
external tools (Solidworks, Google Sketchup etc)."
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
---
```

### 4.6 Hosting

The website is being served using Github pages. It can be accessed [here](https://osrf.github.io/gazebo-doc-index/).


## 5. Progress

- [x]  Front-end HTML templates
- [x]  Population of documentation index with some basic categories, subcategories and items.
- [x]  'Suggest edits' button
- [x]  Contribution guidelines
- [x]  Travis support for index integrity
- [x]  A more comprehensive set of index entries
- [x]  Alpha version launch
- [x]  A tool for suggesting index entries from Bitbucket issues
- [ ]  Beta launch
