const licenseJson = require('./Licenses.json');
const fs = require('fs');

const filename = 'Licenses.txt'

const licenseKeys = Object.keys(licenseJson);

licenseKeys.map((key) => {
  const publisher = licenseJson[key].publisher
  const licenseText = licenseJson[key].licenseText

  const outText = `${key} published by ${publisher}
===========================

${licenseText}

===========================



`;

  fs.appendFileSync(filename, outText, (err, data) => {
    if(err) console.log(err);
    else console.log('write end');
  });
})