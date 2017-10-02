# Indefinite search

Searches for words in text that may contain typos.

## System requirements

* Operating system with Python 3 language support.
* Python 3 interpreter.

#### Prerequisites

Python 3 interpreter can be obtained in [python language official site](http://python.org).

## How to execute

Open your operating system command shell:
* in Windows it can be
    * Windows PowerShell 
    * Command Prompt
    * Bash terminal (if installed)
* in MacOs and Linux it can be
    * Bash terminal
    
#### Full syntax

```
py indefinite_search [-h] [-a | -r] [-n] [-t [text] | -tf [path]]
                     [-w [words] | -wf [path]] [-i] [-b] [-m | -l n]

```

#### Example

```
py indefinite_search -tf "text.txt" -w word list -i
```

#### To get help

```
py indefinite_search --help
```

## How to run tests

Simply type

```
py indefinite_search/tests
```

To get specific information, type

```
py indefinite_search/tests --verbose
```