const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf-8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  const lines = data.split('\n').filter(line => line.trim() !== '');
  const headers = lines.shift().split(',');

  // We'll group students by field (last column), collecting first names
  const fields = {};

  lines.forEach((line) => {
    const columns = line.split(',');
    if (columns.length < headers.length) return; // skip invalid lines

    const firstName = columns[0].trim();
    const field = columns[headers.length - 1].trim();

    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(firstName);
  });

  const totalStudents = Object.values(fields).reduce((acc, arr) => acc + arr.length, 0);

  console.log(`Number of students: ${totalStudents}`);

  Object.keys(fields).forEach((field) => {
    console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
  });
}

module.exports = countStudents;
