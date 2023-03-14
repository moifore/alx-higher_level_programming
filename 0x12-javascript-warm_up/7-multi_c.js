#!/usr/bin/node
// prints x times "C is fun"

let times = parseInt(process.argv[2]);

if (isNaN(times)) console.log('Missing number of occurences');
else {
	while (times > 0) {
		console.log('C is fun');
		times--;
	}
}
