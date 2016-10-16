# Mairangi Bay Tennis Club

### New Container

`docker run -it -v c:/Users/Simon/development/tennis:/srv/www/tennis/tennis -p 8000 --name tennis simondupreez/tennis`
`docker run -it -v ~/development/tennis:/srv/www/tennis/tennis -p 8000 --name tennis simondupreez/tennis`
`docker run -it -v ~/development/sdup/tennis:/srv/www/tennis/tennis -p 8000-8050:80 -e VIRTUAL_HOST=tennis.dev --name tennis sdupz/tennis`
>>>>>>> 51bf9c97b4c9bad5977a73a91341a778110c9fed

### Sass Compiler

https://github.com/sass/node-sass/blob/master/README.md

`curl https://raw.githubusercontent.com/creationix/nvm/v0.16.1/install.sh | sh`
`source ~/.profile`
`nvm install 6.5.0`
`npm install node-sass`
`node compile.js`
