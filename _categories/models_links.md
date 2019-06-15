---
# Contribution guidelines:
# https://github.com/osrf/gz-bigindex/blob/master/CONTRIBUTING.md 

title: "Models: Create static objects in Gazebo (links)"
desc: "How to create or define static objects in the Gazebo simulator using different approaches (GUI, code, ...) and tools."
subcategories: 
  - title: "Modelling concepts"
    items: 
      - title: 'Basic shapes in Gazebo simulator'
        url: 'http://gazebosim.org/tutorials?tut=build_world&cat=build_world#AddingSimpleShapes'
        desc: 'Atomic native objects in Gazebo for composing the different robot parts'
        star: true

  - title: "Creating models from code"
    items: 
      - title: 'SDFormat: Marked language to define models'
        url: 'http://gazebosim.org/tutorials?tut=build_model&cat=build_robot'
        desc: 'Description of the SDFormat marked language used to define objects and robots in Gazebo.'
        star: true
        
      - title: 'SDFormat: Link language specification'
        url: 'http://sdformat.org/spec?ver=1.6&elem=link'
        desc: 'Link to the official sdformat language specification for static parts (links)'
        star: false

      - title: 'SDFormat: API'
        url: 'http://sdformat.org/api'
        desc: 'Link to the official sdformat API'
        star: false
        
      # - title: 'Generating multiple identical objects'
      #   url: 'http://sdformat.org/api' # check
      #   desc: 'How you can create a population of models by using the SDF'
      #   star: false
  
  - title: "Gazebo graphical tools for creating models"
    items: 
      - title: 'The Gazebo Model Editor'
        url: 'http://gazebosim.org/tutorials?tut=model_editor'
        desc: 'Integrated GUI in Gazebo for creating models'
        star: true

      # - title: 'The Gazebo Building Editor'
      #   url: 'http://packages.osrfoundation.org/gz_big_index/1_static.html'
      #   desc: 'Integrated GUI in Gazebo for creating walls and buildings' # check
      #   star: true

      - title: 'The Gazebo SVG struding tool'
        url: 'http://gazebosim.org/tutorials?tut=extrude_svg'
        desc: 'Generate Gazebo objects from struding SVG forms'
        star: true
        
---
