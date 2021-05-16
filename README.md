# Setup some tooling

## Required tooling
- VS Code
- nodejs and npm
- python == must be a `3.7+` -- `3.8+` doesn't seem to be directly supported in the VS code tooling yet, but does work with Functions

## Nodejs and npm installation
> We required node `LTS 14.x` and `npm 6.x+`

Recomend do this first even before VS Code.

You can also use a node version manager - `nvm` and `n` are two options for Linux, macOS.

Volta from LinkedIn is also an option that is cross platform, but works in Windows too.

- [nvm](https://github.com/nvm-sh/nvm)
- [n](https://github.com/tj/n)
- [volta](https://volta.sh/)

> If not using a node version manager, download direct.
> [Latest LTS Version: 14.17.0 (includes npm 6.14.13)](https://nodejs.org/en/download/)

#### Upgrade npm

```
npn i -g npm@7.13.0
```


### Python setup
There are great options for providing many versions of python on a machine. Linux, macOS specifically a tool called `pyenv`.  

If you do use that tool 1) ensure you read the wiki on the dependencies, and install with the `pyenv-installer`.


#### Virtual environment setup.
```bash
# do these steps if you have NOT opened the directory in VS code and allowed the python venv to be created
cd ./api
python -m venv .venv
```


#### Python package upgrades
This is recomended. Wheel support and update provides far faster and seamless installation over `setup`.

```
python -m pip install -U pip wheel
pip install -r requirements.txt
```


#### Azure Functions Core tools v3

This is a must and uses nodejs/npm for installation - [Azure function core tools](https://www.npmjs.com/package/azure-functions-core-tools)

```
npm i -g azure-functions-core-tools@3
```

### Restore packages

```

```

### 

The tool [Azure Static Web Apps CLI](https://github.com/Azure/static-web-apps-cli) is installed as a local package. 
The command cli for the tool is `swa`

# React basic

[Azure Static Web Apps](https://docs.microsoft.com/azure/static-web-apps/overview) allows you to easily build [React](https://reactjs.org/) apps in minutes. Use this repo with the [React quickstart](https://docs.microsoft.com/azure/static-web-apps/getting-started?tabs=react) to build and customize a new static site.

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).
