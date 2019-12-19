# Gazebo Documentation Index

This repository contains code for Gazebo's documentation index.
The documentation index can be accessed at https://osrf.github.io/gazebo-doc-index/.

Status: Alpha version released

More information about the project can be found in the design specification document [`design_spec.md`](https://github.com/osrf/gazebo-doc-index/blob/master/design_spec.md).

## Getting started

#### Prerequisites
- [Jekyll](https://jekyllrb.com)

#### Setup
```
git clone https://github.com/osrf/gazebo-doc-index.git
cd gazebo-doc-index
bundle exec jekyll serve
```

### _categories

This folder is where information about all the categories is stored. Each file represents a category and contains information about sub-categories and items.

### _layout

This folder stores the HTML layouts of the home page and the category page along with a wrapper layout that is the parent layout which includes the navbar and footer components.

### _includes

This folder contains HTML code for the navbar and the footer.

## Contribution guidelines

Refer to [CONTRIBUTING.md](https://github.com/osrf/gazebo-doc-index/blob/master/CONTRIBUTING.md) for information about how to contribute to the project.

