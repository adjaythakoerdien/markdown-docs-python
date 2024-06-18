# Dotfiles Stow 

Have you ever had `lost you overview of where you config files are stored`? Or are having trouble moving and synchronizing you config files between machines?
The answer to this is `gnu/stow`. Stow is a nice way to keep you config files in a central place an synchronize between your machine, or simply share you config files with anyone.
Setup below.

## Directory structure:
Make a new directory to store your `config files` in a central place. My directory is called `dotfiles`. 
In this directory you can make a new directory for the type of config file you want to store. In the e example below I've used `nvim` as an example.
In tha new directory you build up the directory structure of the original config file location. You'll understand later why we do it like this.

> ~/dotfiles/nvim/.config/nvim/

## Move config files to dotfiles directory
Move the original config file to the newly created dotfiles location.

```bash
#zsh / bash

mv ~/.config/nvim ~/dotfiles/nvim/.config/
```

## Stow the files (create symlink = symbolic link)
Use `stow nvim` to create a simlink at the location of the original config file that points to the new location of the config file in the `dotfiles` directory.
The simlink is simply a type of symbolic link that simply

```bash
#zsh / bash

stow nvim
```

### What is a simlink?
A symlink (also called a symbolic link) is a type of file in Linux that points to another file or a folder on your computer. Symlinks are similar but not entirely like aliasses.

## Enjoy
You can put this `dotfiles` directory in a repo in git. This way you can just pull your repo from any computer and immediatly start working with you own personal config files.
When you make changes to you `dotfiles` you can you commit and push the changes to the repo. On any other computer you can then fetch and pull the changes, run you `stow` commands and you are ready to go!

Enjoy your new central place for storing an sharing you config files! 



### Resource
- [Typecraft (YT)](https://www.youtube.com/watch?v=NoFiYOqnC4o&t=1s&ab_channel=typecraft)

