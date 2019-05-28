# Gazebo Documentation Index

This repository contains code for Gazebo's documentation index.

Status: Under development

### Getting started

#### Prerequisites
- [Jekyll](https://jekyllrb.com)

```
git clone https://github.com/osrf/gz-bigindex.git
cd gz-bigindex
bundle exec jekyll serve
```

### Structure

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
├── .gitignore
├── README.md
├── _config.yml
├── Gemfile
├── 404.html
├── index.html
└── style.css
```

### _categories

This folder is where information about all the categories is stored. Each file represents a category and contains information about sub-categories and items.

### _layout

This folder stores the HTML layouts of the home page and the category page along with a wrapper layout that is the parent layout which includes the navbar and footer components.

### _includes

This folder contains HTML code for the navbar and the footer.
