# Twelve Factor Web App

This repository contains my implementation of a Flask backend API that intends to follow good practices on web app architecture, and is a way for me to explore the current code standards, ecosystem, and quality tools to get better equipped to ship production-grade Python code.

## What I have implemented so far

### Package manager

UV was the chosen tool. It is a modern package manager for Python which is getting more adoption as time goes on and I already used it a little, so I figured should go deeper.

### Code quality tools

- **bandit**: for static code security analysis.
- **black**: for consistent code formatting.
- **flake8**: to catch potential errors before running.
- **isort**: to keep imports tidy.
- **pre-commit**: to run all of the above before comitting to the repo.

### Flask

- Application factory

## What I still want to implement

- **Authentication and authorization**: to learn the best practices on JWT tokens and other methods I may come to use.
- **Database integration**: to learn how to best structure my code and deal with migrations and version control.
- **Background jobs**: I haven't come accross many of these so far, so might as well.
- **Web sockets**: I've used them, but not extensively, so it would be good to get more familiar.
- **Docker**: everything should be ready to run with a Docker image. Just set a few environment variables.
- **Find a system to handle environment variables**: with this, I mean an organized, well-defined method.

## What would be nice to implement

It would make the project cooler if I did these things, but I wont focus on clearing this list. Maybe when my motivation is down, I might cross some of these off.

- **Build a frontend**: probably in React.
- **Host this somewhere public**: deploying's always a learning experience.
- **Pentest the app**: but I've got no idea on how to even start this.
- **Monetize something**: I've never done this. Making money is nice so having a way of making money off software would also be nice.
