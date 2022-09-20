<h1 align="center">
  CSC510_G46_lua2py
</h1>

<!--Badges-->
<p align="center">
<a href="https://zenodo.org/badge/latestdoi/533000112">
<img src="https://zenodo.org/badge/533000112.svg" alt="DOI"></a>
</a>
<a href="https://travis-ci.org/gargpriyam21">
<img src="https://travis-ci.org/gargpriyam21/CSC510_G46_lua2py.svg?master" />
</a>
<a href="https://codecov.io/gh/gargpriyam21/CSC510_G46_lua2py" > 
<img src="https://codecov.io/gh/gargpriyam21/CSC510_G46_lua2py/branch/main/graph/badge.svg?token=5PLVQBFU2L" /> 
</a>
</p>

<p align="center">
<a href="https://github.com/gargpriyam21/CSC510_G46_lua2py/blob/main/LICENSE.md" target="blank">
<img src="https://img.shields.io/github/license/gargpriyam21/CSC510_G46_lua2py?style=for-the-badge" alt="CSC510_G46_lua2py license" />
</a>
<a href="https://github.com/gargpriyam21/CSC510_G46_lua2py/fork" target="blank">
<img src="https://img.shields.io/github/forks/gargpriyam21/CSC510_G46_lua2py?style=for-the-badge" alt="CSC510_G46_lua2py forks"/>
</a>
<a href="https://github.com/gargpriyam21/CSC510_G46_lua2py/stargazers" target="blank">
<img src="https://img.shields.io/github/stars/gargpriyam21/CSC510_G46_lua2py?style=for-the-badge" alt="CSC510_G46_lua2py stars"/>
</a>
<a href="https://github.com/gargpriyam21/CSC510_G46_lua2py/issues" target="blank">
<img src="https://img.shields.io/github/issues/gargpriyam21/CSC510_G46_lua2py?style=for-the-badge" alt="CSC510_G46_lua2py issues"/>
</a>
<a href="https://github.com/gargpriyam21/CSC510_G46_lua2py/pulls" target="blank">
<img src="https://img.shields.io/github/issues-pr/gargpriyam21/CSC510_G46_lua2py?style=for-the-badge" alt="CSC510_G46_lua2py pull-requests"/>
</a>
<a href="https://github.com/gargpriyam21/CSC510_G46_lua2py/graphs/contributors" alt="CSC510_G46_lua2py Contributors">
<img src="https://img.shields.io/github/contributors/gargpriyam21/CSC510_G46_lua2py?style=for-the-badge" /></a>
</a>
<a href="https://github.com/gargpriyam21/CSC510_G46_lua2py/graphs/commit-activity" alt="CSC510_G46_lua2py commit activity">
<img src="https://img.shields.io/github/commit-activity/w/gargpriyam21/CSC510_G46_lua2py?style=for-the-badge" /></a> 
</a>
<a href="https://img.shields.io/github/repo-size/gargpriyam21/CSC510_G46_lua2py" alt="CSC510_G46_lua2py repo size">
<img src="https://img.shields.io/github/repo-size/gargpriyam21/CSC510_G46_lua2py?style=for-the-badge" /></a>
</a>
<a href="https://img.shields.io/tokei/lines/github/gargpriyam21/CSC510_G46_lua2py" alt="CSC510_G46_lua2py total lines">
<img src="https://img.shields.io/tokei/lines/github/gargpriyam21/CSC510_G46_lua2py?style=for-the-badge" /></a> 
</a>
</p>

<p align="center">
    <a href="https://github.com/gargpriyam21/CSC510_G46_lua2py/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/gargpriyam21/CSC510_G46_lua2py/issues/new/choose">Request Feature</a>
</p>

## Table of Contents
- [Introduction](#Introduction)
- [Execution Steps](#ExecutionSteps)
- [License](#License)
- [Contributing](#Contributing)
- [Team Members](#TeamMember)

## 📖 Introduction <a name="Introduction"></a>

The project here is the conversion of the source code provided at the [link](https://github.com/txt/se22/blob/main/etc/pdf/csv.pdf) from lua to python.

### Environment

- Python 3.7.13

### Documentation

For the complete documentation of the prject please refer to the [gargpriyam21.github.io/CSC510_G46_lua2py/](https://gargpriyam21.github.io/CSC510_G46_lua2py/)

### Tasks Description:
Homework| Task|
|:------:|:------|
|HW2     | Add the `Num` and `Sym` class and the tests cases `the`, `sym`, `num`, `bignum`.|
|HW3     | Add the `Cols`, `Row`, `Data` class and the test cases `eg.csv, eg.data, eg.stats`.|
|HW4     |  Add all the bling from HW1. Also, add post-commit hooks to auto run all the test cases, the code coverage checks (if your language supports then), and the documentation generators.|

## ⚙️ Execution Steps <a name="ExecutionSteps"></a>

To run the following source code, make sure you have the `auto93.csv` in the data folder.

For installing the additional requirements, execute the following command

``` pip install -r requirements.txt ```

Execute the following command:

``` python csv.py -e ALL```

### Command Line Arguments:

`-e` for running the specific test case "For example to run all test case `-e task` (and `-e ALL`) runs all tests.

`-d` for in case of test failure, exit with stack dump  

`-f` provide the file name in case the data is to be read from some other file

`-h` show the help document for the current code

`-n` upudate the nums to the specific number you provided

`-s` specify the specific seed you want

`-S` feild separator (default ',')

## 📝 License <a name="License"></a>

This project is licensed under the terms of the MIT license. Please check [License](https://github.com/divyang02/CSC510_SE_G46/blob/main/LICENSE) for more details.

## 🍰 Contributing <a name="Contributing"></a>
Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/divyang02/CSC510_SE_G46/compare).

Please read [`CONTRIBUTING`](CONTRIBUTING.md) for details on our [`CODE OF CONDUCT`](CODE_OF_CONDUCT.md), and the process for submitting pull requests to us.

## 👥 Contributors <a name="Contributors"></a>

### Group 46

<table>
  <tr>
    <td align="center"><a href="https://github.com/divyang02"><img src="https://avatars.githubusercontent.com/u/23277855?v=4" width="75px;" alt=""/><br /><sub><b>Divyang Doshi</b></sub></a></td>
    <td align="center"><a href="https://github.com/gargpriyam21"><img src="https://avatars.githubusercontent.com/u/32238511?v=4" width="75px;" alt=""/><br /><sub><b>Priyam Garg</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/bhansaliyash"><img src="https://avatars.githubusercontent.com/u/21220880?v=4" width="75px;" alt=""/><br /><sub><b>Yash Bhansali</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/devmehta1999"><img src="https://avatars.githubusercontent.com/u/48157574?v=4" width="75px;" alt=""/><br /><sub><b>Dev Mehta</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/manognapc"><img src="https://avatars.githubusercontent.com/u/112452957?v=4" width="75px;" alt=""/><br /><sub><b>Manogna Choudary Potluri</b></sub></a><br /></td>
  </tr>
</table>
