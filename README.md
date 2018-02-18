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
                     [-w [words] | -wf [path]] [-i] [-b] [-s] [-e] [-m | -l n]

```

#### Examples

```
py indefinite_search -tf "text.txt" -w word list -i
py indefinite_search -iw word list < "text.txt" 
```

#### To get help

```
py indefinite_search --help
```

## How to run tests

Simply type

```
pytest indefinite_search
```
