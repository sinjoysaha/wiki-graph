# Wikipedia Graph Visualization using NetworkX

[![GitHub contributors](https://img.shields.io/github/contributors/sinjoysaha/wiki-graph.svg)](https://GitHub.com/sinjoysaha/wiki-graph/graphs/contributors/)
[![GitHub forks](https://img.shields.io/github/forks/sinjoysaha/[project_name].svg)](https://GitHub.com/sinjoysaha/wiki-graph/network/)
[![GitHub stars](https://img.shields.io/github/stars/sinjoysaha/wiki-graph.svg)](https://GitHub.com/sinjoysaha/wiki-graph/stargazers/)
[![GitHub watchers](https://img.shields.io/github/watchers/sinjoysaha/wiki-graph.svg)](https://GitHub.com/sinjoysaha/wiki-graph/watchers/)
[![GitHub issues](https://img.shields.io/github/issues/sinjoysaha/wiki-graph.svg)](https://GitHub.com/sinjoysaha/wiki-graph/issues/)
[![Profile views](https://gpvc.arturio.dev/sinjoysaha)](https://GitHub.com/sinjoysaha/)
[![GitHub followers](https://img.shields.io/github/followers/sinjoysaha.svg)](https://github.com/sinjoysaha?tab=followers)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&color=545454)](https://linkedin.com/in/sinjoysaha)
[![Twitter](https://img.shields.io/badge/-Twitter-blue.svg?style=flat-square&logo=twitter&color=b3e0ff)](https://twitter.com/SinjoySaha)

## Table of Contents

* [About the Project](#about-the-project)
  * [Tasks](#tasks)
  * [To Do](#to-do)
  * [Built With](#built-with)
* [Fork the Repo and Contribute](#Fork-the-Repo-and-Contribute)
* [Contact](#contact)

## About the Project

In this project, we explore [NetworkX](https://networkx.org/), a Python library for graph algorithms and visualizations. We scrape Wikipedia pages for any arbitrary search word and get the first web link referred by the wiki page. Then, we visit that page and again get the first link. We recursively keep visiting the web links and store them in a graph. If the link is already visited, we stop. The data is stored using Pickle library in Python.

[![Project Image](docs/images/wiki-graph-projectimage.png)](https://github.com/sinjoysaha/wiki-graph)

### Tasks

1. Webscaping using requests and Beautiful Soup.
2. Cleaning links to get words to be used as graph nodes.
2. Build graph with nodes obtained using NetworkX.

### To Do

1. Recursively visit and store all links from first non-empty \<p> tag in each wiki page.
   Try - 
   * Breadth First Search (BFS)
   * Depth First Search (DFS)

### Built With

* NetworkX
* Beautiful Soup
* Requests
* Pickle
* Jupyter Notebook

## Fork the Repo and Contribute

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project (click on `Fork` in the top-left corner)
2. Create your Feature Branch (`git checkout -b feature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature`)
5. Open a Pull Request

## Contact

Sinjoy Saha 
  * [LinkedIn](https://linkedin.com/in/sinjoysaha)
  * [Twitter](https://twitter.com/SinjoySaha)

