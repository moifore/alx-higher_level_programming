#!/usr/bin/node
//Script prints the first argument passed to it

if (!process.argv[2] === 1 ) console.log ('No argument');
else console.log(process.argv[2]);
